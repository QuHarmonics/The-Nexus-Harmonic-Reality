# Chapter 4: Hardware Specifications for Project 8-Bit Fusion

## Author: Dean Kulik (ORCID: 0009-0003-3128-8828)

---

## 4.1 System Architecture Overview

### 4.1.1 High-Level Block Diagram Description

The Project 8-Bit Fusion hardware architecture implements a comprehensive digital signal processing platform designed for high-throughput, low-latency data acquisition and real-time processing. The system is architected around a central FPGA-based processing core, interfacing with multiple analog front-end channels, high-speed memory subsystems, and external communication interfaces.

The primary system architecture consists of the following major functional blocks:

**Analog Front-End (AFE) Module**: Eight independent analog input channels, each featuring programmable gain amplifiers (PGAs), anti-aliasing filters, and high-speed analog-to-digital converters. The AFE module interfaces directly with the FPGA through dedicated high-speed LVDS data links operating at 1.25 Gbps per channel.

**FPGA Processing Core**: The central processing element implemented on a Xilinx Kintex-7 XC7K325T-2FFG900C FPGA. This device provides 326,080 logic cells, 16,020 Kbits of block RAM, and 840 DSP48E1 slices. The FPGA implements the complete digital signal processing pipeline including data acquisition, filtering, fusion algorithms, and interface management.

**Memory Subsystem**: A hierarchical memory architecture comprising on-chip FPGA block RAM for immediate buffering, external DDR3 SDRAM for intermediate storage, and QSPI flash for non-volatile configuration storage. The DDR3 interface operates at 800 MHz (1600 MT/s) providing 12.8 GB/s aggregate bandwidth.

**Communication Interfaces**: Multiple high-speed communication ports including PCIe Gen2 x4 for host computer interface, Gigabit Ethernet for network connectivity, and USB 3.0 for auxiliary data transfer and debugging. The PCIe interface provides direct memory access (DMA) capability with sustained throughput of 2 GB/s.

**Clock and Synchronization**: A precision clock generation and distribution system featuring a low-phase-noise 100 MHz oven-controlled crystal oscillator (OCXO) as the primary reference. The system generates all required clock frequencies through phase-locked loops (PLLs) and clock distribution networks with sub-picosecond jitter performance.

**Power Management**: Comprehensive power delivery system providing multiple regulated voltage rails with active monitoring and protection. The system implements sequenced power-up/down, overcurrent protection, and thermal monitoring for all major subsystems.

### 4.1.2 Data Flow Paths

The data flow architecture of Project 8-Bit Fusion is designed to maximize throughput while maintaining deterministic latency. The primary data paths are described below:

**Input Data Path**: Analog signals from external sensors are conditioned by the AFE module, converted to digital format by the ADCs, and transmitted to the FPGA via LVDS interfaces. Each ADC channel produces 8-bit parallel data at a sampling rate of 125 MSPS, resulting in 1 Gbps raw data rate per channel. The eight channels aggregate to 8 Gbps total input bandwidth.

Upon reception in the FPGA, data undergoes immediate formatting and alignment. The input data path includes:
1. LVDS receiver deserialization and word alignment
2. Channel-to-channel skew compensation
3. Data packing into 64-bit words for efficient processing
4. Initial buffering in circular FIFO structures

**Processing Data Path**: The digital signal processing pipeline operates on 8-bit fixed-point data throughout. The processing stages include:
1. Digital filtering (FIR and IIR implementations)
2. Data fusion algorithms combining multiple input channels
3. Feature extraction and event detection
4. Data compression and packetization

The processing path is fully pipelined with a throughput of one sample per clock cycle per channel, maintaining continuous data flow without stalls.

**Output Data Path**: Processed data is routed to appropriate output interfaces based on configuration:
1. High-priority data streams via PCIe DMA to host memory
2. Network-bound data via Gigabit Ethernet
3. Debug and monitoring data via USB 3.0
4. Trigger and control signals via dedicated GPIO

**Control Data Path**: Configuration and control commands flow from the host system through PCIe or Ethernet interfaces to the FPGA's control register interface. The control path operates independently of data paths to ensure real-time responsiveness.

### 4.1.3 Control Interfaces

The control architecture implements a hierarchical structure with multiple access points:

**Register Map Interface**: A comprehensive memory-mapped register space accessible via PCIe or Ethernet. The register map includes:
- Configuration registers for AFE parameters (gain, offset, filter settings)
- DSP pipeline configuration registers
- DMA controller settings
- Status and monitoring registers
- Interrupt control and status

**Command Interface**: A packet-based command protocol for high-level operations including:
- System initialization and calibration
- Data acquisition start/stop
- Trigger configuration
- Diagnostic and self-test commands

**Debug Interface**: JTAG-based debugging through the FPGA's built-in debug port, providing:
- Real-time signal probing via Xilinx Integrated Logic Analyzer (ILA)
- Memory read/write access
- Breakpoint and single-step capabilities

**External Trigger Interface**: Dedicated hardware trigger inputs and outputs with configurable polarity and timing. The trigger system supports:
- External synchronization signals
- Cross-channel triggering
- Programmable trigger delays

---

## 4.2 FPGA/ASIC Specifications

### 4.2.1 Target Device Family and Specific Part Numbers

The Project 8-Bit Fusion system is implemented on the Xilinx Kintex-7 FPGA family, specifically utilizing the following devices:

**Primary FPGA**: Xilinx XC7K325T-2FFG900C
- Package: FFG900 (Flip-Chip Fine-pitch BGA, 900 pins)
- Speed Grade: -2 (mid-range performance)
- Temperature Grade: Commercial (0°C to +85°C)

**Alternative/Upgrade Path**: Xilinx XC7K410T-2FFG900C
- Compatible pinout with increased resources
- 406,720 logic cells (25% increase)
- 28,620 Kbits block RAM (79% increase)
- 1,540 DSP48E1 slices (83% increase)

**Configuration Memory**: Micron N25Q256A13ESF40F
- 256 Mbit (32 MB) Quad SPI flash
- 108 MHz maximum clock frequency
- Dual/Quad output read capability
- Sector erase architecture

The selection of the Kintex-7 family was driven by the following requirements:
1. Sufficient logic resources for eight-channel DSP implementation
2. High-speed transceivers for PCIe and Ethernet interfaces
3. Adequate DSP slices for parallel filtering operations
4. Cost-effectiveness for research prototype development
5. Availability of development tools and reference designs

### 4.2.2 Logic Resource Utilization

The FPGA design targets the following resource utilization for the XC7K325T device:

**Logic Resources**:
- Logic Cells: 210,000 / 326,080 (64.4% utilization)
- Slice Registers: 168,000 / 407,600 (41.2% utilization)
- Slice LUTs: 140,000 / 203,800 (68.7% utilization)
- Occupied Slices: 28,000 / 50,950 (54.9% utilization)

**Memory Resources**:
- Block RAM (36Kb blocks): 280 / 890 (31.5% utilization)
- Total Block RAM: 10,080 Kbits / 16,020 Kbits
- Distributed RAM: 1,500 Kbits

**DSP Resources**:
- DSP48E1 Slices: 480 / 840 (57.1% utilization)
- Utilized primarily for FIR filter implementations

**Clocking Resources**:
- MMCM (Mixed-Mode Clock Manager): 4 / 10 (40% utilization)
- PLL (Phase-Locked Loop): 2 / 10 (20% utilization)
- BUFG (Global Clock Buffer): 12 / 32 (37.5% utilization)

**I/O Resources**:
- Total User I/O: 400 / 500 (80% utilization)
- High-speed transceivers (GTX): 8 / 16 (50% utilization)
- LVDS pairs: 80 differential pairs

