# Limits of AI approaches for P vs NP (what is missing)

## Scope
- practical solving vs proof-level progress
- why learning success is not class separation
- what would count as meaningful “AI assistance” (formal artifacts)

## Non-goals
- claiming AI cannot help at all
- predicting future systems
- benchmarking solvers

---

## 1) Practical wins vs theoretical statements
AI-assisted heuristics can solve large real-world instances of NP-hard problems.
This does not imply a polynomial-time algorithm for all instances,
and does not constitute a proof about P vs NP.

---

## 2) Pattern learning is not universality
A proof about P vs NP is universal: it must hold for all input sizes.
Learning systems often generalize within a distribution,
but that is not the same as a universal guarantee.

---

## 3) “Discovering an algorithm” is not the same as proving its complexity
Even if a model proposes an algorithm, proof-level progress requires:
- correctness proof
- runtime proof (polynomial bound)
- clarity about the computational model

---

## 4) Where AI can realistically help
The realistic help looks like tooling:
- assisting with formalization in proof assistants (Lean/Coq/Isabelle)
- proposing intermediate lemmas in restricted settings
- finding counterexamples to conjectures in related combinatorics
- automating verification, not replacing proof discovery

The bar remains: checkable artifacts, not persuasive text.

---

## 5) Open questions
- What artifacts would count as “AI contributed” progress? (e.g., a formally verified lemma)
- Can ML improve proof search without collapsing into pattern matching?
- Can we define benchmarks that correlate with proof-level difficulty?

## References
See ../references/bibliography.md
