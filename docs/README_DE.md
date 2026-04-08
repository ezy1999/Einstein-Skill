**🌐 Sprache:** [中文 (Standard)](../README.md) | [English](./README_EN.md) | [日本語](./README_JA.md) | [Francais](./README_FR.md) | [Deutsch](#)

---

# Einstein-Skill: Einsteins Forschungsgeschmack-Modellierungssystem

> **Evidenzbasierte Modellierung von Albert Einsteins wissenschaftlichem Forschungsgeschmack.**
> Bewerten, ordnen und erklaren Sie, wie Einstein wissenschaftliche Theorien beurteilt hatte.

## Was ist das?

Dieses System modelliert Einsteins **Forschungsgeschmack** - seine dokumentierten Praferenzen fur bestimmte Arten wissenschaftlicher Theorien.

- *"Wie hatte Einstein die Quantenfeldtheorie im Jahr 1935 bewertet?"*
- *"Zwischen verborgenen Variablen und der Kopenhagener Deutung - was hatte Einstein bevorzugt?"*

**Dies ist KEIN Rollenspiel.** Jede Bewertung basiert auf historischen Belegen aus Einsteins Arbeiten, Briefen, Vorlesungen und wissenschaftlichen Analysen.

## Hauptmerkmale

- **8 Geschmachsachsen** aus historischer Forschung (Holton, Howard, Pais, van Dongen)
- **33 Belege** aus Primar- und Sekundarquellen
- **Zeitlicher Grenzwert** - Einstein zu jedem Zeitpunkt zwischen 1900 und 1955 bewerten
- **Trennung Beleg/Schlussfolgerung** - jede Bewertung verweist auf spezifische historische Quellen
- **RAG-Pipeline** - abruferweiterte Generierung

## Die 8 Geschmachsachsen

| # | Achse | Gewicht | Bedeutung |
|---|-------|---------|-----------|
| 1 | **Invarianz** | 0.95 | Gesetze mussen in allen Koordinatensystemen gelten |
| 2 | **Einheit** | 0.90 | Verschiedene Phanomene unter einem Rahmen vereinen |
| 3 | **Einfachheit** | 0.85 | Annahmen minimieren |
| 4 | **Physische Realitat** | 0.80 | Objektive Realitat existiert unabhangig von der Beobachtung |
| 5 | **Kausale Kontinuitat** | 0.75 | Lokale, kontinuierliche Kausalitat bevorzugen |
| 6 | **Mathematische Schonheit** | 0.70 | Eleganz als Wegweiser zur Wahrheit |
| 7 | **Empirische Verankerung** | 0.65 | Theorien mussen an Beobachtbares anknupfen |
| 8 | **Gedankenexperiment** | 0.60 | Gedankenexperiment als primare Methodik |

## Schnellstart

```bash
git clone https://github.com/ezy1999/Einstein-Skill.git
cd Einstein-Skill
pip install -e ".[dev]"
einstein-taste fetch-data

export ANTHROPIC_API_KEY="ihr-schlussel"
# oder Offline-Demo ausfuhren
python scripts/run_demo_offline.py
```

## Voraussetzungen

- Python >= 3.10
- API-Schlussel (optional): Anthropic oder OpenAI

## Lizenz

MIT
