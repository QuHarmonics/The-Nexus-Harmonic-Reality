# Nexus H Concordance Toolkit (stream ↔ frame)

This script estimates the "best" H in two independent ways:

- **Stream**: from time-series alignment (cross-product autocorrelation proxy)
- **Frame** : from geometric focusing (max fraction in a small ball)

Then it prints a **concordance report** and writes a sweep CSV.

## Install deps

- numpy
- pandas
- (optional but recommended) scipy

## Stream CSV format

A CSV with columns:

- `E_mech` : float
- `E_em`   : float

## Frame function contract

Pass a function via:

`--frame_func "module:function"`

That function must return final points:

```python
def run_rays(n_rays: int, H: float, seed: int):
    # ...
    return finals  # shape (n_rays, 2)
```

## Example commands

Stream-only:

```bash
python nexus_h_concordance_toolkit.py --stream_csv stream.csv --mode stream
```

Frame-only:

```bash
python nexus_h_concordance_toolkit.py --frame_func "my_sim:run_rays" --mode frame
```

Both + report:

```bash
python nexus_h_concordance_toolkit.py --stream_csv stream.csv --frame_func "my_sim:run_rays" --mode both
```

## Notes

- The scoring functions are intentionally simple and explainable. Replace them with your preferred metrics as needed.
- The bootstrap in **frame mode** is expensive because it repeats sweeps. Reduce `--n_boot` or `--steps` to speed it up.
