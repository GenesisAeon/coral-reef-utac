"""coral-reef-utac -- NOAA's real coral-bleaching threshold system, honestly presented.

GenesisAeon Package 114. Chosen from a shortlist of 5 candidate gap-topics
proposed via an external AI dialogue about GenesisAeon's environment/
climate/species-protection coverage (`UTACnextSteps.txt`); the other
session's specific numeric claims (invented Gamma_tipping values, a
"Pressure-inverted UTAC" formula falsely presented as extracted from the
codebase, a wrong "strict GPL-3.0 template" claim, a git branch presented
as if already created) did not survive independent verification -- see
DISCLAIMER.md. Built from scratch with independently verified citations.

Documents NOAA Coral Reef Watch's real, official Degree Heating Week
(DHW) heat-stress threshold system (0-20C-weeks, 5 alert levels),
the real, escalating series of four documented global bleaching events
(Hughes et al. 2017/2018, NOAA 2024: 21% -> 37% -> 68% -> 83.7% of reef
area affected), and a real multi-stressor synergy (heat disables corals'
acidification-coping mechanism, Guillermic et al. 2021). Deliberately no
UTAC/CREP/AFET bridge and no invented Gamma value -- see DISCLAIMER.md.

Deliberately NOT one-sided: includes a real complication (Walker et al.
2023) showing that bleaching resistance varies substantially by genotype
and carries real fitness tradeoffs -- a DHW threshold crossing does not
mean uniform bleaching or uniform mortality across a reef.

All citations independently verified 2026-08-24.
"""

from .bleaching_threshold_system import (
    DHW_SYSTEM,
    DegreeHeatingWeekSystem,
    alert_level_for_dhw,
    consequence_for_alert_level,
    is_alert_scale_unchanged_since_the_1990s,
)
from .combined_stressor_interaction import (
    HEAT_BREAKS_ACIDIFICATION_COPING,
    ThermalAcidificationInteraction,
    can_corals_compensate_for_acidification_at_optimal_temperature,
    can_corals_compensate_for_acidification_under_heat_stress,
)
from .constants import (
    HUGHES_2017_CITATION,
    HUGHES_2018_CITATION,
    NOAA_4GBE_CITATION,
    NOAA_CRW_DHW_CITATION,
    PACKAGE_ID,
    THERMAL_ACIDIFICATION_CITATION,
    WALKER_2023_CITATION,
)
from .genotype_resilience_nuance import (
    PALAU_ACROPORA_EVIDENCE,
    GenotypeResilienceEvidence,
    does_heat_resistance_come_without_a_cost,
    is_bleaching_response_uniform_across_genotypes,
    resilience_depends_on_resistance_alone,
)
from .historical_escalation import (
    GBR_2016_DETAIL,
    GLOBAL_EVENTS,
    RETURN_INTERVAL_STUDY,
    GlobalBleachingEventSeries,
    ReturnIntervalStudy,
    ThirdEventGBRDetail,
    is_recovery_window_sufficient_for_full_recovery,
    is_severity_monotonically_increasing,
    recovery_window_years,
)

__version__ = "1.0.0"

__all__ = [
    "DHW_SYSTEM",
    "GBR_2016_DETAIL",
    "GLOBAL_EVENTS",
    "HEAT_BREAKS_ACIDIFICATION_COPING",
    "HUGHES_2017_CITATION",
    "HUGHES_2018_CITATION",
    "NOAA_4GBE_CITATION",
    "NOAA_CRW_DHW_CITATION",
    "PACKAGE_ID",
    "PALAU_ACROPORA_EVIDENCE",
    "RETURN_INTERVAL_STUDY",
    "THERMAL_ACIDIFICATION_CITATION",
    "WALKER_2023_CITATION",
    "DegreeHeatingWeekSystem",
    "GenotypeResilienceEvidence",
    "GlobalBleachingEventSeries",
    "ReturnIntervalStudy",
    "ThermalAcidificationInteraction",
    "ThirdEventGBRDetail",
    "alert_level_for_dhw",
    "can_corals_compensate_for_acidification_at_optimal_temperature",
    "can_corals_compensate_for_acidification_under_heat_stress",
    "consequence_for_alert_level",
    "does_heat_resistance_come_without_a_cost",
    "is_alert_scale_unchanged_since_the_1990s",
    "is_bleaching_response_uniform_across_genotypes",
    "is_recovery_window_sufficient_for_full_recovery",
    "is_severity_monotonically_increasing",
    "recovery_window_years",
    "resilience_depends_on_resistance_alone",
]
