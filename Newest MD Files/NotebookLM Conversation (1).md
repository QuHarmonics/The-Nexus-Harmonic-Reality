> From: https://notebooklm.google.com/notebook/5d62240d-4c52-41b2-9298-e2b2145ea502

# notebooklm response

These sources present a technical investigation into the **transport geometry** of the SHA-256 cryptographic hash function, challenging the idea that its internal mixing is a generic process of diffusion. The research establishes that **word entry time** acts as a measurable coordinate for how perturbations move through the system, creating a visible gradient when inputs are **temporally staggered**. While these effects are prominent within a single data block, the study identifies **simultaneity nulls** at the bit level and across block boundaries where the geometry collapses. Furthermore, the authors introduce the **capacity-gated projection law** to explain why strong recursive echoes in the message schedule often fail to produce new activity in the compression state. Ultimately, the work characterizes the state-space as a **capacity-limited projector** that bottlenecks signals once its support manifold is saturated. This analysis is supported by a **companion workbook** designed to provide empirical verification through a series of algorithmic probes and data visualizations.

---

# you asked

new exciting data on the nexus framework

---

# notebooklm response

The recent data regarding the Nexus framework, particularly as of April 2026, centers on a shift from treating cryptographic functions and arithmetic as "black boxes" to viewing them as **structured geometric environments** [1-3]. This evolution is driven by new empirical findings in SHA-256 transport geometry and a foundational reinterpretation of what a "number" actually is [1, 3].

### 1. The Capacity-Gated Projection Law
A primary breakthrough in the framework is the discovery of the **Capacity-Gated Projection Law**, which provides a quantitative bridge between internal message schedules and visible state changes [4, 5]. The law is defined by the formula:
$$N_{\text{state}}(k,r) \approx \alpha^* H_{\text{sched}}(k,r) C(k,r)^{\beta^*}$$
with fitted parameters **$\alpha^* \approx 10.46$** and **$\beta^* = 0.65$** [6]. 

This data is "exciting" because it resolves a long-standing paradox: while perturbations in SHA-256 recur unconditionally and increase in "schedule space" (with mean echo amplitudes growing from 1.0 to over 16.1), they often produce **zero new support** in the "state space" [7-9]. The Nexus framework explains this by identifying the state as a **nonlinear projector**; it only admits new information if there is remaining "unsaturated capacity" [10, 11]. Once the primary wave consumes the 256-bit support manifold, later echoes are not destroyed but are **bottlenecked** or projected below the visibility threshold [9, 12, 13].

### 2. SHA-256 as a Layered Transport Machine
The framework has moved beyond describing SHA-256 as "generic diffusion" or "shredding" [2, 14]. Instead, new data reveals a **four-stage system** [15, 16]:
*   **Entry:** Staggered word injection ($t=k$) creates a visible transport gradient [15, 17].
*   **Branch:** The recursive schedule topology forces later echoes shaped by **recursive path multiplicity** [15, 18].
*   **Saturate:** Cumulative support grows until remaining capacity ($C(k,r)$) hits zero, causing the state to reject further echoes as support-forming waves [19].
*   **Reset:** At the block boundary, the chaining state injects simultaneously, which **erases the age structure** while preserving magnitude [19, 20].

Empirical measurements show that word entry time acts as a **direct time coordinate**, with the saturation wavefront advancing almost perfectly at a slope of **+0.9991 rounds per word** [21].

### 3. Numbers as Collapsed Event-Histories
On a foundational level, the Nexus framework has introduced a "operator-first" ontology where **numbers are residues of lawful event-histories** [3, 22]. Key concepts in this new data include:
*   **The Stack as Geometry:** The stack is the minimal model of computation, where "shape" records the current configuration and "path" records the sequence of operations that produced it [23, 24].
*   **Arithmetic as Path Composition:** Addition is redefined as continuing one event history with another, while multiplication is **repeated path composition** [25].
*   **Constants as Operator Stances:** Constants (like a modulus or saturation width) are no longer viewed as passive values but as **parameters that choose how event space is shaped** [26].

