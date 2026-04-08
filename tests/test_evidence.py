"""Tests for the evidence management module."""

import pytest
from einstein_taste.core.evidence import (
    EvidenceRecord,
    EvidenceStore,
    SourceType,
    ConfidenceLevel,
)


@pytest.fixture
def sample_records():
    """Create sample evidence records for testing."""
    return [
        EvidenceRecord(
            id="test_001",
            content="Einstein preferred simple theories",
            source_text="Pais, 'Subtle is the Lord' (1982)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1905,
            period="early_revolutionary",
            relevant_axes=["simplicity"],
            axis_valence={"simplicity": 1.0},
        ),
        EvidenceRecord(
            id="test_002",
            content="Einstein sought to unify gravity and electromagnetism",
            source_text="Van Dongen, 'Einstein's Unification' (2010)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1930,
            period="quantum_debates",
            relevant_axes=["unity"],
            axis_valence={"unity": 1.0},
        ),
        EvidenceRecord(
            id="test_003",
            content="Einstein wrote: God does not play dice",
            source_text="Einstein-Born Letters (1926)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1926,
            relevant_axes=["physical_reality"],
            axis_valence={"physical_reality": 1.0},
            is_quote=True,
        ),
    ]


@pytest.fixture
def evidence_store(sample_records):
    store = EvidenceStore()
    store.add_batch(sample_records)
    return store


class TestEvidenceRecord:
    def test_applies_at_year(self, sample_records):
        r = sample_records[0]  # year=1905
        assert r.applies_at_year(1905)
        assert r.applies_at_year(2000)
        assert not r.applies_at_year(1904)

    def test_applies_at_year_undated(self):
        r = EvidenceRecord(
            id="undated", content="test", source_text="test",
            source_type=SourceType.SECONDARY, confidence=ConfidenceLevel.MODERATE,
        )
        assert r.applies_at_year(1900)

    def test_is_primary(self, sample_records):
        assert not sample_records[0].is_primary()
        assert sample_records[2].is_primary()


class TestEvidenceStore:
    def test_count(self, evidence_store):
        assert evidence_store.count() == 3

    def test_filter_by_year(self, evidence_store):
        results = evidence_store.filter(cutoff_year=1910)
        assert len(results) == 1
        assert results[0].id == "test_001"

    def test_filter_by_source_type(self, evidence_store):
        results = evidence_store.filter(source_types=[SourceType.PRIMARY])
        assert len(results) == 1
        assert results[0].id == "test_003"

    def test_filter_by_axes(self, evidence_store):
        results = evidence_store.filter(axes=["unity"])
        assert len(results) == 1

    def test_filter_combined(self, evidence_store):
        results = evidence_store.filter(
            cutoff_year=1930,
            source_types=[SourceType.SECONDARY],
        )
        assert len(results) == 2

    def test_summary(self, evidence_store):
        summary = evidence_store.summary()
        assert summary["total_records"] == 3
        assert summary["by_source_type"]["primary"] == 1
        assert summary["by_source_type"]["secondary"] == 2