**Resource Allocation by Functional Block**:

| Functional Block | LUTs | Registers | BRAM (Kb) | DSP48 |
|-----------------|------|-----------|-----------|-------|
| Data Acquisition | 18,500 | 22,000 | 1,440 | 0 |
| Digital Filtering | 42,000 | 35,000 | 2,880 | 320 |
| Data Fusion Core | 28,000 | 45,000 | 1,728 | 96 |
| PCIe Interface | 15,000 | 28,000 | 576 | 0 |
| Ethernet MAC | 12,000 | 18,000 | 432 | 0 |
| Memory Controller | 8,500 | 12,000 | 864 | 0 |
| Control/Status | 6,000 | 8,000 | 288 | 0 |
| Debug/Monitoring | 10,000 | 15,000 | 720 | 64 |
| **Total** | **140,000** | **183,000** | **8,928** | **480** |

### 4.2.3 Clock Domains and Timing Requirements

The FPGA design implements multiple clock domains to accommodate different interface requirements and optimize power consumption:

**Primary Clock Domains**:

1. **System Clock (clk_sys)**: 100 MHz
   - Source: On-board 100 MHz crystal oscillator
   - Usage: General system logic, control interfaces
   - Jitter requirement: < 100 ps peak-to-peak

2. **ADC Sample Clock (clk_adc)**: 125 MHz
   - Source: PLL derived from 100 MHz reference
   - Usage: ADC interface, input data capture
   - Phase relationship: Fixed phase to clk_sys

3. **DDR3 Memory Clock (clk_ddr)**: 400 MHz (800 MHz DDR)
   - Source: Memory controller PLL
   - Usage: DDR3 interface logic
   - Timing: Center-aligned to DQ signals

4. **PCIe Reference Clock (clk_pcie)**: 100 MHz
   - Source: External PCIe connector
   - Usage: PCIe transceiver and core logic
   - Spread spectrum: -0.5% to 0% modulation

5. **Ethernet Clock (clk_eth)**: 125 MHz
   - Source: External PHY or internal PLL
   - Usage: GMII/RGMII interface logic

6. **Processing Clock (clk_proc)**: 250 MHz
   - Source: MMCM multiplied from 100 MHz reference
   - Usage: DSP pipeline, data fusion algorithms
   - Target frequency for maximum throughput

**Clock Domain Crossing (CDC)**:
All inter-domain data transfers implement proper synchronization:
- Dual-flop synchronizers for control signals
- FIFO-based buffering for data streams
- Gray-code counters for pointer synchronization
- False path and multi-cycle path constraints

**Timing Requirements**:

| Clock Domain | Frequency | Setup Slack | Hold Slack | Target Fmax |
|--------------|-----------|-------------|------------|-------------|
| clk_sys | 100 MHz | > 1.0 ns | > 0.3 ns | 125 MHz |
| clk_adc | 125 MHz | > 0.8 ns | > 0.3 ns | 156 MHz |
| clk_ddr | 400 MHz | > 0.5 ns | > 0.2 ns | 450 MHz |
| clk_pcie | 100 MHz | > 1.5 ns | > 0.3 ns | 125 MHz |
| clk_eth | 125 MHz | > 1.0 ns | > 0.3 ns | 156 MHz |
| clk_proc | 250 MHz | > 0.5 ns | > 0.2 ns | 300 MHz |

**Clock Jitter Specifications**:
- Period Jitter: < 50 ps RMS
- Cycle-to-Cycle Jitter: < 80 ps peak-to-peak
- Long-term Jitter: < 500 ps over 1 ms interval

### 4.2.4 Bit-Resolution Architecture (8-Bit Focus)

The Project 8-Bit Fusion system is specifically architected around 8-bit data processing throughout the signal chain. This design choice provides optimal balance between processing throughput, resource utilization, and signal quality for the target applications.

**8-Bit Data Path Architecture**:

**Input Stage**: The ADCs provide 8-bit resolution with the following characteristics:
- Quantization levels: 256 discrete levels
- LSB size: Vref / 256 (e.g., 7.81 mV for 2.0V reference)
- Theoretical SNR: 49.92 dB (6.02 × 8 + 1.76)
- Effective bits: 7.5 ENOB at Nyquist frequency

**Processing Stage**: All arithmetic operations use 8-bit fixed-point representation:
- Data format: Unsigned 8-bit integer (0 to 255)
- Filter coefficients: 8-bit signed fixed-point (Q7 format)
- Accumulator width: 24-bit to prevent overflow
- Final output: 8-bit with rounding/saturation

**Coefficient Quantization**: Digital filter coefficients are quantized to 8-bit precision:
- Quantization method: Rounding to nearest
- Coefficient scaling: 2^7 × h[n] (Q7 format)
- Quantization error: < 0.4% of coefficient magnitude
- Impact on filter response: < 0.1 dB passband ripple

**Arithmetic Operations**: The DSP pipeline implements:
- Multiplication: 8-bit × 8-bit → 16-bit product
- Accumulation: 16-bit + 24-bit accumulator
- Rounding: Truncation or convergent rounding
- Saturation: Clip to 8-bit range on overflow

**Signal Quality Considerations**:

The 8-bit architecture maintains signal fidelity through:
1. Proper analog front-end gain staging to utilize full ADC range
2. Dithering techniques to reduce quantization artifacts
3. Noise shaping in feedback loops
4. Oversampling where applicable

**Dynamic Range**: 
- Instantaneous dynamic range: 48 dB (8 bits)
- Effective dynamic range with oversampling: 60+ dB
- Spurious-free dynamic range (SFDR): > 50 dBc

**Error Analysis**:
- Quantization noise power: Δ²/12 where Δ = Vref/256
- Signal-to-quantization-noise ratio (SQNR): 49.92 dB for full-scale sine
- Total harmonic distortion (THD): < -50 dBc

---

## 4.3 Signal Processing Chain

### 4.3.1 ADC Specifications

The analog-to-digital conversion subsystem comprises eight identical channels based on the Texas Instruments ADS5273 8-channel, 8-bit ADC.

**ADC Device Specifications (ADS5273IPFP)**:

| Parameter | Specification | Unit |
|-----------|---------------|------|
| Resolution | 8 | bits |
| Sampling Rate (per channel) | 65 | MSPS |
| Parallel Channel Sampling | 8 | channels |
| Total Throughput | 520 | MSPS |
| Analog Input Range | 2.0 | Vpp |
| Input Bandwidth (-3dB) | 300 | MHz |
| SNR (at Nyquist) | 47.5 | dB |
| SFDR (at Nyquist) | 58 | dBc |
| ENOB (at Nyquist) | 7.5 | bits |
| Power Dissipation | 1.35 | W |
| Supply Voltage (Analog) | 3.3 | V |
| Supply Voltage (Digital) | 1.8 | V |
| Package | HTQFP-80 | - |

**Alternative High-Speed ADC (ADS5282IPFP)**:
For applications requiring higher sampling rates:
| Parameter | Specification | Unit |
|-----------|---------------|------|
| Resolution | 8 | bits |
| Sampling Rate (per channel) | 65 | MSPS |
| SNR | 48.5 | dB |
| Power Dissipation | 1.08 | W |

**ADC Interface Specifications**:
- Data Output Format: Parallel CMOS, 1.8V logic levels
- Output Data Width: 8 bits per channel
- Output Enable Control: Individual per channel
- Duty Cycle Stabilizer: Integrated

**Clocking Requirements**:
- Clock Input Frequency: 65 MHz (for 65 MSPS operation)
- Clock Input Level: LVPECL or LVDS compatible
- Clock Duty Cycle: 50% ± 5%
- Aperture Jitter: < 1 ps RMS

