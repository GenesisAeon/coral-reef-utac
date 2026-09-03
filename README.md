# coral-reef-utac

GenesisAeon Package 114 — NOAA Coral Reef Watch's real, official
Degree Heating Week (DHW) coral-bleaching threshold system, and the
real, escalating series of four documented global bleaching events.
**Deliberately has no UTAC/CREP/AFET bridge and no invented Γ value**
— see [DISCLAIMER.md](DISCLAIMER.md) for why.

For a plain-language explanation of the same topic (German, no jargon,
written for general audiences), see [WHITEPAPER.md](WHITEPAPER.md).

## Where this package came from

Chosen from a shortlist of 5 candidate gap-topics proposed via an
external AI dialogue about GenesisAeon's environment/climate/species-
protection coverage (`UTACnextSteps.txt`: Grok, then a separate
Claude-Code-Web session). That session's specific technical claims —
three invented `Γ_tipping` values (0.48/0.62/0.45), a "Pressure-
inverted UTAC" formula presented as if extracted from the codebase, a
"strict GPL-3.0 template" claim, and a git branch presented as if
already created — did **not** survive independent verification (the
formula appears nowhere in the actual code; the license claim was
generalized from a single file, 64 packages are actually MIT vs. 7
GPL-3.0; the branch does not exist in any local repo). Both sessions
converged on the topic being sound; this package is built from scratch
with independently verified citations, not the other session's numbers.

## Deliberately not one-sided

`is_bleaching_response_uniform_across_genotypes()` returns `False` —
Walker et al. (2023) found real, measured variation in heat resistance
between individual coral genotypes, with real fitness tradeoffs
(resistant genotypes grow slower during recovery). A DHW threshold
crossing does not mean uniform bleaching or uniform mortality.

## What's real here

- **NOAA Coral Reef Watch — Degree Heating Week (DHW)** — the actual
  operational metric used to issue global bleaching alerts: 0–20°C-weeks
  accumulated over a 12-week window, 5 alert levels (4/8/12/16/20°C-weeks)
  each with a documented real-world consequence. The scale itself had
  to be expanded from 2 to 5 levels in December 2023 because 2023's
  heat stress exceeded what the original scale described.
- **Hughes et al. (2017, *Nature*)** — the 2015–2016 event, the third
  documented global bleaching event, hit 91% of individual Great
  Barrier Reef reefs.
- **Hughes et al. (2018, *Science*)** — a real 100-site global
  analysis (1980–2016): the median return interval between severe
  bleaching events at a given reef has fallen to just 6 years — too
  short for many coral communities to fully recover.
- **NOAA (2024)** — confirmed the fourth global bleaching event:
  83.7% of the world's reef area affected, Jan 2023–Apr 2025. The full
  documented series is real and monotonically escalating: 21% (1998)
  → 37% (2010) → 68% (2014–2017) → 83.7% (2023–2025).
- **Guillermic et al. (2021, *Science Advances*)** — a real lab
  finding: corals can actively compensate for ocean acidification at
  normal temperature (28°C), but heat stress (31°C) disables that
  compensation entirely — not just an additive second stressor.
- **Walker et al. (2023, *Evolutionary Applications*)** — the
  honesty-check citation: real genotype-level variation in bleaching
  resistance in *Acropora hyacinthus* (Palau), with real fitness costs
  for resistant genotypes.

## Independent confirmation (added 2026-09-02)

The **GCRMN & ICRI "Status of Coral Reefs of the World: 2025"** report
(released 2026-08-31; DOI: [10.59387/LFPR6347](https://doi.org/10.59387/LFPR6347)),
based on 21.1 million observations across 36,886 sites in 124
countries/territories — a far larger and more recent dataset than
Hughes et al. (2018) above — independently confirms the shrinking
recovery window: global mean hard coral cover fell 9.5% relative to the
1980–2009 baseline (30.2% → 27.3%), via four cover-loss events (6.5% /
9.9% / 6.6% / 8.9%, 1998–2024). Recovery is real when reefs get enough
time (+6% cover, 2017–2019) — but that time has compressed to **5–6
years**, converging almost exactly with Hughes 2018's independently
measured 6-year median. As lead author Dr. Manuel González Rivero put
it: *"Coral reefs once had decades to recover after major bleaching
events. Today, they're lucky to get five or six years."*
`is_recovery_window_independently_confirmed_narrow()` checks this
convergence directly. This is a different metric (cover loss) than the
NOAA/Hughes reef-area-affected series above — complementary evidence,
not a duplicate.

## Quickstart

```bash
pip install coral-reef-utac
```

```python
from coral_reef_utac import (
    alert_level_for_dhw, consequence_for_alert_level,
    GLOBAL_EVENTS, is_severity_monotonically_increasing, recovery_window_years,
    can_corals_compensate_for_acidification_under_heat_stress,
    is_bleaching_response_uniform_across_genotypes,
)

print(alert_level_for_dhw(9.5))                 # 2
print(consequence_for_alert_level(2))
print(list(GLOBAL_EVENTS.reef_area_affected_pct_by_event.values()))  # [21.0, 37.0, 68.0, 83.7]
print(is_severity_monotonically_increasing())    # True
print(recovery_window_years())                   # 6.0
print(can_corals_compensate_for_acidification_under_heat_stress())  # False
print(is_bleaching_response_uniform_across_genotypes())              # False
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
