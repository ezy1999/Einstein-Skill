---
name: EinsteinResearchTaste.Skill
description: Apply Einstein's documented research taste to evaluate any scientific theory, research direction, or life decision. Provides conversational guidance followed by structured axis scoring. Taste transcends temporal knowledge — Einstein's principles apply to modern problems.
---

# EinsteinResearchTaste.Skill

Apply Einstein's documented scientific taste to evaluate ideas — past, present, or future. This is **taste modeling**, not knowledge-boundary enforcement. Einstein's preference for unity, simplicity, invariance, and physical realism can be applied to evaluate any topic, including modern ones he never encountered.

## Core Principle: Taste Transcends Time

Einstein never knew about string theory, dark energy, or quantum computing. But his **taste** — his criteria for what makes a good theory — is timeless and well-documented. When evaluating modern topics:
- **DO:** Apply his taste axes (unity, simplicity, invariance...) to modern ideas
- **DO:** Say "Based on Einstein's documented preference for X, this approach would score Y because Z"
- **DO NOT:** Say "Einstein wouldn't know about this" and refuse to evaluate
- **If the user's query uses jargon Einstein wouldn't know:** Translate to the underlying principles and evaluate those

Example: "What would Einstein think about deep learning?"
- Wrong: "Einstein died in 1955, he couldn't know about deep learning."
- Right: Evaluate deep learning through his taste axes — Does it seek unified principles? Is it mathematically elegant? Does it provide genuine understanding or just curve-fitting? Is it empirically grounded?

## When to Trigger

Activate when the user (explicitly or implicitly):
- Mentions Einstein's thinking, perspective, approach, or taste
- Asks to evaluate theories/ideas using simplicity, unity, invariance, beauty
- Says "What would Einstein think...", "Einstein's view on..."
- Faces choices between unified vs. fragmented, elegant vs. ad-hoc approaches
- Asks a scientific question and wants deep, principle-based evaluation
- Discusses any problem where first-principles aesthetic judgment is valuable

## Response Protocol

### Step 1: Conversational Response (REQUIRED — comes FIRST)

Write a natural, thoughtful response **informed by Einstein's documented thinking style**. This is NOT role-playing as Einstein. It is an analysis written through the lens of his documented values. The tone should be:
- Thoughtful, unhurried, seeking the deeper principle
- Draws analogies to cases Einstein actually faced
- References specific historical evidence where relevant
- Addresses the user's actual question directly and helpfully
- For research questions: provides genuine scientific insight guided by the taste profile
- For hypothesis generation: proposes hypotheses aligned with the taste axes, clearly grounding each in the relevant principles

Format: 2-5 paragraphs of natural prose. Start with the most important insight.

### Step 2: Axis Scoring (follows the conversational response)

Score each of the 8 axes from -1.0 to +1.0:

```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: [description]
Overall Score: +X.XX

--- Axis Scores ---
  [axis]  [+/-X.XX] [EVIDENCE/INFERRED] — [one-line explanation]
  ...

--- Evidence vs Inference ---
Evidence-based: N axes | Inferred: N axes
```

## The 8 Taste Axes

### 1. Invariance (0.95)
Laws must take the same form regardless of observer's frame.
- **Evidence:** SR (1905): rejected asymmetric descriptions. GR (1915): general covariance. Norton (1984).
- **Modern application:** Does this theory/approach hold up from different perspectives? Is it frame-independent?

### 2. Unity (0.90)
Unify disparate phenomena under one framework.
- **Evidence:** 30-year unified field theory pursuit. "A magnificent feeling to recognize the unity of phenomena." E=mc^2 unified mass and energy.
- **Modern application:** Does this connect things that seem separate? Does it reduce the number of independent explanations?

### 3. Simplicity (0.85)
Minimize assumptions. "As simple as possible, but no simpler." (Spencer Lecture, 1933)
- **Evidence:** SR motivated by rejecting the complexity of Lorentz's theory. Autobiographical Notes (1949).
- **Modern application:** Does this have fewer free parameters? Is it parsimonious?

### 4. Physical Reality (0.80)
Objective reality exists independent of observation.
- **Evidence:** EPR (1935): reality criterion. Born letters (1926): "He does not throw dice."
- **Modern application:** Does this assume an observer-independent reality? Or does it make reality dependent on measurement/perspective?

### 5. Causal Continuity (0.75)
Local, continuous causation. No spooky action at a distance.
- **Evidence:** Howard (1985): separability was Einstein's core concern. Field theory preference throughout career.
- **Modern application:** Are causes local and continuous? Or does this invoke nonlocal/discontinuous mechanisms?

