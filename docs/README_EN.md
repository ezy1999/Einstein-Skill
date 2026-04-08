**🌐 Language:** [中文（默认）](../README.md) | [English](#) | [日本語](./README_JA.md) | [Français](./README_FR.md) | [Deutsch](./README_DE.md)

---

# Einstein-Skill: Einstein Research Taste Modeling System

> **Evidence-based computational modeling of Albert Einstein's scientific research taste.**
> Evaluate, rank, and explain how Einstein would have assessed candidate scientific theories — grounded in historical evidence, not role-playing.

## What Is This?

This system models Einstein's **research taste** — his documented preferences for certain kinds of scientific theories. It answers questions like:

- *"How would Einstein have evaluated quantum field theory in 1935?"*
- *"Between hidden-variable theory and Copenhagen QM, which would Einstein prefer?"*
- *"How did Einstein's taste for mathematical beauty evolve over his career?"*

**This is NOT role-playing.** Every evaluation is grounded in historical evidence from Einstein's papers, letters, lectures, and scholarly analyses. The system marks what is evidence-based vs. model inference.

## Key Features

- **8 Taste Axes** derived from historical scholarship (Holton, Howard, Pais, van Dongen)
- **33 Evidence Records** from primary and secondary sources
- **Temporal Cutoff** — evaluate Einstein at any year from 1900 to 1955
- **Evidence/Inference Separation** — every score traces to specific historical sources
- **RAG Pipeline** — retrieval-augmented generation grounds evaluations in real evidence
- **6 Benchmark Cases** with difficulty stratification
- **CLI + Python API + Claude Code Skill**

## The 8 Taste Axes

| # | Axis | Weight | Meaning |
|---|------|--------|---------|
| 1 | **Invariance** | 0.95 | Laws must hold in all coordinate systems |
| 2 | **Unity** | 0.90 | Unify disparate phenomena under one framework |
| 3 | **Simplicity** | 0.85 | Minimize assumptions without losing empirical adequacy |
| 4 | **Physical Reality** | 0.80 | Objective reality exists independent of observation |
| 5 | **Causal Continuity** | 0.75 | Local, continuous causation over action-at-distance |
| 6 | **Mathematical Beauty** | 0.70 | Elegance as guide to physical truth |
| 7 | **Empirical Grounding** | 0.65 | Theories must connect to observable phenomena |
| 8 | **Thought Experiment** | 0.60 | Gedankenexperiment as primary methodology |

## Quick Start

```bash
git clone https://github.com/ezy1999/Einstein-Skill.git
cd Einstein-Skill
pip install -e ".[dev]"
einstein-taste fetch-data
einstein-taste info

# Optional: set API key for LLM evaluation
export ANTHROPIC_API_KEY="your-key"

# Or run offline demo
python scripts/run_demo_offline.py
```

## Usage

```bash
einstein-taste evaluate "A theory unifying gravity and electromagnetism"
einstein-taste evaluate "quantum field theory" --cutoff-year 1935
einstein-taste rank "unified field theory" "probabilistic QM" "hidden variables"
einstein-taste benchmark
```

## Requirements

- Python >= 3.10
- API Key (optional): Anthropic or OpenAI

## License

MIT
