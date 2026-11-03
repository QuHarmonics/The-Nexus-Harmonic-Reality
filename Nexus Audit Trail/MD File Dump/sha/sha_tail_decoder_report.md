# SHA Tail-First Decoder Prototype

## Summary
| decoder         |   top1_acc |   top5_acc |   top10_acc |   mean_rank |
|:----------------|-----------:|-----------:|------------:|------------:|
| internal_oracle |  0.422619  |  0.940476  |    1        |     2.25595 |
| digest_only     |  0.0297619 |  0.0714286 |    0.154762 |    29.0833  |

This ranks the true one-block length class (0..55) as a proxy for the control-tail class.

- **internal_oracle** uses execution fingerprints.
- **digest_only** uses final witness features only.

Interpretation:
- if internal decoding works and digest decoding weakens, then the tail-first order is structurally right but the final hash is a compressed shorthand of that order.
