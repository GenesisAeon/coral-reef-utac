"""Honesty check: bleaching resistance varies by genotype, has fitness costs (Walker et al. 2023).

Core module -- exists specifically to prevent this package from
becoming a one-sided "a DHW threshold crossing means uniform bleaching
and uniform mortality" narrative. See WALKER_2023_NOTE.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    WALKER_2023_CITATION,
    WALKER_2023_LOCATION,
    WALKER_2023_NOTE,
    WALKER_2023_SPECIES,
)


@dataclass(frozen=True)
class GenotypeResilienceEvidence:
    """Walker et al. (2023)'s real field/lab evidence of genotype-level resistance variation."""

    species: str
    location: str
    citation: str


PALAU_ACROPORA_EVIDENCE = GenotypeResilienceEvidence(
    species=WALKER_2023_SPECIES,
    location=WALKER_2023_LOCATION,
    citation=WALKER_2023_CITATION,
)


def is_bleaching_response_uniform_across_genotypes() -> bool:
    """Whether all coral genotypes within a species bleach/survive identically.

    Always False. Walker et al. (2023) found real, measured
    genotype-level variation in heat resistance within a single
    species at a single site.
    """
    return False


def does_heat_resistance_come_without_a_cost() -> bool:
    """Whether high heat resistance is a free trait with no downside.

    Always False. Higher heat resistance is linked to real fitness
    tradeoffs (reduced growth during recovery) -- which is exactly why
    resistant genotypes do not simply dominate coral populations over
    time.
    """
    return False


def resilience_depends_on_resistance_alone() -> bool:
    """Whether heat tolerance alone determines overall coral resilience.

    Always False per Walker et al. (2023): overall resilience is the
    product of BOTH resistance to heat stress AND capacity to recover
    afterward -- a genotype that resists bleaching but recovers poorly
    is not simply "more resilient" than one that bleaches but rebounds
    strongly.
    """
    return False


CITATION = WALKER_2023_CITATION
NOTE = WALKER_2023_NOTE