### 4. Harmonic Attractor identification
A particularly intriguing interpretive finding links the empirical SHA-256 data back to broader Nexus theory [14]. The fitted capacity exponent **$\beta^* = 0.65$** suggests a complementary headroom value of **$0.35$** [27]. The framework identifies this with the **harmonic attractor $H = \pi/9 \approx 0.349$** [27]. This identifies SHA-256 as a "constrained folding environment" that preserves ordered informational lineage even when it appears to be destroying it [11, 14].

In summary, the latest Nexus data suggests that what we perceive as static numbers or chaotic cryptographic diffusion are actually **stabilized residues of lawful verbs** acting within finite geometric apertures [11, 28].

---

# you asked

Explain recursive path multiplicity in the schedule graph.

---

# notebooklm response

**Recursive path multiplicity** is a concept within the Nexus framework that explains why later perturbations in the SHA-256 message schedule produce much stronger echoes than earlier ones, a phenomenon known as the **"secondary tail"** [1, 2]. Instead of viewing message schedule propagation as simple "landing arithmetic," this concept treats the schedule as a **branching field** where information flows through multiple recursive dependencies [3, 4].

### 1. The Recursive Mechanism
The SHA-256 message schedule is defined by a recursive formula where each word $W[t]$ (for $t \ge 16$) is derived from four previous words:
$$W[t] = W[t - 16] + \sigma_1(W[t - 15]) + W[t - 7] + \sigma_0(W[t - 2]) \pmod{2^{32}}$$ [5, 6].
Because of this structure, a single perturbation in an initial source word $W[k]$ does not just reappear once; it branches out and reaches deeper stages of the schedule through **multiple independent paths** [2, 3].

### 2. The Path-Multiplicity Matrix ($P$)
To quantify this effect, the framework introduces a **path-multiplicity matrix**. This matrix counts the number of recursive dependency routes through which a source word $W[k]$ can influence a later schedule position $W[i]$ [2, 7]. The matrix is calculated as follows:
*   **Base Case:** $P_{i,k} = 1$ when $i = k$ (the initial injection) [2, 7].
*   **Recursive Step:** $P_{i,k} = P_{i-2,k} + P_{i-7,k} + P_{i-15,k} + P_{i-16,k}$ for all $i \ge 16$ [2, 7].

### 3. Three Regimes of Influence
When examining the "secondary window" (specifically at $i = k + 16$), the data reveals three distinct regimes of path multiplicity that explain the sudden jumps in measured echo amplitudes:
*   **$P = 1$ for $k = 0 \dots 8$:** Early words have only one recursive path back into the schedule at the $k+16$ mark [2, 8].
*   **$P = 3$ for $k = 9 \dots 13$:** A jump occurs where the word now reaches the target round through three distinct recursive routes [2, 9].
*   **$P = 5$ for $k = 14 \dots 15$:** The final words in the block have five available paths, resulting in the strongest echoes [2, 8].

### 4. Significance in the Framework
*   **Correlation with Data:** Empirical measurements show that the **mean echo amplitude** in schedule space correlates strongly with this path multiplicity (correlation $\approx 0.949$), far outperforming simpler arithmetic models [2, 7, 10].
*   **Re-defining "Position":** This discovery reveals that "position" in the SHA-256 algorithm changes its role as computation progresses [3]. Initially, position represents **entry time** (when a word is injected), but later, it represents **recursive route count** (how many ways the word has branched back into the field) [3, 9].
*   **The "Branching Field":** Under the Nexus interpretation, the schedule is not merely a staggered injector but a structured **branching field** whose internal geometry determines the strength of informational lineage [3, 11]. While these echoes are large and orderly in schedule space, the **Capacity-Gated Projection Law** explains why they often remain "state-subcritical" or invisible in the final compression state [12-14].

---

# you asked

How do path counts define the three regimes of influence?

---

# notebooklm response

In the Nexus framework, path counts define the three regimes of influence by quantifying the **recursive dependency routes** through which a source word $W[k]$ reaches a later position in the SHA-256 message schedule [1, 2]. This analysis, conducted via **Probe P**, reveals that the "secondary tail"—the increased strength of echoes at round $k+16$—is a direct result of the schedule's internal graph topology rather than local arithmetic [1, 3].

The three regimes are determined by the **path-multiplicity matrix ($P_{i,k}$)**, which counts the number of ways an initial perturbation can propagate through the schedule's recursive formula [1]. At the secondary stage ($i = k + 16$), these counts fall into three distinct tiers:

