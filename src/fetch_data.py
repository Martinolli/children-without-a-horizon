import requests

# Example: Download a CSV from UNICEF or World Bank – replace the URL with a real one!
def download_csv(url, out_path):
    r = requests.get(url)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        f.write(r.content)
    print(f"Downloaded {out_path}")

if __name__ == "__main__":
    # Replace with real data source URLs
    download_csv(
        "https://example.com/some_unicef_data.csv",
        "../data/raw/child_indicators.csv"
    )
