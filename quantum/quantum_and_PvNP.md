# Quantum computing and P vs NP (limits and what is actually known)

## Scope
This note summarizes:
- BQP as the baseline quantum analogue of polynomial time
- why Shor and Grover do not imply NP-complete problems are easy
- what oracle evidence says (and does not say) about quantum power

Non-goals:
- predicting future algorithms
- speculative claims about “quantum will solve NP-complete”

References use keys like `[BV97]`. See `../references/bibliography.md`.

---

## 1) Minimal class picture

- **BQP**: problems solvable by a quantum computer in polynomial time with bounded error. `[BV97]`
- A central open question is whether NP (or NP-complete problems) are contained in BQP.
No inclusion is known.

A standard containment is:
- BQP ⊆ PP (hence BQP ⊆ PSPACE). `[ADH97]`

This containment is not a separation, but it clarifies where BQP sits in the landscape.

---

## 2) Shor’s algorithm: major impact, but not NP-complete

Shor gives polynomial-time algorithms for factoring and discrete log on an ideal quantum computer. `[Sho97]`
Factoring is not known to be NP-complete, and Shor does not imply efficient SAT solving.

The cryptographic impact is real (RSA-like assumptions), but it is not a statement about NP-completeness.

---

## 3) Grover’s algorithm: quadratic speedup, still exponential for SAT

Grover provides O(sqrt(N)) search for unstructured search. `[Gro97]`
If applied to brute-force SAT over 2^n assignments, this becomes ~2^(n/2),
which is still exponential.

This is a speedup, not a collapse of NP into BQP.

Moreover, Grover-style search is essentially optimal for unstructured search. `[Gro97]`

---

## 4) “Could quantum solve NP-complete?” (conservative view)

Fortnow’s CACM synthesis treats the idea as unlikely given what is known,
absent new structural insights. `[For09]`

This is not a theorem.
It is an evidence-based position: known quantum techniques do not yield polynomial-time NP-complete algorithms.

---

## 5) Oracle evidence: quantum power has limits

Oracle separations show that some hoped-for containments fail in relativized worlds.

- Bennett et al. discuss strengths and weaknesses of quantum computing and provide oracle evidence about limitations. `[BBBV97]`
- Raz–Tal give an oracle separation between BQP and the polynomial hierarchy (PH). `[RT22]`

Oracle results do not settle the unrelativized world,
but they caution against naive “quantum subsumes NP” narratives.

---

## 6) What would be required for quantum to impact P vs NP directly

To affect P vs NP directly, one would need (for example):
- an efficient quantum algorithm for an NP-complete problem (NP ⊆ BQP), or
- a proof technique for classical complexity that uses quantum ideas in a non-relativizing, non-algebrizing way.

Neither is currently established. `[For09] [AW09]`

---

## Pointers
- Core note: `../classical/what_p_vs_np_requires.md`
- Barriers: `../classical/known_barriers.md`
