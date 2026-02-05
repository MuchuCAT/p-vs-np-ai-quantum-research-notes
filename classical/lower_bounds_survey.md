# Lower bounds and why they matter for P vs NP (selected survey)

## Scope
This note explains (at a high level) why lower bounds are central to P vs NP,
and records a few canonical lower bound results for restricted circuit classes.

Non-goals:
- a complete survey
- detailed proofs

References use keys like `[Has86]`. See `../references/bibliography.md`.

## 1) Why lower bounds enter immediately

A common route to proving P ≠ NP is to show that an NP-complete problem (e.g., SAT)
requires super-polynomial resources in some model.

One important model is **nonuniform Boolean circuits** (P/poly):
- If SAT does not have polynomial-size circuits, then P ≠ NP. `[AB09]`
- If NP ⊆ P/poly, then the polynomial hierarchy collapses (Karp–Lipton), which is considered unlikely. `[KL82]`

So circuit lower bounds are tightly connected to the separation question. `[AB09]`

## 2) Restricted circuit classes: what we can prove

### 2.1 AC0: constant depth, unbounded fan-in AND/OR/NOT
A landmark result is that parity cannot be computed by polynomial-size AC0 circuits. `[FSS84]`
Håstad later proved near-optimal size lower bounds for AC0 (via switching lemmas). `[Has86]`

These results show that strong lower bounds are possible in restricted settings.

### 2.2 ACC0: AC0 plus modular counting gates
A major breakthrough is that NEXP is not in nonuniform ACC0 (Williams). `[Wil11]`
This is still far from a general circuit lower bound for SAT, but it demonstrates new technique families.

## 3) Why general circuit lower bounds are hard

Informally, moving from AC0 / ACC0 to general circuits removes structural restrictions
(depth, gate types, etc.) that lower bound arguments exploit.

Additionally, the **natural proofs barrier** explains why a broad family of combinatorial
lower bound techniques is unlikely to prove the strongest general bounds (under standard crypto assumptions). `[RR94]`

## 4) Proof complexity as a neighboring lens

P vs NP is also related to the size of propositional proofs.
Cook–Reckhow formalized propositional proof systems and connected proof size to complexity questions. `[CR79]`

This angle is not a substitute for circuit lower bounds,
but it is a major parallel research axis.

## Pointers
- Barriers: `known_barriers.md`
- Core note: `what_p_vs_np_requires.md`
