# What P vs NP requires (and what it does not)

## Scope
This note explains:
- what the P vs NP question formally asks
- what would count as *proof-level* progress
- why empirical success (solvers, heuristics, benchmarks) is not a separation proof
- how lower bounds and proof barriers enter the story

Non-goals:
- proposing a proof strategy
- surveying all of complexity theory

References use keys like `[Sip12]`. See `../references/bibliography.md`.

## 1) Minimal formal statement

P and NP are classes of *decision problems* (languages) defined by resource bounds.

- **P**: problems decidable by a deterministic Turing machine in polynomial time. `[Sip12]`
- **NP**: problems whose *yes* instances have polynomial-size certificates verifiable in polynomial time. Equivalent: decidable by a nondeterministic Turing machine in polynomial time. `[Sip12]`

**P vs NP** asks whether these classes are equal:
- either **P = NP** (every efficiently verifiable problem is efficiently solvable),
- or **P ≠ NP** (verification can be strictly easier than finding). `[Sip12]`

## 2) NP-completeness and why SAT is central

A problem is **NP-complete** if:
1) it is in NP, and
2) every problem in NP reduces to it via a polynomial-time many-one reduction. `[Coo71] [Kar72] [GJ79]`

Cook showed SAT is NP-complete (Cook–Levin theorem). `[Coo71]`
Karp showed many combinatorial problems are NP-complete via reductions. `[Kar72]`

A standard consequence:
- If any NP-complete problem is in P, then **P = NP**. `[GJ79]`
- If one proves an NP-complete problem is not in P, then **P ≠ NP** (but proving this is exactly the hard part). `[AB09]`

## 3) What counts as “progress” on P vs NP

A result “about” P vs NP is not necessarily progress *on* P vs NP.

### 3.1 Proof-level progress
Typical proof-level progress would look like one of the following:

**(A) Prove P = NP**
- Give a polynomial-time algorithm for an NP-complete problem (e.g., SAT),
- Prove correctness,
- Prove a polynomial runtime bound in an accepted model. `[Sip12] [AB09]`

**(B) Prove P ≠ NP**
- Prove a super-polynomial lower bound excluding *all* polynomial-time algorithms for an NP-complete problem.
In practice this is often approached via **circuit lower bounds** or related models. `[AB09]`

### 3.2 What is not proof-level progress
- “We solved many benchmark SAT instances quickly.”
- “A heuristic works well on real distributions.”
- “A model predicts solutions with high accuracy.”
These are meaningful engineering achievements, but they do not establish a worst-case class separation. `[For09]`

## 4) Worst-case vs average-case, and why the distinction matters

P vs NP is a **worst-case** statement.
A polynomial-time algorithm must work on **all** instances of size n (up to polynomial factors), not merely on typical or structured instances. `[Sip12]`

This is why:
- strong performance on industrial instances does not directly imply P = NP,
- hardness in cryptography is not “settled” by P vs NP alone (it depends on specific assumptions),
- distributions and heuristics matter in practice but are not the same object as a class separation. `[AB09] [For09]`

## 5) Why lower bounds show up immediately

One widely studied route to P ≠ NP is via **nonuniform computation** (circuits):
- If SAT requires super-polynomial size circuits, that implies **P ≠ NP**. `[AB09]`
- Conversely, if NP ⊆ P/poly, major collapses follow (Karp–Lipton). `[KL82]`

However, proving strong lower bounds for general circuits remains out of reach.
We do have strong lower bounds for *restricted* circuit classes (AC0, ACC0, monotone circuits), which is evidence of difficulty rather than a resolution. `[FSS84] [Has86] [Wil11]`

## 6) The three barrier results (why naive techniques fail)

A key part of the modern understanding is that large families of proof techniques are known to be insufficient.

- **Relativization**: there exist oracles A such that P^A = NP^A and oracles B such that P^B ≠ NP^B. Many diagonalization-style arguments “relativize,” so they cannot settle P vs NP. `[BGS75]`
- **Natural proofs**: under standard cryptographic assumptions, a broad class of combinatorial circuit lower bound techniques would break pseudorandomness, suggesting those techniques cannot prove strong lower bounds. `[RR94]`
- **Algebrization**: even some non-relativizing techniques still fail in “algebraic oracle” worlds, extending the barrier landscape. `[AW09]`

This does not prove P vs NP is unresolvable.
It means that a credible proof must be explicit about whether it avoids these barrier patterns. `[AB09] [AW09]`

(See `known_barriers.md` for a careful treatment.)

## 7) What this note commits to (reader contract)

You should be able to quote the following as safe claims:

- P vs NP is a worst-case statement about class equality/separation. `[Sip12]`
- SAT is NP-complete and central via reductions. `[Coo71] [Kar72]`
- Relativization, natural proofs, and algebrization are formal barriers for broad technique families. `[BGS75] [RR94] [AW09]`
- Strong general circuit lower bounds remain unknown; restricted-model lower bounds exist. `[Has86] [Wil11]`

## Pointers
- Barriers: `known_barriers.md`
- Lower bounds survey: `lower_bounds_survey.md`
- Quantum perspective: `../quantum/quantum_and_PvNP.md`
- AI perspective: `../AI/limitations_of_AI.md`

