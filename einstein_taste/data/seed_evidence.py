"""
Seed Evidence Data
===================

Built-in evidence records derived from well-documented historical sources
about Einstein's scientific taste. This provides a minimal working dataset
so the system can function without external data loading.

All evidence here is grounded in published, peer-reviewed scholarship
or Einstein's own published writings.
"""

from einstein_taste.core.evidence import (
    EvidenceRecord,
    SourceType,
    ConfidenceLevel,
)


def get_seed_evidence() -> list[EvidenceRecord]:
    """Return the built-in seed evidence records."""
    return [
        # ── Simplicity ─────────────────────────────────────────────────────
        EvidenceRecord(
            id="seed_simplicity_001",
            content=(
                "Einstein stated in his 1933 Herbert Spencer Lecture: "
                "'It can scarcely be denied that the supreme goal of all theory is to make "
                "the irreducible basic elements as simple and as few as possible without "
                "having to surrender the adequate representation of a single datum of experience.' "
                "This is often paraphrased as 'Everything should be made as simple as possible, "
                "but not simpler.'"
            ),
            source_text="Einstein, 'On the Method of Theoretical Physics', Herbert Spencer Lecture, Oxford (1933)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1933,
            period="quantum_debates",
            relevant_axes=["simplicity", "empirical_grounding"],
            axis_valence={"simplicity": 1.0, "empirical_grounding": 0.8},
            tags=["methodology", "philosophy_of_science"],
            is_quote=True,
        ),
        EvidenceRecord(
            id="seed_simplicity_002",
            content=(
                "In his Autobiographical Notes (1949), Einstein described how his dissatisfaction "
                "with the complexity and ad hoc nature of Lorentz's electron theory motivated "
                "him to seek a simpler foundation, leading to special relativity. He found it "
                "'intolerable' that the theory required asymmetric explanations for symmetric "
                "phenomena (magnet/conductor problem)."
            ),
            source_text="Einstein, 'Autobiographical Notes' in P.A. Schilpp (ed.), Albert Einstein: Philosopher-Scientist (1949)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1949,
            period="unified_field_theory",
            relevant_axes=["simplicity", "invariance"],
            axis_valence={"simplicity": 1.0, "invariance": 0.9},
            tags=["special_relativity", "methodology"],
            is_quote=False,
        ),

        # ── Unity ──────────────────────────────────────────────────────────
        EvidenceRecord(
            id="seed_unity_001",
            content=(
                "Einstein devoted the last 30 years of his life (1925-1955) to the pursuit of "
                "a unified field theory that would combine gravity and electromagnetism into a "
                "single geometric framework. As documented by Pais (1982), this quest persisted "
                "despite repeated failures and increasing isolation from the physics mainstream."
            ),
            source_text="Pais, 'Subtle is the Lord: The Science and the Life of Albert Einstein' (1982), Ch. 17",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1982,
            relevant_axes=["unity", "mathematical_beauty"],
            axis_valence={"unity": 1.0, "mathematical_beauty": 0.7},
            tags=["unified_field_theory", "late_career"],
        ),
        EvidenceRecord(
            id="seed_unity_002",
            content=(
                "Einstein wrote to Marcel Grossmann in 1901: 'It is a magnificent feeling to "
                "recognize the unity of a complex of phenomena that to direct observation "
                "appear to be quite separate things.' This early statement already reveals "
                "the unification drive that would characterize his entire career."
            ),
            source_text="Einstein to Grossmann, 14 April 1901, Collected Papers Vol. 1, Doc. 100",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1901,
            period="early_revolutionary",
            relevant_axes=["unity"],
            axis_valence={"unity": 1.0},
            tags=["early_career", "correspondence"],
            is_quote=True,
        ),

        # ── Invariance ─────────────────────────────────────────────────────
        EvidenceRecord(
            id="seed_invariance_001",
            content=(
                "The principle of general covariance — that the laws of physics should take "
                "the same form in all coordinate systems — was Einstein's guiding principle "
                "in developing general relativity. Norton (1984) documents how Einstein's "
                "commitment to this principle, despite temporary wavering in 1913 (Entwurf theory), "
                "ultimately led him to the correct field equations in November 1915."
            ),
            source_text="Norton, 'How Einstein Found His Field Equations: 1912-1915', Historical Studies in the Physical Sciences (1984)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1984,
            relevant_axes=["invariance", "mathematical_beauty"],
            axis_valence={"invariance": 1.0, "mathematical_beauty": 0.6},
            tags=["general_relativity", "general_covariance"],
        ),
        EvidenceRecord(
            id="seed_invariance_002",
            content=(
                "In the opening of his 1905 paper on special relativity, Einstein identifies "
                "an asymmetry in the description of electromagnetic induction depending on "
                "whether the magnet or conductor is considered to move. He argues this asymmetry "
                "is unphysical and should be removed, motivating the principle of relativity."
            ),
            source_text="Einstein, 'On the Electrodynamics of Moving Bodies', Annalen der Physik 17 (1905)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1905,
            period="early_revolutionary",
            relevant_axes=["invariance", "simplicity"],
            axis_valence={"invariance": 1.0, "simplicity": 0.8},
            tags=["special_relativity", "symmetry"],
            is_quote=False,
        ),

        # ── Physical Reality ───────────────────────────────────────────────
        EvidenceRecord(
            id="seed_reality_001",
            content=(
                "The EPR paper (1935) argued that quantum mechanics is incomplete because "
                "it cannot simultaneously assign definite values to conjugate variables of "
                "spatially separated systems. Einstein's criterion: 'If, without in any way "
                "disturbing a system, we can predict with certainty the value of a physical "
                "quantity, then there exists an element of physical reality corresponding to "
                "this physical quantity.'"
            ),
            source_text="Einstein, Podolsky & Rosen, Physical Review 47 (1935), p. 777",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1935,
            period="quantum_debates",
            relevant_axes=["physical_reality", "causal_continuity"],
            axis_valence={"physical_reality": 1.0, "causal_continuity": 0.8},
            tags=["quantum_mechanics", "EPR", "realism"],
            is_quote=True,
        ),
        EvidenceRecord(
            id="seed_reality_002",
            content=(
                "In the Einstein-Born correspondence (1926), Einstein wrote: "
                "'Quantum mechanics is certainly imposing. But an inner voice tells me that "
                "it is not yet the real thing. The theory says a lot, but does not really "
                "bring us any closer to the secret of the Old One. I, at any rate, am "
                "convinced that He does not throw dice.' This reveals his deep commitment "
                "to deterministic physical reality."
            ),
            source_text="Einstein to Max Born, 4 December 1926, The Born-Einstein Letters (1971)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1926,
            period="quantum_debates",
            relevant_axes=["physical_reality"],
            axis_valence={"physical_reality": 1.0},
            tags=["quantum_mechanics", "determinism", "correspondence"],
            is_quote=True,
        ),

        # ── Mathematical Beauty ────────────────────────────────────────────
        EvidenceRecord(
            id="seed_beauty_001",
            content=(
                "Van Dongen (2010) documents a crucial shift in Einstein's methodology: "
                "before ~1920, Einstein relied primarily on physical intuition (the 'physical "
                "strategy'), but afterward increasingly adopted a 'mathematical strategy' "
                "where mathematical elegance and formal beauty guided theory construction. "
                "This shift is visible in his approach to unified field theories."
            ),
            source_text="van Dongen, 'Einstein's Unification', Cambridge University Press (2010)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=2010,
            relevant_axes=["mathematical_beauty", "unity"],
            axis_valence={"mathematical_beauty": 1.0, "unity": 0.5},
            tags=["methodology_shift", "mathematical_strategy"],
        ),
        EvidenceRecord(
            id="seed_beauty_002",
            content=(
                "In his 1933 Herbert Spencer Lecture, Einstein stated: 'Experience can of "
                "course guide us in our choice of serviceable mathematical concepts; it "
                "cannot possibly be the source from which they are derived; experience of "
                "course remains the sole criterion of the serviceability of a mathematical "
                "construction for physics; but the truly creative principle resides in "
                "mathematics.' This shows his growing appreciation for mathematical aesthetics."
            ),
            source_text="Einstein, 'On the Method of Theoretical Physics', Herbert Spencer Lecture, Oxford (1933)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1933,
            period="quantum_debates",
            relevant_axes=["mathematical_beauty", "empirical_grounding"],
            axis_valence={"mathematical_beauty": 1.0, "empirical_grounding": 0.6},
            tags=["methodology", "mathematics", "philosophy_of_science"],
            is_quote=True,
        ),

        # ── Causal Continuity ──────────────────────────────────────────────
        EvidenceRecord(
            id="seed_causality_001",
            content=(
                "Howard (1985) argues that Einstein's insistence on 'separability' — the "
                "principle that spatially separated systems have independent real states — "
                "was the core of his objections to quantum mechanics, more fundamental even "
                "than determinism. Einstein viewed quantum nonlocality as 'spooky action "
                "at a distance' that violated basic principles of field theory."
            ),
            source_text="Howard, 'Einstein on Locality and Separability', Studies in History and Philosophy of Science (1985)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1985,
            relevant_axes=["causal_continuity", "physical_reality"],
            axis_valence={"causal_continuity": 1.0, "physical_reality": 0.8},
            tags=["locality", "separability", "quantum_mechanics"],
        ),

        # ── Empirical Grounding ────────────────────────────────────────────
        EvidenceRecord(
            id="seed_empirical_001",
            content=(
                "Despite developing highly abstract theories, Einstein always insisted on "
                "empirical testability. For general relativity, he calculated three specific "
                "predictions: Mercury's perihelion precession, light bending by the sun, and "
                "gravitational redshift. When the 1919 Eddington expedition confirmed light "
                "bending, Einstein reportedly told a student: 'I would have felt sorry for "
                "the dear Lord [if it hadn't been confirmed]. The theory is correct.'"
            ),
            source_text="Pais, 'Subtle is the Lord' (1982), Ch. 16; Ilse Rosenthal-Schneider memoir",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1919,
            period="general_relativity",
            relevant_axes=["empirical_grounding"],
            axis_valence={"empirical_grounding": 1.0},
            tags=["general_relativity", "prediction", "confirmation"],
        ),
        EvidenceRecord(
            id="seed_empirical_002",
            content=(
                "In 'Geometry and Experience' (1921), Einstein posed the foundational question: "
                "'How can it be that mathematics, being after all a product of human thought "
                "which is independent of experience, is so admirably appropriate to the objects "
                "of reality?' He argued that insofar as mathematical propositions refer to "
                "reality they are not certain, and insofar as they are certain they do not "
                "refer to reality. This tension shaped his empirical methodology."
            ),
            source_text="Einstein, 'Geometry and Experience', address to Prussian Academy (1921)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1921,
            period="quantum_debates",
            relevant_axes=["empirical_grounding", "mathematical_beauty"],
            axis_valence={"empirical_grounding": 1.0, "mathematical_beauty": 0.5},
            tags=["methodology", "geometry", "philosophy"],
            is_quote=True,
        ),

        # ── Thought Experiments ────────────────────────────────────────────
        EvidenceRecord(
            id="seed_gedanken_001",
            content=(
                "Norton (1991) catalogs Einstein's major thought experiments: chasing a light "
                "beam (age 16, leading to SR), the elevator/equivalence principle (1907, leading "
                "to GR), the rotating disk (1912, non-Euclidean geometry), and numerous quantum "
                "thought experiments (photon box, EPR). Norton argues these were not mere "
                "illustrations but essential tools of theory construction for Einstein."
            ),
            source_text="Norton, 'Thought Experiments in Einstein's Work' in T. Horowitz & G. Massey (eds.), Thought Experiments in Science and Philosophy (1991)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1991,
            relevant_axes=["thought_experiment"],
            axis_valence={"thought_experiment": 1.0},
            tags=["methodology", "Gedankenexperiment"],
        ),
        EvidenceRecord(
            id="seed_gedanken_002",
            content=(
                "In his Autobiographical Notes, Einstein described the thought experiment "
                "that started it all: at age 16, he imagined chasing a beam of light and "
                "asked what the electromagnetic field would look like to such an observer. "
                "He noted that it would be a static oscillating field, which contradicted "
                "Maxwell's equations, creating a paradox that took him 10 years to resolve "
                "with special relativity."
            ),
            source_text="Einstein, 'Autobiographical Notes' in Schilpp (1949), pp. 49-53",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1949,
            period="unified_field_theory",
            relevant_axes=["thought_experiment", "invariance"],
            axis_valence={"thought_experiment": 1.0, "invariance": 0.7},
            tags=["special_relativity", "light_beam", "early_inspiration"],
            is_quote=False,
        ),

        # ── Cross-cutting: Methodology shift ──────────────────────────────
        EvidenceRecord(
            id="seed_methodology_001",
            content=(
                "Holton (1973) identified key 'themata' in Einstein's scientific thinking: "
                "symmetry, unity, simplicity, completeness, continuum, causality, and "
                "invariance. Holton argues these thematic presuppositions guided Einstein's "
                "choices of problems and acceptable solutions throughout his career, often "
                "in opposition to the empirical mainstream of physics."
            ),
            source_text="Holton, 'Thematic Origins of Scientific Thought: Kepler to Einstein', Harvard University Press (1973)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1973,
            relevant_axes=["simplicity", "unity", "invariance", "causal_continuity", "physical_reality"],
            axis_valence={
                "simplicity": 0.9,
                "unity": 0.9,
                "invariance": 0.9,
                "causal_continuity": 0.8,
                "physical_reality": 0.8,
            },
            tags=["themata", "methodology", "philosophy_of_science"],
        ),
    ]