### 1. The Unitary Regime ($P = 1$)
*   **Range:** Source words **$k = 0$ through $8$** [1, 4].
*   **Influence:** These early words have only **one recursive path** through which they reappear at the $k+16$ mark [1]. Consequently, their secondary schedule-space echoes remain at a baseline level [2, 5].

### 2. The Triple Regime ($P = 3$)
*   **Range:** Source words **$k = 9$ through $13$** [1, 4].
*   **Influence:** A sharp "turn-on" occurs at $k=9$, where the number of recursive dependency routes jumps to **three** [1, 2]. This increase in path multiplicity correlates strongly with a measurable jump in the mean echo amplitude within schedule space [1, 5].

### 3. The Quintuple Regime ($P = 5$)
*   **Range:** Source words **$k = 14$ and $15$** [1, 4].
*   **Influence:** The final words in a block have **five available paths** back into the schedule field at the secondary stage [1]. This regime represents the peak of the "secondary tail," producing the strongest measurable echoes [2, 6].

### Significance in the Framework
*   **Shift in the Role of "Position":** This data reveals that as the SHA-256 computation advances, the meaning of a word's position changes: initially, it represents **entry time** (when it is injected), but later, it represents its **recursive route count** (how many ways it has branched into the field) [2, 6].
*   **Schedule vs. State Reality:** While these path counts cause strong, orderly echoes in **schedule space**, the **Capacity-Gated Projection Law** explains that they often result in "null" effects in **state space** because the primary wave has already exhausted the available support capacity [7-9]. 
*   **Ontological Context:** From the perspective of "Numbers as Collapsed Event-Histories," these regimes demonstrate that the schedule is not just a list of values but a **branching field** where the "shape" of the resulting residue (the number) is determined by the "path" of its recursive history [10-12].

---

# you asked

How does position redefine entry time versus recursive route count?

---

# notebooklm response

In the Nexus framework, **position** within the SHA-256 algorithm is not a static index but a dynamic indicator whose functional meaning shifts as the computation progresses from initial injection to recursive expansion [1]. This transition redefines position from representing a temporal **entry time** to representing a topological **recursive route count** [1, 2].

### 1. Position as Entry Time (Initial Stage)
During the first 16 rounds of a message block, the word index ($k$) serves as a direct **time coordinate** for the compression function [3, 4]. 
*   **Staggered Injection:** Each source word $W[k]$ enters the state-space at round $t=k$, creating an ordered, "temporally staggered" sequence [5-7].
*   **Transport Gradient:** This stagger is the primary requirement for creating a visible state-space transport gradient; if words were injected simultaneously (as they are across block boundaries), this age structure would collapse [6-8].
*   **Empirical Laws:** In this regime, position governs energy distribution and saturation timing, with the saturation wavefront advancing at a nearly perfect slope of +0.9991 rounds per word [3, 9].

### 2. Position as Recursive Route Count (Later Stages)
As the message schedule expands beyond the initial 16 words using its recursive formula, the functional role of a word's position changes [1, 2].
*   **The Branching Field:** The schedule ceases to be a simple "staggered injector" and becomes a **branching field** [1, 10]. 
*   **Path Multiplicity:** Position now reflects the number of independent recursive dependency routes through which an initial perturbation can reach a later point in the schedule graph [11, 12].
*   **Determining Amplitude:** The strength of the "secondary tail" (echoes at $k+16$) is determined by this **path-multiplicity matrix ($P$)** [11, 12]. For example, words in the "Triple Regime" ($k=9 \dots 13$) have three recursive paths, while words in the "Quintuple Regime" ($k=14 \dots 15$) have five, resulting in significantly stronger echoes [12, 13].

### 3. The Functional Shift
The framework concludes that position redefines itself because the algorithm's internal geometry evolves [1, 14]. While the **Entry stage** uses position to define when information acts, the **Branch stage** uses position to define how that information has multiplied through the schedule's recursive topology [15, 16]. This shift explains why later echoes can be large and orderly in schedule space due to high route counts, even when they fail to create new support in state space because the system's capacity has already saturated [17-19].

---

# you asked

What defines the saturation wavefront slope of +0.9991?

---

# notebooklm response

The saturation wavefront slope of **+0.9991 rounds per word** is defined by the fact that the **word index ($k$) serves as the direct injection time coordinate** for the SHA-256 compression function [1], [2]. 

