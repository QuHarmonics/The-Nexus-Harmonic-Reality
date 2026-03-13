"""
NEXUS FOLD v3 — The real test.
Does the SPECTRAL STRUCTURE of helix propensity matter,
or is it just "more helical = faster"?

Control for: chain length AND mean helix propensity.
If spectral entropy still predicts → it's the PATTERN, not the AMOUNT.
That's the Nexus claim: the frequency decomposition matters.
"""

import numpy as np
from scipy import stats
from scipy.fft import fft

HYDRO = {'A':1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C':2.5,'E':-3.5,'Q':-3.5,'G':-0.4,'H':-3.2,'I':4.5,'L':3.8,'K':-3.9,'M':1.9,'F':2.8,'P':-1.6,'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V':4.2}
HELIX = {'A':1.42,'R':0.98,'N':0.67,'D':1.01,'C':0.70,'E':1.51,'Q':1.11,'G':0.57,'H':1.00,'I':1.08,'L':1.21,'K':1.16,'M':1.45,'F':1.13,'P':0.57,'S':0.77,'T':0.83,'W':1.08,'Y':0.69,'V':1.06}

FOLDING_DATA = [
    ("Villin HP35", "LSDEDFKAVFGMTRSAFANLPLWKQQNLKKEKGLF", 11.3, 0.10),
    ("Trp-cage", "NLYIQWLKDGGPSSGRPPPS", 13.0, 0.09),
    ("BBA5", "EQYTAKQKIIRLLKTFQNKR", 11.7, 0.11),
    ("Protein L", "MEEVTIKANLIFANGSTQTAEFKGTFEKATSEAYAYADTLKKDNGEWTVDVADKGYTLNIKFAG", 7.5, 0.15),
    ("Protein G", "MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE", 7.1, 0.17),
    ("WW domain", "GSKLPPGWEKRMSRSSGRVYYFNHITNASQFERPSG", 8.7, 0.14),
    ("Lambda rep", "PLTQEQLEDARRLKAIYEKKKNELGLSQESVADKMGMGQSGVGALFNGINALNAP", 8.5, 0.13),
    ("Engrailed", "EKRPRTAFSSEQLARLKREFNENRYLTERRRQQLSSELGLNEAQIKIWFQNKRAKI", 9.8, 0.12),
    ("CI2", "KTEWPELVGKSVEEAKKVILQDKPEAQIIVLPVGTIVTMEYRIDRVRLFVDKLDNIAEVPRVG", 4.1, 0.19),
    ("SH3 src", "MSAEGYQYRALYDYKKEREEDIDLHLGDILTVNKGSLVALGFSDGQEAKPEEIGWLNGYNETTGERGDFPGTYVEYIGRKKISP", 3.2, 0.21),
    ("Ubiquitin", "MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG", 5.0, 0.18),
    ("AcP", "SQLVRNLQAGNTVFVKGHAVGARYFDEHGEVFKVKENGSAAQVRGQVLGFEYAMEENNHIFFITQCKKTFAEQGAKQATDFVVEKFQGRIANFNVK", 2.6, 0.22),
    ("FKBP12", "GVQVETISPGDGRTFPKRGQTCVVHYTGMLEDGKKFDSSRDRNKPFKFMLGKQEVIRGWEEGVAQMSVGQRAKLTISPDYAYGATGHPGIIPPHATLVFDVELLKLE", 1.8, 0.20),
    ("Im7", "SISDYTEAEFVQLLKEIEKENVAATDDILAKYKGSEEKELADFLKEINDALKEIKK", 3.8, 0.15),
    ("Barnase", "AQVINTFDGVADYLQTYHKLPDNYITKSEAQALGWVASKGNLADVAPGKSIGGDIFSNREGKLPGKSGRTWREADINYTSGHIDNAKELAGNLR", 1.2, 0.23),
    ("ChymTryp", "RPDFCLEPPYTGPCKARIIRYFYNAKAGLCQTFVYGGCRAKRNNFKSAEDCMRTCGGA", 2.1, 0.24),
    ("CheY", "MGDKELKFLVVDDFSTMRRIVRNLLKELGFNNVEEAEDGVDALNKLQAGGYGFVISDWNMPNMDGLELLKTIRADASAMSALPVLMVTAEAKKKENIIAAAQAGASYVVKPFTAATLEEKLNKIFEKLGM", 0.5, 0.19),
    ("Myoglobin", "VLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRFKHLKTEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKELGYQG", -0.7, 0.17),
    ("Lysozyme", "KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL", -1.2, 0.21),
]

def get_features(seq):
    """Get all features for a sequence."""
    helix_sig = np.array([HELIX.get(aa, 0) for aa in seq if aa in HELIX])
    hydro_sig = np.array([HYDRO.get(aa, 0) for aa in seq if aa in HYDRO])
    N = len(helix_sig)
    
    # Mean values (the "amount" — known predictor)
    mean_helix = np.mean(helix_sig)
    mean_hydro = np.mean(hydro_sig)
    frac_helix = np.sum(helix_sig > 1.0) / N  # fraction of strong helix formers
    
    # Spectral features (the "pattern" — Nexus predictor)
    for sig, name in [(helix_sig, 'helix'), (hydro_sig, 'hydro')]:
        s = (sig - np.mean(sig)) / (np.std(sig) + 1e-10)
        F = fft(s)
        power = np.abs(F[:N//2])**2
        power = power / (np.sum(power) + 1e-10)
        p = power[power > 1e-15]
        entropy = -np.sum(p * np.log2(p))
        entropy_norm = entropy / np.log2(N/2) if N > 2 else 0
        sorted_p = np.sort(power)[::-1]
        top5 = np.sum(sorted_p[:5])
        
        # Spectral flatness
        log_p = np.log(power[power > 1e-15] + 1e-15)
        geo = np.exp(np.mean(log_p))
        arith = np.mean(power[power > 1e-15])
        flatness = geo / arith if arith > 0 else 0
        
        if name == 'helix':
            helix_entropy = entropy
            helix_entropy_norm = entropy_norm
            helix_top5 = top5
            helix_flatness = flatness
        else:
            hydro_entropy = entropy
            hydro_entropy_norm = entropy_norm
            hydro_top5 = top5
    
    return {
        'L': N, 'logL': np.log(N),
        'mean_helix': mean_helix, 'mean_hydro': mean_hydro,
        'frac_helix': frac_helix,
        'helix_entropy': helix_entropy, 'helix_entropy_norm': helix_entropy_norm,
        'helix_top5': helix_top5, 'helix_flatness': helix_flatness,
        'hydro_entropy': hydro_entropy, 'hydro_entropy_norm': hydro_entropy_norm,
        'hydro_top5': hydro_top5,
    }

# Compute
data = []
for name, seq, lnkf, co in FOLDING_DATA:
    f = get_features(seq)
    f['name'] = name; f['ln_kf'] = lnkf; f['co'] = co
    data.append(f)

n = len(data)
ln_kf = np.array([d['ln_kf'] for d in data])
logL = np.array([d['logL'] for d in data])
co = np.array([d['co'] for d in data])
mean_helix = np.array([d['mean_helix'] for d in data])
frac_helix = np.array([d['frac_helix'] for d in data])
helix_ent = np.array([d['helix_entropy'] for d in data])
helix_ent_norm = np.array([d['helix_entropy_norm'] for d in data])
helix_flat = np.array([d['helix_flatness'] for d in data])

def partial_corr_multi(x, y, covariates):
    """Partial correlation controlling for multiple covariates."""
    Z = np.column_stack(covariates + [np.ones(len(x))])
    # Residualize x
    beta_x = np.linalg.lstsq(Z, x, rcond=None)[0]
    res_x = x - Z @ beta_x
    # Residualize y
    beta_y = np.linalg.lstsq(Z, y, rcond=None)[0]
    res_y = y - Z @ beta_y
    return stats.pearsonr(res_x, res_y)

print("═"*70)
print("  THE REAL TEST: PATTERN vs AMOUNT")
print("═"*70)
print()
print("  Does the spectral STRUCTURE of helix propensity predict folding")
print("  rate beyond what AVERAGE helix propensity and length explain?")
print()
print("  If YES → the frequency pattern matters, not just the composition.")
print("  If NO → it's just 'more helical = faster,' which is already known.")
print()

# Baseline correlations
print("BASELINES:")
r1, p1 = stats.pearsonr(mean_helix, ln_kf)
print(f"  mean_helix vs ln(kf):         r = {r1:+.4f}  p = {p1:.4f}")
r2, p2 = stats.pearsonr(frac_helix, ln_kf)
print(f"  frac_helix vs ln(kf):         r = {r2:+.4f}  p = {p2:.4f}")
r3, p3 = stats.pearsonr(logL, ln_kf)
print(f"  log(length) vs ln(kf):        r = {r3:+.4f}  p = {p3:.4f}")
r4, p4 = stats.pearsonr(helix_ent_norm, ln_kf)
print(f"  helix_entropy_norm vs ln(kf): r = {r4:+.4f}  p = {p4:.4f}")
print()

# THE CRITICAL TEST: control for BOTH length AND mean helix propensity
print("CRITICAL PARTIAL CORRELATIONS:")
print("  (controlling for log(length) AND mean helix propensity)")
print()

for name, vals in [
    ('helix_entropy', helix_ent),
    ('helix_entropy_norm', helix_ent_norm),
    ('helix_flatness', helix_flat),
]:
    r, p = partial_corr_multi(vals, ln_kf, [logL, mean_helix])
    sig = "★★★ SIGNIFICANT" if abs(r) > 0.3 and p < 0.05 else "★★" if abs(r) > 0.3 else ""
    print(f"  {name:25s}  partial r = {r:+.4f}  p = {p:.4f}  {sig}")

# Also control for frac_helix (stricter test)
print()
print("  (controlling for log(length), mean helix, AND frac helix formers)")
for name, vals in [
    ('helix_entropy', helix_ent),
    ('helix_entropy_norm', helix_ent_norm),
]:
    r, p = partial_corr_multi(vals, ln_kf, [logL, mean_helix, frac_helix])
    sig = "★★★ SIGNIFICANT" if abs(r) > 0.3 and p < 0.05 else "★★" if abs(r) > 0.3 else ""
    print(f"  {name:25s}  partial r = {r:+.4f}  p = {p:.4f}  {sig}")

# ═══════════════════════════════════════════════════════════
# Also test: does CO survive controlling for spectral entropy?
# ═══════════════════════════════════════════════════════════
print()
print("REVERSE TEST: Does CO add beyond spectral complexity?")
r_co_partial, p_co = partial_corr_multi(co, ln_kf, [logL, helix_ent_norm])
print(f"  CO partial (controlling for logL + helix_ent_norm): r = {r_co_partial:+.4f}  p = {p_co:.4f}")

# Does spectral entropy add beyond CO?
r_ent_partial, p_ent = partial_corr_multi(helix_ent_norm, ln_kf, [logL, co])
print(f"  helix_ent partial (controlling for logL + CO):      r = {r_ent_partial:+.4f}  p = {p_ent:.4f}")

print()
print("═"*70)
print("  INTERPRETATION")
print("═"*70)
print()

# Model comparison
from numpy.linalg import lstsq
ones = np.ones(n)

# Model: length + mean_helix only (known predictors)
X_known = np.column_stack([logL, mean_helix, ones])
b_known = lstsq(X_known, ln_kf, rcond=None)[0]
pred_known = X_known @ b_known
r_known = np.corrcoef(pred_known, ln_kf)[0,1]
ss_known = np.sum((ln_kf - pred_known)**2)

# Model: length + mean_helix + spectral (Nexus addition)
X_nexus = np.column_stack([logL, mean_helix, helix_ent_norm, ones])
b_nexus = lstsq(X_nexus, ln_kf, rcond=None)[0]
pred_nexus = X_nexus @ b_nexus
r_nexus = np.corrcoef(pred_nexus, ln_kf)[0,1]
ss_nexus = np.sum((ln_kf - pred_nexus)**2)

# Model: length + CO (standard field model)
X_std = np.column_stack([logL, co, ones])
b_std = lstsq(X_std, ln_kf, rcond=None)[0]
pred_std = X_std @ b_std
r_std = np.corrcoef(pred_std, ln_kf)[0,1]
ss_std = np.sum((ln_kf - pred_std)**2)

# Model: spectral ONLY (pure Nexus, sequence-only)
X_pure = np.column_stack([helix_ent_norm, helix_flat, ones])
b_pure = lstsq(X_pure, ln_kf, rcond=None)[0]
pred_pure = X_pure @ b_pure
r_pure = np.corrcoef(pred_pure, ln_kf)[0,1]

print(f"  Known predictors (L + mean_helix):     r = {r_known:.4f}  SS = {ss_known:.2f}")
print(f"  + Nexus spectral (L + helix + entropy): r = {r_nexus:.4f}  SS = {ss_nexus:.2f}")
print(f"  Standard field (L + CO):                r = {r_std:.4f}  SS = {ss_std:.2f}")
print(f"  Pure Nexus (entropy_norm + flatness):   r = {r_pure:.4f}")
print()
print(f"  SS reduction from adding spectral entropy: {(ss_known-ss_nexus)/ss_known*100:.1f}%")
print()

# F-test
if ss_nexus > 0:
    p_known = 3; p_nexus = 4
    F = ((ss_known - ss_nexus)/(p_nexus - p_known)) / (ss_nexus/(n - p_nexus))
    from scipy.stats import f as fdist
    pF = 1 - fdist.cdf(F, p_nexus-p_known, n-p_nexus)
    print(f"  F-test (adding spectral): F = {F:.3f}, p = {pF:.4f}")
    if pF < 0.05:
        print(f"  → ✓ Spectral entropy SIGNIFICANTLY improves the model")
    elif pF < 0.1:
        print(f"  → ~ Marginal improvement (n={n} is small)")
    else:
        print(f"  → ✗ Not significant at conventional levels")

print()
print("═"*70)
print("  BOTTOM LINE")
print("═"*70)