**Timing Specifications**:
- Aperture Delay: 2.5 ns (typical)
- Data Latency: 5.5 clock cycles (pipeline delay)
- Data Valid Window: 12 ns (at 65 MHz)
- Setup Time: 4 ns minimum
- Hold Time: 2 ns minimum

**Performance Characteristics**:

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| Differential Nonlinearity (DNL) | -0.5 | ±0.2 | +0.5 | LSB |
| Integral Nonlinearity (INL) | -0.5 | ±0.3 | +0.5 | LSB |
| Offset Error | -10 | ±2 | +10 | mV |
| Gain Error | -5 | ±1 | +5 | %FS |
| Channel-to-Channel Isolation | - | 75 | - | dB |
| Power Supply Rejection (PSR) | - | 50 | - | dB |

### 4.3.2 Digital Filter Implementations

The digital filtering subsystem implements multiple filter types optimized for 8-bit fixed-point arithmetic:

**FIR Filter Implementation**:

The system implements programmable FIR filters using the FPGA DSP48E1 slices. Filter configurations include:

| Filter Type | Taps | Coefficient Width | Input Width | Output Width |
|-------------|------|-------------------|-------------|--------------|
| Low-Pass (Anti-aliasing) | 64 | 8-bit | 8-bit | 8-bit |
| Band-Pass (Channel Select) | 128 | 8-bit | 8-bit | 8-bit |
| Matched Filter | 32 | 8-bit | 8-bit | 8-bit |
| Decimation Filter | 256 | 8-bit | 8-bit | 8-bit |

**FIR Filter Architecture**:
```
Input (8-bit) → [Delay Line] → [Multiplier Array] → [Adder Tree] → [Round/Sat] → Output (8-bit)
                     ↑
            Coefficient ROM (8-bit × N taps)
```

- Implementation: Transposed direct-form FIR
- Multiplier: DSP48E1 primitive (25×18 multiplier)
- Accumulation: 48-bit accumulator width
- Rounding: Convergent rounding to 8-bit output

**IIR Filter Implementation**:

Second-order IIR sections (biquads) for recursive filtering:

| Parameter | Specification |
|-----------|---------------|
| Structure | Direct Form II Transposed |
| Order | 2 (biquad sections) |
| Coefficient Precision | 8-bit Q7 format |
| Internal Precision | 24-bit |
| Output Precision | 8-bit |
| Cascade Stages | Up to 8 sections |

**IIR Biquad Difference Equations**:
```
w[n] = x[n] - a1*w[n-1] - a2*w[n-2]
y[n] = b0*w[n] + b1*w[n-1] + b2*w[n-2]
```

Where coefficients a1, a2, b0, b1, b2 are 8-bit signed values.

**CIC Filter for Decimation**:

Cascaded Integrator-Comb filters for sample rate reduction:

| Parameter | Value |
|-----------|-------|
| Stages (N) | 4 |
| Differential Delay (M) | 1 |
| Decimation Ratio (R) | 4, 8, 16, or 32 |
| Register Width | 24-bit |
| Output Width | 8-bit |

**Filter Performance Specifications**:

| Filter Type | Passband Ripple | Stopband Attenuation | Transition Band |
|-------------|-----------------|----------------------|-----------------|
| Low-Pass FIR | < 0.1 dB | > 60 dB | 0.2 × fs |
| Band-Pass FIR | < 0.2 dB | > 50 dB | 0.1 × fs |
| CIC (4-stage) | < 0.5 dB | > 67 dB | N/A |

### 4.3.3 Quantization Schemes

The 8-bit quantization strategy employs multiple techniques to minimize signal degradation:

**Uniform Quantization**:
- Type: Mid-tread uniform quantizer
- Step size: Δ = Vref / 256
- Decision levels: (k - 0.5) × Δ for k = 0 to 255
- Reconstruction levels: k × Δ for k = 0 to 255

**Dithering Implementation**:
- Type: Subtractive dither with triangular PDF
- Amplitude: ±0.5 LSB peak-to-peak
- Implementation: Pseudo-random sequence added before quantization
- Effect: Linearizes quantization, reduces spurs

**Noise Shaping**:
- Architecture: First-order sigma-delta modulator
- Noise transfer function: NTF(z) = 1 - z^(-1)
- Oversampling ratio: 4× to 16×
- Effective resolution improvement: 1-2 bits

**Coefficient Quantization**:
- Method: Optimal rounding with error feedback
- Format: Q7 (1 sign bit, 7 fractional bits)
- Range: -1.0 to +0.9921875
- Quantization step: 2^(-7) = 0.0078125

**Dynamic Range Optimization**:
- Automatic gain control (AGC) in analog domain
- Digital scaling before filtering
- Saturation arithmetic to prevent wraparound
- Overflow detection and flagging

### 4.3.4 Fixed-Point Arithmetic Details

The fixed-point arithmetic system is designed for 8-bit data with extended precision for intermediate calculations:

**Number Representation**:

| Format | Width | Range | Precision |
|--------|-------|-------|-----------|
| Unsigned 8-bit | 8 | 0 to 255 | 1 LSB |
| Signed 8-bit (Q7) | 8 | -128 to +127 | 1 LSB |
| Signed 16-bit (Q15) | 16 | -32768 to +32767 | 1 LSB |
| Accumulator (Q23) | 24 | -2^23 to 2^23-1 | 1 LSB |

**Arithmetic Operations**:

**Multiplication** (8-bit × 8-bit):
```
Input A: Q7 format (signed 8-bit)
Input B: Q7 format (signed 8-bit)
Product: Q14 format (signed 16-bit)
Result = (A × B) >> 7  // Back to Q7
```

**Addition** (with saturation):
```
Input A: 8-bit
Input B: 8-bit
Sum: 9-bit intermediate
If sum > 255: result = 255 (saturation)
If sum < 0: result = 0 (saturation)
Else: result = sum[7:0]
```

**MAC Operation** (Multiply-Accumulate):
```
Accumulator = 0 (24-bit)
For each tap:
    Product = coefficient × data (16-bit)
    Accumulator = Accumulator + Product
Output = round_and_saturate(Accumulator)
```

**Rounding Modes**:
1. **Truncation**: Simple bit shifting, introduces bias
2. **Round-Half-Up**: Unbiased for positive numbers
3. **Convergent Rounding**: IEEE 754 round-to-nearest-even, unbiased

**Overflow Handling**:
- Detection: Monitor carry-out from MSB
- Saturation: Clip to maximum/minimum representable value
- Flagging: Set overflow status bit for monitoring
- Counting: Accumulate overflow events for diagnostics

---

## 4.4 Memory Subsystem

### 4.4.1 RAM Requirements and Organization

The memory subsystem implements a hierarchical architecture optimized for the data throughput requirements of the 8-channel processing system.

**On-Chip Block RAM (FPGA)**:

Total available: 16,020 Kbits (890 × 18Kb blocks or 445 × 36Kb blocks)

| Memory Function | Size (Kb) | Configuration | Quantity |
|-----------------|-----------|---------------|----------|
| ADC Input Buffers | 36 | 512 × 72-bit | 8 |
| FIR Coefficient Storage | 16 | 256 × 64-bit | 8 |
| Filter Delay Lines | 72 | 1K × 72-bit | 8 |
| Processing Buffers | 144 | 2K × 72-bit | 4 |
| DMA FIFOs | 72 | 1K × 72-bit | 4 |
| Control Registers | 8 | 1K × 8-bit | 1 |
| Debug Trace Buffer | 144 | 4K × 36-bit | 1 |
| **Total BRAM Used** | **490** | - | - |

