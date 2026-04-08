"""
Enrich the evidence corpus with additional records from web-verified sources.
Adds evidence from SEP Einstein article and newly discovered papers.
"""

import json
from pathlib import Path
from einstein_taste.core.evidence import EvidenceRecord, EvidenceStore, SourceType, ConfidenceLevel
from einstein_taste.data.loader import load_evidence_store, save_evidence_store
from einstein_taste.config.settings import PROCESSED_DATA_DIR

# Load existing store
store = load_evidence_store(PROCESSED_DATA_DIR)
print(f"Existing records: {store.count()}")

# New evidence records from web-verified sources
new_records = [
    # ── From SEP article on Einstein's Philosophy (Don Howard) ─────────
    EvidenceRecord(
        id="sep_holism_001",
        content=(
            "Einstein endorsed theoretical holism derived from Pierre Duhem: theories function "
            "as integrated systems where only the complete structure possesses empirical content. "
            "As he explained in his 1910/11 lecture notes: 'We set up a conceptual system the "
            "individual parts of which do not correspond directly to empirical facts. Only a certain "
            "totality of theoretical material corresponds again to a certain totality of experimental "
            "facts.' This meant empirical evidence underdetermines theory choice in principle."
        ),
        source_text="Howard, 'Einstein's Philosophy of Science', Stanford Encyclopedia of Philosophy (2004/2019); Einstein, lecture notes 1910/11",
        source_type=SourceType.SECONDARY,
        confidence=ConfidenceLevel.STRONG,
        year=1911,
        period="general_relativity",
        relevant_axes=["empirical_grounding", "simplicity"],
        axis_valence={"empirical_grounding": 0.7, "simplicity": 0.5},
        tags=["holism", "philosophy_of_science", "duhem"],
    ),
    EvidenceRecord(
        id="sep_simplicity_001",
        content=(
            "Einstein maintained unwavering confidence that nature embodies mathematical simplicity. "
            "In his 1933 Spencer Lecture, he asserted: 'Our experience hitherto justifies us in "
            "trusting that nature is the realization of the simplest that is mathematically conceivable.' "
            "However, he acknowledged difficulty formalizing 'simplicity,' writing in 1946 that "
            "precision 'meets with great difficulties' and involves 'reciprocal weighing of "
            "incommensurable qualities.'"
        ),
        source_text="Howard, 'Einstein's Philosophy of Science', SEP; Einstein, Spencer Lecture (1933); Einstein, 'Autobiographical Notes' (1946/1949)",
        source_type=SourceType.PRIMARY,
        confidence=ConfidenceLevel.DIRECT,
        year=1933,
        period="quantum_debates",
        relevant_axes=["simplicity", "mathematical_beauty"],
        axis_valence={"simplicity": 1.0, "mathematical_beauty": 0.8},
        tags=["simplicity", "methodology", "spencer_lecture"],
        is_quote=True,
    ),
    EvidenceRecord(
        id="sep_realism_001",
        content=(
            "Einstein's realism differed fundamentally from standard scientific realism. He explicitly "
            "stated to Eduard Study in 1918: 'I concede that the natural sciences concern the \"real,\" "
            "but I am still not a realist.' His position centered on spatial separability—the postulate "
            "that spatially distant systems possess independent physical existence. In a 1948 note: "
            "'That which we conceive as existing (\"actual\") should somehow be localized in time and "
            "space...what is present in B should somehow have an existence independent of what is "
            "present in A.' This separability principle, not conventional realism, grounded his "
            "opposition to quantum mechanics."
        ),
        source_text="Howard, 'Einstein's Philosophy of Science', SEP; Einstein to Study (1918); Einstein, 'Quanten-Mechanik und Wirklichkeit' (1948)",
        source_type=SourceType.PRIMARY,
        confidence=ConfidenceLevel.DIRECT,
        year=1948,
        period="unified_field_theory",
        relevant_axes=["physical_reality", "causal_continuity"],
        axis_valence={"physical_reality": 1.0, "causal_continuity": 0.9},
        tags=["realism", "separability", "quantum_mechanics"],
        is_quote=True,
    ),
    EvidenceRecord(
        id="sep_principle_constructive",
        content=(
            "Einstein drew a sharp distinction between 'constructive theories' (which build up "
            "phenomena from simpler components, e.g., statistical mechanics) and 'principle theories' "
            "(which start from empirically observed general principles, e.g., thermodynamics and "
            "special relativity). He viewed principle theories as more secure and epistemologically "
            "superior. This distinction reveals a key taste axis: preference for theories constrained "
            "by well-confirmed general principles over those built from hypothetical mechanisms."
        ),
        source_text="Howard, 'Einstein's Philosophy of Science', SEP; Einstein, 'What is the Theory of Relativity?' (1919)",
        source_type=SourceType.PRIMARY,
        confidence=ConfidenceLevel.DIRECT,
        year=1919,
        period="general_relativity",
        relevant_axes=["simplicity", "empirical_grounding"],
        axis_valence={"simplicity": 0.8, "empirical_grounding": 0.9},
        tags=["principle_theory", "constructive_theory", "methodology"],
    ),
    EvidenceRecord(
        id="sep_restrictiveness",
        content=(
            "Einstein valued theoretical 'restrictiveness'—a good theory should be highly constrained, "
            "'practically impossible to modify without destroying its structure.' General relativity "
            "exemplified this: once you accept the equivalence principle and general covariance, "
            "the field equations are essentially uniquely determined. This criterion of rigidity "
            "goes beyond simplicity to demand that the theory's structure be self-enforcing."
        ),
        source_text="Howard, 'Einstein's Philosophy of Science', SEP; Norton, 'How Einstein Found His Field Equations' (1984)",
        source_type=SourceType.SECONDARY,
        confidence=ConfidenceLevel.STRONG,
        year=1984,
        relevant_axes=["simplicity", "mathematical_beauty", "invariance"],
        axis_valence={"simplicity": 0.7, "mathematical_beauty": 0.8, "invariance": 0.6},
        tags=["restrictiveness", "rigidity", "general_relativity"],
    ),
    EvidenceRecord(
        id="sep_epistemological_opportunism",
        content=(
            "Einstein famously resisted systematic epistemological commitment. He described himself "
            "as appearing 'as realist...as idealist...as positivist...as Platonist or Pythagorean' "
            "depending on scientific necessity. What critics termed 'opportunism' reflected his "
            "conviction that physical problems, not philosophical systems, should guide theory "
            "construction. This meta-taste—willingness to adopt whatever philosophical stance "
            "serves the physics—is itself a distinctive feature of Einstein's approach."
        ),
        source_text="Howard, 'Einstein's Philosophy of Science', SEP; Einstein, 'Reply to Criticisms' in Schilpp (1949)",
        source_type=SourceType.PRIMARY,
        confidence=ConfidenceLevel.DIRECT,
        year=1949,
        period="unified_field_theory",
        relevant_axes=["empirical_grounding", "simplicity"],
        axis_valence={"empirical_grounding": 0.6, "simplicity": 0.4},
        tags=["epistemology", "opportunism", "methodology"],
        is_quote=True,
    ),

    # ── From Einstein-Solovine correspondence ─────────────────────────
    EvidenceRecord(
        id="solovine_epistemology_diagram",
        content=(
            "In a 1952 letter to Maurice Solovine, Einstein drew his famous epistemological diagram "
            "showing the relationship between sense experience (E), axioms (A), and derived "
            "propositions (S). The axioms are connected to experience not by logical deduction but "
            "by an intuitive 'leap' (represented by a wavy line). This diagram is one of the "
            "clearest expressions of Einstein's view that theoretical concepts are 'free creations "
            "of the human mind' not derivable from experience alone."
        ),
        source_text="Einstein to Solovine, 7 May 1952, in 'Letters to Solovine' (Philosophical Library, 1987)",
        source_type=SourceType.PRIMARY,
        confidence=ConfidenceLevel.DIRECT,
        year=1952,
        period="unified_field_theory",
        relevant_axes=["thought_experiment", "mathematical_beauty", "empirical_grounding"],
        axis_valence={"thought_experiment": 0.7, "mathematical_beauty": 0.6, "empirical_grounding": 0.8},
        tags=["epistemology", "solovine", "correspondence", "free_creation"],
        is_quote=False,
    ),

    # ── From Einstein's own writings ──────────────────────────────────
    EvidenceRecord(
        id="einstein_physics_reality",
        content=(
            "In 'Physics and Reality' (1936), Einstein presented his most philosophically dense "
            "discussion of the epistemology of physics. He argued for a stratification of theoretical "
            "concepts at varying distances from direct sensory experience, with the most fundamental "
            "concepts (like spacetime geometry) being the farthest removed. He insisted that while "
            "experience may suggest mathematical concepts, 'they most certainly cannot be deduced "
            "from it'—the creative principle resides in the theoretical imagination."
        ),
        source_text="Einstein, 'Physics and Reality', Journal of the Franklin Institute 221 (1936), pp. 349-382",
        source_type=SourceType.PRIMARY,
        confidence=ConfidenceLevel.DIRECT,
        year=1936,
        period="quantum_debates",
        relevant_axes=["mathematical_beauty", "empirical_grounding", "thought_experiment"],
        axis_valence={"mathematical_beauty": 0.8, "empirical_grounding": 0.7, "thought_experiment": 0.6},
        tags=["epistemology", "physics_reality", "stratification"],
        is_quote=False,
    ),

    # ── Bose-Einstein work showing cross-domain taste ─────────────────
    EvidenceRecord(
        id="bose_einstein_statistics",
        content=(
            "In 1924-1925, Einstein recognized the significance of Satyendra Nath Bose's paper on "
            "photon statistics, translated it from English, and extended the approach to material "
            "particles—predicting Bose-Einstein condensation. This episode reveals Einstein's taste "
            "for recognizing deep connections: he saw that a statistical method developed for light "
            "quanta could unify the treatment of radiation and matter, exemplifying his drive toward "
            "unity across apparently separate phenomena."
        ),
        source_text="Pais, 'Subtle is the Lord' (1982), Ch. 23; Einstein, 'Quantentheorie des einatomigen idealen Gases' (1924/1925)",
        source_type=SourceType.SECONDARY,
        confidence=ConfidenceLevel.STRONG,
        year=1925,
        period="quantum_debates",
        relevant_axes=["unity", "simplicity"],
        axis_valence={"unity": 1.0, "simplicity": 0.6},
        tags=["bose_einstein", "statistics", "cross_domain"],
    ),
]

# Add new records
for record in new_records:
    if store.get(record.id) is None:
        store.add(record)

# Save updated store
save_evidence_store(store, PROCESSED_DATA_DIR / "evidence.json")

print(f"Updated records: {store.count()}")
summary = store.summary()
print(f"\nEvidence summary:")
print(f"  By source type: {summary['by_source_type']}")
print(f"  By confidence: {summary['by_confidence']}")
print(f"  Axes coverage: {summary['axes_coverage']}")