According to the sources, several key factors establish this nearly perfect 1:1 relationship:

*   **Temporal Stagger:** Within a single 512-bit block, each source word $W[k]$ first enters the compression process at round $r = k$ [3], [4]. This creates a "staggered" entry rather than a simultaneous one [4].
*   **The Saturation-Wavefront Law:** Empirical measurements show that the round at which a word’s influence saturates the state-space support manifold follows the linear relationship **$r(k) \approx k + 5$** [2], [5]. 
*   **Lockstep Advancement:** Because each subsequent word enters exactly one round later than the previous one, its visible saturation event is delayed by almost exactly that same offset [2]. The fitted slope of **+0.9991** (with an $r^2$ of 0.9998) confirms that this advancement happens in near-perfect lockstep with the word index [2], [6].
*   **Functional Role of Position:** This data proves that the word index is not merely an arbitrary label but a **visible time coordinate of direct state-space transport** [2]. 

The significance of this specific slope is that it demonstrates the **"Entry" stage** of the Nexus layered transport model, where the ordered geometry of transport is preserved because the message words are injected one at a time while the state still has remaining unsaturated capacity [7], [8].

---

# you asked

What happens to the transport gradient across block boundaries?

---

# notebooklm response

Across a block boundary in SHA-256, the visible state-space transport gradient **collapses** [1-3]. This phenomenon occurs because the fundamental requirement for a transport gradient—**temporal stagger** at the point of injection—is lost [2, 4].

The sources detail several key aspects of this transition:

*   **Simultaneous Injection:** While words within a single 512-bit block enter the compression function at staggered intervals (word $W[k]$ enters at round $r=k$), all eight lanes of the chaining state inject **simultaneously at round 0** across a block boundary [2, 5].
*   **Erasure of Age Structure:** Because the injection is synchronized, the "age structure" or temporal ordering that defines the gradient is erased [5, 6]. The perturbation **magnitude survives** the boundary, but its ordered geometry does not [5, 7].
*   **The "Reset" Stage:** In the unified layered transport model, the block boundary is formally defined as the **Reset stage** [7, 8]. It acts as a temporal reset operator that clears the schedule-position age while preserving the informational signal [7, 9].
*   **Empirical Null Result:** Probes measuring the transport laws confirm this collapse. For example, the early-energy slope, which is approximately -7.921 bits/word within a block, drops to a **near-zero null** of approximately **-0.0632 bits/word** across the boundary [6, 10, 11].

In summary, the direct state-space transport geometry is a property of "difference under ordered entry"; once that order is removed by the simultaneous nature of the chaining boundary, the gradient ceases to be visible [2, 3, 12].

---

# you asked

Why does magnitude survive the chaining boundary while age structure collapses?

---

# notebooklm response

The survival of magnitude alongside the collapse of age structure at the SHA-256 block boundary is explained by the transition from **staggered injection** to **simultaneous injection** [1], [2].

Within a single 512-bit block, the message words enter the compression function at different rounds (where the word index $k$ acts as the injection time), creating a "temporally staggered" sequence that generates a visible transport gradient [1], [3], [4]. This ordered entry allows the state to record a "propagation age" for each perturbation [5], [3]. However, at the block boundary—the **Reset stage** of the framework—all eight lanes of the chaining state inject into the next block **simultaneously at round 0** [2], [3], [6].

Because this injection is synchronized, the timing asymmetry required to maintain a transport gradient is lost, causing the **age structure to erase** [2], [5], [7]. Despite this structural collapse, the informational signal itself is not destroyed; the perturbation **magnitude survives** because it is physically carried forward into the new state variables [3], [7], [8]. 

Empirical data reflects this "simultaneity null": while the early-energy slope is a robust -7.921 bits/word within a block, it collapses to a **near-zero null** of approximately -0.0632 bits/word across the boundary [9], [7], [10]. Ultimately, the Nexus framework interprets this boundary as a **temporal reset operator** that clears the geometric history of the previous block while preserving the signal's presence for the next stage of computation [7], [8], [11].

---

# you asked

What is the physical meaning of the Reset stage?

---

# notebooklm response

