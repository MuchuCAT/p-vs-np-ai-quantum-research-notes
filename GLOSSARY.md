# Glossary (minimal)

This glossary is intentionally compact. It defines only terms used in this dossier.

- **Decision problem / language**: a set of strings over an alphabet; input is a string; output is YES/NO. `[Sip12]`
- **P**: deterministic polynomial-time decision problems. `[Sip12]`
- **NP**: problems with polynomial-size certificates verifiable in polynomial time. `[Sip12]`
- **coNP**: complements of NP languages.
- **NP-complete**: in NP and NP-hard under polynomial-time many-one reductions. `[GJ79]`
- **Reduction (many-one, poly-time)**: mapping x ↦ f(x) computable in poly-time such that x∈L iff f(x)∈L'. `[Sip12]`
- **PH (Polynomial Hierarchy)**: hierarchy of classes extending NP/coNP via alternations of quantifiers. `[Sip12]`
- **P/poly**: nonuniform polynomial-size circuits (or advice-taking computation). `[KL82]`
- **Circuit lower bound**: a proof that a function requires large circuits in a given model. `[AB09]`
- **AC0**: constant-depth, unbounded fan-in AND/OR/NOT circuits. `[FSS84]`
- **ACC0**: AC0 plus MOD_m gates (fixed m). `[Wil11]`
- **BQP**: bounded-error quantum polynomial time. `[BV97]`
- **Oracle**: black-box subroutine available to the machine; used in relativization results. `[BGS75]`
- **Relativization**: a technique property meaning it remains valid relative to any oracle. `[BGS75]`
- **Natural proofs**: a broad template for circuit lower bounds; limited under crypto assumptions. `[RR94]`
- **Algebrization**: extension of relativization to algebraic oracle worlds. `[AW09]`
