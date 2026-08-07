# Tsolmondorj Natsagdorj — work & proof

Systems + ML engineer (online: **0xSoftBoi**) working on model evaluation, agent infrastructure, and security-critical software. The useful unit here is evidence: every claim below points to a merged upstream change, reproducible repository, or DOI.

Site: [0xsoftboi.github.io](https://0xsoftboi.github.io) · GitHub: [@0xSoftBoi](https://github.com/0xSoftBoi) · ORCID: [0009-0009-6010-6273](https://orcid.org/0009-0009-6010-6273)

## Merged upstream

| Project | Contribution | Proof |
|---|---|---|
| **ml-explore/mlx-lm** | Corrected the XTC sampler threshold default | [merged PR #1372](https://github.com/ml-explore/mlx-lm/pull/1372) |
| **materialyzeai/matgl** | Added `MCDropoutWrapper`; fixed SoftExponential autograd / NaN behavior | [merged PR #801](https://github.com/materialyzeai/matgl/pull/801) · [#809](https://github.com/materialyzeai/matgl/pull/809) |
| **alloy-rs/core** | EIP-712 self-referential struct canonicalization in `dyn-abi` | [merged PR #1105](https://github.com/alloy-rs/core/pull/1105) |
| **uutils/coreutils** | `date` timezone re-zoning | [merged PR #12327](https://github.com/uutils/coreutils/pull/12327) |
| **uutils/parse_datetime** | AM/PM parsing, epoch-floor semantics, and `UT` timezone support | [#284](https://github.com/uutils/parse_datetime/pull/284) · [#285](https://github.com/uutils/parse_datetime/pull/285) · [#287](https://github.com/uutils/parse_datetime/pull/287) |

## Research & evaluation

| Project | What survived scrutiny | Proof |
|---|---|---|
| **BRIDGE-bench** | Eval on real cross-chain exploits. A measurement audit found bug-description leakage in 13/24 prompts and a 14.5-point judge sensitivity; the benchmark now includes sanitization, matched controls, dataset-integrity checks, and judge-validity tests. | [code](https://github.com/0xSoftBoi/anthropic-fellowship) · [DOI 10.5281/zenodo.20604295](https://doi.org/10.5281/zenodo.20604295) |
| **active-materials-discovery** | ~5.15× discovery acceleration on `matbench_perovskites`; MC-dropout uncertainty was miscalibrated (Spearman ρ = -0.47 vs. absolute error), so the gain came from the model mean rather than the uncertainty bonus. | [repo](https://github.com/0xSoftBoi/active-materials-discovery) |

## Systems & security

| Project | Engineering signal | Proof |
|---|---|---|
| **sensorforge** | Robotics monorepo spanning iPhone/ARKit sensor capture, Jetson integration, and a Rust/Metal/CUDA active-inference runtime | [repo](https://github.com/0xSoftBoi/sensorforge) |
| **suwappubot** | Agent-native cross-chain system with provider integrations, SDKs, agent interfaces, and security-critical execution | [repo](https://github.com/0xSoftBoi/suwappubot) |
| **evmsec** | Security CLI with bridge-solvency checks, real incident fixtures, JSON/SARIF output, and CI across Node 20/22 | [repo](https://github.com/0xSoftBoi/evmsec) |
| **lock-mint-bridge-lab** | Lock-and-mint bridge audited with stateful Foundry invariants plus Ronin/Wormhole/Nomad exploit reproductions | [repo](https://github.com/0xSoftBoi/lock-mint-bridge-lab) |

## Writing

Long-form technical work: [0xsoftboi.github.io/blog](https://0xsoftboi.github.io/blog/). I also wrote [Printing Money](https://tsoma2.gumroad.com/l/printingmoney); its [Foundry labs](https://github.com/0xSoftBoi/printing-money-labs) are public and runnable.
