**🌐 Language / 语言选择：** [中文（默认）](#) | [English](./docs/README_EN.md) | [日本語](./docs/README_JA.md) | [Français](./docs/README_FR.md) | [Deutsch](./docs/README_DE.md)

---

# Einstein-Skill：爱因斯坦科研品味建模系统

> **基于史料证据的爱因斯坦科研品味计算建模**
> 评估、排序和解释爱因斯坦会如何评价候选科学理论——基于历史证据，而非角色扮演。

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![Tests](https://img.shields.io/badge/tests-18%20passed-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)]()

---

## 这是什么？

本系统对爱因斯坦的**科研品味（Research Taste）**进行建模——即他对不同类型科学理论的偏好。它能回答如下问题：

- *"1935年的爱因斯坦会如何评价量子场论？"*
- *"在隐变量理论和哥本哈根量子力学之间，爱因斯坦会更倾向哪个？"*
- *"爱因斯坦对数学美感的重视如何随职业生涯演变？"*

**这不是角色扮演。** 每一项评估都以历史证据为基础——来自爱因斯坦的发表论文、书信、演讲，以及学者对其方法论的分析。系统会明确标注哪些是基于证据的评分，哪些是模型推断。

## 核心特性

| 特性 | 说明 |
|------|------|
| **8个品味轴** | 源自 Holton 的主题分析、Howard 的哲学研究等学术成果 |
| **33条证据记录** | 一手史料（爱因斯坦著作）+ 二手学术分析 |
| **时间截止机制** | 防止历史穿越，可评估1900-1955年间任意时点的爱因斯坦 |
| **证据/推断分离** | 每个评分都追溯到具体历史来源 |
| **RAG管道** | 检索增强生成，将评估锚定在真实证据上 |
| **6个基准测试** | 含难度分层（简单/中等/困难） |
| **多种接口** | CLI命令行 + Python API + Claude Code Skill |

## 工作原理

```
用户查询                    证据库 (33条记录)
    |                               |
    v                               v
[1. 证据检索] ──────────> 关键词/语义匹配
    |                               |
    v                               v
[2. LLM评估]              检索到的证据作为上下文
    |                     (Claude/GPT-4 结构化提示)
    v
[3. 轴评分]               每个轴的评分+证据链接
    |                      按职业时期加权
    v
[4. 输出]                 排名结果+解释
                           证据 vs 推断 清晰标注
```

## 8个品味轴

| # | 品味轴 | 权重 | 含义 | 关键证据 |
|---|--------|------|------|---------|
| 1 | **不变性** | 0.95 | 物理定律在所有坐标系中形式相同 | 1905狭义相对论; 1915广义相对论; Norton (1984) |
| 2 | **统一性** | 0.90 | 将不同现象统一到单一框架 | 30年统一场论追求; Pais (1982) |
| 3 | **简单性** | 0.85 | 以最少假设充分表达经验 | Spencer演讲 (1933); 自传笔记 (1949) |
| 4 | **物理实在性** | 0.80 | 客观实在独立于观测存在 | EPR论文 (1935); Einstein-Born书信 |
| 5 | **因果连续性** | 0.75 | 偏好局域、连续的因果关系 | Howard (1985) 论可分离性 |
| 6 | **数学美感** | 0.70 | 数学优雅引导物理真理 | Spencer演讲 (1933); van Dongen (2010) |
| 7 | **经验基础** | 0.65 | 理论必须连接可观测现象 | 广义相对论三大预言; 几何与经验 (1921) |
| 8 | **思想实验** | 0.60 | Gedankenexperiment 作为核心方法 | 追光实验; 电梯实验; Norton (1991) |

## 职业时期（时间动态）

爱因斯坦的品味**随时间演变**。系统按时期调整轴权重：

| 时期 | 年份 | 主导轴 | 变化 |
|------|------|--------|------|
| 早期革命 | 1900–1905 | 经验基础, 思想实验, 简单性 | 专利局时期；物理直觉主导 |
| 广义相对论 | 1906–1915 | 不变性, 统一性, 因果连续性 | 广义协变性成为最高原则 |
| 量子争论 | 1916–1935 | 物理实在性, 因果连续性, 数学美感 | Solvay辩论; EPR论文; 方法论转变 |
| 统一场论 | 1936–1955 | 统一性, 数学美感, 简单性 | 数学策略主导; 日益脱离主流 |

## 快速开始

### 安装

```bash
git clone https://github.com/ezy1999/Einstein-Skill.git
cd Einstein-Skill
pip install -e ".[dev]"       # 安装项目
einstein-taste fetch-data      # 获取历史数据
einstein-taste info            # 验证安装
```

### 设置 API Key（可选，用于 LLM 评估）

```bash
# 方式一：环境变量
export ANTHROPIC_API_KEY="你的密钥"

# 方式二：复制配置文件
cp .env.example .env
# 编辑 .env 填入你的密钥
```

没有 API Key 也能运行离线演示：
```bash
python scripts/run_demo_offline.py
```

### 命令行使用

```bash
# 评估单个理论
einstein-taste evaluate "统一引力和电磁力的几何理论"

# 指定年份（时间截止）
einstein-taste evaluate "量子场论" --cutoff-year 1935

# 排序多个候选理论
einstein-taste rank "统一场论" "概率量子力学" "隐变量理论"

# 比较两个理论
einstein-taste compare "狭义相对论" "洛伦兹以太理论"

# 运行基准测试
einstein-taste benchmark
```

### Python API 使用

```python
from einstein_taste.core.pipeline import TastePipeline

pipeline = TastePipeline.default()

# 评估
result = pipeline.evaluate(
    "确定论的量子力学隐变量理论",
    cutoff_year=1935
)
pipeline.print_evaluation(result)

# 排序
ranked = pipeline.rank_candidates([
    "统一引力和电磁力的几何框架",
    "观测者依赖的概率量子理论",
], cutoff_year=1945)
```

### 作为 Claude Code Skill 使用

**快速模式（零配置，推荐）：**

将 `.claude/skills/einstein-taste/SKILL.md` 拷贝到你的 Claude Code 项目的 `.claude/skills/` 目录下即可。无需 pip install，Claude 直接读取 SKILL.md 中的品味轴定义和证据即可进行评估。

```bash
# 拷贝 skill 文件到你的项目
mkdir -p your-project/.claude/skills/einstein-taste/
cp .claude/skills/einstein-taste/SKILL.md your-project/.claude/skills/einstein-taste/
```

然后在 Claude Code 中直接说：
- "用爱因斯坦的品味评估一下量子引力理论"
- "Einstein would think about this unified approach?"
- "帮我用简单性和统一性原则分析这个方案"

**完整模式（Python API）：**

```python
from einstein_taste.skills.taste_skill import EinsteinTasteSkill

skill = EinsteinTasteSkill()
result = skill.evaluate_taste("通过广义协变性实现的量子引力理论", cutoff_year=1950)
```

## 示例与输出

### 示例1：评估统一场论（科研场景）

**输入：** "通过黎曼几何统一引力和电磁力的理论"（截止年份：1930）

```
EINSTEIN RESEARCH TASTE EVALUATION
═══════════════════════════════════
Candidate: 通过黎曼几何统一引力和电磁力的理论
Cutoff Year: 1930 | Period: quantum_debates
Overall Score: +0.78 (confidence: 0.82)

--- Taste Axis Scores ---
  unity              +0.95 (conf: 0.95) [EVIDENCE]
    爱因斯坦1925-1955年一直追求这个方向。Pais (1982)。
  invariance         +0.90 (conf: 0.90) [EVIDENCE]
    几何框架自然满足广义协变性。Norton (1984)。
  mathematical_beauty +0.85 (conf: 0.80) [EVIDENCE]
    1920年后爱因斯坦转向"数学策略"。van Dongen (2010)。
  causal_continuity  +0.70 (conf: 0.75) [EVIDENCE]
    场论天然是局域连续的。
  simplicity         +0.60 (conf: 0.70) [EVIDENCE]
    几何统一减少了独立概念。Spencer演讲标准。
  empirical_grounding +0.40 (conf: 0.60) [INFERRED]
    需要可检验预言，但描述中未提及。
  physical_reality   +0.30 (conf: 0.50) [INFERRED]
    几何理论与实在论兼容但非重点。
  thought_experiment +0.20 (conf: 0.40) [INFERRED]
    无特定思想实验关联。
```

### 示例2：评估哥本哈根量子力学（科研场景）

**输入：** "概率性量子力学，物理性质在测量前不确定，观测者依赖的实在"（截止：1935）

```
Overall Score: -0.32 (confidence: 0.85)

  physical_reality   -0.90 (conf: 0.95) [EVIDENCE]
    直接矛盾。EPR论文 (1935)，Born书信 (1926)。
  causal_continuity  -0.80 (conf: 0.90) [EVIDENCE]
    违反可分离性。Howard (1985)。
  empirical_grounding +0.60 (conf: 0.70) [EVIDENCE]
    量子力学预言精度极高。爱因斯坦承认这点。
  thought_experiment -0.30 (conf: 0.60) [EVIDENCE]
    爱因斯坦的思想实验(EPR)就是为了攻击这个观点。
```

### 示例3：日常决策——"该走统一路线还是多元化？"

```
Applying Einstein's taste to career strategy:
  unity         +0.90 — 爱因斯坦强烈偏好统一追求。他花30年做一个统一理论。
  simplicity    +0.70 — 一条路 = 更简单的人生结构。
  empirical_grounding +0.50 — 但必须检验：统一路线真的可行吗？

结论：爱因斯坦的品味强烈支持统一路线——但前提是要有"经验基础"
（现实可行性）。他会说：追求统一，但别自欺欺人。
```

### 示例4：方法论选择——"该用简单模型还是复杂模型？"

```
  simplicity    +0.95 — "尽可能简单，但不能更简单了。" Spencer演讲 (1933)。
  empirical_grounding +0.70 — 但简单模型必须能解释数据。
  mathematical_beauty +0.60 — 简单往往更优雅。

结论：从简单模型开始。只在数据迫使你时才增加复杂性。
```

### 理解输出标记

- **[EVIDENCE]** = 有具体历史来源支持的评分
- **[INFERRED]** = 模型推断，无直接证据
- **confidence** = 支持证据的充分程度 (0.0-1.0)
- **Overall Score** 范围 -1.0（强烈冲突）到 +1.0（高度契合）

## 项目结构

```
Einstein-Skill/
├── einstein_taste/            # Python 包
│   ├── config/settings.py     # 品味轴 + 时间段 + 配置
│   ├── core/                  # 证据、检索、评估、评分、管道
│   ├── data/                  # 数据加载、抓取、种子证据
│   ├── evaluation/            # 基准测试
│   ├── agents/                # 对话代理
│   ├── skills/                # Claude Code Skill
│   └── cli.py                 # 命令行工具
├── tests/                     # 18个测试（全通过）
├── scripts/                   # 演示和数据脚本
├── docs/                      # 文献综述 + 项目方案 + 多语言README
└── pyproject.toml             # 项目配置
```

## 环境要求

- **Python** >= 3.10
- **API Key**（可选）：Anthropic 或 OpenAI
- 无 API Key 时可用离线演示

## 主要参考文献

- Holton, G. (1973). *Thematic Origins of Scientific Thought*
- Pais, A. (1982). *Subtle is the Lord*
- Howard, D. (2004). "Einstein's Philosophy of Science" (Stanford Encyclopedia of Philosophy)
- van Dongen, J. (2010). *Einstein's Unification*
- Tong, J. et al. (2026). "AI Can Learn Scientific Taste" (arXiv:2603.14473)

完整44篇引用见 `docs/literature_review.docx`

## 许可证

MIT
