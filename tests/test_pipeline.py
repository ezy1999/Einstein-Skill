"""Tests for the pipeline (offline, no LLM calls)."""

import pytest
from einstein_taste.core.pipeline import TastePipeline
from einstein_taste.core.evidence import EvidenceStore
from einstein_taste.data.seed_evidence import get_seed_evidence


@pytest.fixture
def pipeline():
    """Create a pipeline with seed data (no LLM needed for these tests)."""
    store = EvidenceStore()
    store.add_batch(get_seed_evidence())
    return TastePipeline(store)


class TestPipeline:
    def test_pipeline_creation(self, pipeline):
        assert pipeline.evidence_store.count() > 0
        assert pipeline.retriever is not None
        assert pipeline.scorer is not None

    def test_evidence_retrieval(self, pipeline):
        results = pipeline.retriever.retrieve(
            query="unifying gravity electromagnetism unified field theory unity",
            top_k=10,
            cutoff_year=1955,
        )
        assert len(results) > 0
        # Should find unity-related evidence with expanded query
        axes = set()
        for record, score in results:
            axes.update(record.relevant_axes)
        assert "unity" in axes

    def test_retrieval_temporal_cutoff(self, pipeline):
        # Records from before 1905 only
        results = pipeline.retriever.retrieve(
            query="simplicity in physics",
            top_k=20,
            cutoff_year=1903,
        )
        for record, _ in results:
            if record.year is not None:
                assert record.year <= 1903

    def test_format_evaluation(self):
        from einstein_taste.core.taste_model import TasteEvaluation, AxisScore
        ev = TasteEvaluation(
            candidate_description="Test theory",
            cutoff_year=1905,
            active_period="early_revolutionary",
            axis_scores=[
                AxisScore(axis_name="simplicity", score=0.8, confidence=0.9,
                          explanation="Well-supported", is_evidence_based=True),
            ],
            overall_score=0.8,
            overall_confidence=0.9,
            summary="A promising theory",
        )
        text = TastePipeline.format_evaluation(ev)
        assert "Test theory" in text
        assert "simplicity" in text
        assert "EVIDENCE" in text
