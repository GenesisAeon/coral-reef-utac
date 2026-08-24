"""Heat stress breaks corals' ocean-acidification coping mechanism (Guillermic et al. 2021).

Core module -- documents a real multi-stressor synergy: heat and
acidification are not simply additive, heat specifically disables the
mechanism corals use to cope with acidification alone.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    THERMAL_ACIDIFICATION_CITATION,
    THERMAL_ACIDIFICATION_NOTE,
    THERMAL_ACIDIFICATION_OPTIMAL_TEMP_C,
    THERMAL_ACIDIFICATION_STRESS_TEMP_C,
)


@dataclass(frozen=True)
class ThermalAcidificationInteraction:
    """Guillermic et al. (2021)'s real lab-measured temperature/acidification interaction."""

    optimal_temp_c: float
    stress_temp_c: float
    citation: str


HEAT_BREAKS_ACIDIFICATION_COPING = ThermalAcidificationInteraction(
    optimal_temp_c=THERMAL_ACIDIFICATION_OPTIMAL_TEMP_C,
    stress_temp_c=THERMAL_ACIDIFICATION_STRESS_TEMP_C,
    citation=THERMAL_ACIDIFICATION_CITATION,
)


def can_corals_compensate_for_acidification_at_optimal_temperature() -> bool:
    """Whether corals can actively cope with ocean acidification under normal temperatures.

    True -- at 28C, the tested species elevate calcifying-fluid pH and
    aragonite saturation state to sustain positive calcification
    despite lower-pH water.
    """
    return True


def can_corals_compensate_for_acidification_under_heat_stress() -> bool:
    """Whether that same compensation mechanism still works once heat stress is added.

    Always False per Guillermic et al. (2021): at 31C, neither tested
    species could maintain the compensation, and neither sustained
    positive calcification under any pH treatment. Heat stress does
    not just add to acidification stress -- it disables the coping
    mechanism corals would otherwise use against acidification alone.
    """
    return False


CITATION = THERMAL_ACIDIFICATION_CITATION
NOTE = THERMAL_ACIDIFICATION_NOTE
