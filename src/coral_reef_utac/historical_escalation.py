"""The four documented global coral bleaching events (Hughes 2017/2018 + NOAA 2024).

Core module -- a real, escalating time series of reef area affected by
bleaching-level heat stress across all four documented global events.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    GLOBAL_BLEACHING_EVENTS_REEF_AREA_AFFECTED_PCT,
    HUGHES_2017_CITATION,
    HUGHES_2017_GBR_2016_REEFS_AFFECTED_PCT,
    HUGHES_2018_CITATION,
    HUGHES_2018_MEDIAN_RETURN_INTERVAL_YEARS,
    HUGHES_2018_SITE_COUNT,
    HUGHES_2018_STUDY_PERIOD_YEARS,
    NOAA_4GBE_CITATION,
    NOAA_4GBE_NOTE,
    NOAA_4GBE_PERIOD,
)


@dataclass(frozen=True)
class GlobalBleachingEventSeries:
    """The real, sourced series of global bleaching event severity."""

    reef_area_affected_pct_by_event: dict[str, float]
    fourth_event_period: tuple[str, str]
    citation: str


GLOBAL_EVENTS = GlobalBleachingEventSeries(
    reef_area_affected_pct_by_event=GLOBAL_BLEACHING_EVENTS_REEF_AREA_AFFECTED_PCT,
    fourth_event_period=NOAA_4GBE_PERIOD,
    citation=NOAA_4GBE_CITATION,
)


@dataclass(frozen=True)
class ThirdEventGBRDetail:
    """Hughes et al. (2017)'s Great Barrier Reef detail for the third global event (2016)."""

    reefs_affected_pct: float
    citation: str


GBR_2016_DETAIL = ThirdEventGBRDetail(
    reefs_affected_pct=HUGHES_2017_GBR_2016_REEFS_AFFECTED_PCT,
    citation=HUGHES_2017_CITATION,
)


@dataclass(frozen=True)
class ReturnIntervalStudy:
    """Hughes et al. (2018)'s 100-site global return-interval analysis."""

    site_count: int
    study_period_years: tuple[int, int]
    median_return_interval_years: float
    citation: str


RETURN_INTERVAL_STUDY = ReturnIntervalStudy(
    site_count=HUGHES_2018_SITE_COUNT,
    study_period_years=HUGHES_2018_STUDY_PERIOD_YEARS,
    median_return_interval_years=HUGHES_2018_MEDIAN_RETURN_INTERVAL_YEARS,
    citation=HUGHES_2018_CITATION,
)


def is_severity_monotonically_increasing() -> bool:
    """Whether each documented global event affected more reef area than the last.

    True for the real, observed 1998 -> 2010 -> 2014-2017 -> 2023-2025
    series (21% -> 37% -> 68% -> 83.7%). This module makes no claim
    about what happens in a future, undocumented fifth event.
    """
    values = list(GLOBAL_EVENTS.reef_area_affected_pct_by_event.values())
    return all(later > earlier for earlier, later in zip(values, values[1:], strict=False))


def recovery_window_years() -> float:
    """The real, measured median return time between severe bleaching events.

    6 years (Hughes et al. 2018), down from a pre-1980s interval more
    than double that -- the shrinking recovery window, not the
    bleaching event itself, is what threatens long-term reef survival.
    """
    return HUGHES_2018_MEDIAN_RETURN_INTERVAL_YEARS


def is_recovery_window_sufficient_for_full_recovery() -> bool:
    """Whether the real, measured recovery window allows full coral recovery.

    Always False per Hughes et al. 2018's own conclusion: a 6-year
    median return interval is too narrow for many coral communities to
    fully recover before the next bleaching event.
    """
    return False


CITATION = NOAA_4GBE_CITATION
NOTE = NOAA_4GBE_NOTE
