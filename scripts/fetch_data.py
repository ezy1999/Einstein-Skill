"""Script to fetch Einstein historical data from online sources."""

from einstein_taste.data.fetcher import EinsteinDataFetcher


def main():
    fetcher = EinsteinDataFetcher()
    records = fetcher.fetch_all()
    print(f"\nDone! Fetched and processed {len(records)} evidence records.")


if __name__ == "__main__":
    main()
