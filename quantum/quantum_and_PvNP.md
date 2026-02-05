# Quantum computing and P vs NP (limits and misconceptions)

## Scope
- what BQP represents (quantum polynomial-time with bounded error)
- why Shor and Grover do not imply NP-complete problems are easy
- what is actually known / unknown about NP vs BQP

## Non-goals
- claiming quantum computers will never help
- speculating about unknown algorithms without sources

---

## 1) Complexity classes: the minimal picture
BQP is the class of problems efficiently solvable on a quantum computer (with bounded error).
A key open question is whether NP (or NP-complete problems) are contained in BQP.

No such inclusion is known.

---

## 2) Shor’s algorithm: impressive but not NP-complete
Shor gives polynomial-time factoring and discrete log (on an ideal quantum computer).
Factoring is not known to be NP-complete, and Shor does not imply efficient SAT solving.

---

## 3) Grover’s algorithm: quadratic speedup, still exponential for SAT
Grover provides O(sqrt(N)) search for unstructured search.
Applied to brute-force SAT, it turns 2^n into 2^(n/2): still exponential.

This is a speedup, not a complexity class collapse.

---

## 4) What would be required for a quantum “impact” on P vs NP
To affect P vs NP directly, one would need either:
- NP-complete in BQP (an efficient quantum algorithm for NP-complete problems), or
- a fundamentally new proof technique that uses quantum ideas in complexity theory.

Neither is currently established.

---

## 5) Open questions
- Are there structural reasons NP-complete problems resist quantum speedups?
- Could quantum help indirectly via proof technique innovation (not brute force)?
- What do oracle separations suggest about limits?

## References
See ../references/bibliography.md
