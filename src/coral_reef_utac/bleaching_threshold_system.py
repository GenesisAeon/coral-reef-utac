"""NOAA Coral Reef Watch's real, operational Degree Heating Week (DHW) system.

Core module -- documents the actual, official heat-stress threshold
system used to issue coral bleaching alerts worldwide, not an invented
UTAC/CREP mapping onto it.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DHW_ACCUMULATION_WINDOW_WEEKS,
    DHW_ALERT_LEVEL_CONSEQUENCE,
    DHW_ALERT_LEVEL_THRESHOLDS_C_WEEKS,
    DHW_ALERT_LEVELS_3_TO_5_ADDED_NOTE,
    DHW_ALERT_LEVELS_3_TO_5_ADDED_YEAR,
    DHW_SCALE_MAX_C_WEEKS,
    DHW_SCALE_MIN_C_WEEKS,
    NOAA_CRW_DHW_CITATION,
)


@dataclass(frozen=True)
class DegreeHeatingWeekSystem:
    """NOAA Coral Reef Watch's real operational heat-stress metric."""

    scale_min_c_weeks: float
    scale_max_c_weeks: float
    accumulation_window_weeks: int
    citation: str


DHW_SYSTEM = DegreeHeatingWeekSystem(
    scale_min_c_weeks=DHW_SCALE_MIN_C_WEEKS,
    scale_max_c_weeks=DHW_SCALE_MAX_C_WEEKS,
    accumulation_window_weeks=DHW_ACCUMULATION_WINDOW_WEEKS,
    citation=NOAA_CRW_DHW_CITATION,
)


def alert_level_for_dhw(dhw_c_weeks: float) -> int:
    """Return NOAA's official alert level (0-5) for a given accumulated DHW value.

    Level 0 means below the level-1 (bleaching-risk) threshold.
    """
    if dhw_c_weeks < 0.0:
        raise ValueError("DHW cannot be negative")
    level = 0
    for lvl, threshold in sorted(DHW_ALERT_LEVEL_THRESHOLDS_C_WEEKS.items()):
        if dhw_c_weeks >= threshold:
            level = lvl
    return level


def consequence_for_alert_level(level: int) -> str:
    """Return NOAA's documented real-world consequence text for an alert level."""
    if level == 0:
        return "No significant bleaching-level heat stress"
    return DHW_ALERT_LEVEL_CONSEQUENCE[level]


def is_alert_scale_unchanged_since_the_1990s() -> bool:
    """Whether NOAA's alert scale has stayed fixed since its original design.

    Always False. The scale was expanded from 2 to 5 levels in
    December 2023 because observed heat stress in 2023 exceeded what
    the original scale was designed to describe -- the system itself
    had to be revised in response to real, worsening conditions.
    """
    return DHW_ALERT_LEVELS_3_TO_5_ADDED_YEAR <= 1999


CITATION = NOAA_CRW_DHW_CITATION
NOTE = DHW_ALERT_LEVELS_3_TO_5_ADDED_NOTE
