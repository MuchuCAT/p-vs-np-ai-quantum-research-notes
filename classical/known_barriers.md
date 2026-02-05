# Known proof barriers for P vs NP (relativization, natural proofs, algebrization)

## Scope
This note is limited to three barrier results that constrain broad families of techniques:
- Relativization (Baker–Gill–Solovay)
- Natural proofs (Razborov–Rudich)
- Algebrization (Aaronson–Wigderson)

The goal is not to “predict” what will work.
The goal is to state what these barriers *actually* imply and what they do *not* imply.

References use keys like `[BGS75]`. See `../references/bibliography.md`.

## 0) Why barriers matter

P vs NP is a statement about *all* inputs and *all* polynomial-time algorithms.
Historically, many proof attempts reuse high-level templates (diagonalization, generic combinatorial properties, arithmetization).
Barrier results show that large classes of such templates are insufficient.

A practical consequence:
Any serious proof narrative should state whether (and why) it avoids these barrier patterns. `[AB09]`

## 1) Relativization (Baker–Gill–Solovay)

### 1.1 The statement (informal but precise)
An **oracle** is an idealized black-box subroutine that a machine can query.
Baker–Gill–Solovay constructed oracles A and B such that:
- P^A = NP^A
- P^B ≠ NP^B
Therefore, any proof technique that “relativizes” cannot resolve P vs NP. `[BGS75]`

A related and widely cited fact:
With probability 1, a random oracle separates P and NP (and coNP), illustrating that oracle worlds vary widely. `[BG81]`

### 1.2 What “relativizes” usually means
A technique relativizes if it remains valid when both sides are given the same oracle access.
Many simulation/diagonalization arguments have this property. `[BGS75]`

### 1.3 What relativization does *not* say
- It does not say P vs NP is independent of standard axioms.
- It does not say diagonalization is “useless”; it says *relativizing diagonalization* cannot settle P vs NP.
- It does not rule out proofs that are “white-box” in a way that breaks relativization.

A canonical example of a non-relativizing breakthrough is IP = PSPACE (interactive proofs), which uses algebraic techniques that do not relativize in the same way. `[Sha92]`

## 2) Natural proofs (Razborov–Rudich)

### 2.1 The setting
Much lower-bound work can be phrased as: “the target function has some property P that random functions typically do not have, and circuits of a given size cannot compute functions with that property.”

Razborov–Rudich formalized a broad class of such arguments as **natural proofs**. `[RR94]`

### 2.2 The barrier (what it says)
Under standard cryptographic assumptions (existence of strong pseudorandom generators),
a “natural” method for proving strong circuit lower bounds would also distinguish pseudorandom functions from truly random functions.
That would break the assumed pseudorandomness.
Hence, if standard cryptographic assumptions hold, then natural proofs cannot establish the strongest lower bounds one would need (e.g., general super-polynomial lower bounds for NP). `[RR94]`

### 2.3 What natural proofs do *not* say
- They do not prove that strong lower bounds are impossible.
- They do not say all combinatorial arguments fail; they say a specific broad template fails under standard assumptions.
- They do not rule out “non-natural” approaches (e.g., approaches that rely on properties hard to recognize).

## 3) Algebrization (Aaronson–Wigderson)

### 3.1 Motivation
After relativization, the community searched for non-relativizing techniques, often involving arithmetization and algebraic methods.
Aaronson–Wigderson introduced **algebrization**, extending the oracle framework to “algebraic” oracles (low-degree extensions). `[AW09]`

### 3.2 The barrier (what it says)
Algebrization shows that even some non-relativizing techniques still fail to resolve key questions when moved to algebraic oracle worlds.
In particular, it suggests that settling P vs NP would require methods that are:
- non-relativizing, and also
- non-algebrizing (in the technical sense). `[AW09]`

A useful slogan (not a theorem):
“Arithmetization alone is not a universal escape hatch.”

### 3.3 What algebrization does *not* say
- It does not rule out algebraic approaches that use rigid, representation-theoretic, or highly structured invariants in a way not preserved by low-degree extensions.
- It does not rule out every approach that uses polynomials; it rules out a broad pattern of “generic” low-degree reasoning. `[AW09]`

## 4) How these barriers interact with lower bounds

Strong lower bounds for restricted circuit models exist:
- AC0 lower bounds (parity, switching lemma) `[FSS84] [Has86]`
- ACC0 lower bounds (NEXP not in ACC0) `[Wil11]`

But extending such results to general circuits runs into:
- the need for methods that are not natural (in the Razborov–Rudich sense),
- and often not captured by relativizing/algebrizing templates. `[RR94] [AW09]`

This is not a formal impossibility claim.
It is an explanation of why the remaining path is narrow.

## 5) A “sanity checklist” for evaluating claims (non-hype)

If a manuscript claims to resolve P vs NP, it should answer:

1) **Relativization**: Does the argument relativize? If yes, it cannot settle P vs NP. `[BGS75]`
2) **Naturalness**: Does it define an efficiently checkable property that holds for many random functions? If yes, it risks being “natural.” `[RR94]`
3) **Algebrization**: Does it rely only on generic low-degree extensions / black-box polynomial reasoning? If yes, it risks algebrizing. `[AW09]`

A claim that does not address these points is not necessarily wrong, but it is incomplete as a research narrative.

## Pointers
- Core P vs NP note: `what_p_vs_np_requires.md`
- Lower bounds survey: `lower_bounds_survey.md`
