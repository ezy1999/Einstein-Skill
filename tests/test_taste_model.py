"""Tests for the taste scoring model."""

import pytest
from einstein_taste.core.taste_model import AxisScore, TasteEvaluation, TasteScorer
from einstein_taste.core.evidence import EvidenceStore


@pytest.fixture
def scorer():
    return TasteScorer(EvidenceStore())


class TestTasteScorer:
    def test_get_active_period(self, scorer):
        period = scorer.get_active_period(1905)
        assert period is not None
        assert period.name == "early_revolutionary"

        period = scorer.get_active_period(1920)
        assert period is not None
        assert period.name == "quantum_debates"

    def test_aggregate_scores(self, scorer):
        axis_scores = [
            AxisScore(axis_name="simplicity", score=0.8, confidence=0.9, is_evidence_based=True),
            AxisScore(axis_name="unity", score=0.6, confidence=0.8, is_evidence_based=True),
        ]
        overall, conf = scorer.aggregate_scores(axis_scores, cutoff_year=1905)
        assert -1.0 <= overall <= 1.0
        assert 0.0 <= conf <= 1.0

    def test_aggregate_empty(self, scorer):
        overall, conf = scorer.aggregate_scores([], cutoff_year=1905)
        assert overall == 0.0
        assert conf == 0.0

    def test_rank_candidates(self, scorer):
        evals = [
            TasteEvaluation(
                candidate_description="Theory A", cutoff_year=1905,
                active_period="early_revolutionary", overall_score=0.5, overall_confidence=0.8,
            ),
            TasteEvaluation(
                candidate_description="Theory B", cutoff_year=1905,
                active_period="early_revolutionary", overall_score=0.8, overall_confidence=0.9,
            ),
        ]
        ranked = scorer.rank_candidates(evals)
        assert ranked[0].candidate_description == "Theory B"

    def test_period_weights(self, scorer):
        period = scorer.get_active_period(1905)
        weights = scorer.get_period_weights(period)
        # Early period dominant axes should get boosted
        assert weights["empirical_grounding"] > weights["mathematical_beauty"]