**External DDR3 SDRAM**:

Device: Micron MT41K256M16HA-125:E
- Capacity: 4 Gbit (512 MB)
- Organization: 256M × 16-bit
- Speed Grade: DDR3-1600 (800 MHz clock, 1600 MT/s)
- Package: FBGA-96

| Parameter | Specification |
|-----------|---------------|
| Data Rate | 1600 MT/s |
| CAS Latency (CL) | 11 cycles |
| Row Cycle Time (tRC) | 48.75 ns |
| Refresh Interval | 7.8 μs |
| Operating Voltage | 1.5V ± 0.075V |
| Operating Temperature | 0°C to +95°C |

**Flash Memory**:

Device: Micron N25Q256A13ESF40F
- Capacity: 256 Mbit (32 MB)
| Parameter | Specification |
|-----------|---------------|
| Interface | Quad SPI |
| Clock Rate | 108 MHz max |
| Read Throughput | 54 MB/s (quad mode) |
| Page Size | 256 bytes |
| Sector Size | 64 KB |
| Endurance | 100,000 cycles |
| Data Retention | 20 years |

### 4.4.2 Buffer Architectures

**Circular Buffer Implementation**:

The system implements circular buffers for continuous data streaming:

```
Structure CircularBuffer:
    base_address: 32-bit pointer
    write_pointer: 32-bit index
    read_pointer: 32-bit index
    depth: 16-bit (buffer size in samples)
    element_size: 8-bit (bytes per element)
```

**Buffer Types**:

| Buffer Name | Depth | Width | Purpose |
|-------------|-------|-------|---------|
| ADC Raw Buffer | 4096 | 64-bit | Pre-processing storage |
| Filter Output Buffer | 2048 | 8-bit | Post-filter samples |
| Fusion Output Buffer | 1024 | 64-bit | Fused data packets |
| DMA Transmit Buffer | 8192 | 64-bit | PCIe DMA staging |

**Buffer Management**:
- Lock-free implementation using atomic pointer updates
- Watermark-based flow control
- Overflow/underflow detection with interrupt generation
- Double-buffering for seamless data transfer

**FIFO Architecture**:

Asynchronous FIFOs for clock domain crossing:
- Dual-port memory implementation
- Gray-coded read/write pointers
- Programmable almost-full/almost-empty flags
- Depth: 512 to 4096 elements

### 4.4.3 Data Throughput Specifications

**Peak Throughput Requirements**:

| Data Path | Rate | Direction | Total Bandwidth |
|-----------|------|-----------|-----------------|
| ADC Inputs (8 ch) | 65 MSPS × 8-bit × 8 | In | 4.16 Gbps |
| DDR3 Interface | 1600 MT/s × 16-bit | Bi | 25.6 Gbps |
| PCIe Gen2 x4 | 5 GT/s × 4 lanes | Bi | 16 Gbps |
| Gigabit Ethernet | 1 Gbps | Bi | 1 Gbps |
| USB 3.0 | 5 Gbps | Bi | 5 Gbps |

**Sustained Throughput Budget**:

| Operation | Samples/sec | Bits/sample | Bandwidth |
|-----------|-------------|-------------|-----------|
| Raw ADC capture | 520M | 8 | 4.16 Gbps |
| Filtered output | 520M | 8 | 4.16 Gbps |
| Fused data | 65M | 64 | 4.16 Gbps |
| PCIe upload | 65M | 64 | 4.16 Gbps |

**Memory Bandwidth Allocation**:

| Function | Read BW | Write BW | Total |
|----------|---------|----------|-------|
| Filter coefficients | 2.08 Gbps | 0 | 2.08 Gbps |
| Delay line access | 2.08 Gbps | 2.08 Gbps | 4.16 Gbps |
| DDR3 data storage | 4.16 Gbps | 4.16 Gbps | 8.32 Gbps |
| DMA operations | 4.16 Gbps | 4.16 Gbps | 8.32 Gbps |
| **Total** | **12.48 Gbps** | **10.4 Gbps** | **22.88 Gbps** |

---

## 4.5 Interface Specifications

### 4.5.1 Communication Protocols

**PCI Express Interface**:

Configuration: PCI Express Gen2, 4 lanes (x4)

| Parameter | Specification |
|-----------|---------------|
| Protocol Version | PCIe Base Specification 2.1 |
| Link Width | x4 |
| Data Rate | 5 GT/s per lane |
| Effective Bandwidth | 2 GB/s (per direction) |
| Payload Size | 256 bytes (MPS) |
| Max Read Request | 512 bytes |
| Completion Timeout | 50 ms |

**PCIe Endpoint Configuration**:
- Vendor ID: 0x10EE (Xilinx)
- Device ID: 0x7024
- Class Code: 0x118000 (Data Acquisition)
- BAR0: 1 MB (Register space)
- BAR1: 64 MB (DMA buffer descriptor)
- MSI-X Capable: Yes (32 vectors)

**Gigabit Ethernet Interface**:

Configuration: 1000BASE-T, RGMII interface to PHY

| Parameter | Specification |
|-----------|---------------|
| Standard | IEEE 802.3ab |
| Data Rate | 1 Gbps |
| Interface | RGMII v2.0 |
| Clock | 125 MHz (TX and RX) |
| PHY Device | Marvell 88E1512 |
| Auto-Negotiation | Yes (10/100/1000) |
| MDIO Address | 0x01 |

**USB 3.0 Interface**:

Configuration: USB 3.0 SuperSpeed Device

| Parameter | Specification |
|-----------|---------------|
| Specification | USB 3.0 |
| Data Rate | 5 Gbps |
| Connector | USB 3.0 Micro-B |
| Device Class | Vendor Specific |
| Endpoints | 8 (4 IN, 4 OUT) |
| Max Packet Size | 1024 bytes |

### 4.5.2 Pin Assignments

**FPGA Pin Allocation Summary**:

| Function | Pin Count | I/O Standard |
|----------|-----------|--------------|
| ADC Data (8 ch × 8-bit) | 64 | LVCMOS18 |
| ADC Clock/Control | 16 | LVCMOS18 |
| DDR3 Data | 16 | SSTL15 |
| DDR3 Address/Command | 28 | SSTL15 |
| DDR3 Clock/Control | 8 | SSTL15 |
| PCIe Transceivers | 8 | High-speed diff |
| PCIe Clock/Reset | 4 | HSTL/LVCMOS |
| Ethernet RGMII | 16 | LVCMOS33 |
| Ethernet PHY Control | 4 | LVCMOS33 |
| USB 3.0 | 12 | High-speed diff |
| JTAG Debug | 5 | LVCMOS33 |
| Power/Configuration | 20 | Various |
| GPIO | 48 | LVCMOS33 |
| **Total** | **267** | - |

**Critical Pin Assignments (FPGA Bank 12 - ADC Interface)**:

| Signal | Pin | Direction | I/O Standard |
|--------|-----|-----------|--------------|
| ADC0_D[0] | H12 | Input | LVCMOS18 |
| ADC0_D[1] | H13 | Input | LVCMOS18 |
| ADC0_D[2] | J12 | Input | LVCMOS18 |
| ADC0_D[3] | J13 | Input | LVCMOS18 |
| ADC0_D[4] | K12 | Input | LVCMOS18 |
| ADC0_D[5] | K13 | Input | LVCMOS18 |
| ADC0_D[6] | L12 | Input | LVCMOS18 |
| ADC0_D[7] | L13 | Input | LVCMOS18 |
| ADC0_CLK | M12 | Input | LVCMOS18 |
| ADC0_OV | M13 | Input | LVCMOS18 |

