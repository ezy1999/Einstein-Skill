"""
Download real Einstein data from public web sources.
Saves raw JSON/text files to einstein_taste/data/raw/.
"""

import json
import time
import os
import requests
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "einstein_taste" / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "EinsteinResearchTaste/0.1 (academic research)"}


def fetch_url(url, delay=1.0):
    time.sleep(delay)
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"  FAIL: {url}: {e}")
        return None


def download_wikipedia_detailed():
    """Download detailed Wikipedia articles related to Einstein."""
    print("=== Wikipedia Detailed Articles ===")
    pages = {
        "Albert_Einstein": "einstein_biography",
        "Einstein%27s_thought_experiments": "thought_experiments",
        "Annus_Mirabilis_papers": "annus_mirabilis",
        "EPR_paradox": "epr_paradox",
        "Einstein_field_equations": "field_equations",
        "Unified_field_theory": "unified_field_theory",
        "Photoelectric_effect": "photoelectric_effect",
        "Brownian_motion": "brownian_motion",
        "Special_relativity": "special_relativity",
        "General_relativity": "general_relativity",
        "Bohr%E2%80%93Einstein_debates": "bohr_einstein_debates",
        "Einstein%27s_unsuccessful_investigations": "unsuccessful_investigations",
        "Religious_and_philosophical_views_of_Albert_Einstein": "philosophy_religion",
    }
    results = {}
    for page, key in pages.items():
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page}"
        r = fetch_url(url)
        if r:
            data = r.json()
            results[key] = {
                "title": data.get("title", ""),
                "extract": data.get("extract", ""),
                "description": data.get("description", ""),
                "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
            }
            print(f"  OK: {key} ({len(data.get('extract',''))} chars)")

    # Also get full article extracts (longer)
    for page, key in list(pages.items())[:5]:
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page}&prop=extracts&exintro=false&explaintext=true&format=json"
        r = fetch_url(url)
        if r:
            data = r.json()
            page_data = list(data.get("query", {}).get("pages", {}).values())
            if page_data:
                full_text = page_data[0].get("extract", "")
                results[key]["full_extract"] = full_text[:20000]  # Cap at 20k chars
                print(f"  FULL: {key} ({len(full_text)} chars, capped at 20k)")

    path = RAW_DIR / "wikipedia_detailed.json"
    path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Saved to {path}")
    return results


def download_wikisource_texts():
    """Download Einstein texts from Wikisource."""
    print("\n=== Wikisource Texts ===")
    texts = {
        "Ether_and_the_Theory_of_Relativity": "ether_relativity_1920",
        "A_Brief_Outline_of_the_Development_of_the_Theory_of_Relativity": "brief_outline_1921",
        "Time,_Space,_and_Gravitation": "time_space_gravitation_1919",
        "Dialog_about_Objections_against_the_Theory_of_Relativity": "dialog_objections_1918",
    }
    results = {}
    for page, key in texts.items():
        url = f"https://en.wikisource.org/w/api.php?action=query&titles={page}&prop=extracts&explaintext=true&format=json"
        r = fetch_url(url)
        if r:
            data = r.json()
            page_data = list(data.get("query", {}).get("pages", {}).values())
            if page_data and "extract" in page_data[0]:
                text = page_data[0]["extract"]
                results[key] = {"title": page.replace("_", " "), "text": text[:30000]}
                print(f"  OK: {key} ({len(text)} chars)")
            else:
                print(f"  EMPTY: {key}")

    path = RAW_DIR / "wikisource_texts.json"
    path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Saved to {path}")
    return results


def download_sep_einstein():
    """Download Stanford Encyclopedia of Philosophy articles."""
    print("\n=== Stanford Encyclopedia of Philosophy ===")
    entries = {
        "einstein-philscience": "einstein_philosophy",
        "qt-epr": "epr_quantum",
    }
    results = {}
    for entry, key in entries.items():
        url = f"https://plato.stanford.edu/entries/{entry}/"
        r = fetch_url(url)
        if r:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(r.text, "html.parser")
            # Get main article text
            article = soup.find("div", id="main-text") or soup.find("div", id="aueditable")
            if article:
                text = article.get_text(separator="\n", strip=True)
                results[key] = {"entry": entry, "url": url, "text": text[:50000]}
                print(f"  OK: {key} ({len(text)} chars, capped at 50k)")
            else:
                # Try getting all paragraphs
                paragraphs = soup.find_all("p")
                text = "\n".join(p.get_text(strip=True) for p in paragraphs)
                results[key] = {"entry": entry, "url": url, "text": text[:50000]}
                print(f"  OK (paragraphs): {key} ({len(text)} chars)")

    path = RAW_DIR / "sep_full_articles.json"
    path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Saved to {path}")
    return results


def download_einstein_quotes():
    """Download Einstein quotes from Wikiquote."""
    print("\n=== Wikiquote Einstein ===")
    url = "https://en.wikiquote.org/w/api.php?action=query&titles=Albert_Einstein&prop=extracts&explaintext=true&format=json"
    r = fetch_url(url)
    if r:
        data = r.json()
        page_data = list(data.get("query", {}).get("pages", {}).values())
        if page_data:
            text = page_data[0].get("extract", "")
            path = RAW_DIR / "wikiquote_einstein.json"
            path.write_text(json.dumps({"quotes_text": text[:50000]}, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  OK: {len(text)} chars of quotes (capped at 50k)")
            return text
    print("  FAIL")
    return ""


def download_semantic_scholar():
    """Download Einstein-related papers from Semantic Scholar API."""
    print("\n=== Semantic Scholar (Einstein scholarship) ===")
    queries = [
        "Einstein scientific methodology philosophy",
        "Einstein research taste aesthetic judgment physics",
        "Einstein unified field theory motivation",
    ]
    all_papers = []
    for q in queries:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={q}&limit=10&fields=title,year,authors,abstract,citationCount"
        r = fetch_url(url, delay=3.0)  # Rate limit
        if r:
            data = r.json()
            papers = data.get("data", [])
            all_papers.extend(papers)
            print(f"  OK: '{q}' → {len(papers)} papers")

    path = RAW_DIR / "semantic_scholar_papers.json"
    path.write_text(json.dumps(all_papers, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Saved {len(all_papers)} papers to {path}")
    return all_papers


def main():
    print("=" * 60)
    print("DOWNLOADING REAL EINSTEIN DATA")
    print("=" * 60)

    download_wikipedia_detailed()
    download_wikisource_texts()
    download_sep_einstein()
    download_einstein_quotes()
    download_semantic_scholar()

    # Show what was downloaded
    print("\n=== Download Summary ===")
    total_size = 0
    for f in sorted(RAW_DIR.glob("*.json")):
        size = f.stat().st_size
        total_size += size
        print(f"  {f.name}: {size:,} bytes")
    print(f"  TOTAL: {total_size:,} bytes ({total_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
