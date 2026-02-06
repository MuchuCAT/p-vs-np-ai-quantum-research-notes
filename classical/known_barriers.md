# Known proof barriers for P vs NP (relativization, natural proofs, algebrization)

## Scope
This note covers three classic barriers that constrain broad families of proof techniques:
- Relativization (oracle access) [BGS75]
- Natural proofs (circuit lower-bound template) [RR94]
- Algebrization (algebraic oracle access) [AW09]

Goal: state what these results *imply* and what they *do not imply*, in an audit-friendly way.
Citation keys like `[BGS75]` refer to `../references/bibliography.md`.

## Why barriers matter
P vs NP is a worst-case, asymptotic statement about *all* inputs and *all* polynomial-time algorithms. [For09]
Barrier results do not “predict” outcomes; they delimit which broad proof templates cannot work *as stated*. [AB09]

---

## Relativization

### Definition
An oracle is an idealized black-box subroutine that a machine may query. Complexity classes can be relativized by granting the same oracle access to all machines being compared (e.g., P^A, NP^A). [BGS75]

Baker–Gill–Solovay constructed oracles A and B such that P^A = NP^A while P^B ≠ NP^B. This establishes that the P vs NP relation can differ across oracle worlds. [BGS75]

A related result shows that, with probability 1, a random oracle separates P from NP (and coNP), emphasizing that oracle behavior is not a reliable proxy for the unrelativized world. [BG81]

### What it rules out
- Any proof technique that *relativizes* (i.e., would remain valid after adding the same oracle to both sides) cannot resolve P vs NP, because it would contradict at least one of the BGS oracle worlds. [BGS75]
- In particular, “black-box simulation + diagonalization” templates that do not use non-relativizing structure are insufficient as a complete approach. [AB09]

### What it does NOT rule out
- It does not prove P vs NP is independent of standard axioms (independence would require a different kind of argument). [AB09]
- It does not rule out non-relativizing techniques; it only says a successful proof must use some step that fails under arbitrary oracle access. [BGS75]

### Typical misconceptions
- “Oracles are unrealistic, so relativization is irrelevant.” (False: the barrier critiques proof *methods*, not hardware.)
- “Relativization implies independence.” (Overreach: oracle separations ≠ logical independence.)
- “Diagonalization is dead.” (Too strong: only *relativizing* diagonalization is ruled out.)

### Key citations
[BGS75] [BG81] (context: [AB09])

---

## Natural proofs

### Definition
Natural proofs formalize a common circuit lower-bound template: identify a combinatorial property of Boolean functions that is (i) efficiently testable given a truth table (“constructive”), (ii) holds for many functions (“large”), and (iii) excludes all functions computable by a target circuit class (“useful”). [RR94]

Razborov–Rudich show that if such a natural property is strong enough to separate certain powerful circuit classes, then it can be converted into an efficient distinguisher that breaks standard pseudorandomness assumptions used in cryptography. The statement is conditional on those assumptions (as framed in the paper). [RR94]

### What it rules out
- Under the paper’s cryptographic assumptions, a large class of “generic” combinatorial lower-bound arguments (constructive + large + useful) cannot yield the strongest circuit lower bounds one would want for P vs NP via P/poly-style reasoning. [RR94]
- Practically: “find a simple, efficiently checkable property shared by most hard functions, then prove SAT has it” is not a safe plan at high generality. [RR94]

### What it does NOT rule out
- It does not prove strong lower bounds are impossible; it restricts a broad template under assumptions. [RR94]
- It does not rule out “non-natural” approaches (e.g., properties that are not efficiently recognizable, or not large, or otherwise outside the definition). [RR94]
- It does not by itself settle P vs NP in either direction. [AB09]

### Typical misconceptions
- “Natural proofs imply P ≠ NP is unprovable.” (False: it is a conditional barrier about one family of methods.)
- “All combinatorial arguments are ruled out.” (False: only those fitting the natural-proof definition.)
- “The barrier is unconditional.” (Misleading: it is conditional as stated in the original result.)

### Key citations
[RR94] (context: [AB09])

---

## Algebrization

### Definition
Algebrization extends relativization by giving machines access not only to an oracle, but also to an associated “algebraic” oracle (informally: low-degree extensions that support polynomial-based query access). [AW09]

Aaronson–Wigderson show there are algebraic oracle worlds in which key class relationships differ, in a way analogous to BGS but in a more “algebra-friendly” setting. This motivates the notion that some non-relativizing techniques may still “algebrize.” [AW09]

### What it rules out
- Any proof technique that *algebrizes* (i.e., remains valid in the algebraic-oracle framework) cannot resolve certain central separations, because contradictory algebraic oracle worlds exist. [AW09]
- Concretely: “generic arithmetization / low-degree reasoning as a black-box escape from relativization” is not, by itself, a complete strategy for P vs NP. [AW09]

### What it does NOT rule out
- It does not claim “algebra is useless.” It restricts approaches that survive the algebraic-oracle lift in the specific technical sense of the paper. [AW09]
- It does not provide a positive characterization of what *will* work; it only marks a boundary. [AB09]

### Typical misconceptions
- “Algebrization = relativization, so nothing new.” (False: it is a stricter, algebra-aware framework.)
- “Algebrization kills all algebraic approaches.” (Overclaim: it targets algebrizing templates, not every algebraic idea.)
- “This is a final barrier.” (Not a theorem: it is one barrier among others.)

### Key citations
[AW09] (context: [AB09])

---

## How these barriers relate to lower bounds
Strong lower bounds exist for restricted circuit classes (e.g., AC^0). [FSS84] [Has86]
There are also major nonuniform lower bounds for certain restricted models (e.g., NEXP vs ACC^0). [Wil11]

These successes do not automatically scale to general circuits; the barriers above explain why many broad templates fail when pushed to the regimes relevant for P vs NP. [RR94] [AW09]

## Sanity checklist for evaluating claimed resolutions
If a manuscript claims to resolve P vs NP, it should clearly address:
1) Relativization: does the method relativize? If yes, it cannot resolve P vs NP. [BGS75]
2) Natural proofs: does it fit the constructive+large template useful against strong circuits? If yes, it risks the RR barrier (under assumptions). [RR94]
3) Algebrization: does it survive the algebraic-oracle lift as in AW? If yes, it risks algebrization limits. [AW09]
