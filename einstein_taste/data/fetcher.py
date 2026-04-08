"""
Data Fetcher Module
====================

Fetches real historical data about Einstein from publicly available sources:
- Einstein Papers Project (Caltech) metadata
- Wikipedia structured data
- Stanford Encyclopedia of Philosophy
- Project Gutenberg (public domain texts)

All fetched data is stored in raw/ and processed into evidence records.
"""

from __future__ import annotations

import json
import time
import re
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup

from einstein_taste.config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR
from einstein_taste.core.evidence import (
    EvidenceRecord,
    SourceType,
    ConfidenceLevel,
)


class EinsteinDataFetcher:
    """Fetches and processes historical Einstein data from public sources."""

    HEADERS = {
        "User-Agent": "EinsteinResearchTaste/0.1 (academic research project)"
    }
    REQUEST_DELAY = 1.0  # seconds between requests (be polite)

    def __init__(self, raw_dir: Path | None = None, processed_dir: Path | None = None):
        self.raw_dir = raw_dir or RAW_DATA_DIR
        self.processed_dir = processed_dir or PROCESSED_DATA_DIR
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def _get(self, url: str) -> requests.Response | None:
        """Make a polite HTTP GET request."""
        try:
            time.sleep(self.REQUEST_DELAY)
            resp = requests.get(url, headers=self.HEADERS, timeout=30)
            resp.raise_for_status()
            return resp
        except Exception as e:
            print(f"Warning: Failed to fetch {url}: {e}")
            return None

    # ── Wikipedia Data ─────────────────────────────────────────────────────

    def fetch_einstein_wikipedia(self) -> list[dict]:
        """Fetch structured data about Einstein from Wikipedia API."""
        print("Fetching Einstein data from Wikipedia...")

        pages = [
            "Albert_Einstein",
            "Einstein%27s_philosophy_of_science",
            "EPR_paradox",
            "Annus_Mirabilis_papers",
            "Einstein_field_equations",
            "Unified_field_theory",
            "Photoelectric_effect",
            "Brownian_motion",
        ]

        results = []
        for page in pages:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page}"
            resp = self._get(url)
            if resp:
                data = resp.json()
                results.append({
                    "title": data.get("title", page),
                    "extract": data.get("extract", ""),
                    "description": data.get("description", ""),
                    "source_url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
                })

        # Save raw data
        output_path = self.raw_dir / "wikipedia_einstein.json"
        output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Saved {len(results)} Wikipedia entries to {output_path}")
        return results

    # ── Einstein Papers Project ────────────────────────────────────────────

    def fetch_einstein_papers_metadata(self) -> list[dict]:
        """
        Fetch metadata about Einstein's published papers.
        Uses the Einstein Papers Project's public information.
        """
        print("Fetching Einstein Papers Project metadata...")

        # Key papers with metadata (manually curated from public sources)
        papers = [
            {
                "title": "On a Heuristic Point of View Concerning the Production and Transformation of Light",
                "year": 1905, "journal": "Annalen der Physik", "volume": "17",
                "topic": "photoelectric_effect", "significance": "Nobel Prize work",
                "taste_relevance": "Shows Einstein's willingness to challenge established wave theory of light; quantum hypothesis applied to radiation",
            },
            {
                "title": "On the Movement of Small Particles Suspended in Stationary Liquids Required by the Molecular-Kinetic Theory of Heat",
                "year": 1905, "journal": "Annalen der Physik", "volume": "17",
                "topic": "brownian_motion", "significance": "Confirmed molecular reality",
                "taste_relevance": "Demonstrates taste for connecting statistical mechanics to observable phenomena",
            },
            {
                "title": "On the Electrodynamics of Moving Bodies",
                "year": 1905, "journal": "Annalen der Physik", "volume": "17",
                "topic": "special_relativity", "significance": "Foundation of special relativity",
                "taste_relevance": "Motivated by aesthetic dissatisfaction with asymmetry in electromagnetic theory",
            },
            {
                "title": "Does the Inertia of a Body Depend Upon Its Energy Content?",
                "year": 1905, "journal": "Annalen der Physik", "volume": "18",
                "topic": "mass_energy_equivalence", "significance": "E=mc^2",
                "taste_relevance": "Exemplifies drive toward unity - connecting mass and energy",
            },
            {
                "title": "The Foundation of the General Theory of Relativity",
                "year": 1916, "journal": "Annalen der Physik", "volume": "49",
                "topic": "general_relativity", "significance": "Complete GR theory",
                "taste_relevance": "Culmination of invariance principle - general covariance requirement",
            },
            {
                "title": "Cosmological Considerations on the General Theory of Relativity",
                "year": 1917, "journal": "Sitzungsberichte der Preussischen Akademie",
                "topic": "cosmology", "significance": "First application of GR to cosmology",
                "taste_relevance": "Shows unity drive - applying GR to the universe as a whole",
            },
            {
                "title": "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?",
                "year": 1935, "journal": "Physical Review", "volume": "47",
                "topic": "EPR_paradox", "significance": "EPR paper, quantum foundations",
                "taste_relevance": "Clearest expression of realism and locality commitments",
            },
            {
                "title": "The Meaning of Relativity",
                "year": 1922, "journal": "Princeton University Press (book)",
                "topic": "relativity_exposition", "significance": "Einstein's own exposition of relativity",
                "taste_relevance": "Shows how Einstein organized and valued different aspects of his theories",
            },
        ]

        output_path = self.raw_dir / "einstein_papers.json"
        output_path.write_text(json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Saved {len(papers)} paper records to {output_path}")
        return papers

    # ── Stanford Encyclopedia ──────────────────────────────────────────────

    def fetch_sep_entries(self) -> list[dict]:
        """Fetch relevant entries from Stanford Encyclopedia of Philosophy."""
        print("Fetching Stanford Encyclopedia entries...")

        entries = [
            "einstein-philscience",
            "qt-epr",
            "scientific-aesthetics",
        ]

        results = []
        for entry_id in entries:
            url = f"https://plato.stanford.edu/entries/{entry_id}/"
            resp = self._get(url)
            if resp:
                soup = BeautifulSoup(resp.text, "html.parser")
                # Get the preamble/abstract
                preamble = soup.find("div", id="preamble")
                preamble_text = preamble.get_text(strip=True) if preamble else ""

                # Get section headings for structure
                toc = soup.find("div", id="toc")
                sections = []
                if toc:
                    for li in toc.find_all("li"):
                        sections.append(li.get_text(strip=True))

                results.append({
                    "entry_id": entry_id,
                    "url": url,
                    "preamble": preamble_text[:2000],  # Truncate for space
                    "sections": sections[:20],
                })

        output_path = self.raw_dir / "sep_entries.json"
        output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Saved {len(results)} SEP entries to {output_path}")
        return results

    # ── Process into Evidence Records ──────────────────────────────────────

    def process_papers_to_evidence(self, papers: list[dict]) -> list[EvidenceRecord]:
        """Convert paper metadata into evidence records."""
        records = []
        for i, paper in enumerate(papers):
            record = EvidenceRecord(
                id=f"paper_{paper['topic']}_{paper['year']}",
                content=(
                    f"Einstein published '{paper['title']}' in {paper['journal']} ({paper['year']}). "
                    f"Significance: {paper['significance']}. "
                    f"Research taste relevance: {paper['taste_relevance']}"
                ),
                source_text=f"Einstein, '{paper['title']}', {paper['journal']} ({paper['year']})",
                source_type=SourceType.PRIMARY,
                confidence=ConfidenceLevel.STRONG,
                year=paper["year"],
                relevant_axes=self._infer_axes_from_paper(paper),
                tags=[paper["topic"], "publication"],
            )
            records.append(record)
        return records

    def _infer_axes_from_paper(self, paper: dict) -> list[str]:
        """Infer relevant taste axes from a paper's metadata."""
        topic = paper.get("topic", "")
        taste_text = paper.get("taste_relevance", "").lower()
        axes = []

        keyword_map = {
            "simplicity": ["simplicity", "simple", "economy", "asymmetry"],
            "unity": ["unity", "unif", "connecting", "synthesis"],
            "invariance": ["invariance", "covariance", "symmetry", "coordinate"],
            "physical_reality": ["realism", "reality", "completeness", "determinism"],
            "mathematical_beauty": ["beauty", "elegance", "mathematical", "geometric"],
            "causal_continuity": ["causal", "locality", "continuity", "field"],
            "empirical_grounding": ["empirical", "observable", "experiment", "prediction"],
            "thought_experiment": ["thought experiment", "gedanken", "mental"],
        }

        for axis, keywords in keyword_map.items():
            if any(kw in taste_text for kw in keywords):
                axes.append(axis)

        if not axes:
            axes = ["empirical_grounding"]  # Default

        return axes

    # ── Full Fetch Pipeline ────────────────────────────────────────────────

    def fetch_all(self) -> list[EvidenceRecord]:
        """Run all data fetchers and return processed evidence records."""
        all_records = []

        # Fetch from various sources
        wiki_data = self.fetch_einstein_wikipedia()
        papers_data = self.fetch_einstein_papers_metadata()
        sep_data = self.fetch_sep_entries()

        # Process papers into evidence
        paper_records = self.process_papers_to_evidence(papers_data)
        all_records.extend(paper_records)

        # Save processed evidence
        from einstein_taste.data.loader import save_evidence_store
        from einstein_taste.core.evidence import EvidenceStore

        # Combine with seed data
        from einstein_taste.data.seed_evidence import get_seed_evidence
        all_records.extend(get_seed_evidence())

        store = EvidenceStore()
        store.add_batch(all_records)
        save_evidence_store(store, self.processed_dir / "evidence.json")

        print(f"\nTotal evidence records: {store.count()}")
        print(f"Evidence summary: {json.dumps(store.summary(), indent=2)}")

        return all_records
