# ✅ "THE code" to review **BytesOfPI.xlsm** and expose **route symmetry + bit-length accidents**

You're right to focus on **routes**. In your workbook, a "route" is literally a **byte-lane**:

- Moving along **a** (first digit) changes the **most significant byte** ⇒ fixed step of $2^{24} = 16,777,216$ (this is your recurring **−16777216** "Difference" wall).
- Moving along **b** (second digit) changes the **third byte** ⇒ fixed step of $2^{8} = 256$.

That's the symmetry between routes: **same manifold, different byte-weight axes**.

And the "bit length chart accident" is reproducible as **bit-length of the even-padded binary of the last-two-decimal-digits (residue)**---exactly what your sheet is computing when it prints things like `01011101` and a length like `8`.

## Download

- [Download `nexus_excel_routes.py`](sandbox:/mnt/data/nexus_excel_routes.py)\
  Single script. Ingests your workbook, extracts the full "Hex Math Gap Analysis" structure, recomputes the math *from first principles*, and exports everything.

- [Download bundle (script + sample outputs)](sandbox:/mnt/data/nexus_excel_review_bundle.zip)\
  Includes:

- the script

- `gap_routes_extracted.csv`

- `symmetry_summary.json`

- `sheets_csv/` (every sheet dumped to CSV so you can "review the entire excel" outside Excel)

## What this script does (in plain terms)

### 1) Reviews the entire workbook

With `--dump-all-sheets`, it exports **every sheet** as cached-value CSV:

    out/sheets_csv/Recursive_PI.csv
    out/sheets_csv/Hex_Additon.csv
    out/sheets_csv/Hex_Math_Gap_Analysis.csv
    ...

That's your full "review the entire excel" step without clicking around.

### 2) Extracts the meaningful computational substrate

From **Hex Math Gap Analysis**, it extracts each fixed‑b "route" and records, per expression:

- `expr` (like `3+5=`)
- `hex` (like `332B353D`)
- `dec` (like `858469693`)
- `sum_digits(dec)`
- `last2 = dec % 100`
- `last2_bin` (Excel-style **even padded** binary)
- `last2_bitlen` (the chart bar height)

...and it also keeps the adjacent "Difference" columns so you can study the route deltas.

### 3) Recomputes everything from the true definition

It does **not** trust Excel formulas؛ it recomputes via:

$$\text{hex} = \text{ASCII}\left( \text{"a+b="} \right),\quad\text{dec} = \text{int(hex,16)}$$

and then projects:

$$\text{last2} = \text{dec}\ mod\ 100,\quad\text{last2\_bin} = \text{bin(last2) with even padding}$$

### 4) Produces a symmetry summary JSON

Outputs `symmetry_summary.json` including:

- route step verification: checks every fixed‑b route has constant `+2^24` stepping in `a`
- swap symmetry stats: compares `(a,b)` vs `(b,a)` behavior
- per-route minima of your bit-length metric (the "happy accidents")
- global minima / maxima across all extracted pairs
- focus readout for `3+5=`, `5+3=`, `3+7=`, `4+5=` (so you can sanity check the exact claim)

## Run it

From a terminal in the same directory as the workbook (or pass a full path):

    python nexus_excel_routes.py --workbook BytesOfPI.xlsm --out out --dump-all-sheets

If you also want the plot (heatmap of residue-bitlen across the grid), install matplotlib and omit `--no-plots`:

    python nexus_excel_routes.py --workbook BytesOfPI.xlsm --out out --dump-all-sheets

## What you'll see immediately (the symmetry you suspected)

After running, open:

- `out/gap_routes_extracted.csv`\
  This shows the **decoded route tables** and validation flags (`hex_match`, `dec_match`, etc.)

- `out/symmetry_summary.json`\
  You'll see each `b` route has:

<!-- -->

    "unique_steps": [16777216],
    "all_steps_match_2pow24": true

That's the byte-axis symmetry in black and white.

## One important correction your code will make obvious

If your "bitlen" is the workbook's **even-padded binary length of last-two-decimal-digits**, then:

- `3+5=` produces `last2 = 93 → bin = 01011101 → bitlen = 8`
- but `5+3=` produces `last2 = 13 → bin = 1101 → bitlen = 4`
- and `3+7=` produces `last2 = 05 → bin = 0101 → bitlen = 4`

So if you *saw* "3+5 lowest", it's very likely the chart was actually picking up the **swap route** (`5+3`) or a neighboring "route-minimum" like `4+5` (which also bottoms at 4-bit residue in your b=5 route).

The script reports this explicitly in `focus_expressions` and in the minima lists, so we stop guessing and read it from the field.

------------------------------------------------------------------------

If you tell me **which exact bar chart selection** you meant (which operand‑slice: "everything involving 3", or "sum=8 diagonal", or "b=5 route"), I can add a second tiny function to this same script that reproduces *that exact chart* as a PNG and prints the top‑N minima in that slice.

------------------------------------------------------------------------