**DDR3 Pin Assignments (FPGA Banks 33-34)**:

| Signal | Pin | Direction | I/O Standard |
|--------|-----|-----------|--------------|
| DDR3_DQ[0:15] | Various | Bidir | SSTL15 |
| DDR3_DM[0:1] | Various | Output | SSTL15 |
| DDR3_DQS[0:1] | Various | Bidir | DIFF_SSTL15 |
| DDR3_A[0:14] | Various | Output | SSTL15 |
| DDR3_BA[0:2] | Various | Output | SSTL15 |
| DDR3_RAS_N | Various | Output | SSTL15 |
| DDR3_CAS_N | Various | Output | SSTL15 |
| DDR3_WE_N | Various | Output | SSTL15 |
| DDR3_CK/CK_N | Various | Output | DIFF_SSTL15 |
| DDR3_CKE | Various | Output | SSTL15 |
| DDR3_ODT | Various | Output | SSTL15 |
| DDR3_RESET_N | Various | Output | LVCMOS15 |

### 4.5.3 Electrical Characteristics

**I/O Voltage Levels**:

| Interface | Vccio | Voh (min) | Vol (max) | Vih (min) | Vil (max) |
|-----------|-------|-----------|-----------|-----------|-----------|
| LVCMOS18 | 1.8V | 1.35V | 0.45V | 1.17V | 0.63V |
| LVCMOS33 | 3.3V | 2.4V | 0.4V | 2.0V | 0.8V |
| SSTL15 | 1.5V | 1.075V | 0.4V | Vref+0.1 | Vref-0.1 |
| HSTL15 | 1.5V | 1.1V | 0.4V | 0.9V | 0.65V |

**Drive Strength Settings**:

| Interface | Drive Strength | Slew Rate |
|-----------|----------------|-----------|
| LVCMOS18 | 8 mA | FAST |
| LVCMOS33 | 12 mA | FAST |
| SSTL15 | 40 Ω termination | - |
| DDR3 | 34 Ω driver | - |

**LVDS Specifications (GTX Transceivers)**:

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| Output Voltage Swing | 800 | - | 1200 | mVpp |
| Common Mode Voltage | - | 1.2 | - | V |
| Rise/Fall Time | - | 80 | 120 | ps |
| Deterministic Jitter | - | 20 | 40 | ps |
| Random Jitter | - | 1 | 2 | ps RMS |

**Thermal Specifications**:

| Parameter | Specification |
|-----------|---------------|
| Operating Temperature | 0°C to +70°C (Commercial) |
| Storage Temperature | -40°C to +100°C |
| Junction Temperature (max) | +125°C |
| Theta-JA (natural convection) | 12°C/W |
| Theta-JC | 0.5°C/W |

---

## 4.6 Power and Thermal

### 4.6.1 Power Consumption Estimates by Component

**FPGA Power Consumption (XC7K325T)**:

| Power Domain | Voltage | Current | Power |
|--------------|---------|---------|-------|
| VCCINT (Core) | 1.0V | 8.5A | 8.5W |
| VCCBRAM | 1.0V | 1.2A | 1.2W |
| VCCAUX (Auxiliary) | 1.8V | 0.8A | 1.44W |
| VCCO_0 (Config) | 3.3V | 0.1A | 0.33W |
| VCCO_12 (ADC) | 1.8V | 0.5A | 0.9W |
| VCCO_33 (DDR3) | 1.5V | 0.3A | 0.45W |
| VCCO_34 (DDR3) | 1.5V | 0.3A | 0.45W |
| VCCO_13 (Eth) | 3.3V | 0.4A | 1.32W |
| MGTAVCC (GTX) | 1.0V | 2.5A | 2.5W |
| MGTAVTT (GTX) | 1.2V | 1.5A | 1.8W |
| MGTVCCAUX | 1.8V | 0.2A | 0.36W |
| **FPGA Total** | - | - | **19.25W** |

**ADC Power Consumption (ADS5273)**:

| Parameter | Value |
|-----------|-------|
| Analog Supply (3.3V) | 270 mA |
| Digital Supply (1.8V) | 320 mA |
| Total Power | 1.35W |
| Power per Channel | 169 mW |

**DDR3 Memory Power (MT41K256M16)**:

| Mode | Power |
|------|-------|
| Active (read/write) | 400 mW |
| Active standby | 180 mW |
| Precharge standby | 120 mW |
| Self-refresh | 15 mW |

**Ethernet PHY Power (88E1512)**:

| Mode | Power |
|------|-------|
| 1000BASE-T Active | 700 mW |
| 100BASE-TX Active | 350 mW |
| Power Down | 50 mW |

**System Power Budget Summary**:

| Component | Quantity | Unit Power | Total Power |
|-----------|----------|------------|-------------|
| FPGA (XC7K325T) | 1 | 19.25W | 19.25W |
| ADC (ADS5273) | 1 | 1.35W | 1.35W |
| DDR3 Memory | 1 | 0.4W | 0.4W |
| Ethernet PHY | 1 | 0.7W | 0.7W |
| USB 3.0 PHY | 1 | 0.5W | 0.5W |
| PCIe Retimers | 2 | 0.3W | 0.6W |
| Voltage Regulators | 8 | 0.5W | 4.0W |
| Miscellaneous | - | - | 2.0W |
| **System Total** | - | - | **28.8W** |
| **Design Margin (20%)** | - | - | **5.76W** |
| **Total with Margin** | - | - | **34.56W** |

### 4.6.2 Thermal Design Requirements

**Thermal Management Strategy**:

The system employs active cooling with forced air convection:

1. **FPGA Cooling**: Heatsink with integrated fan
   - Heatsink thermal resistance: 2.5°C/W
   - Fan airflow: 8 CFM
   - Acoustic noise: < 35 dBA

2. **ADC Cooling**: Passive heatsink
   - Thermal pad interface
   - Heatsink thermal resistance: 8°C/W

3. **System Cooling**: Chassis-mounted fans
   - Quantity: 2 × 40mm axial fans
   - Airflow per fan: 10 CFM
   - Control: Temperature-based PWM

**Temperature Monitoring**:

| Location | Sensor Type | Threshold |
|----------|-------------|-----------|
| FPGA Junction | Internal XADC | 100°C warning, 115°C shutdown |
| ADC Surface | External I2C | 85°C warning, 95°C shutdown |
| Ambient | External I2C | 60°C warning |
| Heatsink | Thermistor | 70°C warning |

**Thermal Calculations**:

Maximum ambient temperature: 45°C
FPGA power dissipation: 19.25W
Heatsink thermal resistance: 2.5°C/W
Junction-to-case thermal resistance: 0.5°C/W

Junction temperature calculation:
```
Tj = Ta + (θja × Pd)
Tj = 45°C + (3.0°C/W × 19.25W)
Tj = 45°C + 57.75°C
Tj = 102.75°C
```

With 15°C margin to maximum junction temperature (125°C), the design is thermally safe.

### 4.6.3 Cooling Specifications

**Forced Air Cooling System**:

| Parameter | Specification |
|-----------|---------------|
| Fan Type | 40mm × 40mm × 10mm DC brushless |
| Operating Voltage | 12V DC |
| Operating Current | 120 mA |
| Airflow | 10 CFM |
| Static Pressure | 0.15 inch H₂O |
| Speed Control | PWM, 20-100% |
| Bearing Type | Ball bearing |
| Life Expectancy | 50,000 hours at 40°C |

**Heatsink Specifications (FPGA)**:

