import numpy as np, math, random, pandas as pd

AA20 = "ACDEFGHIKLMNPQRSTVWY"
AA_SET = set(AA20)

AA3 = {
    "A":"ALA","C":"CYS","D":"ASP","E":"GLU","F":"PHE","G":"GLY","H":"HIS","I":"ILE",
    "K":"LYS","L":"LEU","M":"MET","N":"ASN","P":"PRO","Q":"GLN","R":"ARG","S":"SER",
    "T":"THR","V":"VAL","W":"TRP","Y":"TYR"
}

AA_SCALAR_PROXY = {
    "A":  0.62, "C":  0.29, "D": -0.90, "E": -0.74, "F":  1.19,
    "G":  0.48, "H": -0.40, "I":  1.38, "K": -1.50, "L":  1.06,
    "M":  0.64, "N": -0.78, "P": -0.10, "Q": -0.85, "R": -2.53,
    "S": -0.18, "T": -0.05, "V":  1.08, "W":  0.81, "Y":  0.26,
}

def seq_to_signal(seq, aa_scalar=AA_SCALAR_PROXY):
    seq = seq.strip().upper()
    if not set(seq).issubset(AA_SET):
        bad = set(seq) - AA_SET
        raise ValueError(f"Non-canonical residues: {bad}")
    x = np.array([aa_scalar[a] for a in seq], dtype=float)
    x -= x.mean()
    return x

def autocorr_lag(x, lag):
    if lag <= 0 or lag >= len(x):
        return np.nan
    a = x[:-lag]; b = x[lag:]
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(a.dot(b) / denom) if denom > 1e-12 else 0.0

def sarrus_linkage(seq, aa_scalar=AA_SCALAR_PROXY, n_shuffles=1000, seed=0):
    rng = random.Random(seed)
    x = seq_to_signal(seq, aa_scalar)
    helix_obs = 0.5 * (autocorr_lag(x, 3) + autocorr_lag(x, 4))
    sheet_obs = autocorr_lag(x, 2)

    seq_list = list(seq.upper())
    helix_null = np.empty(n_shuffles, dtype=float)
    sheet_null = np.empty(n_shuffles, dtype=float)
    for i in range(n_shuffles):
        rng.shuffle(seq_list)
        xs = seq_to_signal("".join(seq_list), aa_scalar)
        helix_null[i] = 0.5 * (autocorr_lag(xs, 3) + autocorr_lag(xs, 4))
        sheet_null[i] = autocorr_lag(xs, 2)

    def zscore(obs, null):
        mu = float(null.mean())
        sd = float(null.std(ddof=1))
        return (obs - mu) / sd if sd > 1e-12 else 0.0

    ZH = zscore(helix_obs, helix_null)
    ZS = zscore(sheet_obs, sheet_null)
    return {"ZH": ZH, "ZS": ZS, "S": ZH - ZS, "helix_obs": helix_obs, "sheet_obs": sheet_obs}

def windowed_coherence(seq, aa_scalar=AA_SCALAR_PROXY, win=15):
    x = seq_to_signal(seq, aa_scalar)
    n = len(x)
    hel = np.zeros(n, dtype=float)
    sht = np.zeros(n, dtype=float)
    half = win // 2
    for i in range(n):
        a = max(0, i - half); b = min(n, i + half + 1)
        seg = x[a:b]
        h3 = autocorr_lag(seg, 3) if len(seg) > 5 else 0.0
        h4 = autocorr_lag(seg, 4) if len(seg) > 6 else 0.0
        s2 = autocorr_lag(seg, 2) if len(seg) > 4 else 0.0
        hel[i] = np.nanmean([h3, h4])
        sht[i] = s2 if not np.isnan(s2) else 0.0
    hel = (hel - hel.mean()) / (hel.std(ddof=1) + 1e-12)
    sht = (sht - sht.mean()) / (sht.std(ddof=1) + 1e-12)
    return hel, sht

def compile_constraints(seq, hel_z, sht_z,
                        hel_thresh=0.85, sht_thresh=0.85,
                        contact_k=10, contact_sep=8,
                        contact_freq=2, seed=0):
    rng = random.Random(seed)
    n = len(seq)
    d_hel_3, d_hel_4, d_sht_2, d_contact = 5.4, 6.2, 6.8, 7.5
    kinds = {"helix3": [], "helix4": [], "sheet2": [], "contact": []}

    for i in range(n):
        if hel_z[i] > hel_thresh:
            if i + 3 < n: kinds["helix3"].append((i, i+3, d_hel_3, 0.9, 1, 0))
            if i + 4 < n: kinds["helix4"].append((i, i+4, d_hel_4, 0.9, 1, 0))
        if sht_z[i] > sht_thresh and i + 2 < n:
            kinds["sheet2"].append((i, i+2, d_sht_2, 0.8, 1, 0))

    x = seq_to_signal(seq)
    pairs = []
    for i in range(n):
        for j in range(i + contact_sep, n):
            pairs.append((x[i]*x[j], i, j))
    pairs.sort(reverse=True, key=lambda t: t[0])

    used = set(); chosen = 0
    for score, i, j in pairs:
        if chosen >= contact_k: break
        if i in used or j in used: continue
        used.add(i); used.add(j)
        phase = chosen % contact_freq
        kinds["contact"].append((i, j, d_contact, 0.6, contact_freq, phase))
        chosen += 1

    def to_arrays(rows):
        if not rows:
            return {"i":np.array([],dtype=int),"j":np.array([],dtype=int),
                    "d0":np.array([],dtype=float),"w":np.array([],dtype=float),
                    "freq":np.array([],dtype=int),"phase":np.array([],dtype=int)}
        arr = np.array(rows, dtype=float)
        return {"i":arr[:,0].astype(int),"j":arr[:,1].astype(int),
                "d0":arr[:,2].astype(float),"w":arr[:,3].astype(float),
                "freq":arr[:,4].astype(int),"phase":arr[:,5].astype(int)}
    return {k: to_arrays(v) for k, v in kinds.items()}

