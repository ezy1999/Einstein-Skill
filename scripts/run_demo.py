"""
Demo script showing the Einstein Research Taste system in action.

Evaluates several candidate theories and ranks them, demonstrating
the system's core capabilities including temporal cutoff and
evidence-based scoring.
"""

import json
from einstein_taste.core.pipeline import TastePipeline
from einstein_taste.config.settings import ModelConfig


def main():
    print("=" * 60)
    print("EINSTEIN RESEARCH TASTE - DEMO")
    print("=" * 60)

    # Initialize pipeline with seed data
    config = ModelConfig()
    pipeline = TastePipeline.default(config)

    # Show system info
    store_summary = pipeline.evidence_store.summary()
    print(f"\nEvidence store: {store_summary['total_records']} records")
    print(f"Axes covered: {list(store_summary['axes_coverage'].keys())}")

    # Demo 1: Evaluate a single theory
    print("\n" + "=" * 60)
    print("DEMO 1: Single Theory Evaluation")
    print("=" * 60)

    candidate = (
        "A theory that unifies electromagnetic and gravitational forces "
        "through a modified spacetime geometry with additional dimensions, "
        "requiring no preferred reference frame and making testable "
        "predictions about light deflection near massive objects."
    )

    result = pipeline.evaluate(candidate, cutoff_year=1930)
    pipeline.print_evaluation(result)

    # Demo 2: Rank competing theories
    print("\n" + "=" * 60)
    print("DEMO 2: Ranking Competing Approaches")
    print("=" * 60)

    candidates = [
        "A probabilistic theory where physical properties are fundamentally "
        "indeterminate until measured, with no underlying deterministic reality.",

        "A deterministic hidden-variable theory that reproduces quantum predictions "
        "while maintaining objective physical reality independent of measurement.",

        "A theory that abandons both determinism and locality, accepting "
        "instantaneous action at a distance as a fundamental feature of nature.",
    ]

    ranked = pipeline.rank_candidates(candidates, cutoff_year=1935)
    for i, ev in enumerate(ranked, 1):
        print(f"\n  #{i} (score: {ev.overall_score:+.3f})")
        print(f"  {ev.candidate_description[:80]}...")
        if ev.caveats:
            print(f"  Caveat: {ev.caveats[0]}")

    # Demo 3: Temporal sensitivity
    print("\n" + "=" * 60)
    print("DEMO 3: Temporal Sensitivity")
    print("=" * 60)

    theory = (
        "An approach to theoretical physics guided primarily by mathematical "
        "elegance and formal beauty, seeking physically meaningful interpretations "
        "of mathematically natural structures."
    )

    for year in [1910, 1925, 1945]:
        result = pipeline.evaluate(theory, cutoff_year=year)
        print(f"\n  Year {year} ({result.active_period}):")
        print(f"    Overall score: {result.overall_score:+.3f}")
        if result.axis_scores:
            beauty_score = next(
                (s for s in result.axis_scores if s.axis_name == "mathematical_beauty"),
                None
            )
            if beauty_score:
                print(f"    Mathematical beauty axis: {beauty_score.score:+.3f}")

    print("\n" + "=" * 60)
    print("Demo complete!")


if __name__ == "__main__":
    main()
