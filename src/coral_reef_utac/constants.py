"""Verified constants for coral bleaching as a real, official threshold system.

GenesisAeon Package 114. Chosen from a shortlist of 5 candidate gap-topics
(biodiversity/species-criticality, coral-reef, pollinator-network, forest-
tipping, invasive-species) proposed via an external AI dialogue
(`UTACnextSteps.txt`, Grok + a separate Claude-Code-Web session) about
GenesisAeon's environment/climate/species-protection coverage. That
proposal's specific numeric claims (three invented "Gamma_tipping" values
0.48/0.62/0.45, a "Pressure-inverted UTAC" formula presented as if it
already existed in the codebase, a "strict GPL-3.0 template" claim, and a
git branch presented as if already created) were independently checked
and found NOT to hold up -- see the session's own correction exchange in
UTACnextSteps.txt. This package is built from scratch, using only
independently verified citations, not the other session's proposal.

Coral bleaching was chosen over the other three remaining candidates
because NOAA Coral Reef Watch's own operational system (Degree Heating
Weeks, DHW) is ALREADY a real, official, quantitative accumulated-stress
threshold-crossing system -- the closest natural fit to this ecosystem's
general threshold-activation interest, without needing to invent a bridge
or a Gamma value. Deliberately NO UTAC/CREP/AFET bridge and NO invented
Gamma value for this package -- see [[feedback_utac_crep_prevalence_not_validation]]
and DISCLAIMER.md for why: this session independently confirmed that the
"Gamma=0.251 universal across domains" claim repeated elsewhere in this
ecosystem is actually just the AMOC-specific calibration value
(resilience-core/benchmarks/calibration.py's own Atlas table shows real
Gamma values ranging 0.05-0.92 across domains, not a constant) -- so no
new Gamma value is assigned here without a real data-fitting pipeline,
which does not yet exist (see the "R-Herleitung/Falsifizierung" open
item, deferred to a future session).

All citations independently verified via direct source lookup on
2026-08-24.
"""

PACKAGE_ID = 114

# =====================================================================
# NOAA Coral Reef Watch: Degree Heating Week (DHW) operational system
# =====================================================================

NOAA_CRW_DHW_CITATION = (
    "NOAA Coral Reef Watch (2024). Daily 5km Satellite Coral Bleaching "
    "Heat Stress Degree Heating Week Product (Version 3.1). "
    "https://coralreefwatch.noaa.gov/product/5km/index_5km_dhw.php"
)

DHW_SCALE_MIN_C_WEEKS = 0.0
DHW_SCALE_MAX_C_WEEKS = 20.0
DHW_ACCUMULATION_WINDOW_WEEKS = 12

DHW_ALERT_LEVEL_THRESHOLDS_C_WEEKS: dict[int, float] = {
    1: 4.0,
    2: 8.0,
    3: 12.0,
    4: 16.0,
    5: 20.0,
}

DHW_ALERT_LEVEL_CONSEQUENCE: dict[int, str] = {
    1: "Bleaching risk: reef-wide bleaching likely for heat-sensitive corals",
    2: "Severe, widespread bleaching AND mortality of heat-sensitive corals likely",
    3: "Risk of mortality for multiple species",
    4: "Risk of severe multi-species mortality (>50% of corals)",
    5: "Risk of near-complete mortality (>80% of corals)",
}

DHW_ALERT_LEVELS_3_TO_5_ADDED_YEAR = 2024
DHW_ALERT_LEVELS_3_TO_5_ADDED_NOTE = (
    "NOAA Coral Reef Watch expanded its alert scale from 2 levels to 5 "
    "levels in December 2023 (in effect from 2024), specifically in "
    "response to extreme, previously-unprecedented marine heat stress "
    "observed in 2023 -- the existing 2-level scale from the 1990s no "
    "longer captured the range of real outcomes being measured."
)

# =====================================================================
# Hughes et al. 2017: the third global bleaching event (2015-2016)
# =====================================================================

HUGHES_2017_CITATION = (
    "Hughes, T.P., Kerry, J.T., Alvarez-Noriega, M., et al. (2017). "
    "Global warming and recurrent mass bleaching of corals. Nature, "
    "543, 373-377. DOI: 10.1038/nature21707"
)
HUGHES_2017_DOI = "10.1038/nature21707"

HUGHES_2017_GBR_2016_REEFS_AFFECTED_PCT = 91.0
HUGHES_2017_NOTE = (
    "2015-2016 record temperatures triggered a pan-tropical episode of "
    "coral bleaching -- the third global-scale event since mass "
    "bleaching was first documented in the 1980s. On the Great Barrier "
    "Reef specifically, the 2016 event was the most severe on record, "
    "affecting 91% of individual reefs. Local water-quality protection "
    "and fishing-pressure management had minimal effect on bleaching "
    "severity in 2016 -- local reef protection affords little "
    "resistance to extreme regional heat."
)

# =====================================================================
# Hughes et al. 2018: shrinking recovery windows between events
# =====================================================================

