# Nexus 4 Ψ Analyzer — Sample Report

This report demonstrates the companion analyzer on a few example inputs. Each input is hashed with SHA‑256; features and the unified Ψ score are computed per the spec.

## Input: `abc`
```json
{
  "H": 0.18994854235735512,
  "align": 0.7555554457559012,
  "rcq": 0.9888171374297436,
  "avg_abs_eps": 0.4775840199227296,
  "avg_ZH": 0.17567313434493645,
  "avg_Zsym": 0.30739301021559085,
  "avg_Knorm": 0.08614602559920917,
  "frac_constructive": 0.3870967741935484,
  "frac_ray": 0.08064516129032258,
  "Psi": 0.7194123338898207,
  "hex": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

## Input: `Nexus`
```json
{
  "H": 0.06624314451752704,
  "align": 0.5655125698127206,
  "rcq": 0.9969065209791731,
  "avg_abs_eps": 0.33525641025641023,
  "avg_ZH": 0.13419469761392944,
  "avg_Zsym": 0.24589711363904912,
  "avg_Knorm": 0.08425438954815002,
  "frac_constructive": 0.43548387096774194,
  "frac_ray": 0.11290322580645161,
  "Psi": 0.6925062221821341,
  "hex": "7ec8aa5a08624a1f4d540e2534a3b3db5d8c61e2e69954a7cb7022c5c69f971f"
}
```

## Input: `hello world`
```json
{
  "H": 0.15956440013748194,
  "align": 0.7088776946523658,
  "rcq": 0.9970561207241696,
  "avg_abs_eps": 0.32857532252693544,
  "avg_ZH": 0.13435402298825733,
  "avg_Zsym": 0.2517429702913574,
  "avg_Knorm": 0.10926122201025881,
  "frac_constructive": 0.5,
  "frac_ray": 0.14516129032258066,
  "Psi": 0.7380980208620888,
  "hex": "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
}
```
