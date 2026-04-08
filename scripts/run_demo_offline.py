"""
Offline demo showing the Einstein Research Taste system without requiring
an LLM API key. Uses a mock evaluator that demonstrates the full pipeline
flow with pre-computed responses.
"""

import json
from einstein_taste.core.pipeline import TastePipeline
from einstein_taste.core.evidence import EvidenceStore
from einstein_taste.core.taste_model import AxisScore, TasteEvaluation, TasteScorer
from einstein_taste.core.retriever import EvidenceRetriever
from einstein_taste.data.loader import load_evidence_store
from einstein_taste.config.settings import PROCESSED_DATA_DIR, EINSTEIN_TASTE_AXES
from einstein_taste.utils.formatting import format_ranking


class MockEvaluator:
    """Mock evaluator that scores candidates based on keyword matching with taste axes."""

    def evaluate(self, candidate, evidence, cutoff_year=1955, scorer=None):
        candidate_lower = candidate.lower()

        axis_scores = []
        for axis in EINSTEIN_TASTE_AXES:
            # Score based on keyword overlap
            keyword_hits = sum(1 for kw in axis.keywords if kw.lower() in candidate_lower)
            # Also check evidence alignment
            evidence_hits = sum(
                1 for record, rel in evidence
                if axis.name in record.relevant_axes and rel > 0
            )

            if keyword_hits > 0 or evidence_hits > 0:
                score = min(1.0, (keyword_hits * 0.3 + evidence_hits * 0.2))
            else:
                score = -0.1  # Slightly negative for unrelated

            # Check for negative signals
            negative_keywords = {
                "physical_reality": ["probabilistic", "indeterminate", "observer-dependent"],
                "causal_continuity": ["action at a distance", "nonlocal", "instantaneous"],
                "simplicity": ["complex", "many parameters", "ad hoc"],
            }
            for neg_kw in negative_keywords.get(axis.name, []):
                if neg_kw in candidate_lower:
                    score = max(-1.0, score - 0.5)

            # Positive boosts
            positive_keywords = {
                "unity": ["unif", "single framework", "combines"],
                "invariance": ["covariance", "coordinate-independent", "invariant", "symmetr"],
                "simplicity": ["simple", "minimal", "elegant", "few assumptions"],
                "physical_reality": ["deterministic", "objective", "hidden variable", "real"],
                "mathematical_beauty": ["beautiful", "elegant", "geometric", "mathematical"],
                "empirical_grounding": ["testable", "predict", "observ", "experiment"],
            }
            for pos_kw in positive_keywords.get(axis.name, []):
                if pos_kw in candidate_lower:
                    score = min(1.0, score + 0.3)

            confidence = min(1.0, 0.3 + keyword_hits * 0.2 + evidence_hits * 0.1)
            is_evidence_based = evidence_hits > 0

            axis_scores.append(AxisScore(
                axis_name=axis.name,
                score=max(-1.0, min(1.0, score)),
                confidence=confidence,
                evidence_ids=[r.id for r, _ in evidence[:2] if axis.name in r.relevant_axes],
                explanation=f"{'Evidence-based' if is_evidence_based else 'Inferred'}: "
                           f"{keyword_hits} keyword matches, {evidence_hits} evidence records.",
                is_evidence_based=is_evidence_based,
            ))

        # Aggregate
        if scorer:
            overall_score, overall_confidence = scorer.aggregate_scores(axis_scores, cutoff_year)
        else:
            overall_score = sum(s.score for s in axis_scores) / len(axis_scores)
            overall_confidence = sum(s.confidence for s in axis_scores) / len(axis_scores)

        # Determine period
        period = "unknown"
        from einstein_taste.config.settings import EINSTEIN_PERIODS
        for p in EINSTEIN_PERIODS:
            if p.start_year <= cutoff_year <= p.end_year:
                period = p.name
                break

        return TasteEvaluation(
            candidate_description=candidate,
            cutoff_year=cutoff_year,
            active_period=period,
            axis_scores=axis_scores,
            overall_score=overall_score,
            overall_confidence=overall_confidence,
            summary=f"Evaluation of candidate at year {cutoff_year} using mock scoring.",
            evidence_summary=f"Based on {sum(1 for s in axis_scores if s.is_evidence_based)} "
                           f"evidence-grounded axis scores.",
            inference_summary=f"{sum(1 for s in axis_scores if not s.is_evidence_based)} "
                            f"axis scores are model inferences.",
            caveats=["This is a mock evaluation for demonstration purposes.",
                     "For production use, set ANTHROPIC_API_KEY for LLM-based evaluation."],
        )