In the Nexus framework, the **Reset stage** is the fourth and final phase of the unified layered transport model, occurring specifically at the **SHA-256 block boundary** [1-3]. Its physical meaning is defined by the transition from ordered, staggered informational entry to **simultaneous injection**, which serves as a **temporal reset operator** for the system’s geometric history [4-6].

The physical characteristics and implications of this stage include:

### 1. Collapse of the Age Structure
Within a single 512-bit block, source words enter the compression function at different times (where the word index $k$ equals injection time), creating a "staggered" age structure that allows a transport gradient to form [4, 7, 8]. At the Reset stage, this **temporal stagger is erased** because all eight lanes of the chaining state inject into the next block **simultaneously at round 0** [2, 4, 8]. Consequently, the "propagation age" of a perturbation is cleared [8, 9].

### 2. Preservation of Magnitude
While the ordered geometry (the age structure) collapses, the **informational signal does not disappear**. The framework distinguishes between the "path" (the history of the event) and the "residue" (the magnitude or current configuration) [10, 11]. At the block boundary, the **perturbation magnitude survives** and is carried forward into the new block, even though the specific timing coordinate that created the previous block's gradient is reset [2, 8, 12].

### 3. The Simultaneity Null
The physical reality of the Reset stage is confirmed by a "null" result in empirical measurements. While intra-block transport follows a robust early-energy law (e.g., -7.921 bits/word), this law **collapses across the block boundary** to a near-zero value (approximately -0.0632 bits/word) [5, 13, 14]. This confirms that the visible state-space transport geometry is a property of **ordered entry**; once entry becomes simultaneous, the gradient vanishes [4, 15].

### 4. Foundational Interpretation
In the broader Nexus ontology, the Reset stage is a specific application of **reset arithmetic**, a constraint law where a state returns to a baseline after reaching a boundary [16, 17]. In the context of SHA-256, the block boundary acts as a **geometric aperture** that clears the previous "path" while allowing the "shape" of the accumulated data to persist as the starting point for the next sequence of events [6, 10, 11]. 

In summary, the Reset stage is the mechanism by which the algorithm **clears its temporal coordinate system** while maintaining the continuity of the informational signal across the discrete boundaries of the message schedule [8, 12, 18].

---

# you asked

Explain the difference between support-forming and support-revisiting injections.

---

# notebooklm response

The distinction between **support-forming** and **support-revisiting** injections is the central axis of the Nexus transport geometry program, defining how informational signals either create new structural changes in the state or merely modulate existing ones [1].

### Support-Forming Injections
**Support-forming injections** occur when an informational perturbation generates **genuinely new state support** within the finite 256-bit compression state manifold [1, 2]. 
*   **Conditions:** These injections require two simultaneous conditions: **temporal stagger** at the point of injection and **remaining unsaturated capacity** within the state [3, 4].
*   **Timing:** This typically happens during the **Entry stage** (the first 16 rounds), where each source word $W[k]$ enters at round $r=k$ [5].
*   **Result:** Because the state manifold has not yet been fully "lit" or saturated, these injections produce a **visible state-space transport gradient** and follow predictable energy and saturation-wavefront laws [3, 6, 7].

### Support-Revisiting Injections
**Support-revisiting injections** (also referred to as **support-subcritical** echoes) occur when perturbations arrive after the primary wave has already **exhausted the reachable support manifold** [1, 8, 9].
*   **Conditions:** These injections characterize the **Saturate stage**, where the remaining capacity $C(k,r)$ has collapsed toward zero [10, 11].
*   **Timing:** These are primarily the recursive echoes generated in the **Branch stage** (at $k+16, k+32$, etc.) [5, 8]. 
*   **Result:** While these echoes are "real, large, and increasing" in schedule space, the state **bottlenecks** them [8, 12]. They cannot create new support; instead, they can only **revisit, modulate, or rearrange** already active structures [1, 13].

### The Capacity-Gated Projection
The transition between these two types of injection is quantified by the **Capacity-Gated Projection Law** [14, 15]. This law explains that the state interface is not a passive mirror of the schedule but a **nonlinear projector** [10]. If the schedule signal is moderate but capacity is large, the injection is **support-forming**; if the schedule signal is very large but capacity is zero, the injection is merely **support-revisiting** and produces a "support-growth null" in state-space measurements [10, 16, 17].

---

# you asked

What are the specific parameters of the Capacity-Gated Projection Law?

