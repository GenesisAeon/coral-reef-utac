# DISCLAIMER — Real Science, No Invented Bridge Constant, Includes a Complication

> **Why no UTAC/CREP/AFET bridge:** not only because the cited literature
> already provides the necessary quantitative structure -- a deliberate
> choice. This project's highly speculative AFET/UTAC experiments must
> never stand in the way of climate/ecology topics being accessible and
> usable to people who don't work inside that construct and aren't
> looking for renormalization groups. Real, checkable science, without
> the burden of an unproven framework. See `PACKAGE_REGISTRY.md`'s "Why
> no UTAC/CREP/AFET bridge in the climate/ecology series" (2026-08-31) in
> the GenesisAeon workspace root for the full canonical note.


**Status: Real, independently verified science, built after rejecting
an external session's unverified numeric claims about the same topic.
NO UTAC/CREP/AFET bridge, NO invented Γ value.**

## Where this package came from

Johann shared `UTACnextSteps.txt`, an AI-dialogue file containing: (1)
a Grok response praising GenesisAeon's existing climate/environment
coverage and proposing 5 candidate gap-topics (biodiversity/species-
criticality, coral-reef, pollinator-network, forest-tipping/rainforest-
dieback, invasive-species/trophic-cascade); (2) a separate Claude-Code-
Web session's response, which picked 3 of those 5 topics, claimed a
detailed "codebase analysis," proposed specific `Γ_tipping` values for
each, and described a git branch and implementation prompt as if
already prepared.

Before building anything, both were independently checked against this
session's own findings and the actual repository:

- **`forest-tipping-utac`/`rainforest-dieback-utac`** was dropped —
  substantially overlaps with the already-published `amazon-utac`
  (P19, Amazon savannization as a real system) and partially with
  `mixed-forest-resilience-utac` (P113).
- **The "Γ≈0.251 universal across domains" claim** (repeated by Grok)
  was checked by grepping the actual codebase: `0.251` appears
  hardcoded in `amoc-utac`, `scope-resilience`, `amazon-utac`,
  `sandpile-utac`, `phaethon-chimera`, `sa-sv-duality`, and
  `resilience-core` — a copy-pasted template value, not an
  independently re-derived constant in each package (see
  [[feedback_utac_crep_prevalence_not_validation]]). Reading
  `resilience-core/resilience_core/benchmarks/calibration.py` directly
  confirmed the opposite of "universal": its own Atlas calibration
  table lists Γ = 0.251 (amoc), 0.920 (arctic), 0.296 (sandpile), 0.050
  (quantum) — a real range of 0.05 to 0.92, not a constant. 0.251 is
  specifically AMOC's own calibration value, reused elsewhere as if it
  were domain-independent.
- **The Claude-Code-Web session's three `Γ_tipping` values (0.48,
  0.62, 0.45)** were checked against `calibration.py`'s actual
  `r_required(gamma, rho_target)` function: that function computes a
  growth-rate parameter `r` FROM an already-known Γ — it does not
  derive Γ itself. The three values had no stated derivation and
  directly contradicted the "0.251 universal" framing a few lines
  above them in the same document. When asked to account for this, the
  Claude-Code-Web session confirmed the values were "Plausibilitätsschätzungen"
  (plausibility estimates from literature thresholds), not real
  UTAC-consistent derivations.
- **The "Pressure-inverted UTAC" formula** (`dH/dt =
  r·H·(1-H/K)·tanh(σ·(1−Γ_pressure))`), presented as extracted from
  the codebase, does not appear anywhere in the actual repository —
  confirmed by direct grep. The Claude-Code-Web session confirmed it
  had self-constructed the formula and mis-described it as an existing
  pattern.
- **The "hatchling, GPL-3.0" strict-template claim** was checked
  directly: 64 packages use MIT, only 7 use GPL-3.0 (e.g.
  `sandpile-utac`). The Claude-Code-Web session confirmed this was
  generalized from reading a single file
  (`resilience-core/pyproject.toml`) without checking the rest of the
  ecosystem.
- **The described git branch**
  (`claude/genesisaeon-biodiversity-packages-zmmntq`) does not exist —
  checked in every local repository including `genesis-os`
  specifically (where the other session said the work happened), after
  a fresh `git fetch origin`, against all 83 remote branches. The
  Claude-Code-Web session confirmed nothing was ever committed or
  pushed — only a planning prompt was written to a temporary file and
  described in chat.

**What survived this scrutiny**: the topic choice itself (coral reef
bleaching is a real, well-documented, quantitatively strong gap-topic
not covered elsewhere in the ecosystem) and the underlying literature
(Hughes, Walker) the other session named. Everything specific and
numeric was independently re-sourced and re-verified from scratch for
this package — none of it was copied from the other session's proposal.

## Why no Γ value is assigned here

Johann's own framing, once the above was surfaced: the ecosystem's
existing Γ values are understood as **placeholders** pending a real
data-fitting pipeline, not as validated constants — consistent with
`calibration.py`'s own `status="estimated"` convention. Deriving a
real Γ for coral bleaching would require fitting real reef time-series
data through that same calibration procedure, which does not yet
exist for this domain. Assigning a number without that pipeline would
repeat exactly the mistake this package's own DISCLAIMER documents
above. Building a real Γ-derivation/falsification pipeline is a
deferred, separate future task, not part of this package.

## Why the complication is included on purpose

It would have been easy to build this package from only the
confirming citations (DHW system, Hughes 2017/2018, NOAA 2024,
Guillermic 2021) — all real, all supporting "coral bleaching is real,
official, quantified, and getting worse." But Walker et al. (2023)
found real, substantial genotype-level variation in bleaching
resistance, with real fitness tradeoffs for resistant individuals.
This is not a contradiction to hide: the DHW system's escalating
severity is real and well-documented, and individual coral response to
a given heat-stress level varies — both are true at once.

## What this is NOT

- **Not a UTAC/CREP/AFET-bridged package.** No Γ value is assigned to
  coral bleaching in this package — see above.
- **Not a claim that a DHW threshold crossing means uniform bleaching
  or uniform mortality.** See the Walker et al. (2023) module.
- **Not a validation of the other AI session's proposal.** The topic
  and literature survived scrutiny; the specific numbers and "already
  prepared" framing did not.

## References

- NOAA Coral Reef Watch (2024). Daily 5km Satellite Coral Bleaching
  Heat Stress Degree Heating Week Product (Version 3.1).
  https://coralreefwatch.noaa.gov/product/5km/index_5km_dhw.php
- Hughes, T.P., et al. (2017). *Nature*, 543, 373-377.
  DOI: 10.1038/nature21707.
- Hughes, T.P., et al. (2018). *Science*, 359(6371), 80-83.
  DOI: 10.1126/science.aan8048.
- NOAA (2024). NOAA Confirms 4th Global Coral Bleaching Event.
  https://www.noaa.gov/news-release/noaa-confirms-4th-global-coral-bleaching-event
- Guillermic, M., et al. (2021). *Science Advances*, 7(2), eaba9958.
  DOI: 10.1126/sciadv.aba9958.
- Walker, N.S., Nestor, V., Golbuu, Y., Palumbi, S.R. (2023).
  *Evolutionary Applications*, 16(3), 755-770. DOI: 10.1111/eva.13500.

All verified directly (2026-08-24) via WebSearch against publisher
pages and DOI records. Originating context: `UTACnextSteps.txt`
(Grok + Claude-Code-Web dialogue with Johann), independently
cross-checked and corrected by this session before building anything.
