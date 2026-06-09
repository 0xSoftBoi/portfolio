# Tsolmondorj Natsagdorj — work & proof

Security & systems engineer (online: **0xSoftBoi**). Cross-chain infrastructure and
smart-contract security — Rust and the EVM. Every item below links to a **primary source
you can verify yourself** (a merged PR, a DOI, a public repo).

Site: [0xsoftboi.github.io](https://0xsoftboi.github.io) · GitHub: [@0xSoftBoi](https://github.com/0xSoftBoi) · ORCID: [0009-0009-6010-6273](https://orcid.org/0009-0009-6010-6273)

## Merged into upstream projects
| Project | Contribution | Proof |
|---|---|---|
| **alloy-rs/core** (the Rust lib behind Foundry & Reth) | EIP-712 self-referential struct canonicalization in `dyn-abi` | [merged PR #1105](https://github.com/alloy-rs/core/pull/1105) |
| **uutils/coreutils** (Rust rewrite of GNU coreutils) | `date` timezone re-zoning | [merged PR #12327](https://github.com/uutils/coreutils/pull/12327) |

## Security
| Project | What it is | Link |
|---|---|---|
| **lock-mint-bridge-lab** | Lock-and-mint bridge audited end-to-end: `supply ≤ collateral` invariant, attestation-gate fix, 512×100 Foundry invariant suite, Ronin/Wormhole/Nomad exploit reproductions | [repo](https://github.com/0xSoftBoi/lock-mint-bridge-lab) |
| **quantgroup** | Constant-product AMM annotated for auditors: attack simulations, stateful invariants, Wake fuzzing, SWC/CWE mapping | [repo](https://github.com/0xSoftBoi/quantgroup) |
| **cowswaprouter** | TWAP order splitter for CoW Protocol with a Wake fuzz suite | [repo](https://github.com/0xSoftBoi/cowswaprouter) |
| **zk-dark-chess** | ZK move-legality over a Poseidon commitment (Circom + Groth16), verified on-chain | [repo](https://github.com/0xSoftBoi/zk-dark-chess) |
| **fhe-dark-chess** | Fog-of-war chess over an encrypted board (Zama tfhe-rs) | [repo](https://github.com/0xSoftBoi/fhe-dark-chess) |

## Research
| Project | Result | Link |
|---|---|---|
| **BRIDGE-bench** | LLM reasoning vs. real cross-chain bridge exploits — static analysis ~0% F1, static-pre-filtered LLM ~40% F1 | [code](https://github.com/0xSoftBoi/anthropic-fellowship) · [DOI 10.5281/zenodo.20604295](https://doi.org/10.5281/zenodo.20604295) |
| **gnome-materials** | GNoME-style active learning on a pretrained CHGNet potential — 95% top-100 recall at a 20% labeling budget | [repo](https://github.com/0xSoftBoi/gnome-materials) |

## Writing
Long-form technical write-ups (bridge & DeFi security, on-chain randomness, applied ML,
systems): [0xsoftboi.github.io/blog](https://0xsoftboi.github.io/blog/)