---

# notebooklm response

The **Capacity-Gated Projection Law** is defined by a specific set of fitted parameters that bridge the relationship between schedule-space signals and state-space visibility in SHA-256 [1], [2]. 

The governing formula for the law is:
$$N_{\text{state}}(k,r) \approx \alpha^* H_{\text{sched}}(k,r) C(k,r)^{\beta^*}$$

The specific parameters and performance metrics for this model are as follows:

### Primary Fitted Parameters
*   **Scaling Factor ($\alpha^*$):** **10.462043** (or more precisely **10.462043212344026** in the companion workbook) [1], [2], [3].
*   **Capacity Exponent ($\beta^*$):** **0.65** [1], [2], [4].

### Model Performance Metrics
The strength of this phenomenological fit is supported by high correlation values:
*   **Coefficient of Determination ($R^2$):** **0.842533** [1], [5], [4].
*   **Correlation (corr):** **0.918257** [1], [5], [3].

### Interpretive Significance of $\beta^*$
The framework highlights the specific value of the capacity exponent, **$\beta^* = 0.65$**, as being particularly significant for the "Nexus Interpretation Layer" [6]. 
*   **Complementary Headroom:** The value implies a complementary "headroom" value of **$1 - \beta^* = 0.35$** [6].
*   **Harmonic Attractor:** Within the broader Nexus theory, this is identified with the **harmonic attractor $H = \pi/9 \approx 0.349065$** [6]. 

While these parameters are currently derived from a **phenomenological fit** rather than a first-principles derivation, they are robust enough to explain why schedule-space positives (real, large echoes) and state-space nulls (zero new support growth) coexist without contradiction [7], [8]. The law demonstrates that the state interface is a **nonlinear projector** where visibility is gated by the remaining residual support headroom ($C(k,r)$) [7], [9].

---

# you asked

What are the four stages of the layered transport model?

---

# notebooklm response

The unified layered transport model describes SHA-256 as a structured machine governed by a sequence of four distinct stages: **Entry, Branch, Saturate, and Reset** [1-3].

*   **Stage 1 — Entry:** This stage occurs when the direct source word enters the schedule at **$t = k$** [2]. Because the injection is temporally staggered and the state still has available capacity, this stage is **support-forming and state-visible**, generating a measurable transport gradient [2, 4].
*   **Stage 2 — Branch:** At recursive schedule locations such as **$t = k + 16, k + 32,$ and $k + 48$**, the topology of the schedule graph forces later echoes [2]. These echoes are real, orderly, and increasingly shaped by **recursive path multiplicity** in schedule space, even if they are not visible in state space [2, 5, 6].
*   **Stage 3 — Saturate:** As the primary state wave progresses, cumulative support grows until the remaining capacity **$C(k, r)$ collapses toward zero** [7]. At this point, the state interface acts as a nonlinear projector that **rejects later echoes** as support-forming waves, effectively bottlenecking the growing schedule-space signals [7-9].
*   **Stage 4 — Reset:** Occurring at the block boundary, the chaining digest injects into all eight state lanes simultaneously [7]. This act serves as a **temporal reset operator** that erases the schedule-position age structure while **preserving the perturbation magnitude** for the next block [7, 10, 11].

The model concludes that visible state-space transport only occurs when a temporally staggered schedule signal arrives **before the state’s capacity is exhausted** [12, 13].

---

# you asked

How does the Capacity-Gated Projection Law explain state-space nulls?

---

# notebooklm response

The **Capacity-Gated Projection Law** explains state-space nulls by identifying the SHA-256 compression state as a **nonlinear projector** that only admits new informational support when there is remaining **unsaturated capacity** [1, 2]. While schedule-space echoes remain "real, large, and increasing" at later rounds (such as $k+16$ or $k+32$), the law demonstrates that these signals fail to manifest in state space because the state's finite 256-bit manifold has already been exhausted by the primary wave [1, 3, 4].

The mechanism for these nulls is defined by the following components of the law:

