# Tsolmondorj Natsagdorj — selected work

Systems & research engineer working on **reliable AI, autonomous systems, and security-critical infrastructure**. This page is deliberately evidence-first: merged upstream code, measured results, public research, and reproducible systems work.

[GitHub](https://github.com/0xSoftBoi) · [writing](https://0xsoftboi.github.io) · [ORCID 0009-0009-6010-6273](https://orcid.org/0009-0009-6010-6273)

## Upstream contributions

Code accepted by projects I do not control.

| Project | Contribution | Proof |
|---|---|---|
| **MatGL** | Added reusable MC-dropout uncertainty estimation for pretrained materials models, with batched inference and regression coverage | [merged #801](https://github.com/materialyzeai/matgl/pull/801) |
| **MatGL** | Made `SoftExponential` autograd-correct and guarded its numerically invalid regions | [merged #809](https://github.com/materialyzeai/matgl/pull/809) |
| **MLX-LM** | Corrected XTC sampling defaults that could collapse the candidate distribution | [merged #1372](https://github.com/ml-explore/mlx-lm/pull/1372) |
| **Alloy** | Added EIP-712 canonicalization support for legal self-referential struct types while preserving cycle rejection where required | [merged #1105](https://github.com/alloy-rs/core/pull/1105) |
| **uutils/coreutils** | Fixed `date` so timezone abbreviations describe input time while output is re-zoned like GNU `date` | [merged #12327](https://github.com/uutils/coreutils/pull/12327) |
| **uutils/parse_datetime** | Added AM/PM combined parsing | [merged #284](https://github.com/uutils/parse_datetime/pull/284) |
| **uutils/parse_datetime** | Corrected floor semantics for negative fractional Unix timestamps | [merged #285](https://github.com/uutils/parse_datetime/pull/285) |
| **uutils/parse_datetime** | Added bare `UT` / `ut` UTC compatibility | [merged #287](https://github.com/uutils/parse_datetime/pull/287) |

## Flagship work

### [roce-preflight](https://github.com/0xSoftBoi/roce-preflight)

RDMA/RoCE diagnostic tooling built around a simple rule: distinguish what was **observed on hardware** from what was inferred or simulated. Real RDMA CI exposed failures that a large unit-test suite did not.

**Signal:** networking · Linux/RDMA · systems diagnostics · hardware-backed validation

### [BRIDGE-bench](https://github.com/0xSoftBoi/anthropic-fellowship)

Evaluation research on whether static analysis and LLM-assisted methods detect compositional cross-chain failures. The project explicitly investigates benchmark leakage and evaluator validity rather than preserving a flattering headline metric.

**Signal:** evaluations · AI security · experimental design · research integrity

### [active-materials-discovery](https://github.com/0xSoftBoi/active-materials-discovery)

Active-learning experiments over pretrained materials models. Includes batched MC-dropout performance work and calibration analysis showing when uncertainty estimates do not provide useful acquisition information. Part of this work became the upstream MatGL uncertainty utility above.

**Signal:** PyTorch · scientific ML · uncertainty · profiling/performance

### [aiur](https://github.com/0xSoftBoi/aiur)

Autonomous airborne-carrier research prototype. The project decomposes a speculative vehicle concept into constrained simulation, docking/recovery control, test tooling, BOMs, and measurable prototype milestones.

**Signal:** autonomy · controls/simulation · robotics · hardware/software systems

## Security-critical systems

### [lock-mint-bridge-lab](https://github.com/0xSoftBoi/lock-mint-bridge-lab)

A lock-and-mint bridge treated as an adversarial systems problem: stateful solvency invariants, static analysis, formal/symbolic checks, and reproductions of historical bridge failure modes.

### Suwappu / Lattice

I build [Suwappu](https://suwappu.bot), with work spanning transaction infrastructure, distributed systems, cryptographic protocols, bridge safety, post-quantum experiments, proof verification, and production reliability. Product work is kept separate here from third-party upstream contributions: the upstream table above is the external-review signal.

## Current upstream work

I also contribute fixes and experiments around Rust ML inference, model serving, numerical correctness, parser/system compatibility, and developer tooling. Open work is intentionally not counted as an accepted upstream contribution until maintainers merge it.

## Engineering thesis

The common thread across these projects is **correctness under hidden failure modes**: abstractions that behave differently on real hardware, benchmarks that measure the wrong thing, numerical methods whose uncertainty is not calibrated, parsers with edge-case semantics, and distributed protocols operating under adversarial conditions.

I prefer reproducible failures, explicit boundaries, measured results, and tests that can falsify the implementation.