| Parameter | Value |
|-----------|-------|
| Material | Aluminum 6063-T5 |
| Dimensions | 45mm × 45mm × 20mm |
| Fin Count | 25 fins |
| Base Thickness | 5mm |
| Thermal Resistance | 2.5°C/W @ 200 LFM |
| Mounting | Spring-loaded push pins |
| Interface | Thermal grease, 0.1mm thickness |

**Airflow Requirements**:

| Component | Airflow (LFM) | Direction |
|-----------|---------------|-----------|
| FPGA Heatsink | 200 | Vertical |
| ADC Heatsink | 100 | Horizontal |
| Voltage Regulators | 150 | Vertical |
| Chassis Intake | 300 | Front to back |

---

## 4.7 Calibration Hardware

### 4.7.1 Reference Signal Generation

The calibration subsystem provides precision reference signals for system characterization and periodic calibration.

**Reference Oscillator**:

Device: Connor-Winfield OH200-61003CF-010.0M
- Type: Oven-Controlled Crystal Oscillator (OCXO)
- Frequency: 10.000000 MHz
- Stability: ±5 ppb (0°C to +70°C)
- Aging: < 0.5 ppb/day
- Phase Noise: -140 dBc/Hz @ 1 kHz offset
- Warm-up Time: < 5 minutes to ±50 ppb
- Power: 1.5W (steady state)

**Reference Voltage Source**:

Device: Analog Devices ADR444BRZ
- Output Voltage: 4.096V
- Initial Accuracy: ±0.04%
- Temperature Coefficient: 3 ppm/°C max
- Line Regulation: 10 ppm/V
- Load Regulation: 20 ppm/mA
- Noise: 1.5 μVpp (0.1 Hz to 10 Hz)

**Calibration Signal Generator**:

The FPGA implements a digital calibration signal generator:
- Waveforms: Sine, Square, Triangle, Ramp
- Frequency Range: 1 Hz to 10 MHz
- Amplitude Resolution: 8-bit
- Frequency Resolution: 0.01 Hz
- Output: DAC (ADS8320, 16-bit)

### 4.7.2 Calibration Procedures

**Factory Calibration**:

Performed during manufacturing to establish baseline performance:

1. **DC Offset Calibration**:
   - Apply 0V to all inputs
   - Measure ADC output codes
   - Store offset correction values in EEPROM
   - Target residual offset: < 0.5 LSB

2. **Gain Calibration**:
   - Apply +FS and -FS reference voltages
   - Calculate gain error
   - Store gain correction coefficients
   - Target gain error: < 0.1%

3. **Phase Calibration**:
   - Apply common signal to all channels
   - Measure inter-channel phase differences
   - Compute delay compensation values
   - Target phase match: < 1° at Nyquist

4. **Frequency Response**:
   - Sweep input frequency from DC to Nyquist
   - Measure amplitude response
   - Characterize filter response
   - Store compensation curves

**Field Calibration**:

User-initiated calibration procedures:

1. **Quick Calibration** (5 minutes):
   - DC offset correction
   - Gain verification
   - Noise floor measurement

2. **Full Calibration** (30 minutes):
   - Complete DC calibration
   - AC linearity verification
   - Channel matching
   - Temperature compensation update

3. **Automatic Calibration**:
   - Triggered by temperature change > 10°C
   - Background offset tracking
   - Periodic gain verification

**Calibration Data Storage**:

| Parameter | Storage Location | Size |
|-----------|------------------|------|
| Offset Coefficients | EEPROM | 16 bytes |
| Gain Coefficients | EEPROM | 16 bytes |
| Phase Delays | EEPROM | 32 bytes |
| Temperature Curves | Flash | 256 bytes |
| Factory Constants | OTP | 64 bytes |

### 4.7.3 Adjustment Mechanisms

**Analog Adjustments**:

1. **Programmable Gain Amplifier (PGA)**:
   - Device: Texas Instruments PGA280
   - Gain Range: 0.125 V/V to 128 V/V
   - Gain Steps: 0.5 dB increments
   - Bandwidth: 2 MHz at G=1
   - Interface: SPI

2. **Offset DAC**:
   - Device: Texas Instruments DAC8551
   - Resolution: 16-bit
   - Output Range: ±2.5V
   - Update Rate: 1 MSPS
   - Interface: SPI

**Digital Adjustments**:

1. **Digital Gain Correction**:
   - Multiplier: 8-bit coefficient
   - Range: 0.5× to 2.0×
   - Resolution: 0.4%

2. **Digital Offset Correction**:
   - Adder: 8-bit signed value
   - Range: -128 to +127 LSB
   - Resolution: 1 LSB

3. **Phase Correction**:
   - Programmable delay line
   - Range: 0 to 31 samples
   - Resolution: 1 sample period

**Calibration Registers**:

| Register | Address | Width | Description |
|----------|---------|-------|-------------|
| CAL_CTRL | 0x100 | 8-bit | Calibration control |
| CAL_STATUS | 0x101 | 8-bit | Calibration status |
| OFFSET_CH0 | 0x110 | 8-bit | Channel 0 offset |
| GAIN_CH0 | 0x111 | 8-bit | Channel 0 gain |
| PHASE_CH0 | 0x112 | 8-bit | Channel 0 phase |
| TEMP_COEF | 0x180 | 16-bit | Temperature coefficient |

---

## 4.8 Physical Implementation

### 4.8.1 PCB Layer Stackup

The Project 8-Bit Fusion PCB is implemented on a 12-layer board with controlled impedance for high-speed signals.

**Layer Stackup Configuration**:

| Layer | Type | Thickness | Material | Function |
|-------|------|-----------|----------|----------|
| 1 | Signal | 0.5 oz | Copper | Top signals, components |
| 2 | Ground | 1.0 oz | Copper | Solid ground plane |
| 3 | Signal | 0.5 oz | Copper | High-speed signals |
| 4 | Power | 1.0 oz | Copper | 1.0V plane |
| 5 | Signal | 0.5 oz | Copper | DDR3 address/command |
| 6 | Ground | 1.0 oz | Copper | Solid ground plane |
| 7 | Power | 1.0 oz | Copper | 1.8V, 3.3V planes |
| 8 | Signal | 0.5 oz | Copper | DDR3 data |
| 9 | Ground | 1.0 oz | Copper | Solid ground plane |
| 10 | Power | 1.0 oz | Copper | 1.5V plane |
| 11 | Ground | 1.0 oz | Copper | Solid ground plane |
| 12 | Signal | 0.5 oz | Copper | Bottom signals |

**Dielectric Specifications**:

| Parameter | Value |
|-----------|-------|
| Core Material | FR-4, Tg 170°C |
| Prepreg Material | FR-4, 2116 style |
| Dielectric Constant (εr) | 4.3 @ 1 GHz |
| Loss Tangent (tan δ) | 0.02 @ 1 GHz |
| Total Board Thickness | 1.6 mm (63 mil) |

**Controlled Impedance Requirements**:

| Signal Type | Impedance | Tolerance | Layer |
|-------------|-----------|-----------|-------|
| DDR3 Data | 40 Ω SE | ±10% | Layer 8 |
| DDR3 DQS | 80 Ω diff | ±10% | Layer 8 |
| DDR3 Clock | 100 Ω diff | ±10% | Layer 5 |
| PCIe | 85 Ω diff | ±10% | Layer 3 |
| Ethernet | 100 Ω diff | ±10% | Layer 3 |
| USB 3.0 | 90 Ω diff | ±10% | Layer 3 |

### 4.8.2 Component Placement Considerations

**Placement Strategy**:

1. **FPGA Placement**:
   - Centered on PCB for optimal routing
   - Orientation: Pin 1 toward board edge
   - Clearance: 5mm from board edge
   - Heatsink mounting holes: 4× M2.5

