"""
Benchmark Module
=================

Provides benchmark scenarios for evaluating the taste model's accuracy.

The benchmark consists of pairs/sets of scientific theories or questions
where Einstein's historical preference is well-documented. The model should
rank these consistently with Einstein's known choices.

Benchmark types:
1. Binary preference: "Einstein preferred A over B" (documented)
2. Temporal ranking: "At year Y, Einstein would have prioritized..."
3. Axis alignment: "This theory scores high on axis X because..."
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class BenchmarkCase(BaseModel):
    """A single benchmark test case."""
    id: str
    description: str
    candidates: list[str] = Field(description="List of candidate theories/questions")
    expected_ranking: list[int] = Field(
        description="Expected ranking indices (0-based), best first"
    )
    cutoff_year: int
    evidence_basis: str = Field(
        description="Historical evidence for the expected ranking"
    )
    difficulty: str = "medium"  # easy, medium, hard
    tags: list[str] = Field(default_factory=list)


def get_benchmark_cases() -> list[BenchmarkCase]:
    """Return the built-in benchmark cases."""
    return [
        # ── Easy: Clear historical preferences ─────────────────────────────
        BenchmarkCase(
            id="bench_sr_vs_lorentz",
            description=(
                "Special relativity vs. Lorentz's electron theory. "
                "Einstein explicitly chose the simpler, more symmetric formulation."
            ),
            candidates=[
                "A theory of electrodynamics based on the principle of relativity, "
                "requiring no preferred reference frame and deriving length contraction "
                "and time dilation from two postulates.",
                "A theory that explains the Michelson-Morley result through physical "
                "contraction of objects moving through the ether, with compensating "
                "effects in electromagnetic theory.",
            ],
            expected_ranking=[0, 1],
            cutoff_year=1905,
            evidence_basis=(
                "Einstein's 1905 SR paper explicitly rejects the ether and asymmetric "
                "descriptions. Autobiographical Notes (1949) confirms this motivation."
            ),
            difficulty="easy",
            tags=["special_relativity", "simplicity", "invariance"],
        ),
        BenchmarkCase(
            id="bench_gr_vs_nordstrom",
            description=(
                "General relativity vs. Nordstrom's scalar theory of gravity. "
                "Einstein chose the tensor theory for its general covariance."
            ),
            candidates=[
                "A tensor theory of gravity where spacetime curvature is determined "
                "by the stress-energy tensor, satisfying general covariance.",
                "A scalar theory of gravity that modifies Newtonian gravity to be "
                "Lorentz-invariant, simpler mathematically but lacks general covariance.",
            ],
            expected_ranking=[0, 1],
            cutoff_year=1915,
            evidence_basis=(
                "Einstein chose GR over Nordstrom's theory despite Nordstrom's "
                "being simpler, because GR satisfied general covariance. "
                "Norton (1992) documents this choice."
            ),
            difficulty="easy",
            tags=["general_relativity", "invariance", "mathematical_beauty"],
        ),

        # ── Medium: Nuanced preferences ────────────────────────────────────
        BenchmarkCase(
            id="bench_quantum_interpretations",
            description=(
                "Copenhagen vs. hidden variables interpretation. "
                "Einstein's well-known preference for realism."
            ),
            candidates=[
                "A complete description of quantum phenomena through wave function "
                "collapse and complementarity, where the act of measurement plays "
                "a fundamental role in determining physical properties.",
                "A theory where quantum mechanical results arise from underlying "
                "deterministic hidden variables, with the wave function being an "
                "incomplete description of a deeper reality.",
            ],
            expected_ranking=[1, 0],
            cutoff_year=1935,
            evidence_basis=(
                "EPR paper (1935), Einstein-Born letters, and numerous Solvay "
                "conference debates document Einstein's preference for hidden "
                "variables / realist interpretation over Copenhagen."
            ),
            difficulty="medium",
            tags=["quantum_mechanics", "physical_reality", "determinism"],
        ),
        BenchmarkCase(
            id="bench_unified_vs_separate",
            description=(
                "Unified field theory vs. separate treatment of gravity and EM."
            ),
            candidates=[
                "A framework that treats gravity and electromagnetism as separate "
                "fundamental forces with independent field equations and no "
                "geometric connection between them.",
                "A theory that unifies gravity and electromagnetism into a single "
                "geometric framework, potentially through extra dimensions or "
                "modified spacetime geometry.",
            ],
            expected_ranking=[1, 0],
            cutoff_year=1930,
            evidence_basis=(
                "Einstein pursued unified field theory from the 1920s onward. "
                "Van Dongen (2010) documents his persistent preference for unification "
                "despite repeated failures."
            ),
            difficulty="medium",
            tags=["unified_field_theory", "unity"],
        ),

        # ── Hard: Temporal sensitivity ─────────────────────────────────────
        BenchmarkCase(
            id="bench_beauty_shift",
            description=(
                "Testing the temporal shift in Einstein's methodology: "
                "pre-1920 physical intuition vs. post-1920 mathematical strategy."
            ),
            candidates=[
                "A theory development approach that starts from physical principles "
                "and physical intuition, using mathematics as a tool to formalize "
                "pre-existing physical insights.",
                "A theory development approach that starts from mathematical elegance "
                "and formal beauty, seeking physically meaningful interpretations of "
                "mathematically natural structures.",
            ],
            expected_ranking=[0, 1],  # Before 1920, Einstein preferred physical strategy
            cutoff_year=1910,
            evidence_basis=(
                "Van Dongen (2010) documents Einstein's shift from 'physical strategy' "
                "to 'mathematical strategy' around 1920. Before this shift, Einstein "
                "relied on physical intuition."
            ),
            difficulty="hard",
            tags=["methodology", "mathematical_beauty", "temporal_sensitivity"],
        ),
        BenchmarkCase(
            id="bench_beauty_shift_late",
            description=(
                "Same as above but at a later cutoff: post-shift Einstein "
                "should prefer mathematical elegance."
            ),
            candidates=[
                "A theory development approach that starts from physical principles "
                "and physical intuition, using mathematics as a tool to formalize "
                "pre-existing physical insights.",
                "A theory development approach that starts from mathematical elegance "
                "and formal beauty, seeking physically meaningful interpretations of "
                "mathematically natural structures.",
            ],
            expected_ranking=[1, 0],  # After 1920, Einstein shifted to mathematical strategy
            cutoff_year=1940,
            evidence_basis=(
                "Van Dongen (2010): after GR, Einstein increasingly relied on "
                "mathematical elegance as a guide. His unified field theory work "
                "(1930s-50s) exemplifies the mathematical strategy."
            ),
            difficulty="hard",
            tags=["methodology", "mathematical_beauty", "temporal_sensitivity"],
        ),
    ]


def run_benchmark(pipeline, verbose: bool = True) -> dict:
    """
    Run all benchmark cases and compute accuracy metrics.

    Args:
        pipeline: TastePipeline instance
        verbose: Whether to print detailed results

    Returns:
        Dict with metrics: accuracy, per-case results, breakdown by difficulty
    """
    cases = get_benchmark_cases()
    results = []

    for case in cases:
        if verbose:
            print(f"\nRunning benchmark: {case.id}")
            print(f"  Description: {case.description}")

        evaluations = pipeline.rank_candidates(
            case.candidates,
            cutoff_year=case.cutoff_year,
        )

        # Check if ranking matches expected
        actual_ranking = [
            case.candidates.index(ev.candidate_description)
            for ev in evaluations
        ]
        correct = actual_ranking == case.expected_ranking

        result = {
            "case_id": case.id,
            "difficulty": case.difficulty,
            "correct": correct,
            "expected": case.expected_ranking,
            "actual": actual_ranking,
            "scores": [ev.overall_score for ev in evaluations],
        }
        results.append(result)

        if verbose:
            status = "PASS" if correct else "FAIL"
            print(f"  Result: {status}")
            print(f"  Expected: {case.expected_ranking}, Got: {actual_ranking}")

    # Compute metrics
    total = len(results)
    correct = sum(1 for r in results if r["correct"])
    accuracy = correct / total if total > 0 else 0.0

    by_difficulty = {}
    for diff in ["easy", "medium", "hard"]:
        diff_results = [r for r in results if r["difficulty"] == diff]
        diff_correct = sum(1 for r in diff_results if r["correct"])
        by_difficulty[diff] = {
            "total": len(diff_results),
            "correct": diff_correct,
            "accuracy": diff_correct / len(diff_results) if diff_results else 0.0,
        }

    return {
        "total": total,
        "correct": correct,
        "accuracy": accuracy,
        "by_difficulty": by_difficulty,
        "cases": results,
    }
