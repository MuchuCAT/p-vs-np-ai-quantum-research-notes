# What P vs NP requires (and what it does not)

## Scope
This note focuses on:
- what the P vs NP question formally asks
- what would count as progress (proof-level progress)
- why “solving many instances” is not the same as proving a separation
- the main known barriers that shape what kinds of techniques are likely insufficient

## Non-goals
- presenting a proof sketch
- surveying every subfield related to P vs NP
- discussing practical SAT solving performance beyond illustrating the proof/empirical gap

---

## 1) The question, stated precisely
P vs NP asks whether every decision problem whose solutions can be verified in polynomial time
(NP) can also be solved in polynomial time (P).

A key point: this is a statement about *all input sizes* and *worst-case* complexity.

---

## 2) What counts as progress?
Progress on P vs NP typically means one of the following:

1) A proof that P = NP:
   - e.g. an explicit polynomial-time algorithm for an NP-complete problem (like SAT),
     with a proof of correctness and polynomial running time.

2) A proof that P ≠ NP:
   - e.g. a super-polynomial lower bound that rules out *all* polynomial-time algorithms
     for NP-complete problems (often framed via circuit lower bounds or related models).

Importantly, empirical success on many instances is not proof-level progress.

---

## 3) Verification vs finding
It is easy to confuse:
- verifying a given solution (polynomial)
with
- finding a solution (unknown in general)

P vs NP is exactly about whether this gap is real in the worst case.

---

## 4) Why “heuristics solve hard instances” is not a solution
Modern solvers can solve large real-world instances (SAT, scheduling, etc.).
This demonstrates:
- structure in many practical distributions
- strong engineering and heuristics

It does *not* establish:
- a polynomial-time algorithm for all instances
- a proof of separation between complexity classes

---

## 5) Known proof barriers (why the problem resists standard techniques)

### 5.1 Relativization (Baker–Gill–Solovay)
There exist oracles relative to which P = NP, and oracles relative to which P ≠ NP.
This suggests that proof techniques that “relativize” are insufficient to resolve P vs NP.

### 5.2 Natural proofs (Razborov–Rudich)
A broad family of circuit lower bound techniques (captured by “natural proofs”)
would, under standard cryptographic assumptions, also break pseudorandomness.
This implies that a large class of “combinatorial” lower bound strategies is unlikely to work.

### 5.3 Algebrization (Aaronson–Wigderson)
Even some non-relativizing techniques still “algebrize”.
Algebrization extends the barrier landscape and suggests that resolving P vs NP
requires techniques that are neither relativizing, nor natural, nor algebrizing.

---

## 6) What this implies (high-level)
Any credible attack on P vs NP must be clear about:
- whether it relativizes
- whether it looks “natural”
- whether it algebrizes

This does not prove impossibility of a solution,
but it explains why many naive narratives do not meet the proof bar.

---

## References (short list)
See ../references/bibliography.md