2. **ADC Placement**:
   - Adjacent to analog input connectors
   - Distance to FPGA: < 50mm
   - Analog inputs on opposite side from digital
   - Dedicated analog ground area

3. **DDR3 Memory Placement**:
   - Within 25mm of FPGA DDR pins
   - Fly-by topology for address/command
   - Matched trace lengths for data
   - Reference plane integrity

4. **Power Regulators**:
   - Distributed placement near loads
   - 1.0V core regulator: < 30mm from FPGA
   - Decoupling capacitors: immediate proximity
   - Thermal vias under regulators

**Critical Placement Dimensions**:

| Component | X Position | Y Position | Rotation |
|-----------|------------|------------|----------|
| FPGA (U1) | 100mm | 80mm | 0° |
| ADC (U2) | 30mm | 80mm | 90° |
| DDR3 (U3) | 100mm | 40mm | 0° |
| Ethernet PHY (U4) | 160mm | 120mm | 0° |
| PCIe Connector (J1) | 180mm | 80mm | 0° |
| Power Conn (J2) | 20mm | 20mm | 0° |

**Clearance Requirements**:

| Component Type | Minimum Clearance |
|----------------|-------------------|
| FPGA to other ICs | 5mm |
| ADC analog section | 10mm isolation |
| High-speed connectors | 3mm from board edge |
| Heatsink keepout | 2mm from components |
| Test point access | 1mm clearance |

### 4.8.3 Signal Integrity Requirements

**High-Speed Design Rules**:

1. **DDR3 Interface**:
   - Data trace length matching: ±2.5mm
   - Address/command matching: ±5mm
   - Clock-to-strobe matching: ±1mm
   - Via count: Maximum 2 per signal
   - Trace spacing: 3× dielectric thickness

2. **PCIe Interface**:
   - Lane-to-lane skew: < 5 ps
   - Total insertion loss: < 10 dB @ 5 GHz
   - AC coupling: 100nF capacitors
   - Via stub control: Back-drill if > 12 mil

3. **Ethernet Interface**:
   - RGMII trace length: < 75mm
   - Impedance control: 100 Ω differential
   - Magnetics placement: < 25mm from PHY
   - ESD protection: TVS diodes at connector

**Power Integrity Requirements**:

| Power Rail | Target Impedance | Frequency Range |
|------------|------------------|-----------------|
| 1.0V (VCCINT) | < 10 mΩ | DC to 100 MHz |
| 1.8V (VCCAUX) | < 20 mΩ | DC to 50 MHz |
| 1.5V (DDR3) | < 15 mΩ | DC to 100 MHz |
| 3.3V | < 30 mΩ | DC to 50 MHz |

**Decoupling Strategy**:

| Capacitor Value | Quantity | Location |
|-----------------|----------|----------|
| 100 μF (tantalum) | 4 | Power entry |
| 10 μF (X5R) | 16 | Near regulators |
| 1 μF (X7R) | 32 | Near FPGA pins |
| 0.1 μF (X7R) | 64 | Near FPGA pins |
| 0.01 μF (NP0) | 32 | Near high-speed ICs |

**EMI/EMC Considerations**:

- Shielding: Metal can over FPGA and ADC
- Ferrite beads: All I/O lines
- Common-mode chokes: Ethernet and USB
- Ground stitching: Every 10mm along edges
- Controlled edge rates: All high-speed signals

---

## 4.9 Performance Metrics

### 4.9.1 Processing Latency

The processing latency is defined as the time from analog input to processed data output.

**Latency Breakdown**:

| Stage | Latency | Notes |
|-------|---------|-------|
| Anti-aliasing Filter | 2 samples | Analog domain |
| ADC Conversion | 5.5 clock cycles | Pipeline delay |
| FPGA Input Buffer | 4 samples | Deserialization |
| FIR Filter (64-tap) | 32 samples | Group delay |
| Data Fusion | 8 samples | Processing delay |
| Output Formatting | 2 samples | Packetization |
| PCIe Transfer | 2 μs | DMA overhead |
| **Total Latency** | **~52 samples + 2 μs** | At 65 MSPS |

**Latency Calculations**:

At 65 MSPS sampling rate:
- Sample period: 15.38 ns
- Digital processing latency: 50 samples × 15.38 ns = 769 ns
- Total latency: 769 ns + 2000 ns = 2.77 μs

**Latency Specifications**:

| Parameter | Target | Maximum |
|-----------|--------|---------|
| Input-to-output latency | 3 μs | 5 μs |
| Channel-to-channel skew | 1 ns | 5 ns |
| Trigger-to-data latency | 1 μs | 2 μs |
| PCIe round-trip | 5 μs | 10 μs |

### 4.9.2 Throughput Specifications

**Sustained Throughput**:

| Data Path | Specification | Notes |
|-----------|---------------|-------|
| ADC Input (aggregate) | 520 MSPS | 8 channels × 65 MSPS |
| Processing Pipeline | 520 MSPS | Real-time processing |
| DDR3 Bandwidth | 12.8 GB/s | Theoretical max |
| PCIe Upload | 2 GB/s | Sustained |
| Ethernet Output | 125 MB/s | 1 Gbps |

**Data Rate Summary**:

| Mode | Input Rate | Output Rate | Processing Load |
|------|------------|-------------|-----------------|
| Raw Capture | 4.16 Gbps | 4.16 Gbps | 100% |
| Filtered Output | 4.16 Gbps | 4.16 Gbps | 85% |
| Decimated (4×) | 4.16 Gbps | 1.04 Gbps | 60% |
| Decimated (16×) | 4.16 Gbps | 260 Mbps | 30% |

**Buffer Capacities**:

| Buffer | Depth | Data Type | Duration @ 65 MSPS |
|--------|-------|-----------|-------------------|
| ADC Input | 4096 | 8-bit | 63 μs |
| Filter Output | 2048 | 8-bit | 31.5 μs |
| DDR3 Storage | 512 MB | 64-bit | 8 seconds |
| PCIe DMA | 64 MB | 64-bit | 1 second |

### 4.9.3 Accuracy/Precision Metrics

**ADC Performance**:

| Parameter | Specification | Test Condition |
|-----------|---------------|----------------|
| Resolution | 8 bits | - |
| ENOB | 7.5 bits | At Nyquist |
| SNR | 47.5 dB | Full-scale input |
| SFDR | 58 dBc | Full-scale input |
| THD | -50 dBc | Full-scale input |
| DNL | ±0.3 LSB | - |
| INL | ±0.3 LSB | - |

**System Accuracy**:

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| DC Accuracy | ±0.5% | After calibration |
| Gain Accuracy | ±0.1% | After calibration |
| Phase Accuracy | ±1° | Channel matching |
| Timing Accuracy | ±10 ppm | OCXO reference |
| Temperature Drift | 50 ppm/°C | 0°C to 70°C |

**Digital Processing Accuracy**:

| Operation | Precision | Error Source |
|-----------|-----------|--------------|
| FIR Filtering | 8-bit output | Coefficient quantization |
| IIR Filtering | 8-bit output | Accumulator truncation |
| Data Fusion | 8-bit output | Arithmetic rounding |
| Magnitude Calculation | 8-bit output | Square root approximation |

**Measurement Uncertainty**:

| Measurement | Uncertainty (k=2) | Coverage |
|-------------|-------------------|----------|
| Voltage (DC) | ±0.5 mV | Full scale |
| Voltage (AC) | ±1% | 1 kHz to 10 MHz |
| Frequency | ±0.1 ppm | 10 MHz reference |
| Time Interval | ±10 ns | Single-shot |
| Phase | ±0.5° | At 1 MHz |

