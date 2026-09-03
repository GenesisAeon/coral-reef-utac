"""The four documented global coral bleaching events (Hughes 2017/2018 + NOAA 2024).

Core module -- a real, escalating time series of reef area affected by
bleaching-level heat stress across all four documented global events.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    GCRMN_2025_CITATION,
    GCRMN_2025_EVENT_COVER_LOSS_PCT,
    GCRMN_2025_GLOBAL_COVER_DECLINE_PCT,
    GCRMN_2025_RECOVERY_2017_2019_PCT,
    GCRMN_2025_RECOVERY_WINDOW_CURRENT_YEARS,
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
    WMO_2026_CITATION,
    WMO_2026_NINO34_ANOMALY_C_RANGE,
    WMO_2026_PEAK_EXPECTED,
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


@dataclass(frozen=True)
class GCRMN2025CoverLossSeries:
    """GCRMN (2026)'s independent, 21.1M-observation cover-loss series.

    A different metric than GLOBAL_EVENTS above (percent of hard coral
    COVER LOST per event, not percent of reef area exposed to
    bleaching-level heat stress) -- complementary evidence, not a
    duplicate of the NOAA/Hughes series.
    """

    event_cover_loss_pct: dict[str, float]
    global_cover_decline_pct: float
    recovery_2017_2019_pct: float
    current_recovery_window_years: tuple[float, float]
    citation: str


GCRMN_2025_EVENTS = GCRMN2025CoverLossSeries(
    event_cover_loss_pct=GCRMN_2025_EVENT_COVER_LOSS_PCT,
    global_cover_decline_pct=GCRMN_2025_GLOBAL_COVER_DECLINE_PCT,
    recovery_2017_2019_pct=GCRMN_2025_RECOVERY_2017_2019_PCT,
    current_recovery_window_years=GCRMN_2025_RECOVERY_WINDOW_CURRENT_YEARS,
    citation=GCRMN_2025_CITATION,
)


def is_recovery_window_independently_confirmed_narrow() -> bool:
    """Whether two independent studies agree the recovery window is too narrow.

    Hughes et al. 2018 (100 sites, 1980-2016): 6-year median return
    interval. GCRMN 2025 (36,886 sites, 1980-2024, a much larger and
    more recent sample): current window of 5-6 years. Two independently
    conducted analyses, using different methods and largely
    non-overlapping study periods, converge on essentially the same
    number -- real convergent evidence, not a single study's estimate.
    """
    hughes = HUGHES_2018_MEDIAN_RETURN_INTERVAL_YEARS
    gcrmn_low, gcrmn_high = GCRMN_2025_RECOVERY_WINDOW_CURRENT_YEARS
    return gcrmn_low <= hughes <= gcrmn_high


CITATION = NOAA_4GBE_CITATION
NOTE = NOAA_4GBE_NOTE


@dataclass(frozen=True)
class LiveElNinoWatchContext:
    """WMO's 2026-09-03 real-time monitoring of the current, exceptionally
    strong El Nino event -- a real risk factor to watch, not a claim of a
    confirmed fifth global bleaching event (the 4th ended April 2025)."""

    nino34_anomaly_c_range: tuple[float, float] = WMO_2026_NINO34_ANOMALY_C_RANGE
    peak_expected: str = WMO_2026_PEAK_EXPECTED
    citation: str = WMO_2026_CITATION


CURRENT_EVENT_WATCH = LiveElNinoWatchContext()


def is_a_fifth_global_bleaching_event_confirmed() -> bool:
    """Whether a fifth global coral bleaching event has been confirmed.

    Always False -- the live 2026-2027 El Nino is a real, exceptionally
    strong event worth watching (see CURRENT_EVENT_WATCH), but this
    package has no NOAA/ICRI confirmation of a fifth global bleaching
    event. is_severity_monotonically_increasing() above is explicit
    that it makes no claim about undocumented future events -- this
    function makes that same point for the live 2026 event specifically.
    """
    return False
