import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading dataset; trying KaggleHub first, then fallback to local file if that fails
try:
    import kagglehub
    from kagglehub import KaggleDatasetAdapter

    file_path = "birdsong_metadata.csv"
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "rtatman/british-birdsong-dataset",
        file_path,
    )
except Exception as e:
    # internet issue fallback
    df = pd.read_csv("/mnt/data/birdsong_metadata (1).csv")

# cleaning up dataset
df = df.copy()

# normalize column names a bit
df.columns = [c.strip() for c in df.columns]

# fix the known typos
if "longitute" in df.columns and "longitude" not in df.columns:
    df = df.rename(columns={"longitute": "longitude"})

# make sure lat/long are numeric
for col in ["latitude", "longitude"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# clean text columns
for col in ["english_cname", "country"]:
    if col in df.columns:
        df[col] = df[col].astype("string").str.strip()


# top species count
species = df["english_cname"].dropna()
top_species = species.value_counts().head(20)

plt.figure(figsize=(10, 6))
plt.barh(top_species.index[::-1], top_species.values[::-1])
plt.title("Top 20 species by # recordings")
plt.xlabel("# recordings")
plt.tight_layout()
plt.show()

# recordings per country
countries = df["country"].dropna()
top_countries = countries.value_counts().head(15)

plt.figure(figsize=(10, 6))
plt.barh(top_countries.index[::-1], top_countries.values[::-1])
plt.title("Top 15 countries by # recordings")
plt.xlabel("# recordings")
plt.tight_layout()
plt.show()

# locations scatter w/ longitude/latitude (if available)
if {"latitude", "longitude"}.issubset(df.columns):
    has_geo = df[["latitude", "longitude"]].notna().all(axis=1)

    # keeping only plausible ranges
    geo = df.loc[has_geo].copy()
    geo = geo[(geo["latitude"].between(-90, 90)) & (geo["longitude"].between(-180, 180))]

    plt.figure(figsize=(7, 5))
    plt.scatter(geo["longitude"], geo["latitude"], s=18, alpha=0.7)
    plt.title("Recording locations (lat/long)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.show()
else:
    print("No latitude/longitude columns found, skipping scatter plot.")