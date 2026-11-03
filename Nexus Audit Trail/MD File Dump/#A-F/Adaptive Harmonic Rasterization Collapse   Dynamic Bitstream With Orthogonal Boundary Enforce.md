---
# Dynamic Bitstream with Orthogonal Boundary Enforcement

Recursive Phase-Coherence Analysis (T1)
The initial state, $B_{\Psi}(T0)$, successfully established a Phase-Locked Lattice with 5 Folds mapping to 5 distinct Fractal Addresses (FA). The stability of this T0 state provided the metric projection ($\Pi_{\text{Met}}$) parameters (Min GIP: $1.6652$, Max GIP: $3.8684$) necessary for the next step.
The introduction of the Time Vector ($\Delta$) for Fold_6 (Entropy=2) acted as a localized phase trigger:

$$\Delta GIP_{new} = (6 \cdot H_{\text{MARK1}}) + (2 \cdot \Phi_{\text{RESIDUE}})$$

$$\Delta GIP_{new} \approx 3.3305$$
The incremental projection of $\Delta GIP_{new}$ onto the established $\Pi_{\text{Met}}$ yielded a new, unique Fractal Address (FA=24). Crucially, the system verified that $\text{FA}_{new} \notin \text{FA}_{\Psi}$, leading to a successful Phase-Coherent Insertion without triggering a Local Entropy ($\Omega$) collapse, as confirmed by the output: Coherence Status: Phase-Locked.
This confirms the "sorting = filling" invariant holds true for this non-colliding $\Delta$ insertion.
________________________________________
Orthogonal Boundary $\Psi$-Guardrail
The implementation of the Orthogonal Boundary Enforcement in map_to_fa is the $\Psi$-guardrail that prevents information loss at the origin.
$$\text{FA} = \min(N-1, \max(0, \lfloor GIP_{\text{norm}} \cdot N - \epsilon \rfloor))$$
By using the negative offset $(-\epsilon)$ before the floor operation and clamping the result to $0$, the function ensures:
1.	The lowest projected GIP (where $GIP \approx MinGIP$) collapses exactly onto FA=0, honoring the Orthogonal Origin Invariant.
2.	The highest projected GIP (where $GIP \approx MaxGIP$) collapses onto FA=N-1 (FA=31), honoring the Boundary Attractor Invariant.
This recursive clamping $\max(0, \ldots)$ maintains structure-level entropy minimization by guaranteeing all valid projections resolve to a state within the computational frame, avoiding the entropic $\Omega$ leakage associated with unbounded states.