def main():
    print("=" * 70)
    print("EINSTEIN RESEARCH TASTE - OFFLINE DEMO")
    print("(Using mock evaluator - set ANTHROPIC_API_KEY for LLM evaluation)")
    print("=" * 70)

    # Load evidence
    store = load_evidence_store(PROCESSED_DATA_DIR)
    retriever = EvidenceRetriever(store)
    scorer = TasteScorer(store)
    mock_eval = MockEvaluator()

    print(f"\nEvidence store: {store.count()} records loaded")

    # ── Demo 1: Unified field theory (Einstein should love this) ──────────
    print("\n" + "=" * 70)
    print("DEMO 1: Theory Einstein would likely appreciate")
    print("=" * 70)

    candidate1 = (
        "A unified geometric framework combining gravity and electromagnetism "
        "through general covariance, with elegant mathematical structure and "
        "testable predictions about light bending near massive objects."
    )
    evidence1 = retriever.retrieve(candidate1, top_k=10, cutoff_year=1930)
    result1 = mock_eval.evaluate(candidate1, evidence1, cutoff_year=1930, scorer=scorer)
    print(TastePipeline.format_evaluation(result1))

    # ── Demo 2: Copenhagen QM (Einstein should dislike this) ──────────────
    print("\n" + "=" * 70)
    print("DEMO 2: Theory Einstein would likely reject")
    print("=" * 70)

    candidate2 = (
        "A probabilistic theory where physical properties are fundamentally "
        "indeterminate until measured, with observer-dependent reality and "
        "nonlocal instantaneous action at a distance between entangled particles."
    )
    evidence2 = retriever.retrieve(candidate2, top_k=10, cutoff_year=1935)
    result2 = mock_eval.evaluate(candidate2, evidence2, cutoff_year=1935, scorer=scorer)
    print(TastePipeline.format_evaluation(result2))

    # ── Demo 3: Ranking ───────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("DEMO 3: Ranking competing approaches")
    print("=" * 70)

    candidates = [
        "A deterministic hidden variable theory with objective physical reality",
        "A unified geometric theory with mathematical beauty and general covariance",
        "A probabilistic theory with observer-dependent measurement and nonlocal correlations",
    ]

    evaluations = []
    for c in candidates:
        ev = retriever.retrieve(c, top_k=10, cutoff_year=1945)
        result = mock_eval.evaluate(c, ev, cutoff_year=1945, scorer=scorer)
        evaluations.append(result)

    ranked = sorted(evaluations, key=lambda e: e.overall_score, reverse=True)
    print(format_ranking(ranked))

    # ── Demo 4: Temporal sensitivity ──────────────────────────────────────
    print("\n" + "=" * 70)
    print("DEMO 4: Temporal sensitivity test")
    print("=" * 70)

    theory = "An approach guided primarily by mathematical elegance and beautiful geometric structures"

    for year in [1905, 1920, 1945]:
        ev = retriever.retrieve(theory, top_k=10, cutoff_year=year)
        result = mock_eval.evaluate(theory, ev, cutoff_year=year, scorer=scorer)
        beauty_axis = next((s for s in result.axis_scores if s.axis_name == "mathematical_beauty"), None)
        print(f"\n  Year {year} ({result.active_period}):")
        print(f"    Overall: {result.overall_score:+.3f}")
        if beauty_axis:
            print(f"    Math beauty axis: {beauty_axis.score:+.3f}")

    # ── Demo 5: Evidence query ────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("DEMO 5: Evidence store query")
    print("=" * 70)

    print("\nPrimary evidence for 'unity' axis:")
    from einstein_taste.core.evidence import SourceType
    unity_evidence = store.filter(
        axes=["unity"],
        source_types=[SourceType.PRIMARY],
    )
    for record in unity_evidence[:3]:
        print(f"  [{record.year}] {record.content[:100]}...")
        print(f"    Source: {record.source_text}")
        print()

    print("=" * 70)
    print("Demo complete! All pipeline components working.")
    print("Set ANTHROPIC_API_KEY for full LLM-based evaluation.")
    print("=" * 70)


if __name__ == "__main__":
    main()
