import pandas as pd

def clean_data(infile, outfile):
    df = pd.read_csv(infile)
    # Example: Remove rows with any missing values
    df_clean = df.dropna()
    df_clean.to_csv(outfile, index=False)
    print(f"Cleaned data saved to {outfile}")

if __name__ == "__main__":
    clean_data("../data/raw/child_indicators.csv", "../data/processed/child_indicators_clean.csv")