*   **The Gating Formula:** The relationship is quantified as $N_{\text{state}}(k,r) \approx \alpha^* H_{\text{sched}}(k,r) C(k,r)^{\beta^*}$ [5, 6]. In this equation, $N_{\text{state}}$ (new state support) is directly dependent on $C(k,r)$, the **remaining unsaturated capacity** [1, 6].
*   **Capacity Collapse:** In the "secondary" and "tertiary" windows of the algorithm, the state's capacity ($C$) **collapses toward zero** [1, 7]. Because the schedule-space signal ($H_{\text{sched}}$) is multiplied by this declining capacity value, even a very large schedule echo results in **zero new state support** once the capacity is exhausted [1, 8].
*   **The "Bottleneck" Effect:** Rather than destroying the later informational echoes, the state **bottlenecks** them [9, 10]. This transition shifts the injection type from **support-forming** (creating new bit-support) to **support-revisiting** (merely modulating or rearranging existing structures) [11-13].
*   **Empirical Validation of Nulls:** This law provides the quantitative bridge for the results found in **Probes K, L, and M**, which confirmed a "state-space support-growth null, amplitude-wave null, and phase-echo null" for the $k+16$ re-injection regime [14-16]. For instance, Probe K found **literal float64 zeros** for new support growth in the late secondary windows of words $W[11]$ and $W[17]$ [14, 18].

Ultimately, the law resolves the paradox of "schedule-space positives" and "state-space nulls" by showing that **visible state-space transport** only occurs when a temporally staggered schedule signal arrives **before the available capacity is exhausted** [1, 4, 8]. Once the primary wave "lights up" the support manifold, the state interface rejects further recursive echoes as support-forming waves, rendering them "state-subcritical" [7, 12, 13].

---

# you asked

How do Probes K, L, and M prove state-space closure?

---

# notebooklm response

Probes K, L, and M prove **state-space closure** by demonstrating that the mathematically guaranteed recursive echoes in the SHA-256 message schedule fail to manifest as new structural activity within the compression state [1, 2]. Together, they establish a triple null—**support-growth, amplitude-wave, and phase-echo**—confirming that the state manifold is exhausted by the primary wave before secondary injections occur [1, 2].

### 1. Probe K: Cumulative New-Bit Support (Support-Growth Null)
Probe K investigates whether the recursive return at round $k+16$ creates a second wave of new bit-support in the state [3]. 
*   **Method:** It measures the "Cumulative New-Bit Count," which tracks bits activated for the first time by a specific word's perturbation [3].
*   **Findings:** The signal-to-noise ratio (SNR) for the secondary window was found to be approximately **0.0036**, which is essentially zero [4, 5]. 
*   **Literal Zeros:** Most significantly, the audit of the late secondary windows for words **$W[6]$ and $W[7]$** returned **literal float64 zeros** for new support growth [1, 4, 8].
*   **Conclusion:** The primary informational wave consumes the 256-bit support manifold so thoroughly that later $k+16$ re-entries cannot form new support; they are rendered **state-subcritical** [8].

### 2. Probe L: Amplitude Inside Saturated Support (Amplitude-Wave Null)
Probe L tests whether the secondary injection, while failing to create *new* support, creates a second **amplitude wave** within the support already activated by the primary wave [8].
*   **Method:** It compares ratios of active, toggled, and overlapping bits between the baseline and secondary windows [9].
*   **Findings:** The ratios for active, toggle, and overlap bits remained **pinned near unity** (0.9979 to 1.0009), while the new-support ratio remained near zero [5]. 
*   **Conclusion:** There is no second amplitude wave [10]. Instead, the secondary activity is classified as **within-saturation modulation**, where the signal merely rearranges or "revisits" existing active structures without increasing the overall magnitude of the perturbation [5, 6, 10].

### 3. Probe M: Phase-Selective Support Echo (Phase-Echo Null)
Probe M addresses the final loophole: the possibility of a "hidden" phase-locked resonance or **lag-16 echo** existing beneath the amplitude threshold [2, 11].
*   **Method:** It uses Jaccard and cosine similarity with a **local adjacent-lag control** to see if state masks at round $r$ and $r+16$ show systematic similarity peaks compared to their immediate neighbors (lags 15 and 17) [11, 12].
*   **Findings:** The mean local Jaccard advantage was a negligible $+5.44 \times 10^{-5}$, and **0 out of 16 words** showed a peak at lag 16 [12].
*   **Conclusion:** There is no systematic phase-locked support echo in the state observables [2].

