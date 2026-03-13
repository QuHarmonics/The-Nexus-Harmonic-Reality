#!/usr/bin/env python3
"""
Run WMW v2 with Nexus Ψ‑damping kernel.

Example:
    python run_wmw2.py --model_ckpt models/wmw2_default.ckpt --out_dir psi_test
"""
import argparse, pathlib, pickle, yaml, numpy as np, matplotlib.pyplot as plt

def calc_ripple(spec):
    """Return ripple amplitude (max of spectrum slice)."""
    return float(np.max(spec))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_ckpt", required=True, help="Path to WMW v2 pickle")
    ap.add_argument("--out_dir", default="psi_test", help="Output folder")
    ap.add_argument("--psi_cfg", default="psi_weights.yml", help="Ψ‑kernel YAML")
    args = ap.parse_args()

    outdir = pathlib.Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    # load model (expects .ripple_spectrum after run_forecast call)
    with open(args.model_ckpt, "rb") as f:
        model = pickle.load(f)

    # baseline run
    baseline_spec = model.run_forecast().ripple_spectrum
    baseline = calc_ripple(baseline_spec)
    np.savetxt(outdir / "ripple_before.csv", baseline_spec, delimiter=",")

    # inject ψ‑kernel
    psi = yaml.safe_load(open(args.psi_cfg))
    model.latent_weights = psi["w_n"]
    model.theta0 = np.deg2rad(psi["theta0_deg"])

    # second run
    test_spec = model.run_forecast().ripple_spectrum
    after = calc_ripple(test_spec)
    np.savetxt(outdir / "ripple_after.csv", test_spec, delimiter=",")

    # plots
    for tag, spec in [("before", baseline_spec), ("after", test_spec)]:
        plt.figure()
        plt.plot(spec)
        plt.title(f"Ripple spectrum ({tag})")
        plt.ylabel("amplitude")
        plt.xlabel("frequency bin")
        plt.savefig(outdir / f"ripple_{tag}.png")
        plt.close()

    print(f"Ripple % BEFORE: {baseline*100:.5f}")
    print(f"Ripple %  AFTER: {after*100:.5f}")
    if after <= 0.0007:
        print("PASS ✅ (≤ 0.07 %)")
    else:
        print("FAIL ❌ (tune θ₀ or add depth decay)")

if __name__ == "__main__":
    main()