HUGHES_2018_CITATION = (
    "Hughes, T.P., Anderson, K.D., Connolly, S.R., et al. (2018). "
    "Spatial and temporal patterns of mass bleaching of corals in the "
    "Anthropocene. Science, 359(6371), 80-83. "
    "DOI: 10.1126/science.aan8048"
)
HUGHES_2018_DOI = "10.1126/science.aan8048"

HUGHES_2018_SITE_COUNT = 100
HUGHES_2018_STUDY_PERIOD_YEARS = (1980, 2016)
HUGHES_2018_MEDIAN_RETURN_INTERVAL_YEARS = 6.0
HUGHES_2018_NOTE = (
    "A real analysis of bleaching records at 100 globally distributed "
    "reef locations, 1980-2016: the median return time between severe "
    "bleaching events at a given reef has fallen to just 6 years, less "
    "than half the interval typical before the 1980s -- a window too "
    "narrow for many coral communities to fully recover before the "
    "next event."
)

# =====================================================================
# NOAA 2024: the fourth global bleaching event, confirmed
# =====================================================================

NOAA_4GBE_CITATION = (
    "NOAA (2024). NOAA Confirms 4th Global Coral Bleaching Event. "
    "https://www.noaa.gov/news-release/noaa-confirms-4th-global-coral-bleaching-event"
)
NOAA_4GBE_LIKELY_ENDED_CITATION = (
    "NOAA/NESDIS (2026). World's Fourth Mass Coral Bleaching Event Likely "
    "Ended in 2025. "
    "https://www.nesdis.noaa.gov/news/worlds-fourth-mass-coral-bleaching-event-likely-ended-2025"
)

GLOBAL_BLEACHING_EVENTS_REEF_AREA_AFFECTED_PCT: dict[str, float] = {
    "1998_1st_event": 21.0,
    "2010_2nd_event": 37.0,
    "2014_2017_3rd_event": 68.0,
    "2023_2025_4th_event": 84.4,
}
NOAA_4GBE_PERIOD = ("2023-01", "2025-09")
NOAA_4GBE_LIKELY_ENDED: bool = True  # per NOAA/NESDIS, likely concluded mid-2025
NOAA_4GBE_NOTE = (
    "NOAA and the International Coral Reef Initiative confirmed a "
    "fourth global coral bleaching event: bleaching-level heat stress "
    "affected 84.4% of the world's coral reef area between January "
    "2023 and September 2025 (updated from an earlier 83.7% figure "
    "covering through April 2025 -- the event continued and grew "
    "before NOAA/NESDIS assessed it as likely ended in 2025), across "
    "at least 83 countries and territories -- a real, escalating "
    "series across all four documented global events (21% -> 37% -> "
    "68% -> 84.4%), the largest on record, surpassing the third "
    "event's 68%. This is the observed area-affected trend (bleaching-"
    "level heat stress exposure), not a claim that bleaching equals "
    "uniform mortality -- see the genotype-resilience nuance module "
    "for why."
)

# =====================================================================
# Thermal-acidification interaction (real multi-stressor synergy)
# =====================================================================

THERMAL_ACIDIFICATION_CITATION = (
    "Guillermic, M., et al. (2021). Thermal stress reduces "
    "pocilloporid coral resilience to ocean acidification by "
    "impairing control over calcifying fluid chemistry. Science "
    "Advances, 7(2), eaba9958. DOI: 10.1126/sciadv.aba9958"
)
THERMAL_ACIDIFICATION_DOI = "10.1126/sciadv.aba9958"

THERMAL_ACIDIFICATION_OPTIMAL_TEMP_C = 28.0
THERMAL_ACIDIFICATION_STRESS_TEMP_C = 31.0
THERMAL_ACIDIFICATION_NOTE = (
    "Two reef-building coral species (Pocillopora damicornis, "
    "Stylophora pistillata) can compensate for ocean acidification at "
    "a normal temperature (28C) by actively elevating pH and aragonite "
    "saturation state in their calcifying fluid. At an elevated "
    "temperature (31C), neither species could maintain this "
    "compensation, and neither could sustain positive calcification "
    "under any pH treatment tested -- heat stress specifically breaks "
    "the mechanism corals use to cope with acidification, not just an "
    "additive second stressor."
)

# =====================================================================
# Walker et al. 2023: the deliberate honesty check -- bleaching
# resistance varies by genotype and carries real fitness tradeoffs
# =====================================================================

WALKER_2023_CITATION = (
    "Walker, N.S., Nestor, V., Golbuu, Y., Palumbi, S.R. (2023). "
    "Coral bleaching resistance variation is linked to differential "
    "mortality and skeletal growth during recovery. Evolutionary "
    "Applications, 16(3), 755-770. DOI: 10.1111/eva.13500"
)
WALKER_2023_DOI = "10.1111/eva.13500"

