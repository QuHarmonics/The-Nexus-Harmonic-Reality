---
title: "The Nexus 4 Framework - Article144"
source_pdf: "The Nexus 4 Framework - Article144.pdf"
created_utc: "2025-11-27T11:10:05.8336849Z"
page_count: 6
---

# The Nexus 4 Framework - Article144

## Extracted Text

```text
----------- Page1 ------------
Abstract
Harmonics are the major issues in Variable Frequency Drive systems. The objective of project is the analysis of harmonics
in the signatures of motor current in various fault conditions of Variable Frequency Drive systems. The simulation is
done on VSI fed induction motor at constant voltage/frequency and was carried out using MATLAB/ Simulink. Variable
Frequency drives commonly uses “Insulated Gate Bipolar Transistor” (IGBT).To get sine wave at required frequency IGBT
uses “Pulse Width Modulation” technique for simulation. Simulation of an induction was developed and by observing
the current, torque and speed responses, its dynamic response was verified to set up the acceptability of the developed
system. Simulation of three various fault conditions were carried out here: one IGBTs gate signal is open circuited, one
IGBT in the inverter section is blown off, line to ground fault occurs in one phase of the motor terminal. The technique of
frequency domain analysis is used as a method to discriminate various faulty conditions. For various faulted conditions
frequency responses characteristics were analyzed and collated to setup the use of Fast Fourier Transform algorithm to
distinguish the characteristics of fault. Frequency responses of three various faulty states were emphatically different and
were indubitably shown.
Harmonic Analysis of Inverter-Fed Induction Motor
Drive System under Fault Conditions using FFT
Prathibha S. Babu*
Department of Electrical and Electronics Engineering, Amrita School of Engineering, Amritapuri, Amrita Vishwa
Vidyapeetham, Kerala-690525 Amrita University, India; prathibhababu@am.amrita.edu
Keywords:
Fast Fourier Transform, Insulated Gate Bipolar Transistor, Pulse Width Modulation, Variable Frequency Drive
1. Introduction
Induction motors are the vital element of any industrial
operation and they are regularly integrated for industrial
operations and commercial available equipments. Core
capabilities often provide by motor-driven equipments
are needed for business comfort and equipment and per-
sonal safety. They are broadly used motors for industrial
control appliances, so they are known as the “workhorse
of the motion industry” . They are authentic, robust and
sturdy. In early periods induction motors constant speed
motor and now changed to a “variable speed, variable
torque machine” . DC motors can be controlled easily at
low power applications so it has undergone many evolu-
tions. Induction motors are efficiently used in applications
that require huge amounts of torque and power. The use of
an induction motor has increased by a large amount with
the innovation of “Variable Voltage, Variable Frequency
drives” . The speed control of 3-phase squirrel cage IM over
a wide range by varying the frequency of stator and are
done with Variable frequency VSI’s. So the Voltge Source
Inverters are commonly preferred for medium power to
maximum power variable speed drive systems in indus-
tries or driving parallely connected group of motors.
Most advanced variable frequency drives operates with
rectifier which converts a 3φ voltage source to DC. Then
a DC bus stores the rectified power. A capacitor is used
in the DC link in order to retrieve and stores the power
from the rectifier, and the power is fed to the inverter.
Transistors are used in inverter for delivering power to
the motor. The “Insulated Gate Bipolar Transistor” is gen-
erally used in modern VFDs. The IGBT switches on and
off several times in a second and indubitably the power
is controlled and brought to the motor. The technique of
“Pulse Width Modulation” (PWM) is applied here for the
*Author for correspondence
Indian Journal of Science and Technology, Vol 9(S1),
DOI: 10.17485/ijst/2016/v9iS1/108359, December 2016
ISSN (Print) : 0974-6846
ISSN (Online) : 0974-5645----------- Page2 ------------
Harmonic Analysis of Inverter-Fed Induction Motor Drive System under Fault Conditions using FFT
Indian Journal of Science and Technology
2
Vol 9 (S1) | December 2016 | www.indjst.org
simulation of a sine wave at the required frequency to the
motor.
The 3Φ stator winding of IM is excited by the 6-step
VSI .V/f control is used here. Such an induction motor is
simulated and its dynamic responses are validated from the
current, torque and speed characteristics to make adequacy
of the system. Simulations of three different post faults are
carried out here: one IGBTs gate signal is open circuited,
one IGBT in the inverter section is blown off, line to ground
fault occurs in one phase of the motor terminal. Then ana-
lyze the frequency domain and time domain under these
faulty conditions to discriminate fault types.
2. System Configuration
Figure 1 shows the proposed system block diagram. To
the VSI fed induction motor a three phase supply is given
as input. The rectifier is uncontrolled and is preceded by a
dc link capacitor in the first stage. IGBT switches are used
in Inverter to controls the Induction motor. The controller
used is sinusoidal pulse width modulator (SPWM) which
generates the control signals for switches. By adjusting
the control parameters the frequency and motor termi-
nal voltage magnitude are adjusted, in order to maintain
‘V/f’ ratio constant. In this model, the induction motor is
applied by a constant torque load.
2.1 Substantiation of the Simulation Model
After simulating the model, by analyzing the dynamic
response of the motor drive system such as rotor cur-
rent, speed, torque, the reliability and performance of
the model have been verified. Figure 2 shows Rotor cur-
rent v/s Time characteristics, Figure 3 shows Speed v/s
Time characteristics and Figure 4 shows Torque v/s Time
characteristics.
By analyzing the above profiles it can be finalize that
the model is crystal clear.
2.2 Conditions under Study
Simulation studies were done on a 3Φ IM. Different faulty
conditions were created in the simulated model by the
three different ways.
One IGBT’s gate signal is open circuited 1.
One IGBT in the inverter section is blown off 2.
One phase of the motor terminal is given a line to 3.
ground fault. Figure 1. Induction Motor Drive System.
Figure 2. Rotor Current v/s Time.
Figure 3. Speed v/s Time.
Figure 4. Torque v/s Time.----------- Page3 ------------
Prathibha S. Babu
Indian Journal of Science and Technology
3
Vol 9 (S1) | December 2016 | www.indjst.org
3. Results of Simulation
3.1 One IGBTs Gate Terminal is Open
Circuited
In this case, phase A ’s upper IGBT is grounded for obtaining
the simulation in the specified condition. Motor-current
signatures of phases A and B are displayed. Figure 5 shows
the A phase motor current signature and Figure 6 shows
the B and C phase Motor-current signatures with Fault at
IGBT gate terminal in phase A.
Figure 7. Shows FFT of A phase motor-current signa-
ture at the condition of the motor working at a speed of
314 rpm and Figure 8. Shows the FFT of A phase motor-
current signature at the condition of the motor working
at a speed of 376 rpm.
Figure 9. shows FFT of B and C phase motor-current
signature at the condition of the motor working at a
speed of 314 rpm and Figure 10. shows the FFT of B and
C phase motor-current signature at the condition of the
motor working at a speed of 376 rpm.
From Figure 7 and Figure 9, it is obvious that the FFT
signatures of the phase-A and the salutary motor FFT
signature are not matching.
Figure 7. FFT of A phase motor current signature when
motor is at a speed of 376 rpm
Figure 5. A phase Motor-current signature with Fault at
IGBT gate terminal in phase A.
Figure 6. B and C phase Motor-current signature with
Fault at IGBT gate terminal in phase A.
Figure 8. FFT of A phase motor current signature when
motor is at a speed of 314 rpm
Figure 9. FFT of B and C phase motor current signature
the motor is at a speed of 314 rpm
Figure 10. FFT of B and C phase motor current when
signature when the motor is at a speed of 376 rpm----------- Page4 ------------
Harmonic Analysis of Inverter-Fed Induction Motor Drive System under Fault Conditions using FFT
Indian Journal of Science and Technology
4
Vol 9 (S1) | December 2016 | www.indjst.org
3.2 One IGBT in the Inverter Section is
Blown Off
The IGBT in the upper section of phase A was replaced
and a high resistance is introduced for the simulation of
the condition in the system. This condition in simulation
can be done by the addition of the high resistance along
with one of the six IGBTs. The motor -current signatures
are displayed and FFT profiles are obtained for analyzing
and comparing with the salutary motor drive system. The
current-signatures of the motor are shown in Figure 11
and corresponding FFT profile with motor working at a
speed of 314 rpm and 376 rpm are showed in the Figure
12 and Figure 13 respectively.
3.3 Line to Ground Fault Occurs at the
Motor Terminal’s One Phase
A switch is introduced in the phase A for this type of
simulation. At first open condition is made in the switch,
i.e. phase-A is a healthy. A fault of line to ground is cre-
ated at Phase-C. Here the fault is occurred in the period
from 9s to 9.5s .The motor-current profiles are displayed.
To the motor current signatures, FFT is applied to obtain
frequency domain. Frequency domain of three phases of
Figure 11. Current-profile of motor in phase A when one
IGBT is blown.
Figure 12. FFTs of Motor-current signature of phase A
when the motor is at speed 314 rpm
Figure 13. FFTs of Motor-current signature of phase A
when the motor is at speed 376 rpm
Figure 14. Current profiles of motor in phase A, Band C
when line to ground fault occurs in phase A
Figure 15. FFT of motor-current profile of phase A when
line to ground fault occur in phase A, the motor is at speed
314 rpm.
Figure 16. FFT of motor-current profile of phase A ground
fault occur in phase A, the motor is at a speed of 376 rpm.----------- Page5 ------------
Prathibha S. Babu
Indian Journal of Science and Technology
5
Vol 9 (S1) | December 2016 | www.indjst.org
current signatures of motor are shown in the Figure14
Figure 15 shows the FFT of motor current profile at
phase A when line to ground fault occur in phase A and
the motor is at speed 314 rpm and Figure 16 shows the
FFTs of motor current profile of phase-A when line to
ground fault occur in phase A and the motor is at speed
376 rpm.
4. Conclusion
In order to discriminate various fault states, frequency
domain analysis technique was used. The frequency
responses for various faultly conditions were analysed and
their FFTs were compared to distinguish the fault’s nature.
Frequency responses of the three disparate faulty condi-
tions, one of the six IGBT’s gate signal is open circuited,
one IGBT in the inverter section is blown off, line to
ground fault occurs at the motor terminal’s one phase, are
distinctly different. Hence, by analyzing FFT profiles, we
can identify which type of fault is occurred.
5. References
1. Biswas B, Das S, Purkait P , Mandal MS and Mitra D. Current
Harmonics Analysis of Inverter-Fed Induction Motor Drive
System under Fault Conditions. Hong Kong: IMECS 2009,
Proc. International Multi Conference of Engineers and
Computer Scientists. 2009 March 18–20; II.
2. Namburi NR and Barton TH. Time Domain Response
of Induction Motors with PWM Supplies, IEEE Trans.
Industry Applications. 1985 Mar; IA-21(2):448–55.
3. Sun L, Li Heming H, and Xu B. Analysis on the transient of
stator-rotor-hybrid fault in squirrel cage induction motors,
in Proc. 2005 ICEMS Eighth International Conference on
Electrical Machines and Systems, 2005 Sept; 3:1939-44.
4. Jung JH, Lee JJ and Kwon BH. Online Diagnosis of Induction
Motors Using MCSA, IEEE Trans. Industrial Electronics,
2006 Dec.; 53(6):1842–52.
5. Benbouzid BEH. A review of induction motors signature
analysis as a medium for faults detection, IEEE Trans.
Industrial Electronics. 2000 Oct; 47(5):984–93.
6. Blodt M, Regnier J, Chabert M and Faucher J. Fault Indicators
for Stator Current Based Detection of Torque Oscillations in
Induction Motors at Variable Speed Using Time-Frequency
Analysis, in Proc. The 3rd IET International Conference
on Power Electronics, Machines and Drives. 2006 Mar;
p. 56–60.
7. Hwang DH, Lee KC, Kim YJ, Bae SW , Kim DH and Ro CG.
Voltage stresses on stator windings of induction motors
driven by IGBT PWM inverters. Proc. 38th IAS Annual
Meeting. Conference Record of the Industry Applications
Conference. 2003 Oct; 1:439- 44.
8. Hwang DH, Kim YJ, Bae SW , Kim DH, Ro CG and Lee IW .
Analysis of voltage stress in stator winding of IGBT PWM
inverter-fed induction motor systems. Proc. ICEMS 2003
Sixth International Conference on Electrical Machines and
Systems. 2003 Nov; 1:440–44.
9. Eason G, Noble B and Sneddon IN. On certain integrals
of Lipschitz-Hankel type involving products of Bessel
functions. Phil. Trans. Roy. Soc. London. 1955 April;
A247:529–51.
10. Reshma NR and Babu Prathibha S. A method for error
detection and correction of the PMU measurements.
International Conference on Computation of Power,
Energy, Information and Communication (ICCPEIC).
2014; p. 99–103.
11. Jacobs IS and Bean CP . New York: Academic: Fine particles,
thin films and exchange anisotropy, in Magnetism. III, G.T.
Rado and H. Suhl, Eds. 1963; p. 271-350.
12. Yorozu, Hirano M, Oka K and Tagawa Y . Electron spec-
troscopy studies on magneto-optical media and plastic
substrate interface. IEEE Transl. J. Magn. Japan. 1987
August; 2:740–41. [Digests 9th Annual Conf. Magnetics
Japan. 1982; p. 301]
13. Discenzo FM. et al. Motor diagnostics: Technological driv-
ers leading to 21st century predictive diagnostics. Knoxville,
TN: Proc. Int. Conf. Maintenance and Reliability. 1997;
1:30.01–12.
14. Bonnett AH. et al. Cause and analysis of stator and rotor
failures in three-phase squirrel-cage induction motors,
IEEE Trans. Ind. Applicat. 1992 July/Aug; 28:921–37.
15. Vas P . Parameter Estimation, Condition Monitoring, and
Diagnosis of Electrical Machines. Oxford, U.K.: Clarendon,
1993. [19] Kliman GB. et al. Methods of motor current sig-
nature analysis. Elect. Mach. Power Syst. 1992 Sept; 20(5):
463-74.
16. Benbouzid MEH.et al., “Induction motor diagnos-
tics via stator current monitoring,” in Proc. 1997 Int.
Conf. Maintenance and Reliability, vol. 1, Knoxville, TN,
pp. 36.01–36.10.
17. Kryter RC. et al. Condition monitoring of machinery using
motor current signature analysis. Sound Vib. 1989 Sept;
p. 14–21,
18. Subhasis Nandi, Thirumarai Chelvan Ilamparithi, Sang Bin
Lee and Doosoo Hyun. Detection of Eccentricity Faults in
Induction Machines Based on Nameplate Parameters. IEEE
Transactions on Industrial Electronics. 2011 May; 58(5).
19. Nandi S, Bharadwaj RM and Toliyat HA. Performance
analysis of a three phase induction motor under incipient
mixed eccentricity condition. IEEE Trans. Energy Convers.
2002 September; 17(3):392–99.----------- Page6 ------------
Harmonic Analysis of Inverter-Fed Induction Motor Drive System under Fault Conditions using FFT
Indian Journal of Science and Technology
6
Vol 9 (S1) | December 2016 | www.indjst.org
20. Li X, Wu Q and Nandi S. Performance analysis of a three-
phase induction machine with inclined static eccentricity.
IEEE Trans. Ind. Appl. 2007 March/April; 43(2):531–41.
21. Pedro Vicente Jover Rodriguez, Marian Negrei and Antero
Arkkio. A General Scheme for Induction Motor Condition
Monitoring. Vienna, Austria: SDEMPED 2005, International
Symposium on Diagnostics f or Electric Machines, Power
Electronics and Drives. 2005 September 7–9.
22. Kliman GB, Koegl RA. Stein J and Endicott RD. Noninvasive
Detection of Broken Rotor Bars in Operating Induction
Motors. IEEE Trans. Energy Conversion. 1988 December;
3:873–79.
23. Joksimovic GM and Penman J. The Detection of Inter-
Turn Short Circuits in the Stator Winding of Operating
Motors. IEEE Transactions on Industrial Applications.
2000 October; 47(5):1078 –84.
24. Gu IYH and Bollen MHJ. Estimating interharmonics by
using sliding window ESPRIT. IEEE Trans. Power Deliv.
2008; 23(1):13-23.
25. Bollen MHJ, Gu IYH, Santoso S, McGranaghan MF,
Crossley PA, Ribeiro MV , and Ribeiro PF. Bridging the gap
between signal and power. IEEE Signal Process. Mag. 2009;
26(4):12– 31.
26. Liem Ek Bien & Sudarno. Testing Harmonics and Harmonic
Disorder Reduction Efforts in Energy Efficient Lighting.
Trisakti University, 2004.
27. Elih Mulyana. Measurement of Voltage and Current
Harmonic Generation in the UPI ICT Directorate Building.
Indonesia Educational University. 2008.
28. Irianto, Sukmawidjaja CG, M Wisnu A. Reducing Harmonics
in Three Phase Transformers. Trisakti University. 2008.
29. Mini R, Shabana Backer, Hariram Satheesh B, Dinesh
MN. MRAS Speed Observer for Low Speed Estimation
in Sensorless DTC-SVM Induction Motor Drives.
International journal of Applied Engineering Research.
2015; 10(17):37751–57.
30. Priya S, Rashmi MR, Suresh A. A Novel Scheme for
Reduction of Torque Ripple in Direct Torque Control of
Three Phase Squirrel Cage Induction Motor Using Seven
Level Neutral Point Clamped Inverter. Journal of Applied
Sciences, Engineering and Technology. ISSN: 2040-7459;
e-ISSN: 2040–7467.
```