def init_chain(n, bond=3.8, seed=0):
    rng = np.random.default_rng(seed)
    X = np.zeros((n, 3), dtype=float)
    dirs = rng.normal(size=(n-1, 3))
    dirs /= (np.linalg.norm(dirs, axis=1, keepdims=True) + 1e-12)
    X[1:] = np.cumsum(dirs * bond, axis=0)
    X += 0.3 * rng.normal(size=X.shape)
    return X

def project_bonds_vec(X, bond=3.8):
    X = X.copy()
    v = X[1:] - X[:-1]
    d = np.linalg.norm(v, axis=1) + 1e-12
    corr = ((bond - d) / d)[:, None] * v
    X[:-1] -= 0.5 * corr
    X[1:]  += 0.5 * corr
    return X

def anneal_sigmoid(step, steps, mid=0.5, k=10.0):
    t = step / max(1, steps-1)
    return float(1.0 / (1.0 + math.exp(-k*(t-mid))))

def constraint_energy_grad(X, C, step, w_scale=1.0):
    i = C["i"]
    if i.size == 0: return 0.0, np.zeros_like(X), 0.0
    active = ((step + C["phase"]) % C["freq"]) == 0
    if not np.any(active): return 0.0, np.zeros_like(X), 0.0
    ia = i[active]; ja = C["j"][active]
    d0 = C["d0"][active]
    w  = w_scale * C["w"][active]
    v = X[ja] - X[ia]
    d = np.linalg.norm(v, axis=1) + 1e-12
    diff = d - d0
    coef = (2.0 * w * diff / d)[:, None]
    gvec = coef * v
    G = np.zeros_like(X)
    np.add.at(G, ia, -gvec)
    np.add.at(G, ja,  gvec)
    E = float(np.sum(w * diff * diff))
    return E, G, float(np.max(np.abs(diff)))

def simulate_fold(seq, lr=0.33, steps=800, seed=0,
                  bond=3.8, grad_clip=4.0, trust=True,
                  contact_freq=2, contact_k=10,
                  trace_every=25, max_v_thresh=2.5, contact_v_thresh=1.2):
    hel_z, sht_z = windowed_coherence(seq)
    C = compile_constraints(seq, hel_z, sht_z, contact_k=contact_k, contact_freq=contact_freq, seed=seed)
    X = init_chain(len(seq), bond=bond, seed=seed)
    X = project_bonds_vec(X, bond=bond)

    trace = {"step": [], "E": [], "grad_norm": [], "step_scale": [], "v_max": [], "v_contact": []}
    status = "OK"
    for t in range(steps):
        X = project_bonds_vec(X, bond=bond)
        a_local = anneal_sigmoid(t, steps, mid=0.45, k=10.0)
        a_cont  = anneal_sigmoid(t, steps, mid=0.65, k=12.0)
        E3,G3,v3 = constraint_energy_grad(X, C["helix3"], t, w_scale=a_local)
        E4,G4,v4 = constraint_energy_grad(X, C["helix4"], t, w_scale=a_local)
        Es,Gs,vs = constraint_energy_grad(X, C["sheet2"], t, w_scale=a_local)
        Ec,Gc,vc = constraint_energy_grad(X, C["contact"], t, w_scale=a_cont)

        E = E3+E4+Es+Ec
        G = G3+G4+Gs+Gc
        gnorm = float(np.linalg.norm(G))
        if not np.isfinite(E) or not np.isfinite(gnorm):
            status = "DEAD_NaN"; break
        step_scale = lr / (gnorm / math.sqrt(X.size) + 1e-12) if trust else lr
        if gnorm > grad_clip:
            G *= grad_clip / (gnorm + 1e-12)
            gnorm = float(np.linalg.norm(G))
        X = X - step_scale * G
        if (t % trace_every) == 0 or t == steps-1:
            vmax = max(v3,v4,vs,vc)
            trace["step"].append(t)
            trace["E"].append(E)
            trace["grad_norm"].append(gnorm)
            trace["step_scale"].append(step_scale)
            trace["v_max"].append(vmax)
            trace["v_contact"].append(vc)

    # checkpoint
    E3,_,v3 = constraint_energy_grad(X, C["helix3"], steps-1, w_scale=1.0)
    E4,_,v4 = constraint_energy_grad(X, C["helix4"], steps-1, w_scale=1.0)
    Es,_,vs = constraint_energy_grad(X, C["sheet2"], steps-1, w_scale=1.0)
    Ec,_,vc = constraint_energy_grad(X, C["contact"], steps-1, w_scale=1.0)
    Ef = E3+E4+Es+Ec
    vmax = max(v3,v4,vs,vc)
    if status == "OK":
        status = "BORN" if (vmax <= max_v_thresh and vc <= contact_v_thresh) else "DEAD_CHECKPOINT"
    return {"status":status,"X":X,"Ef":float(Ef),"vmax":float(vmax),"v_contact":float(vc),"trace":trace}

def write_ca_pdb(seq, X, path, chain_id="A"):
    with open(path, "w") as f:
        atom_id = 1
        for res_id, (aa, (x,y,z)) in enumerate(zip(seq, X), start=1):
            resn = AA3.get(aa, "UNK")
            f.write(
                f"ATOM  {atom_id:5d}  CA  {resn:>3s} {chain_id}{res_id:4d}    "
                f"{x:8.3f}{y:8.3f}{z:8.3f}  1.00 20.00           C\n"
            )
            atom_id += 1
        f.write("END\n")
