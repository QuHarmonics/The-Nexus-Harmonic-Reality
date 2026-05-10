# SHA-256 Shape-Only Probe v0

## Purpose

Test the claim:

$$
\boxed{\text{the hidden space is in shape, not scalar value}}
$$

The probe runs two controlled experiments.

1. **Same value, different input location.** The same 32-bit value, `0xffffffff`, is inserted into different message-word positions of an otherwise zero 55-byte one-block message. Length, value, and bit-count are held constant. Only spatial placement changes.

2. **Same length and same Hamming weight, different geometry.** 480 messages are generated with identical length and identical message Hamming weight, but with different bit-shapes: cluster, double-cluster, uniform, random, alternating, and mirror.

The SHA-256 implementation was verified against `hashlib` for `b"abc"`.

---

## Experiment 1 — Same value, different shape/location

The scalar perturbation is always:

$$
v=0xffffffff
$$

and it is moved through word positions:

$$
M_k=v,\quad k=0,1,\dots,12.
$$

The measured state difference is the Hamming distance between the perturbed trajectory and the all-zero baseline trajectory:

$$
D_r(k)=HW\big(x_r^{(k)}\oplus x_r^{(0)}\big).
$$

### Result table

|   word_index |   first_full_lane_round |   first_ge_128_bits_round |   max_state_diff_hw |   state_diff_auc |   digest_hamming_distance |
|-------------:|------------------------:|--------------------------:|--------------------:|-----------------:|--------------------------:|
|            0 |                       4 |                        13 |                 143 |             7922 |                       114 |
|            1 |                       5 |                         7 |                 149 |             7788 |                       128 |
|            2 |                       6 |                         8 |                 147 |             7725 |                       141 |
|            3 |                       7 |                         9 |                 144 |             7582 |                       131 |
|            4 |                       8 |                        12 |                 152 |             7383 |                       127 |
|            5 |                       9 |                        12 |                 140 |             7118 |                       127 |
|            6 |                      10 |                        17 |                 140 |             6997 |                       128 |
|            7 |                      11 |                        14 |                 142 |             6864 |                       134 |
|            8 |                      12 |                        14 |                 144 |             6791 |                       134 |
|            9 |                      13 |                        15 |                 145 |             6644 |                       129 |
|           10 |                      14 |                        22 |                 139 |             6531 |                       135 |
|           11 |                      15 |                        17 |                 139 |             6341 |                       137 |
|           12 |                      16 |                        30 |                 150 |             6267 |                       122 |

### Collapse

The first all-lane saturation round obeyed:

$$
\boxed{r_{full}=k+4}
$$

with correlation:

$$
\operatorname{corr}(k,r_{full})=1.000000.
$$

The state-difference area under curve decreased almost perfectly with word position:

$$
\operatorname{corr}\left(k,\sum_r D_r(k)\right)=-0.995135.
$$

This is the strongest v0 result:

$$
\boxed{\text{same value + different placement shape}\Rightarrow\text{different trajectory geometry}}
$$

The value did not change. The shape of the input changed.

---

## Experiment 2 — Same length and Hamming weight, different bit geometry

All samples use:

$$
\text{length}=55\text{ bytes},\qquad HW(M)=64.
$$

Only the spatial arrangement of the 64 set bits changes.

### Family means

| family         |   transitions |   one_runs |   longest_one_run |   spread |   t2_carry_mean |   t1_carry_union_mean |   digest_hw |   nibble_curvature_abs_mean |
|:---------------|--------------:|-----------:|------------------:|---------:|----------------:|----------------------:|------------:|----------------------------:|
| alternating    |      128      |    64      |            1      |  36.9459 |         15.8184 |               31.2287 |     129.012 |                      9.3091 |
| cluster        |        2      |     1      |           64      |  18.473  |         15.8211 |               31.191  |     127.375 |                      9.3992 |
| double_cluster |        3.9625 |     1.9875 |           32.4    |  83.5864 |         15.7721 |               31.207  |     128.738 |                      9.351  |
| mirror         |      108.975  |    54.5875 |            2.7125 | 125.421  |         15.5574 |               31.2271 |     126.562 |                      9.376  |
| random         |      108.562  |    54.375  |            3.05   | 124.799  |         15.5957 |               31.2467 |     126.688 |                      9.2135 |
| uniform        |      125.75   |    63.0125 |            1.9875 | 126.876  |         15.508  |               31.2574 |     126.562 |                      9.3165 |

### ANOVA / permutation significance

| metric                    |   eta2_family |        F |     perm_p |
|:--------------------------|--------------:|---------:|-----------:|
| t2_carry_mean             |    0.0346339  | 3.40109  | 0.00664452 |
| t1_carry_union_mean       |    0.0309104  | 3.02377  | 0.00996678 |
| T1T2_angle_mean           |    0.0174447  | 1.68312  | 0.152824   |
| digest_hw                 |    0.0162232  | 1.56332  | 0.166113   |
| nibble_equal_neighbors    |    0.012568   | 1.20662  | 0.315615   |
| T1_hw_mean                |    0.0116268  | 1.11519  | 0.358804   |
| t1_carry_mean             |    0.0113976  | 1.09295  | 0.401993   |
| nibble_reversals          |    0.0110147  | 1.05582  | 0.438538   |
| T2_hw_mean                |    0.0104574  | 1.00184  | 0.408638   |
| digest_transitions        |    0.00594298 | 0.566763 | 0.69103    |
| nibble_curvature_abs_mean |    0.00309459 | 0.294278 | 0.933555   |

The strongest shape effects were in the internal carry geometry:

$$
\eta^2_{family}(\text{T2 carry mean})=0.034634,
\qquad p\approx 0.006645.
$$

$$
\eta^2_{family}(\text{T1 carry union mean})=0.030910,
\qquad p\approx 0.009967.
$$

Digest-surface metrics were weaker, which is expected: the digest is the stripped interface. The internal carry path is where the shape is still visible.

---

## Interpretation

The shape-only result is not a full inversion proof. It is a controlled proof-of-principle:

$$
\boxed{\text{SHA does not only respond to scalar value; it responds to placement geometry.}}
$$

The one-word experiment is decisive because the inserted value is constant. The only thing varied is where the same event enters the field.

The family experiment shows the same principle at a higher level: when length and Hamming weight are held fixed, internal carry metrics still change with geometric arrangement.

Therefore the hidden space is not "out there." It lives in:

$$
\boxed{\text{position, adjacency, support, transport time, carry topology, and boundary closure}}
$$

The digest hides most of this. The event-history field records it.

---

## Stable collapse

$$
\boxed{\text{value is the residue; shape is the path that made the residue possible.}}
$$

$$
\boxed{\text{inversion must track shape through the field, not stare at final values.}}
$$
