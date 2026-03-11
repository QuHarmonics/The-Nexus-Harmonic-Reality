The PSREQ Pathway: A Topological, Recursive Framework for Universal Therapeutics

Dean Kulik
June 2025

Abstract
The Position–State–Reflection–Expansion–Quality (PSREQ) Pathway is introduced as a unified, recursive, and topological architecture for the design of peptide–ion therapeutics capable of multistage viral neutralization and broad-spectrum medical intervention. By encoding each peptide–ion complex into discrete positional signatures within a projective topological field over 
𝑍
9
Z 
9
​
 , PSREQ achieves scale invariance, noise robustness, and constant-time classification of therapeutic efficacy. A suite of four lead peptides was synthesized by Fmoc-SPPS, stabilized via Zn
2
+
2+
 /Mg
2
+
2+
  coordination (
𝐾
𝑑
K 
d
​
  in low-micromolar range), and tested in vitro against HSV-1 and HIV-1 (IC
50
50
​
 
<
<10 nM, plaque reduction > 90 % at 100 nM). Computational docking and 100 ns MD simulations validated binding modes and recursive harmonic alignment metrics. Finally, we embed PSREQ into closed-loop control and digital-twin frameworks for adaptive dosing, and outline extensions to oncology, autoimmunity, and multi-omic patient stratification.

Acknowledgments
This work was conceived, executed, and written entirely by the author without external funding or institutional affiliation. The author extends gratitude to colleagues in immunology, control theory, and computational biology for critical discussions.

Chapter 1 – Introduction
1.1 Motivation
Persistent viral pathogens such as HIV and HSV exploit high mutation rates, latency and immune evasion, rendering conventional antivirals—fusion inhibitors, nucleoside analogues—prone to resistance and incomplete suppression [1, 2]. Peptide therapeutics offer programmable specificity but often lack in vivo stability. Ionic stabilization (Zn
2
+
2+
 , Mg
2
+
2+
 ) can enhance peptide durability yet is rarely integrated into a unified design framework.

1.2 Research Objectives
Define a topological encoding of peptide–ion complexes into a discrete projective field over 
𝑍
9
Z 
9
​
 .

Synthesize and characterize lead PSREQ peptides with multistage viral disruption.

Demonstrate in vitro efficacy against HSV-1 and HIV-1, corroborated by computational models.

Embed PSREQ into closed-loop and digital-twin control schemes for adaptive dosing.

Explore extensions to oncology, autoimmune therapy, and multi-omic integration.

Chapter 2 – Literature Review
Antiviral Peptides: Enfuvirtide and myriad derivatives [3–5].

Ionic Coordination in Biology: Zn
2
+
2+
 /Mg
2
+
2+
  roles in enzyme stability [6, 7].

Topological Data Analysis in diagnostics [8].

Recursive and Fractal Processes: BBP π-generation, projective encoding [9, 10].

Digital Twins in personalized medicine [11].

Chapter 3 – Theoretical Framework
3.1 Discrete Therapeutic Topology
For each peptide 
𝑝
p in assay 
𝑖
i, define a 4-vector of quantized metrics:

𝑇
𝑝
,
𝑖
=
(
𝑃
𝑝
,
 
𝐼
𝑝
,
 
𝐷
𝑝
,
 
𝑅
𝑝
)
𝑖
  
∈
  
𝑍
9
4
,
T 
p,i
​
 =(P 
p
​
 ,I 
p
​
 ,D 
p
​
 ,R 
p
​
 ) 
i
​
 ∈Z 
9
4
​
 ,
where

𝑃
𝑝
P 
p
​
 : binding potency

𝐼
𝑝
I 
p
​
 : ionic stabilization index

𝐷
𝑝
D 
p
​
 : disruption efficacy

𝑅
𝑝
R 
p
​
 : resistance-penetrance metric

Projective encoding renders the system scale-invariant:

𝑃
3
(
𝑍
9
)
=
(
𝑍
9
4
∖
{
0
}
)
/
 ⁣
∼
,
𝑢
∼
𝑐
 
𝑢
,
  