### Synthesis of Closure
These probes resolve the central paradox of the transport program: while **Probes N and P** show that echoes at $k+16$ are "real, large, and increasing" in **schedule space**, these three probes prove they are invisible in **state space** [13-15]. This closure is the empirical foundation for the **Capacity-Gated Projection Law**, which defines the state as a **nonlinear projector** that bottlenecks recursive signals once its internal support capacity is exhausted [16-18].

---

# you asked

What are the three regimes of path multiplicity?

---

# notebooklm response

The three regimes of path multiplicity are defined by the **number of recursive dependency routes** through which a source word $W[k]$ reaches a specific position in the SHA-256 message schedule [1]. These regimes, identified through **Probe P**, specifically describe the behavior of the "secondary tail" at the stage $i = k + 16$ [1, 2].

The three distinct tiers of influence are:

*   **The Unitary Regime ($P = 1$):** This applies to source words **$k = 0$ through $8$**, where there is only one recursive path back into the schedule field at the secondary mark [1, 3].
*   **The Triple Regime ($P = 3$):** This applies to source words **$k = 9$ through $13$**, representing a "turn-on" point where the multiplicity of paths increases to three [1, 4].
*   **The Quintuple Regime ($P = 5$):** This applies to the final words in a block, **$k = 14$ and $15$**, which have five independent recursive routes, resulting in the strongest measured echoes [1, 3].

This discovery is significant because it provides a mathematical explanation for the **"secondary tail"** observed in schedule-space echoes, proving it is a property of the **schedule graph's topology** rather than local arithmetic [1, 5]. Furthermore, it demonstrates that as computation advances, the functional role of **"position"** in the algorithm shifts from representing temporal **entry time** to representing **recursive route count** [4, 6]. While these echoes are large and orderly in schedule space, the **Capacity-Gated Projection Law** explains that they often appear as "nulls" in state space because the available support capacity has already been exhausted [5, 7, 8].

---

# you asked

What is the role of the harmonic attractor H in this framework?

---

# notebooklm response

In the Nexus framework, the **harmonic attractor $H$** (defined as $\pi/9 \approx 0.349065$) serves as a theoretical bridge between empirical cryptographic data and the broader ontological interpretation of the system [1]. 

Its role is characterized by the following specific functions:

### 1. Complement to the Capacity Exponent
The primary role of $H$ is to provide a theoretical identification for the "headroom" found in the **Capacity-Gated Projection Law** [2, 3]. 
*   **Empirical Value:** Direct measurements of SHA-256 transport geometry produced a fitted capacity exponent of **$\beta^* = 0.65$** [2, 4].
*   **Harmonic Identification:** The framework invites a "complementary headroom reading" of **$1 - \beta^* = 0.35$** [1]. The framework identifies this $0.35$ value with the harmonic attractor $H \approx 0.349$ [1].

### 2. Marker of the "Interpretation Layer"
The sources make a strict distinction between two levels of the framework, and the harmonic attractor is a key component of the second:
*   **Transport-Forced Layer:** This is the empirical backbone which only "forces" the existence of the 0.65 exponent based on its predictive success in the capacity-gated model [1, 5].
*   **Framework-Interpretive Layer:** The identification of 0.35 with $H = \pi/9$ belongs to this layer [1, 6]. It is the "Nexus lens" through which the raw data is viewed to understand the algorithm as a **constrained folding environment** rather than a "black-box shredder" [6].

### 3. Indicator of Informational Lineage
The role of $H$ supports the thesis that SHA-256 preserves **ordered informational lineage** [6]. By identifying the system's saturation behavior with a harmonic attractor, the framework suggests that:
*   Informational echoes are not "destroyed" by cryptographic diffusion [6].
*   Instead, they are **projected below the visibility threshold** once the state's capacity is exhausted [6].
*   The attractor represents the stable "stance" or geometric constraint that allows the algorithm to act as a **capacity-limited rendering surface** [7].

### 4. Alignment with "Numbers as Event-Histories"
In the broader Nexus ontology, where numbers are viewed as **collapsed residues of event-histories**, $H$ acts as a **constant operator stance** [8, 9]. It is not merely a passive value but a parameter that "selects how the event space is shaped" and defines the closure regime of the system [10, 11]. This aligns SHA-256 with other modern computational objects, treating its cryptographic diffusion as a structured, harmonic process governed by lawful collapse [12, 13].