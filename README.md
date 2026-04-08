# Einstein Research Taste Modeling System

> **Evidence-based computational modeling of Albert Einstein's scientific research taste.**
> Evaluate, rank, and explain how Einstein would have assessed candidate scientific theories — grounded in historical evidence, not role-playing.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![Tests](https://img.shields.io/badge/tests-18%20passed-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)]()

---

## What Is This?

This system models Einstein's **research taste** — his documented preferences for certain kinds of scientific theories. It answers questions like:

- *"How would Einstein have evaluated quantum field theory in 1935?"*
- *"Between hidden-variable theory and Copenhagen QM, which would Einstein prefer?"*
- *"How did Einstein's taste for mathematical beauty evolve over his career?"*

**This is NOT role-playing.** Every evaluation is grounded in historical evidence from Einstein's published papers, letters, lectures, and scholarly analyses of his methodology. The system explicitly marks what is evidence-based vs. what is model inference.

## Key Features

- **8 Taste Axes** derived from historical scholarship (Holton's themata, Howard's analyses)
- **33 Evidence Records** from primary sources (Einstein's writings) and secondary scholarship
- **Temporal Cutoff** prevents anachronism — evaluate Einstein at any year from 1900 to 1955
- **Evidence/Inference Separation** — every score traces back to specific historical sources
- **RAG Pipeline** — retrieval-augmented generation grounds evaluations in real evidence
- **6 Benchmark Cases** with difficulty stratification (easy/medium/hard)
- **CLI + Python API + Claude Code Skill** — multiple interfaces

## How It Works

```
User Query                    Evidence Store (33 records)
    |                               |
    v                               v
[1. Evidence Retrieval] -----> Keyword/Semantic matching
    |                               |
    v                               v
[2. LLM Evaluation]           Retrieved evidence as context
    |                          (Claude/GPT-4 with structured prompt)
    v
[3. Axis Scoring]             Per-axis scores with evidence links
    |                          Weighted by career period
    v
[4. Output]                   Ranked results with explanations
                               Evidence vs. inference clearly marked
```

## The 8 Taste Axes

Each axis represents a documented dimension of Einstein's scientific preferences:

| # | Axis | Weight | What It Means | Key Evidence |
|---|------|--------|---------------|-------------|
| 1 | **Invariance** | 0.95 | Laws must be the same in all coordinate systems | 1905 SR paper; 1915 GR; Norton (1984) |
| 2 | **Unity** | 0.90 | Unify disparate phenomena under one framework | 30-year unified field theory pursuit; Pais (1982) |
| 3 | **Simplicity** | 0.85 | Minimize assumptions without losing empirical adequacy | Spencer Lecture (1933); Autobiographical Notes (1949) |
| 4 | **Physical Reality** | 0.80 | Objective reality exists independent of observation | EPR paper (1935); Einstein-Born Letters |
| 5 | **Causal Continuity** | 0.75 | Prefer local, continuous causation over action-at-distance | Howard (1985) on separability; field theory preference |
| 6 | **Mathematical Beauty** | 0.70 | Mathematical elegance guides physical truth | Spencer Lecture (1933); van Dongen (2010) |
| 7 | **Empirical Grounding** | 0.65 | Theories must connect to observable phenomena | GR predictions (1915); Geometry and Experience (1921) |
| 8 | **Thought Experiment** | 0.60 | Gedankenexperiment as a primary methodology | Light-beam chase (age 16); elevator (1907); Norton (1991) |

## Career Periods (Temporal Dynamics)

Einstein's taste **evolved** over his career. The system adjusts axis weights per period:

| Period | Years | Dominant Axes | What Changed |
|--------|-------|---------------|-------------|
| Early Revolutionary | 1900–1905 | Empirical grounding, Thought experiment, Simplicity | Patent office years; driven by physical intuition |
| General Relativity | 1906–1915 | Invariance, Unity, Causal continuity | General covariance becomes paramount |
| Quantum Debates | 1916–1935 | Physical reality, Causal continuity, Math beauty | Solvay debates; EPR paper; methodology shift begins |
| Unified Field Theory | 1936–1955 | Unity, Mathematical beauty, Simplicity | Mathematical strategy dominates; increasing isolation |

## Quick Start

### Installation

```bash
# Clone or navigate to the project
cd EinsteinResearchTaste

# Install (requires Python 3.10+)
pip install -e ".[dev]"

# Fetch historical data from online sources
einstein-taste fetch-data

# Verify installation
einstein-taste info
```

### Set Up API Key (for LLM evaluation)

```bash
# Option 1: Environment variable
export ANTHROPIC_API_KEY="your-key-here"

# Option 2: Copy the example file
cp .env.example .env
# Then edit .env with your key
```

Without an API key, you can still run the offline demo:
```bash
python scripts/run_demo_offline.py
```

### CLI Usage

```bash
# Evaluate a single theory
einstein-taste evaluate "A theory unifying gravity and electromagnetism through geometric means"

# Evaluate at a specific year (temporal cutoff)
einstein-taste evaluate "quantum field theory" --cutoff-year 1935

# Rank multiple candidates
einstein-taste rank "unified field theory" "probabilistic quantum mechanics" "hidden variable theory"

# Compare two theories
einstein-taste compare "special relativity" "Lorentz ether theory"

# Run benchmark suite
einstein-taste benchmark

# Output as JSON
einstein-taste evaluate "general covariance" --json-output
```

### Python API Usage

```python
from einstein_taste.core.pipeline import TastePipeline

# Create pipeline with built-in evidence
pipeline = TastePipeline.default()

# Evaluate a theory
result = pipeline.evaluate(
    "A deterministic hidden-variable theory underlying quantum mechanics",
    cutoff_year=1935
)
pipeline.print_evaluation(result)

# Rank multiple candidates
ranked = pipeline.rank_candidates([
    "Unified field theory combining gravity and electromagnetism",
    "Probabilistic quantum theory with observer-dependent reality",
    "Continuous field theory with strict locality",
], cutoff_year=1945)

# Compare two theories
comparison = pipeline.compare(
    "General relativity with general covariance",
    "Nordstrom's scalar gravity theory",
    cutoff_year=1915
)
```

### Claude Code Skill

```python
from einstein_taste.skills.taste_skill import EinsteinTasteSkill

skill = EinsteinTasteSkill()
result = skill.evaluate_taste(
    "A theory of quantum gravity preserving general covariance",
    cutoff_year=1950
)
print(result)
```

## Project Structure

```
EinsteinResearchTaste/
├── einstein_taste/                 # Main Python package
│   ├── config/
│   │   └── settings.py             # 8 taste axes, 4 periods, model config
│   ├── core/
│   │   ├── evidence.py             # Evidence data model + store + filtering
│   │   ├── retriever.py            # RAG retrieval (keyword + semantic)
│   │   ├── evaluator.py            # LLM-based axis evaluation + prompt engineering
│   │   ├── taste_model.py          # Scoring model + weighted aggregation
│   │   └── pipeline.py             # End-to-end orchestration
│   ├── data/
│   │   ├── seed_evidence.py        # 16 built-in evidence records
│   │   ├── fetcher.py              # Fetch data from Wikipedia, SEP, etc.
│   │   ├── loader.py               # Load/save evidence stores
│   │   ├── raw/                    # Raw fetched data (JSON)
│   │   └── processed/              # Processed evidence (JSON)
│   ├── evaluation/
│   │   └── benchmark.py            # 6 benchmark cases + metrics
│   ├── agents/
│   │   └── taste_agent.py          # Conversational agent interface
│   ├── skills/
│   │   └── taste_skill.py          # Claude Code skill wrapper
│   ├── utils/
│   │   └── formatting.py           # Output formatting utilities
│   └── cli.py                      # Command-line interface
├── tests/                          # 18 tests (all passing)
├── scripts/
│   ├── fetch_data.py               # Data fetching script
│   ├── run_demo_offline.py         # Offline demo (no API key needed)
│   └── enrich_evidence.py          # Add evidence from web sources
├── docs/
│   ├── literature_review.docx      # 44-reference literature review
│   └── project_proposal.docx       # Technical proposal document
├── .claude/skills/einstein-taste/
│   └── SKILL.md                    # Claude Code skill definition
├── pyproject.toml                  # Project configuration
└── README.md                       # This file
```

## Understanding the Output

When you evaluate a theory, you get:

```
======================================================================
EINSTEIN RESEARCH TASTE EVALUATION
======================================================================

Candidate: A unified geometric framework combining gravity and EM...
Cutoff Year: 1930
Active Period: quantum_debates

Overall Score: +0.522 (confidence: 0.50)

--- Taste Axis Scores ---
  unity                     +1.000 (conf: 0.70) [EVIDENCE]    <-- Evidence-based
    Evidence-based: 4 evidence records support this score.
  invariance                +1.000 (conf: 0.70) [EVIDENCE]
  physical_reality          -0.100 (conf: 0.30) [INFERRED]    <-- Model inference
    Inferred: No direct evidence found.

--- Evidence-Based Assessment ---
Based on 5 evidence-grounded axis scores.

--- Model Inference (NOT historically grounded) ---
3 axis scores are model inferences.

--- Caveats ---
  ! This is a mock evaluation for demonstration purposes.
```

- **[EVIDENCE]** = Score is grounded in specific historical sources
- **[INFERRED]** = Score is the model's inference, not directly supported
- **Confidence** = How much evidence supports the score (0.0 to 1.0)
- **Caveats** = Limitations and warnings

## Requirements

- **Python** >= 3.10
- **API Key** (optional): Anthropic (`ANTHROPIC_API_KEY`) or OpenAI (`OPENAI_API_KEY`)
- Without an API key, the offline demo still works (uses keyword-based mock scoring)

## Key References

This system is grounded in extensive historical scholarship:

- Holton, G. (1973). *Thematic Origins of Scientific Thought*
- Pais, A. (1982). *Subtle is the Lord*
- Howard, D. (2004). "Einstein's Philosophy of Science" (Stanford Encyclopedia of Philosophy)
- van Dongen, J. (2010). *Einstein's Unification*
- Fine, A. (1986). *The Shaky Game*
- Norton, J. (1984). "How Einstein Found His Field Equations"
- Tong, J. et al. (2026). "AI Can Learn Scientific Taste" (arXiv:2603.14473)

See `docs/literature_review.docx` for the full 44-reference review.

## License

MIT
