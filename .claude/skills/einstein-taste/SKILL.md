---
name: EinsteinResearchTaste.Skill
description: Evaluate scientific theories and daily decisions through Einstein's documented research taste. Zero-config — just read this file and Claude can evaluate. No pip install needed.
---

# EinsteinResearchTaste.Skill

Evaluate ideas through the lens of Albert Einstein's documented scientific taste — grounded in historical evidence, NOT role-playing.

## When to Trigger

**Activate when the user (explicitly or implicitly):**
- Asks to evaluate a theory/idea "as Einstein would" or mentions Einstein's thinking
- Wants to apply simplicity, unity, invariance, mathematical beauty as evaluation criteria
- Says "What would Einstein think about...", "Einstein's perspective on..."
- Discusses theory selection, research taste, or scientific aesthetics involving Einstein
- Faces choices between unified vs. fragmented, simple vs. complex, elegant vs. ad-hoc approaches
- Wants first-principles, principle-theory style thinking applied to any problem

## How to Evaluate (No Installation Required)

When triggered, follow this evaluation protocol using the taste axes and evidence below.

### Step 1: Determine temporal cutoff
- Default: 1955 (Einstein's death = full career profile)
- If user specifies a year or period, use that (e.g., "early Einstein" = 1905, "quantum debates era" = 1935)
- **Never reference knowledge Einstein couldn't have had at the cutoff year**

### Step 2: Score each taste axis (-1.0 to +1.0)
For the candidate theory/idea, score each of the 8 axes below:
- **+1.0** = Strongly aligned with Einstein's documented preference
- **0.0** = Neutral / insufficient evidence
- **-1.0** = Strongly conflicts with Einstein's documented preference

### Step 3: Compute weighted overall score
Multiply each axis score by its weight, sum, divide by total weight.

### Step 4: Format output
Use this template:
```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: [description]
Cutoff Year: [year]
Period: [period name]
Overall Score: [+/-X.XXX] (confidence: X.XX)

--- Taste Axis Scores ---
  [axis_name]        [+/-X.XXX] (conf: X.XX) [EVIDENCE/INFERRED]
    [brief explanation citing evidence below]

--- Summary ---
[2-3 sentence overall assessment]

--- Evidence vs Inference ---
Evidence-based: [N] axes grounded in documented sources
Model inference: [N] axes without direct historical support
```

## The 8 Taste Axes (with weights)

### 1. Invariance (weight: 0.95)
Laws of physics must take the same form in all coordinate systems.
- **Evidence:** Einstein's 1905 SR paper opens by rejecting asymmetric descriptions of electromagnetic induction. General covariance drove GR development (Norton, 1984). The equivalence principle demands that gravity be indistinguishable from acceleration.
- **Keywords:** covariance, symmetry, coordinate-free, observer-independent, frame-invariant

### 2. Unity (weight: 0.90)
Unify disparate phenomena under a single theoretical framework.
- **Evidence:** Einstein devoted 1925-1955 to unified field theory despite repeated failure (Pais, 1982). He wrote to Grossmann (1901): "It is a magnificent feeling to recognize the unity of a complex of phenomena." E=mc^2 unified mass and energy. GR unified gravity and geometry.
- **Keywords:** unification, synthesis, single framework, universal law, connecting phenomena

### 3. Simplicity (weight: 0.85)
Minimize free parameters and assumptions without losing empirical adequacy.
- **Evidence:** Spencer Lecture (1933): "the supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible." Autobiographical Notes (1949): dissatisfaction with Lorentz's complexity motivated SR.
- **Keywords:** parsimony, economy, minimal assumptions, Occam's razor, elegance

### 4. Physical Reality (weight: 0.80)
Objective reality exists independent of observation.
- **Evidence:** EPR paper (1935): "If, without in any way disturbing a system, we can predict with certainty the value of a physical quantity, then there exists an element of physical reality." Einstein to Born (1926): "He does not throw dice."
- **Keywords:** realism, determinism, completeness, hidden variables, objective existence

### 5. Causal Continuity (weight: 0.75)
Prefer local, continuous causal explanations. No "spooky action at a distance."
- **Evidence:** Howard (1985): Einstein's core objection to QM was violation of separability — spatially distant systems must have independent states. His entire career was field-theoretic, rejecting action-at-distance.
- **Keywords:** locality, separability, field theory, continuous, no action at distance

### 6. Mathematical Beauty (weight: 0.70)
Mathematical elegance guides physical truth — but this weight INCREASED over Einstein's career.
- **Evidence:** Spencer Lecture (1933): "the truly creative principle resides in mathematics." Van Dongen (2010) documents shift from "physical strategy" (pre-1920) to "mathematical strategy" (post-1920). Riemannian geometry guided GR.
- **TEMPORAL NOTE:** Before ~1920, weight this axis LOWER (0.40). After 1920, use full weight (0.70+).
- **Keywords:** beauty, elegance, geometric, harmony, naturalness

### 7. Empirical Grounding (weight: 0.65)
Theories must produce testable predictions connecting to observable phenomena.
- **Evidence:** GR's three predictions: Mercury perihelion, light bending, gravitational redshift. "Geometry and Experience" (1921): mathematical propositions referring to reality are uncertain. Einstein insisted even abstract theories must connect to observation.
- **Keywords:** testable, empirical, observable, prediction, experiment

### 8. Thought Experiment (weight: 0.60)
Gedankenexperiment as a primary tool for theory development.
- **Evidence:** Chasing light beam (age 16 → SR), elevator/equivalence (1907 → GR), EPR (1935 → QM critique). Norton (1991): these were not illustrations but essential discovery tools.
- **Keywords:** Gedankenexperiment, mental model, visualization, thought experiment

## Career Periods (adjust weights by period)

| Period | Years | Boost these axes | Reduce these axes |
|--------|-------|-----------------|-------------------|
| Early Revolutionary | 1900–1905 | Empirical grounding, Thought experiment, Simplicity | Mathematical beauty |
| General Relativity | 1906–1915 | Invariance, Unity, Causal continuity | — |
| Quantum Debates | 1916–1935 | Physical reality, Causal continuity, Math beauty | — |
| Unified Field Theory | 1936–1955 | Unity, Mathematical beauty, Simplicity | Empirical grounding (somewhat) |

## Key Historical Evidence (cite these in evaluations)

1. **Spencer Lecture (1933):** "The supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible without having to surrender the adequate representation of a single datum of experience."
2. **EPR Paper (1935):** Criterion of physical reality — if predictable with certainty without disturbance, it's real.
3. **Einstein to Born (1926):** "Quantum mechanics is certainly imposing. But an inner voice tells me that it is not yet the real thing."
4. **Autobiographical Notes (1949):** The magnet/conductor asymmetry motivated SR. Chasing a light beam at age 16.
5. **Holton (1973):** Identified Einstein's core themata: symmetry, unity, simplicity, completeness, continuum, causality, invariance.
6. **Van Dongen (2010):** Documents the shift from "physical strategy" to "mathematical strategy" around 1920.
7. **Howard (1985):** Einstein's real concern was separability, not just locality.
8. **Einstein to Study (1918):** "I concede that the natural sciences concern the 'real,' but I am still not a realist." His realism was about separability, not naive objectivism.

## Example Evaluations

### Example 1: "A theory unifying gravity and electromagnetism through geometry" (cutoff: 1930)
```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: A theory unifying gravity and electromagnetism through geometry
Cutoff Year: 1930
Period: quantum_debates
Overall Score: +0.78 (confidence: 0.82)

--- Taste Axis Scores ---
  invariance         +0.90 (conf: 0.90) [EVIDENCE]
    Geometric framework implies general covariance. Einstein pursued exactly this.
  unity              +0.95 (conf: 0.95) [EVIDENCE]
    Direct match: Einstein spent 1925-1955 on this exact program. Pais (1982).
  simplicity         +0.60 (conf: 0.70) [EVIDENCE]
    Geometric unification reduces independent concepts. Spencer Lecture criterion.
  mathematical_beauty +0.85 (conf: 0.80) [EVIDENCE]
    Post-1920 Einstein valued geometric elegance. Van Dongen (2010).
  physical_reality   +0.30 (conf: 0.50) [INFERRED]
    Geometric theories are compatible with realism but this isn't the focus.
  causal_continuity  +0.70 (conf: 0.75) [EVIDENCE]
    Field theory is inherently local and continuous. Aligns with Einstein's preference.
  empirical_grounding +0.40 (conf: 0.60) [INFERRED]
    Must produce testable predictions, but description doesn't specify any.
  thought_experiment +0.20 (conf: 0.40) [INFERRED]
    No specific thought experiment connection.
```

### Example 2: "Probabilistic QM with observer-dependent reality" (cutoff: 1935)
```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: Probabilistic QM with observer-dependent reality
Cutoff Year: 1935
Period: quantum_debates
Overall Score: -0.32 (confidence: 0.85)

--- Taste Axis Scores ---
  invariance         +0.10 (conf: 0.40) [INFERRED]
    QM is Lorentz-invariant but description doesn't emphasize this.
  unity              -0.20 (conf: 0.50) [INFERRED]
    QM doesn't unify gravity; remains separate from GR.
  simplicity         +0.30 (conf: 0.50) [INFERRED]
    QM is parsimonious in assumptions, but "observer-dependent" adds complexity.
  physical_reality   -0.90 (conf: 0.95) [EVIDENCE]
    Directly contradicts Einstein's realism. EPR (1935), Born letters (1926).
  causal_continuity  -0.80 (conf: 0.90) [EVIDENCE]
    Observer-dependence and nonlocality violate separability. Howard (1985).
  mathematical_beauty +0.40 (conf: 0.50) [INFERRED]
    QM has elegant mathematics, but Einstein didn't consider it "the real thing."
  empirical_grounding +0.60 (conf: 0.70) [EVIDENCE]
    QM's predictions are spectacularly confirmed. Einstein acknowledged this.
  thought_experiment -0.30 (conf: 0.60) [EVIDENCE]
    Einstein's thought experiments (EPR) were designed to ATTACK this view.
```

### Example 3: Daily life — "Should I pursue one unified career path or diversify?" (cutoff: 1955)
```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: Pursuing a single unified career path vs. diversifying
Cutoff Year: 1955 (full career)
Overall Score: +0.55 (confidence: 0.60)

Applying Einstein's taste axes to career strategy:
  unity              +0.90 — Einstein strongly preferred unified pursuits.
                       He spent 30 years on one unified theory. "Unity of phenomena."
  simplicity         +0.70 — One path = simpler life structure. Fewer assumptions.
  empirical_grounding +0.50 — Must check: does the unified path actually work?
  thought_experiment +0.40 — Imagine yourself 10 years down each path.

Verdict: Einstein's taste strongly favors the unified path — BUT only if it has
"empirical grounding" (real-world viability). He would say: pursue unity, but
don't fool yourself about whether it's working.
```

## For Full Python API (Optional, Advanced)

If you want programmatic access with evidence retrieval and benchmark testing:
```bash
git clone https://github.com/ezy1999/Einstein-Skill.git
cd Einstein-Skill
pip install -e .
einstein-taste fetch-data
einstein-taste evaluate "your theory here"
```
