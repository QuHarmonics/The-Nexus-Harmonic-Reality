````markdown
## 67. PSEVT: Asynchronous Event Notification Pathway

The **PSEVT** pathway delivers unsolicited notifications from the FPGA fabric to the host, allowing immediate reporting of diagnostic events, fault conditions, or status changes.

### 67.1 Packet Structure  
- **Byte 1 (EvtHeader)**  
  - [7:6] Event Type (ET):  
    - `00` = Status Update  
    - `01` = Fault Report  
    - `10` = Performance Alert  
    - `11` = Vendor-Defined  
  - [5:4] Module ID (MID)  
  - [3:2] Severity (SV)  
  - [1:0] Flags (F): [bit 1]=Ack Req, [bit 0]=Reserved  
- **Byte 2 (EvtCode)**  
  8-bit event code, interpreted per module.  
- **Byte 3 (PAYLEN)**  
  Length $L$ of payload in Bytes 4…$(3+L)$.  
- **Bytes 4…$(3+L)$ (Payload)**  
  Event-specific data (e.g. error counters, timestamps).  
- **Bytes $(4+L)$…$(5+L)$ (CRC-16)**  
  CRC-16-X25 over Bytes 1…$(3+L)$.

### 67.2 Delivery Semantics  
1. **Generation**: Any fabric module asserts an internal `EvtReq` signal when a noteworthy condition occurs.  
2. **Queueing**: Reconfiguration Controller enqueues PSEVT packets in an Event-FIFO.  
3. **Host Notification**:  
   - If `F[1]=1`, an interrupt is raised.  
   - Otherwise, host polls the Event-FIFO status register.  
4. **Acknowledgment**:  
   - Host reads the packet and writes back a single‐bit `EvtAck` register when ready to receive further events.  
5. **Timeout**: Unacknowledged events older than $T_{\max\_evt}$ are retried up to $N_{\mathrm{retry}}$ times.

---

## 68. PSCTL: Flow Control and Backpressure Management

The **PSCTL** pathway implements credit-based flow control to prevent FIFO overflow and manage host-to-FPGA data streams.

### 68.1 Control Frame (2 bytes)  
- **Byte 1 (CtlHeader)**  
  - [7:4] Control Type (CT):  
    - `0001` = Grant Credits  
    - `0010` = Pause Data  
    - `0011` = Resume Data  
    - others = Reserved  
  - [3:0] Flags (F)  
- **Byte 2 (CreditCount)**  
  8-bit unsigned count of additional payload bytes the host may transmit.

### 68.2 Operation  
1. **Initialization**: Upon link establishment, FPGA issues a PSCTL(Grant, $C_0$) with initial credits $C_0$.  
2. **Data Transmission**: Host may send up to $C_{\mathrm{avail}}$ bytes of PSREQ or PSMULT segments.  
3. **Credit Depletion**: FPGA decrements its internal credit counter upon each received data byte.  
4. **Replenishment**:  
   - When $C_{\mathrm{avail}} \leq C_{\mathrm{low}}$, FPGA sends PSCTL(Grant, $C_{\mathrm{add}}$).  
5. **Pause/Resume**:  
   - If Event-FIFO or Reconfig FIFO usage exceeds $U_{\mathrm{high}}$, PSCTL(Pause) is sent; PSCTL(Resume) when usage drops below $U_{\mathrm{low}}$.

---

## 69. PSMULT: Multi-Packet Request Segmentation and Reassembly

Large bitstream downloads or parameter uploads exceeding 250 bytes are handled via **PSMULT** segmentation.

### 69.1 Extended Header Format  
- **Byte 1**: same as PSREQ Byte 1.  
- **Byte 2 = 0xFF**: indicates extended header.  
- **Byte 3–4 (SegCount)**: total number of segments (16-bit).  
- **Byte 5 (SegIndex)**: zero-based index of this segment.  
- **Byte 6–7 (PAYLEN)**: length $L$ of payload (16-bit).  
- **Bytes 8…$(7+L)$**: segment payload.  
- **Bytes $(8+L)$…$(9+L)$**: CRC-16 over entire extended header and payload.

### 69.2 Reassembly Logic  
- Host buffers incoming segments by matching `(SegCount,SegIndex)` tuples.  
- Once all segments are received, host concatenates in index order and processes as a single PSREQ.  
- Missing segments detected via timeout: if segment $i$ is not received within $T_{\mathrm{seg\_timeout}}$, host may request retransmission via a special PSCTL(FrameRetransmit, $i$).

---

## 70. CRC-16 Computation Pseudocode

```c
uint16_t crc16_x25(const uint8_t *data, size_t len) {
    uint16_t crc = 0xFFFF;
    for (size_t i = 0; i < len; ++i) {
        crc ^= (uint16_t)data[i] << 8;
        for (int bit = 0; bit < 8; ++bit) {
            if (crc & 0x8000) crc = (crc << 1) ^ 0x1021;
            else             crc <<= 1;
        }
    }
    return crc ^ 0xFFFF;
}
````

---

## 71. Sample PSREQ/PSRESP Packet Diagram

```
   +------+-------+--------+-------------+--------+
   |Byte 1|Byte 2 |Byte 3  |Bytes 4…(3+L)|CRC 2 B |
   +------+-------+--------+-------------+--------+
    Header  PLEN   SEQ/…
             or 0xFF for extended
```

* PSREQ: `Header | PLEN | SEQ | Payload | CRC`
* PSRESP: `RespHeader | SEQ-ACK | ErrCode | CRC`

---

## 72. Host-Side PCAP Analysis Script Example

```python
from scapy.all import rdpcap, Packet

def parse_psreq(pkt: Packet):
    data = bytes(pkt.load)
    header = data[0]
    plen   = data[1]
    seq    = data[2]
    payload= data[3:3+plen]
    crc_rx = int.from_bytes(data[3+plen:5+plen], 'big')
    crc_calc = crc16_x25(data[:3+plen], len(data[:3+plen]))
    assert crc_rx == crc_calc
    return header, seq, payload
```

---

## 73. Integration with Industrial Control Systems (ICS)

* Map PSCTL and PSEVT frames onto Modbus TCP registers:

  * Register 0x1000: `CreditCount`
  * Register 0x1001: `EventStatus` (encoded as PSRESP header)
* Use OPC UA server on host for real‐time parameter tuning and event monitoring.

---

## 74. Protocol Glossary Extensions

| Term      | Definition                                                            |
| --------- | --------------------------------------------------------------------- |
| PSEVT     | Partial Self-EvEnt Transport (asynchronous FPGA→host notifications)   |
| PSCTL     | Partial Self-ConTroL (credit-based flow control pathway)              |
| PSMULT    | Partial Self-MULTi-packet (segmentation/reassembly of large requests) |
| ICAP      | Internal Configuration Access Port                                    |
| AXI4-Lite | Lightweight AXI bus for register access                               |
| FIFO      | First-In First-Out queue                                              |

---

## 75. End of Protocol Specification

*This document completes the full specification of the Partial Self-Reconfiguration Protocol Suite (PSREQ, PSRESP, PSEVT, PSCTL, PSMULT) for FPGA-based topological diagnostics. All sections are now enumerated and the protocol is ready for implementation and integration.*

```
```