---

## 4.10 Complete Parameter Tables

### Table 4.1: FPGA Resource Utilization Summary

| Resource | Used | Available | Utilization |
|----------|------|-----------|-------------|
| Logic Cells | 210,000 | 326,080 | 64.4% |
| Slice Registers | 168,000 | 407,600 | 41.2% |
| Slice LUTs | 140,000 | 203,800 | 68.7% |
| Block RAM (36Kb) | 280 | 890 | 31.5% |
| DSP48E1 Slices | 480 | 840 | 57.1% |
| MMCM | 4 | 10 | 40.0% |
| PLL | 2 | 10 | 20.0% |
| BUFG | 12 | 32 | 37.5% |
| GTX Transceivers | 8 | 16 | 50.0% |
| User I/O | 400 | 500 | 80.0% |

### Table 4.2: Clock Domain Specifications

| Clock Domain | Frequency | Source | Purpose |
|--------------|-----------|--------|---------|
| clk_sys | 100 MHz | Crystal | System logic |
| clk_adc | 125 MHz | PLL | ADC interface |
| clk_ddr | 400 MHz | MCB | DDR3 interface |
| clk_pcie | 100 MHz | External | PCIe reference |
| clk_eth | 125 MHz | PHY | Ethernet interface |
| clk_proc | 250 MHz | MMCM | DSP processing |

### Table 4.3: Power Consumption Budget

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| FPGA VCCINT | 1.0V | 8.5A | 8.5W |
| FPGA VCCBRAM | 1.0V | 1.2A | 1.2W |
| FPGA VCCAUX | 1.8V | 0.8A | 1.44W |
| FPGA VCCO (various) | 1.5-3.3V | 1.3A | 3.5W |
| FPGA GTX | 1.0/1.2V | 4.0A | 4.3W |
| ADC | 3.3/1.8V | 410mA | 1.35W |
| DDR3 Memory | 1.5V | 270mA | 0.4W |
| Ethernet PHY | 1.0/2.5V | 280mA | 0.7W |
| USB PHY | 3.3V | 150mA | 0.5W |
| Regulators (loss) | - | - | 4.0W |
| Miscellaneous | - | - | 2.0W |
| **Total** | - | - | **28.8W** |

### Table 4.4: ADC Performance Specifications

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Resolution | 8 | bits | - |
| Sampling Rate | 65 | MSPS | Per channel |
| Channels | 8 | - | Simultaneous |
| Input Range | 2.0 | Vpp | Differential |
| Input Bandwidth | 300 | MHz | -3dB |
| SNR | 47.5 | dB | @ Nyquist |
| SFDR | 58 | dBc | @ Nyquist |
| ENOB | 7.5 | bits | @ Nyquist |
| DNL | ±0.3 | LSB | - |
| INL | ±0.3 | LSB | - |
| Power | 1.35 | W | All channels |

### Table 4.5: Memory Specifications

| Memory Type | Device | Capacity | Speed | Interface |
|-------------|--------|----------|-------|-----------|
| FPGA BRAM | XC7K325T | 16,020 Kb | 500 MHz | Internal |
| External DDR3 | MT41K256M16 | 4 Gb | 1600 MT/s | 16-bit |
| Configuration Flash | N25Q256A | 256 Mb | 108 MHz | QSPI |
| EEPROM | 24LC256 | 256 Kb | 400 kHz | I2C |

### Table 4.6: Interface Specifications

| Interface | Standard | Data Rate | Connector | Cable |
|-----------|----------|-----------|-----------|-------|
| PCIe | Gen2 x4 | 16 Gbps | Edge card | - |
| Ethernet | 1000BASE-T | 1 Gbps | RJ45 | Cat5e/6 |
| USB | USB 3.0 | 5 Gbps | Micro-B | USB 3.0 |
| JTAG | IEEE 1149.1 | - | 10-pin header | - |
| Analog Input | - | - | BNC (8×) | Coax |
| GPIO | LVCMOS33 | - | 40-pin header | - |

### Table 4.7: Physical Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| PCB Dimensions | 200 × 150 | mm |
| PCB Layers | 12 | - |
| PCB Thickness | 1.6 | mm |
| FPGA Package | FFG900 | - |
| Operating Temperature | 0 to 70 | °C |
| Storage Temperature | -40 to 100 | °C |
| Relative Humidity | 5 to 95 | % |
| Altitude | 0 to 3000 | m |

### Table 4.8: Performance Summary

| Metric | Value | Unit |
|--------|-------|------|
| Maximum Sampling Rate | 65 | MSPS/ch |
| Total Throughput | 520 | MSPS |
| Processing Latency | 2.8 | μs |
| PCIe Bandwidth | 2 | GB/s |
| Power Consumption | 28.8 | W |
| ENOB | 7.5 | bits |
| Channel Isolation | 75 | dB |
| Trigger Latency | 1 | μs |

### Table 4.9: Calibration Parameters

| Parameter | Range | Resolution | Accuracy |
|-----------|-------|------------|----------|
| Gain Adjustment | 0.5-2.0× | 0.4% | 0.1% |
| Offset Adjustment | ±128 LSB | 1 LSB | 0.5 LSB |
| Phase Adjustment | 0-31 samples | 1 sample | 0.1 sample |
| Temperature Compensation | -40 to +85°C | 0.1°C | 1°C |
| Reference Frequency | 10 MHz | 0.01 Hz | 5 ppb |

### Table 4.10: Environmental Specifications

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Operating Temperature | 0°C to +70°C | Commercial grade |
| Storage Temperature | -40°C to +100°C | Non-operating |
| Operating Humidity | 5% to 95% RH | Non-condensing |
| Altitude | 0 to 3,000 m | Operating |
| Vibration | 2 g RMS | 5-500 Hz |
| Shock | 30 g | 11 ms half-sine |
| ESD Protection | ±8 kV | Contact discharge |

---

## 4.11 Summary

This chapter has presented the comprehensive hardware specifications for Project 8-Bit Fusion, a high-performance digital signal processing platform designed for multi-channel data acquisition and real-time processing. The system architecture centers on a Xilinx Kintex-7 FPGA implementing an 8-bit fixed-point processing pipeline, interfacing with eight channels of 65 MSPS ADCs and supporting high-speed communication via PCIe Gen2, Gigabit Ethernet, and USB 3.0.

Key specifications include:
- Total system throughput of 520 MSPS across eight channels
- Processing latency of approximately 2.8 microseconds
- Power consumption of 28.8 watts with comprehensive thermal management
- 7.5 effective bits of resolution with optimized 8-bit quantization
- Comprehensive calibration subsystem with OCXO reference

The hardware design balances performance, power efficiency, and cost-effectiveness, making it suitable for research applications in experimental physics requiring high-throughput data acquisition with real-time processing capabilities. The modular architecture allows for future expansion and adaptation to specific experimental requirements.

---

## References

1. Xilinx, "7 Series FPGAs Overview," DS180 (v1.17), 2018.
2. Texas Instruments, "ADS5273 8-Channel, 65MSPS Analog-to-Digital Converter," Datasheet, 2015.
3. Micron Technology, "DDR3 SDRAM MT41K256M16," Datasheet, 2019.
4. PCI-SIG, "PCI Express Base Specification Revision 2.1," 2009.
5. IEEE, "IEEE Std 802.3-2018 - IEEE Standard for Ethernet," 2018.
6. USB Implementers Forum, "Universal Serial Bus 3.0 Specification," 2011.

---

*Document Version: 1.0*
*Last Updated: 2024*
*Author: Dean Kulik (ORCID: 0009-0003-3128-8828)*
