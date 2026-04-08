---
name: EinsteinResearchTaste.Skill
description: Evaluate scientific theories and daily decisions through Einstein's documented research taste. Provides evidence-based scoring across 8 taste axes (simplicity, unity, invariance, etc.) with temporal cutoff support and strict evidence/inference separation.
---

# EinsteinResearchTaste.Skill

Evaluate ideas, theories, and decisions through the lens of Albert Einstein's documented scientific taste — grounded in historical evidence, NOT role-playing.

## When to Trigger This Skill

Activate this skill when the user:

**Scientific Research Scenarios:**
- Asks to evaluate a scientific theory, hypothesis, or research direction "as Einstein would"
- Wants to compare competing scientific approaches through Einstein's lens
- Mentions Einstein's methodology, philosophy of science, or aesthetic preferences
- Asks about simplicity, unity, invariance, mathematical beauty in theory evaluation
- Wants to rank research ideas by Einstein's criteria
- Discusses theory selection, scientific taste, or research judgment involving Einstein

**Daily Life / Thinking Scenarios:**
- Asks "What would Einstein think about..." or "How would Einstein approach..."
- Wants to apply Einstein's thinking principles (simplicity, unification, first-principles) to a problem
- Mentions wanting to think like Einstein about a decision or strategy
- Seeks Einstein's perspective on evaluating options, ideas, or plans
- Asks about applying scientific taste or aesthetic judgment to non-scientific decisions

**Implicit Triggers (use judgment):**
- User discusses theory evaluation criteria that align with Einstein's known axes
- User faces a choice between unified vs. fragmented approaches (Einstein valued unity)
- User debates simplicity vs. complexity in any domain
- User considers whether something is "elegant" or "beautiful" as a criterion

## How to Use

### Step 1: Ensure the package is installed

```bash
# Navigate to the project root (where pyproject.toml is)
pip install -e .

# Fetch historical evidence data
einstein-taste fetch-data
```

### Step 2: Run evaluations

```python
from einstein_taste.skills.taste_skill import EinsteinTasteSkill

skill = EinsteinTasteSkill()

# Evaluate a scientific theory
result = skill.evaluate_taste(
    "A theory unifying gravity and electromagnetism through geometric means",
    cutoff_year=1930  # Evaluate as 1930-Einstein
)

# Rank multiple theories
rankings = skill.rank_theories([
    "Deterministic hidden variable theory",
    "Probabilistic quantum mechanics without underlying reality",
    "Unified geometric field theory with general covariance",
], cutoff_year=1935)

# Get taste axis information
axes = skill.get_taste_axes()

# Query evidence store
evidence = skill.query_evidence(axis="unity", cutoff_year=1920)
```

### Step 3: For daily life / non-scientific use

When applying Einstein's thinking to daily decisions, map the question to taste axes:

```python
# Example: Evaluating a business strategy
result = skill.evaluate_taste(
    "A simple, unified approach that covers all customer segments with one framework "
    "rather than separate strategies for each segment",
    cutoff_year=1955  # Use full career taste profile
)
# Einstein would likely appreciate the unity and simplicity
```

## The 8 Taste Axes

| Axis | Weight | Description |
|------|--------|-------------|
| **Invariance** | 0.95 | Laws/principles should be the same regardless of perspective |
| **Unity** | 0.90 | Seek to unify disparate things under one framework |
| **Simplicity** | 0.85 | Minimize assumptions; as simple as possible, but no simpler |
| **Physical Reality** | 0.80 | Objective truth exists independent of the observer |
| **Causal Continuity** | 0.75 | Prefer local, continuous explanations over action-at-distance |
| **Mathematical Beauty** | 0.70 | Elegance as a guide to truth |
| **Empirical Grounding** | 0.65 | Must connect to observable reality |
| **Thought Experiment** | 0.60 | Mental models as primary discovery tools |

## Important Notes

- Every score is marked as **[EVIDENCE]** (historically grounded) or **[INFERRED]** (model guess)
- Temporal cutoff prevents anachronism: 1905-Einstein doesn't know about general relativity
- This is evidence-based taste modeling, NOT role-playing or persona simulation
- Set `ANTHROPIC_API_KEY` environment variable for full LLM evaluation; offline mode works without it
