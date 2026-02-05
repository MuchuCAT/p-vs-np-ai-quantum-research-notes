# Roadmap (12 months)

This roadmap is scoped to produce a credible, audit-friendly dossier.

## Month 1–3: foundation and consistency (v0.1 → v0.2)
Deliverables:
- Stabilize definitions and citation keys across all notes.
- Expand `classical/what_p_vs_np_requires.md` with one short subsection on:
  - NP vs coNP / proof systems link (still conservative) `[CR79]`
  - P/poly and why it matters `[KL82]`
- Keep `references/bibliography.md` curated (no link rot, DOI/arXiv preferred).
- Add a short “reader contract” paragraph to each note (scope + non-goals).

Optional (light code):
- A tiny script to validate citation keys used in markdown exist in bibliography.

## Month 4–6: deepen the classical spine (v0.2 → v0.3)
Deliverables:
- Expand `lower_bounds_survey.md` with:
  - clearer separation: uniform vs nonuniform
  - one paragraph on why restricted-model lower bounds do not lift automatically
- Add one new note (optional): `classical/proof_complexity_bridge.md` (2–3 pages max)
  - define Cook–Reckhow proof systems `[CR79]`
  - state the NP vs coNP connection carefully
- Tighten `known_barriers.md` with one “what would bypass look like?” paragraph per barrier (non-speculative).

## Month 7–9: quantum and AI sections become reference-quality (v0.3 → v0.4)
Quantum:
- Add a short subsection explaining why oracle results are evidence but not resolution.
- Add a compact paragraph on BQP ⊆ PP and why it matters. `[ADH97]`

AI:
- Add one subsection: “formal artifacts pipeline”
  - Lean/SMT tooling citations only `[dM15] [dMB08]`
  - no benchmark hype

Optional (code):
- A small Lean project stub (empty) only if you commit to maintaining it.

## Month 10–12: polish + external readability (v0.4 → v1.0)
Deliverables:
- Add an executive “1-page overview” appendix (still conservative).
- Ensure every claim that sounds like a theorem is cited.
- Remove any remaining informal sources from the main notes.
- Tag `v1.0` only when:
  - citation keys are stable
  - glossary covers all classes referenced
  - notes cross-link cleanly

Release discipline:
- small commits
- clear commit messages
- no “breakthrough” language
