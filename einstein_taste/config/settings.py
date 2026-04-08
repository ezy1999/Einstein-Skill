"""
Global configuration for the Einstein Research Taste system.

Defines taste axes, temporal periods, model parameters, and data paths.
All taste axes are derived from documented historical evidence about Einstein's
scientific methodology and philosophy.
"""

from pathlib import Path
from pydantic import BaseModel, Field


# ── Project paths ──────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "einstein_taste" / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"


# ── Taste Axes ─────────────────────────────────────────────────────────────────
# Each axis represents a documented dimension of Einstein's scientific taste,
# grounded in his writings, letters, and scholarly analyses of his methodology.

class TasteAxis(BaseModel):
    """A single dimension of scientific taste with historical grounding."""
    name: str
    description: str
    weight: float = Field(ge=0.0, le=1.0, description="Default weight in [0,1]")
    evidence_sources: list[str] = Field(
        default_factory=list,
        description="Historical sources supporting this axis"
    )
    keywords: list[str] = Field(
        default_factory=list,
        description="Keywords associated with this axis for retrieval"
    )


# Einstein's core taste axes, derived from historical scholarship
EINSTEIN_TASTE_AXES: list[TasteAxis] = [
    TasteAxis(
        name="simplicity",
        description=(
            "Preference for theories with minimal free parameters and assumptions. "
            "Einstein frequently cited Occam's razor and sought the simplest possible "
            "explanations consistent with observation."
        ),
        weight=0.85,
        evidence_sources=[
            "Einstein, 'On the Method of Theoretical Physics' (1933 Herbert Spencer Lecture)",
            "Einstein, 'Autobiographical Notes' in Schilpp (1949)",
            "Holton, 'Thematic Origins of Scientific Thought' (1973)",
        ],
        keywords=["simplicity", "economy", "parsimony", "minimal assumptions", "elegance"],
    ),
    TasteAxis(
        name="unity",
        description=(
            "Drive toward unification of disparate phenomena under a single framework. "
            "Einstein's career-long pursuit of unified field theory exemplifies this. "
            "He sought to reduce the number of independent theoretical constructs."
        ),
        weight=0.90,
        evidence_sources=[
            "Einstein, 'The Meaning of Relativity' (1922)",
            "Pais, 'Subtle is the Lord' (1982), Ch. 17 on unified field theory",
            "van Dongen, 'Einstein's Unification' (2010)",
        ],
        keywords=["unification", "unity", "synthesis", "single framework", "universal"],
    ),
    TasteAxis(
        name="invariance",
        description=(
            "Insistence that fundamental laws must be invariant under coordinate "
            "transformations. This principle drove both special and general relativity. "
            "Einstein viewed observer-dependent quantities as secondary."
        ),
        weight=0.95,
        evidence_sources=[
            "Einstein, 'On the Electrodynamics of Moving Bodies' (1905)",
            "Einstein, 'The Foundation of the General Theory of Relativity' (1916)",
            "Norton, 'How Einstein Found His Field Equations' (1984)",
        ],
        keywords=["invariance", "covariance", "symmetry", "coordinate-free", "observer-independent"],
    ),
    TasteAxis(
        name="physical_reality",
        description=(
            "Commitment to an objective physical reality independent of observation. "
            "Einstein's realism led to the EPR paper and his famous objections to "
            "quantum mechanical completeness."
        ),
        weight=0.80,
        evidence_sources=[
            "Einstein, Podolsky & Rosen, 'Can Quantum-Mechanical Description...' (1935)",
            "Einstein-Born Letters (1916-1955)",
            "Fine, 'The Shaky Game: Einstein Realism and the Quantum Theory' (1986)",
        ],
        keywords=["realism", "objective reality", "determinism", "completeness", "hidden variables"],
    ),
    TasteAxis(
        name="mathematical_beauty",
        description=(
            "Appreciation for mathematical elegance as a guide to physical truth. "
            "Einstein valued aesthetic qualities of mathematical formulations, though "
            "he subordinated this to physical intuition in his earlier career."
        ),
        weight=0.70,
        evidence_sources=[
            "Einstein, 'On the Method of Theoretical Physics' (1933)",
            "Holton, 'Thematic Origins of Scientific Thought' (1973)",
            "van Dongen, 'Einstein's Unification' (2010), on the shift to mathematical strategy",
        ],
        keywords=["beauty", "elegance", "mathematical aesthetics", "harmony", "naturalness"],
    ),
    TasteAxis(
        name="causal_continuity",
        description=(
            "Preference for continuous, local, causal explanations over action-at-a-distance. "
            "This drove Einstein's field-theoretic approach and his discomfort with "
            "quantum nonlocality."
        ),
        weight=0.75,
        evidence_sources=[
            "Einstein, 'Physics and Reality' (1936)",
            "Howard, 'Einstein on Locality and Separability' (1985)",
            "Einstein-Born Letters, discussions on quantum mechanics",
        ],
        keywords=["causality", "locality", "continuity", "field theory", "no action at distance"],
    ),
    TasteAxis(
        name="empirical_grounding",
        description=(
            "Theories must connect to observable phenomena, despite Einstein's reputation "
            "as a pure theorist. He insisted on empirical testability (e.g., light bending, "
            "perihelion precession) even for highly abstract theories."
        ),
        weight=0.65,
        evidence_sources=[
            "Einstein, 'Geometry and Experience' (1921)",
            "Pais, 'Subtle is the Lord' (1982), Ch. 16",
            "Howard, 'Einstein and the History of Quantum Theory' (1990)",
        ],
        keywords=["empirical", "testable", "observable", "experiment", "prediction"],
    ),
    TasteAxis(
        name="thought_experiment",
        description=(
            "Reliance on Gedankenexperiment as a primary methodology for theory development. "
            "Einstein's most famous contributions were preceded by vivid thought experiments "
            "(chasing a light beam, elevator, twin clocks)."
        ),
        weight=0.60,
        evidence_sources=[
            "Einstein, 'Autobiographical Notes' in Schilpp (1949)",
            "Norton, 'Thought Experiments in Einstein's Work' (1991)",
            "Isaacson, 'Einstein: His Life and Universe' (2007), Ch. 6",
        ],
        keywords=["thought experiment", "Gedankenexperiment", "mental model", "visualization"],
    ),
]


