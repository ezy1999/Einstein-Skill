**🌐 Langue :** [中文 (par defaut)](../README.md) | [English](./README_EN.md) | [日本語](./README_JA.md) | [Francais](#) | [Deutsch](./README_DE.md)

---

# Einstein-Skill : Systeme de Modelisation du Gout Scientifique d'Einstein

> **Modelisation computationnelle du gout scientifique d'Albert Einstein basee sur des preuves historiques.**
> Evaluez, classez et expliquez comment Einstein aurait juge des theories scientifiques candidates.

## Qu'est-ce que c'est ?

Ce systeme modelise le **gout de recherche** d'Einstein - ses preferences documentees pour certains types de theories scientifiques.

- *"Comment Einstein aurait-il evalue la theorie quantique des champs en 1935 ?"*
- *"Entre les variables cachees et l'interpretation de Copenhague, que prefererait Einstein ?"*

**Ce n'est PAS du jeu de role.** Chaque evaluation est fondee sur des preuves historiques provenant des articles, lettres et conferences d'Einstein, ainsi que des analyses savantes.

## Caracteristiques

- **8 axes de gout** derives de recherches historiques (Holton, Howard, Pais, van Dongen)
- **33 enregistrements de preuves** de sources primaires et secondaires
- **Coupure temporelle** - evaluez Einstein a n'importe quelle annee entre 1900 et 1955
- **Separation preuves/inferences** - chaque score est trace a des sources historiques
- **Pipeline RAG** - generation augmentee par recuperation

## Les 8 axes de gout

| # | Axe | Poids | Signification |
|---|-----|-------|---------------|
| 1 | **Invariance** | 0.95 | Les lois doivent etre les memes dans tous les systemes de coordonnees |
| 2 | **Unite** | 0.90 | Unifier les phenomenes sous un seul cadre |
| 3 | **Simplicite** | 0.85 | Minimiser les hypotheses |
| 4 | **Realite physique** | 0.80 | La realite objective existe independamment de l'observation |
| 5 | **Continuite causale** | 0.75 | Causalite locale et continue |
| 6 | **Beaute mathematique** | 0.70 | L'elegance comme guide vers la verite |
| 7 | **Ancrage empirique** | 0.65 | Les theories doivent se connecter a l'observable |
| 8 | **Experience de pensee** | 0.60 | Gedankenexperiment comme methodologie principale |

## Demarrage rapide

```bash
git clone https://github.com/ezy1999/Einstein-Skill.git
cd Einstein-Skill
pip install -e ".[dev]"
einstein-taste fetch-data

export ANTHROPIC_API_KEY="votre-cle"
# ou lancez la demo hors ligne
python scripts/run_demo_offline.py
```

## Prerequis

- Python >= 3.10
- Cle API (optionnelle) : Anthropic ou OpenAI

## Licence

MIT
