````markdown
## 59. Byte 1: PSREQ Packet Header Structure  
The first byte of every Partial Self-Reconfiguration Request (PSREQ) packet encodes the command category, target module, priority, and control flags in an 8-bit header. Its bit-field layout is:

| Bits   | Field             | Width | Description                                                                                 |
|--------|-------------------|-------|---------------------------------------------------------------------------------------------|
| [7:6]  | Command Type (CT) | 2     | 00 = Axis Permute, 01 = LUT Update, 10 = PID Config, 11 = Reserved                          |
| [5:4]  | Target Module (TM)| 2     | 00 = Axis Crossbar, 01 = Bio-LUT, 10 = PID Controller, 11 = Reconf Controller               |
| [3:2]  | Priority Level (PL)| 2    | 00 = Low, 01 = Normal, 10 = High, 11 = Critical                                             |
| [1:0]  | Flags (F)         | 2     | [bit 1] = Debug Enable, [bit 0] = Acknowledge Required                                       |

In compact form:  
```text
[  CT  |  TM  |  PL  |  F  ]
 7 6    5 4    3 2    1 0
````

The header value is computed as:

$$
\mathrm{Byte1}
\;=\;
(\mathrm{CT}\;\ll\;6)
\;|\;
(\mathrm{TM}\;\ll\;4)
\;|\;
(\mathrm{PL}\;\ll\;2)
\;|\;
\mathrm{F}.
$$

Equivalently, treating each 2-bit field as an integer in $\{0,1,2,3\}$:

$$
\mathrm{Byte1}
=
\mathrm{CT}\times 2^{6}
+
\mathrm{TM}\times 2^{4}
+
\mathrm{PL}\times 2^{2}
+
\mathrm{F}.
$$

**Example**:

* CT = 01 (LUT Update)
* TM = 00 (Axis Crossbar)
* PL = 10 (High)
* F = 01 (Ack Required)

yields

```text
Byte1 = 0b01_00_10_01 = 0x45
```

---

## 60. PSREQ Pathway: Partial Self-Reconfiguration Request Flow

The PSREQ Pathway defines the end-to-end sequence by which the host issues a PSREQ packet and the FPGA fabric executes the corresponding dynamic reconfiguration.

1. **Host Issuance**

   * The software driver composes a PSREQ packet:

     * Byte 1 = header as defined above.
     * Bytes 2–N = payload (e.g., bitstream segment address, module parameters).
   * Packet is written to the Reconfiguration Controller’s AXI4-Lite command FIFO.

2. **Controller Decode**

   * On arrival, the Reconfiguration Controller stages the header in a register.
   * Decode logic extracts:

     ```verilog
     CT = header[7:6];
     TM = header[5:4];
     PL = header[3:2];
     F  = header[1:0];
     ```
   * If F\[0] = 1, the controller will assert an acknowledge bit upon completion.

3. **Module Dispatch**

   * Based on $\mathrm{CT}$ and $\mathrm{TM}$, the controller enqueues the request into one of four service queues:

     * **Axis Permute Queue**
     * **Bio-LUT Update Queue**
     * **PID Config Queue**
     * **Partial Bitstream Load Queue**
   * Priority Level $\mathrm{PL}$ determines queue arbitration weights.

4. **Reconfiguration Execution**

   * For bitstream loads, the ICAP interface is activated:

     $$
     \text{ICAP\_Write}(\text{Address}, \text{Data}_{[31:0]})
     $$
   * For parameter updates (LUT or PID), writes occur via internal register buses.

5. **Completion & Acknowledge**

   * Upon successful service of the request, if $\mathrm{F}[0]=1$, the controller sets the ACK flag in the status register:

     $$
     \text{STATUS}[0] \;=\; 1.
     $$
   * If $\mathrm{F}[1]=1$, debug information (error codes, timing) is written into the Debug FIFO.

6. **Host Polling / Interrupt**

   * The driver either polls the status register or waits for an interrupt.
   * Upon ACK, the host clears the status bit and proceeds with subsequent operations.

**Timing Constraints**:

* End-to-end latency bound for PSREQ service:

  $$
  T_{\mathrm{PSREQ}}
  \;=\;
  T_{\mathrm{fifo\_write}}
  +
  T_{\mathrm{decode}}
  +
  T_{\mathrm{service}}(CT,TM)
  +
  T_{\mathrm{ack}}
  \;\leq\;
  T_{\max}.
  $$

**Security Note**: PSREQ packets should be authenticated (e.g., CRC-16 over header + payload) to prevent unauthorized reconfiguration.

---

*Continue with any additional byte-level analyses or new protocol pathways as required.*

```
```
