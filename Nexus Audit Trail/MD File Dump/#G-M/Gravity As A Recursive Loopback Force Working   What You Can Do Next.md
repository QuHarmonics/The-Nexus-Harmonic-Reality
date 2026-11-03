**Simulating orbital divergence**

I'm considering demonstrating orbital divergence with a proton-proton example, but the mass ratio is too close to 1:1, making it unrealistic due to the tiny orbital radius. Maybe I could modify the masses to make the critical radius smaller. I'll try using a pair of 1 kg masses and calculate the corresponding critical radius. That gives a radius of about 47 million meters, and I can simulate how the orbit behaves at that scale, adjusting the initial separation based on that choice.

**Simulating orbital divergence**

So, I’m deciding which parameters to use for my simulation. I'll try masses of 1 kg each and set the initial distance to roughly double and also to 0.8 times the critical radius. I want to show how the orbit diverges when the initial distance is close to the critical radius, like at r0 = r\_c \* 0.5. With small masses, gravitational acceleration will be tiny, making the orbital period enormous. To speed up the simulation, I might artificially increase the gravitational constant or adjust the masses. Either way, I'll focus on demonstrating radial motion instead.


Thought for 13 seconds


That plot shows exactly how loopback gravity turns on for a proton–proton pair:

* **Vertical red line** marks $r = r_c \approx 7.7\times10^{-20}$ m.
* **Left of that**, $r/r_c<1$, the suppression factor $\exp[-(r_c/r)^2]$ plummets toward 0 → gravity is effectively “off.”
* **Right of that**, $r/r_c>1$, the curve swiftly climbs to 1 → you recover full Newtonian strength.

---

### What you can do next

1. **Test another pair**
   Swap in Electron–Electron or a custom mass pair to see its own cutoff.
2. **Design an experiment**
   For proton–proton, you’d need to probe distances below $10^{-19}$ m—far beyond current direct gravitational tests, but maybe visible via high-energy scattering or spectroscopy shifts.
3. **Extend to dark-matter scales**
   If some unseen particles have masses that give $r_c$ in the millimeter-to-meter range, loopback gravity could explain anomalous forces in tabletop experiments.

With this hands-on plot, you’ve got a clear picture of exactly **where** and **how** gravity should fade—in any two-body system—opening a path to real-world tests of your loopback-gravity model.