# ── Temporal Periods ───────────────────────────────────────────────────────────
# Einstein's taste evolved over his career. These periods capture major shifts.

class TemporalPeriod(BaseModel):
    """A distinct period in Einstein's scientific career with characteristic focus."""
    name: str
    start_year: int
    end_year: int
    description: str
    dominant_axes: list[str] = Field(
        default_factory=list,
        description="Names of taste axes that were most prominent in this period"
    )


EINSTEIN_PERIODS: list[TemporalPeriod] = [
    TemporalPeriod(
        name="early_revolutionary",
        start_year=1900,
        end_year=1905,
        description=(
            "Patent office years. Focus on thermodynamics, molecular reality, "
            "and the electrodynamics of moving bodies. Empirical grounding and "
            "thought experiments dominate."
        ),
        dominant_axes=["empirical_grounding", "thought_experiment", "simplicity"],
    ),
    TemporalPeriod(
        name="general_relativity",
        start_year=1906,
        end_year=1915,
        description=(
            "Development of general relativity. Equivalence principle, "
            "general covariance, and geometrization of gravity. "
            "Invariance and unity become paramount."
        ),
        dominant_axes=["invariance", "unity", "causal_continuity"],
    ),
    TemporalPeriod(
        name="quantum_debates",
        start_year=1916,
        end_year=1935,
        description=(
            "Engagement with quantum mechanics, Solvay debates, EPR paper. "
            "Physical realism and determinism vs. Copenhagen interpretation. "
            "Increasing emphasis on mathematical beauty."
        ),
        dominant_axes=["physical_reality", "causal_continuity", "mathematical_beauty"],
    ),
    TemporalPeriod(
        name="unified_field_theory",
        start_year=1936,
        end_year=1955,
        description=(
            "Late career pursuit of unified field theory. Mathematical elegance "
            "and unification become dominant drivers. Increasing isolation from "
            "mainstream physics."
        ),
        dominant_axes=["unity", "mathematical_beauty", "simplicity"],
    ),
]


# ── Model Configuration ───────────────────────────────────────────────────────

class ModelConfig(BaseModel):
    """Configuration for the LLM-based taste modeling pipeline."""
    # LLM settings
    llm_provider: str = "anthropic"
    llm_model: str = "claude-sonnet-4-20250514"
    temperature: float = 0.3
    max_tokens: int = 4096

    # Retrieval settings
    embedding_model: str = "all-MiniLM-L6-v2"
    top_k_evidence: int = 10
    similarity_threshold: float = 0.5

    # Scoring settings
    normalize_scores: bool = True
    require_evidence: bool = True  # Require historical evidence for each axis score
    min_evidence_count: int = 1   # Minimum evidence pieces per axis

    # Temporal settings
    default_cutoff_year: int = 1955  # Einstein's death
    enforce_temporal_cutoff: bool = True


DEFAULT_CONFIG = ModelConfig()
