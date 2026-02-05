# Limits of AI approaches for P vs NP (what is missing)

## Scope
This note distinguishes:
- practical performance on NP-hard instances (solvers, heuristics, learned guidance)
from
- proof-level progress on P vs NP (class separation, worst-case guarantees)

Non-goals:
- claiming AI cannot contribute to mathematics
- forecasting future AI capabilities

References use keys like `[AvH14]`. See `../references/bibliography.md`.

---

## 1) The mismatch: empirical success vs universal statements

P vs NP is a universal, worst-case statement. `[Sip12]`
Success on many instances (even very large instances) does not imply:
- a polynomial-time algorithm for all instances, or
- a proof that no such algorithm exists.

Therefore “AI solves hard SAT benchmarks” is not, by itself, progress on P vs NP. `[For09]`

---

## 2) What would count as AI-relevant progress (conservative definition)

AI can matter for P vs NP if it produces *checkable artifacts* that fit into accepted proof workflows, e.g.:
- formally verified lemmas in proof assistants,
- machine-checked reductions or complexity-theoretic statements,
- verified proofs about restricted circuit classes,
- verified proof-complexity statements.

The key property is auditability: a human (or checker) can validate it. `[AvH14] [dM15]`

---

## 3) Why “model proposes an algorithm” is not enough

Even if a model proposes an algorithm, proof-level relevance requires:
- a correctness proof,
- a runtime bound proof (polynomial in input length),
- clarity about the computational model (uniform/nonuniform, randomization, advice, etc.). `[Sip12] [AB09]`

Without these, it is at best a hypothesis generator.

---

## 4) The realistic role of formal methods (where AI fits)

Formal verification has already succeeded in large mathematical proofs
(Kepler conjecture, Odd Order theorem), using proof assistants and extensive engineering. `[Hal17] [Gon13]`

This suggests a realistic “AI lane”:
- accelerate formalization,
- improve proof search,
- help manage large proof graphs.

But the *mathematical content* still must satisfy the complexity-theory constraints (including barriers). `[BGS75] [RR94] [AW09]`

---

## 5) Why theorem proving is not the same as “reasoning text”

Modern proof assistants (Lean, Coq, Isabelle) enforce precise semantics.
They do not accept persuasive prose; they accept derivations from axioms via inference rules. `[dM15]`

This matters because “LLM-style explanations” are not proof objects unless translated into a formal system.

---

## 6) Open questions (conservative)
- Can ML meaningfully improve search in formalized complexity theory while producing verifiable artifacts?
- Can we define benchmarks that correlate with *proof* difficulty (not just solving instances)?
- Can AI help explore “non-natural” candidate properties without falling into natural-proof patterns? `[RR94]`

---

## Pointers
- Core note: `../classical/what_p_vs_np_requires.md`
- Barriers: `../classical/known_barriers.md`