WALKER_2023_SPECIES = "Acropora hyacinthus"
WALKER_2023_LOCATION = "Palau"
WALKER_2023_NOTE = (
    "Real field and lab evidence from Acropora hyacinthus colonies in "
    "Palau: individual coral genotypes vary substantially in heat "
    "resistance, and higher heat resistance is linked to real fitness "
    "tradeoffs (reduced growth) during recovery -- resistant genotypes "
    "do not dominate populations precisely because resistance has a "
    "cost. Overall resilience is the product of BOTH resistance to "
    "heat AND capacity to recover afterward, not heat tolerance alone. "
    "Deliberate honesty check for this package: a given DHW threshold "
    "crossing does not mean uniform bleaching or uniform mortality "
    "across a reef -- real, measured, genotype-level variation exists, "
    "and that variation is exactly what real-world coral restoration "
    "and assisted-evolution programs try to leverage."
)

# =====================================================================
# GCRMN 2025: independent, larger-scale confirmation of the shrinking
# recovery window (added 2026-09-02)
# =====================================================================
# Johann flagged a Spektrum.de article on this report; verified directly
# against the GCRMN's own release page (gcrmn.net) before adding. This is
# a SEPARATE, much larger dataset (21.1 million observations, 87,299
# surveys, 36,886 sites, 124 countries/territories, 1980-2024) than
# Hughes et al. 2018's 100-site study above -- it measures a DIFFERENT
# metric (percent of hard CORAL COVER LOST per event) than
# GLOBAL_BLEACHING_EVENTS_REEF_AREA_AFFECTED_PCT above (percent of REEF
# AREA exposed to bleaching-level heat stress), so the two series are
# complementary, not duplicates, and should not be conflated. The two
# independent recovery-window estimates DO agree: Hughes 2018's 6-year
# median return interval (1980-2016 data) and GCRMN 2025's current
# 5-6 year window (1980-2024 data, cross-checked below).

GCRMN_2025_CITATION = (
    "GCRMN & ICRI (2026). Status of Coral Reefs of the World: 2025. "
    "Global Coral Reef Monitoring Network / International Coral Reef "
    "Initiative. DOI: 10.59387/LFPR6347"
)
GCRMN_2025_DOI = "10.59387/LFPR6347"
GCRMN_2025_RELEASE_DATE = "2026-08-31"

GCRMN_2025_BASELINE_COVER_PCT = 30.2   # global mean hard coral cover, 1980-2009 baseline
GCRMN_2025_CURRENT_COVER_PCT = 27.3    # global mean hard coral cover, as of 2024
GCRMN_2025_GLOBAL_COVER_DECLINE_PCT = 9.5  # relative decline: (30.2-27.3)/30.2 * 100

GCRMN_2025_EVENT_COVER_LOSS_PCT: dict[str, float] = {
    "1998_1999": 6.5,
    "2010_2011": 9.9,
    "2016_2017": 6.6,
    "2023_2024": 8.9,
}
GCRMN_2025_RECOVERY_2017_2019_PCT = 6.0  # real observed recovery: cover CAN rebound given time

GCRMN_2025_RECOVERY_WINDOW_HISTORICAL_YEARS = "decades"
GCRMN_2025_RECOVERY_WINDOW_CURRENT_YEARS: tuple[float, float] = (5.0, 6.0)

GCRMN_2025_GONZALEZ_RIVERO_QUOTE = (
    "Coral reefs once had decades to recover after major bleaching "
    "events. Today, they're lucky to get five or six years. "
    "-- Dr. Manuel Gonzalez Rivero (AIMS), lead author"
)
GCRMN_2025_NOTE = (
    "The 2017-2019 recovery (+6% cover) is real evidence that recovery "
    "IS mechanistically possible when reefs get enough time -- the "
    "threat is not that corals can't recover, but that the interval "
    "between severe events has compressed to roughly the same length "
    "as the recovery process itself. This does not change "
    "HUGHES_2018_MEDIAN_RETURN_INTERVAL_YEARS or "
    "GLOBAL_BLEACHING_EVENTS_REEF_AREA_AFFECTED_PCT above -- it is an "
    "independent, more recent, much larger-sample confirmation of the "
    "same shrinking-window mechanism, using a different underlying "
    "metric (cover loss, not heat-stress area exposure)."
)

# =====================================================================
# Live current-event context (added 2026-09-03, context only) -- WMO
# =====================================================================
# WMO press release (2026-09-03): a live, exceptionally strong El Nino
# event, Nino 3.4 index +2.2 to +2.6C above average, near-100%
# probability of persisting through February 2027, peak expected end
# of 2026. The 4th global bleaching event (NOAA_4GBE_PERIOD) already
# ended April 2025, and this package's own is_severity_monotonically_
# increasing() docstring is explicit that it makes no claim about a
# future, undocumented fifth event. This new, exceptionally strong El
# Nino is a real risk factor worth watching via NOAA Coral Reef Watch's
# real-time DHW monitoring (already documented above) -- it is NOT
# evidence of a confirmed fifth global bleaching event.
WMO_2026_CITATION = (
    "WMO (2026-09-03), \"El Nino set to become very strong, raising "
    "risks of extreme weather into 2027\", "
    "https://wmo.int/news/media-centre/el-nino-set-become-very-strong-"
    "raising-risks-of-extreme-weather-2027"
)
WMO_2026_NINO34_ANOMALY_C_RANGE = (2.2, 2.6)
WMO_2026_PEAK_EXPECTED = "end of 2026"