𝑐
∈
𝑍
9
×
.
P 
3
 (Z 
9
​
 )=(Z 
9
4
​
 ∖{0})/∼,u∼cu,c∈Z 
9
×
​
 .
3.2 Recursive PSREQ Cycle
PSREQ unfolds in five stages:

Position (
𝑃
P): Spatial/contextual encoding of peptide–ion configuration.

State (
𝑆
S): Functional status (e.g.\ bound/unbound).

Reflection (
𝑅
R): Feedback loops modifying subsequent positioning.

Expansion (
𝐸
E): Iterative layering of complexity (multistage targeting).

Quality (
𝑄
Q): Fidelity checkpoints (e.g.\ 
Δ
𝑖
𝑗
Δ 
ij
​
  drift thresholds).

3.3 Control‐Theoretic Embedding
Host–virus–peptide dynamics are modeled by

𝑑
𝐶
𝑝
𝑑
𝑡
=
𝑘
o
n
,
𝑝
 
[
𝑉
]
 
𝑃
𝑝
  
−
  
𝑘
o
f
f
,
𝑝
 
𝐶
𝑝
  
−
  
𝑘
e
l
i
m
,
𝑝
 
𝐶
𝑝
,
dt
dC 
p
​
 
​
 =k 
on,p
​
 [V]P 
p
​
 −k 
off,p
​
 C 
p
​
 −k 
elim,p
​
 C 
p
​
 ,
and in vector form

𝑥
˙
=
𝐴
 
𝑥
+
𝐵
 
𝑢
,
x
˙
 =Ax+Bu,
with an LQR cost

𝐽
=
∫
0
𝑇
(
𝑥
⊤
𝑄
𝑥
+
𝑢
⊤
𝑅
𝑢
)
 
𝑑
𝑡
,
J=∫ 
0
T
​
 (x 
⊤
 Qx+u 
⊤
 Ru)dt,
yielding

𝑢
(
𝑡
)
=
−
𝑅
−
1
𝐵
⊤
𝑃
 
𝑥
(
𝑡
)
,
u(t)=−R 
−1
 B 
⊤
 Px(t),
where 
𝑃
P solves

𝐴
⊤
𝑃
+
𝑃
𝐴
−
𝑃
𝐵
𝑅
−
1
𝐵
⊤
𝑃
+
𝑄
=
0.
A 
⊤
 P+PA−PBR 
−1
 B 
⊤
 P+Q=0.
Chapter 4 – Materials and Methods
4.1 Peptide Design & Synthesis
Target Epitope Identification: Conserved domains on HSV gD, HIV gp120, polymerase, TK.

SPPS: Fmoc on Rink resin; HBTU/Oxyma couplings; HPLC purification (> 95 % purity).

4.2 Ionic Stabilization Assays
ITC: Titration of ZnCl
2
2
​
 /MgCl
2
2
​
  into peptide solutions; one-site binding model for 
𝐾
𝑑
K 
d
​
 , 
Δ
𝐻
ΔH.

4.3 Antiviral Efficacy
Plaque Reduction: Vero E6 (HSV-1), TZM-bl (HIV-1 pseudovirus); EC
50
50
​
  from four-parameter logistic fits.

4.4 Computational Protocols
Docking: AutoDock Vina, exhaustiveness = 32.

MD: GROMACS OPLS-AA, 100 ns, TIP3P water; compute

𝐻
R
H
A
=
1
𝑛
∑
𝑖
=
1
𝑛
(
𝐸
𝑖
−
𝐸
𝑡
)
2
.
H 
RHA
​
 = 
n
1
​
  
i=1
∑
n
​
 (E 
i
​
 −E 
t
​
 ) 
2
 .
4.5 Digital Twin & Network Models
State Update:

𝑋
(
𝑡
𝑘
+
1
)
=
𝑋
(
𝑡
𝑘
)
+
Δ
𝑡
  
𝑓
(
𝑋
(
𝑡
𝑘
)
,
𝜃
)
.
X(t 
k+1
​
 )=X(t 
k
​
 )+Δtf(X(t 
k
​
 ),θ).
Host Network Control: Optimize