"""Tests for coral-reef-utac."""

from coral_reef_utac import (
    DHW_SYSTEM,
    GBR_2016_DETAIL,
    GLOBAL_EVENTS,
    HEAT_BREAKS_ACIDIFICATION_COPING,
    PACKAGE_ID,
    PALAU_ACROPORA_EVIDENCE,
    RETURN_INTERVAL_STUDY,
    __version__,
    alert_level_for_dhw,
    can_corals_compensate_for_acidification_at_optimal_temperature,
    can_corals_compensate_for_acidification_under_heat_stress,
    consequence_for_alert_level,
    does_heat_resistance_come_without_a_cost,
    is_alert_scale_unchanged_since_the_1990s,
    is_bleaching_response_uniform_across_genotypes,
    is_recovery_window_sufficient_for_full_recovery,
    is_severity_monotonically_increasing,
    recovery_window_years,
    resilience_depends_on_resistance_alone,
)


def test_version():
    assert __version__ == "1.0.0"


def test_package_id():
    assert PACKAGE_ID == 114


# --- bleaching_threshold_system.py (core) -----------------------------------


def test_dhw_system_values():
    assert DHW_SYSTEM.scale_min_c_weeks == 0.0
    assert DHW_SYSTEM.scale_max_c_weeks == 20.0
    assert DHW_SYSTEM.accumulation_window_weeks == 12
    assert DHW_SYSTEM.citation


def test_alert_level_for_dhw_boundaries():
    assert alert_level_for_dhw(0.0) == 0
    assert alert_level_for_dhw(3.9) == 0
    assert alert_level_for_dhw(4.0) == 1
    assert alert_level_for_dhw(7.9) == 1
    assert alert_level_for_dhw(8.0) == 2
    assert alert_level_for_dhw(12.0) == 3
    assert alert_level_for_dhw(16.0) == 4
    assert alert_level_for_dhw(20.0) == 5
    assert alert_level_for_dhw(25.0) == 5  # off the scale top, still max level


def test_alert_level_for_dhw_rejects_negative():
    try:
        alert_level_for_dhw(-1.0)
        raise AssertionError("expected ValueError")
    except ValueError:
        pass


def test_consequence_for_alert_level():
    assert consequence_for_alert_level(0) == "No significant bleaching-level heat stress"
    assert "mortality" in consequence_for_alert_level(5).lower()


def test_is_alert_scale_unchanged_since_the_1990s_always_false():
    # The key honesty check: the alert scale itself had to be expanded
    # in Dec 2023 because real conditions exceeded its original design.
    assert is_alert_scale_unchanged_since_the_1990s() is False


# --- historical_escalation.py (core) -----------------------------------------


def test_global_events_series_values():
    values = list(GLOBAL_EVENTS.reef_area_affected_pct_by_event.values())
    assert values == [21.0, 37.0, 68.0, 83.7]
    assert GLOBAL_EVENTS.fourth_event_period == ("2023-01", "2025-04")
    assert GLOBAL_EVENTS.citation


def test_is_severity_monotonically_increasing_true():
    assert is_severity_monotonically_increasing() is True


def test_gbr_2016_detail_values():
    assert GBR_2016_DETAIL.reefs_affected_pct == 91.0
    assert GBR_2016_DETAIL.citation


def test_return_interval_study_values():
    assert RETURN_INTERVAL_STUDY.site_count == 100
    assert RETURN_INTERVAL_STUDY.study_period_years == (1980, 2016)
    assert RETURN_INTERVAL_STUDY.median_return_interval_years == 6.0
    assert RETURN_INTERVAL_STUDY.citation


def test_recovery_window_years():
    assert recovery_window_years() == 6.0


def test_is_recovery_window_sufficient_for_full_recovery_always_false():
    assert is_recovery_window_sufficient_for_full_recovery() is False


# --- combined_stressor_interaction.py (core) ---------------------------------


def test_heat_breaks_acidification_coping_values():
    assert HEAT_BREAKS_ACIDIFICATION_COPING.optimal_temp_c == 28.0
    assert HEAT_BREAKS_ACIDIFICATION_COPING.stress_temp_c == 31.0
    assert HEAT_BREAKS_ACIDIFICATION_COPING.citation


def test_can_compensate_at_optimal_temperature_true():
    assert can_corals_compensate_for_acidification_at_optimal_temperature() is True


def test_can_compensate_under_heat_stress_always_false():
    assert can_corals_compensate_for_acidification_under_heat_stress() is False


# --- genotype_resilience_nuance.py (core, honesty-check module) -------------


def test_palau_acropora_evidence_values():
    assert PALAU_ACROPORA_EVIDENCE.species == "Acropora hyacinthus"
    assert PALAU_ACROPORA_EVIDENCE.location == "Palau"
    assert PALAU_ACROPORA_EVIDENCE.citation


def test_is_bleaching_response_uniform_across_genotypes_always_false():
    assert is_bleaching_response_uniform_across_genotypes() is False


def test_does_heat_resistance_come_without_a_cost_always_false():
    assert does_heat_resistance_come_without_a_cost() is False


def test_resilience_depends_on_resistance_alone_always_false():
    assert resilience_depends_on_resistance_alone() is False


def test_nuance_does_not_contradict_the_core_findings():
    # All can be true at once: NOAA's DHW system is a real, official,
    # worsening threshold system, and bleaching events really are
    # getting more frequent and severe -- AND individual coral
    # genotypes vary in resistance and recovery, so a threshold
    # crossing does not mean uniform mortality. Resilience is a
    # matter of degree and of who, not a single number.
    assert is_severity_monotonically_increasing() is True
    assert is_recovery_window_sufficient_for_full_recovery() is False
    assert is_bleaching_response_uniform_across_genotypes() is False
    assert can_corals_compensate_for_acidification_under_heat_stress() is False