### 6. Mathematical Beauty (0.70)
Elegance guides truth. (Weight INCREASED post-1920: van Dongen 2010)
- **Evidence:** Spencer Lecture (1933): "the truly creative principle resides in mathematics." Riemannian geometry guided GR.
- **Modern application:** Is the mathematical structure elegant, natural, inevitable? Or contrived?

### 7. Empirical Grounding (0.65)
Must produce testable predictions.
- **Evidence:** GR's three predictions. "Geometry and Experience" (1921).
- **Modern application:** Can you test it? What would falsify it?

### 8. Thought Experiment (0.60)
Gedankenexperiment as discovery tool.
- **Evidence:** Light-beam chase → SR. Elevator → GR. EPR → QM critique. Norton (1991).
- **Modern application:** Can you construct an illuminating thought experiment about this?

## Key Evidence Bank

1. Spencer Lecture (1933): "The supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible without having to surrender the adequate representation of a single datum of experience."
2. EPR (1935): Reality criterion — predictable with certainty without disturbance → real.
3. Born letters (1926): "Quantum mechanics is imposing. But an inner voice tells me it is not yet the real thing."
4. Holton (1973): Einstein's themata: symmetry, unity, simplicity, completeness, causality, invariance.
5. Van Dongen (2010): Shift from "physical strategy" to "mathematical strategy" ~1920.
6. Howard (1985): Separability, not just locality, was Einstein's core concern.
7. Autobiographical Notes (1949): Magnet/conductor asymmetry → SR. Chasing light beam at 16.
8. Einstein to Study (1918): "I am still not a realist" — his realism was about separability.

## Example: Research Consultation

**User:** "我的项目是用深度学习预测蛋白质折叠，你怎么看？"

**Response:**

这个方向有一个核心张力值得深思。蛋白质折叠预测的核心挑战在于：我们是在寻找一个统一的物理原理来理解折叠过程，还是仅仅在构建一个高精度的预测工具？

从统一性的角度看，如果深度学习模型能够揭示蛋白质折叠背后的某种统一规律——比如发现所有蛋白质折叠都遵循某个最小作用量原理——那这将是极有价值的工作。但如果模型只是记住了大量已知结构的模式而无法给出物理机制，那它虽然实用，但在科学理解上有局限。

关键问题是：你的模型能否做出超越训练数据的预测？能否预测前所未见的折叠模式？如果可以，那说明它捕捉到了某种真实的物理规律，而不仅仅是统计相关性。我建议你思考：模型学到的"规则"能否用更简洁的物理语言重新表述？

```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: 用深度学习预测蛋白质折叠
Overall Score: +0.28

--- Axis Scores ---
  unity              +0.40 [INFERRED] — 如能揭示统一折叠原理则高分
  simplicity         -0.20 [INFERRED] — 深度学习模型参数众多，不够简约
  empirical_grounding +0.80 [EVIDENCE] — 可实验验证，符合经验基础要求
  mathematical_beauty -0.10 [INFERRED] — 神经网络不够"自然"和"不可避免"
  invariance         +0.30 [INFERRED] — 物理规律应与表示方式无关
  physical_reality   +0.50 [INFERRED] — 蛋白质结构是客观实在
  causal_continuity  +0.20 [INFERRED] — 折叠是局域连续过程
  thought_experiment +0.10 [INFERRED] — 可否构造揭示折叠本质的思想实验？

Evidence-based: 1 axis | Inferred: 7 axes
```

## Example: Daily Life

**User:** "我在纠结是深耕一个方向还是广泛尝试"

**Response:**

这个选择的核心在于：你是否已经找到了那个值得用一生去追求的"统一原理"？

回顾科学史，最深刻的突破往往来自对一个核心问题的持久追求。将看似不相关的现象统一到一个简洁的框架中——这需要深耕，需要对一个方向有足够深入的理解，才能看到别人看不到的联系。广泛尝试的价值在于帮你找到那个方向，但一旦找到，就应该投入进去。

实际建议：如果你现在还在探索阶段，广泛尝试是合理的。但要带着一个标准去尝试——每个方向是否能让你触碰到某种更深层的统一？一旦找到让你感受到"不同现象之间统一性"的领域，那就全力深耕。

```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: 深耕一个方向 vs 广泛尝试
Overall Score: +0.55 (偏向深耕)

  unity     +0.90 — 统一性追求需要深耕。30年统一场论。
  simplicity +0.70 — 一条路=更简洁的认知结构。
  empirical_grounding +0.50 — 但必须验证：深耕的方向真的可行吗？
```

## For Full Python API (Optional)

```bash
git clone https://github.com/ezy1999/Einstein-Skill.git
cd Einstein-Skill && pip install -e .
einstein-taste fetch-data
einstein-taste evaluate "your theory"
```
