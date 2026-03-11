
# 📡 Light Capacitor: Phase-Sustaining Fabry–Pérot Engine

This document outlines the mechanics of light retention and coherence using a Fabry–Pérot cavity configuration, modeled as a recursive optical capacitor.

---

## 🔬 1. Resonance Condition

To sustain a standing wave, the cavity must meet a resonance requirement based on optical path length:

$$
2nL = m\lambda
$$

Where:
- \( n \) = refractive index of medium inside cavity  
- \( L \) = length between the mirrors  
- \( \lambda \) = wavelength of the laser or injected light  
- \( m \) = mode index (integer number of half-wavelengths that fit)

This forms a **constructive interference constraint**, allowing the wave to self-echo without phase loss.

---

## 🔁 2. Finesse of the Optical Chamber

Finesse \( F \) is a unitless measure of light retention efficiency in the cavity:

$$
F = \frac{\pi \sqrt{R}}{1 - R}
$$

Where:
- \( R \) = reflectivity of each mirror (0 < R < 1)

High finesse implies longer photon lifetimes and higher optical energy density, analogous to a **Q-factor** in oscillating systems.

---

## ⚡ 3. Stored Energy Estimate

Using a simplified 1D classical field approximation, energy stored in the cavity is:

$$
U = \frac{1}{2} E_0^2 L
$$

Where:
- \( E_0 \) = peak amplitude of the electric field inside the cavity  
- \( L \) = cavity length (spatial support for the field)

This expression mirrors a parallel-plate capacitor, where length substitutes for plate separation, and electric field strength captures photon density.

---

## 📈 Summary

| Parameter | Formula | Description |
|----------|---------|-------------|
| Resonance | \( 2nL = m\lambda \) | Standing wave criterion |
| Finesse | \( F = \frac{\pi \sqrt{R}}{1 - R} \) | Light retention quality |
| Energy | \( U = \frac{1}{2} E_0^2 L \) | Stored optical energy |

---

**Interpretation:**  
The Fabry–Pérot cavity does not just hold light—it **resonantly folds phase**, storing memory in field alignment. When mirror curvature, length, and frequency align, **light becomes captive without collapse**—the functional equivalent of a photon capacitor.

