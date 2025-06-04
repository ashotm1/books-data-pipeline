import pandas as pd
import numpy as np
import os
from datetime import datetime

# 1. Setup paths
raw_path = "./raw_books_data/books_data/books.csv"
clean_dir = "./cleaned_data"
clean_path = os.path.join(clean_dir, "books_cleaned.csv")
def cleaner(raw_path, clean_dir):
# 2. Create cleaned_data folder
    os.makedirs(clean_dir, exist_ok=True)

    # 3. Load data
    df = df = pd.read_csv(
        raw_path,
        encoding='latin1',  # Fixes the Unicode decode error
        on_bad_lines='warn'  # Optional: skips problematic rows
    )

    # 4. Debug: Pre-cleaning report
    print("\n=== PRE-CLEANING REPORT ===")
    print("Missing values:")
    print(df.isna().sum())
    print("\nYear stats:")
    print(f"Min: {df['year_of_publication'].min()}, Max: {df['year_of_publication'].max()}")
    print(f"Invalid years: {df[df['year_of_publication'] > datetime.now().year].shape[0]}")

    # 5. Cleaning steps
    ## A. Handle missing values
    df_cleaned = df.copy()
    df_cleaned['author'].fillna('Unknown', inplace=True)
    df_cleaned['publisher'].fillna('Unknown', inplace=True)

    ## B. Fix year anomalies
    current_year = datetime.now().year
    df_cleaned = df_cleaned[df_cleaned['year_of_publication'] <= current_year]
    df_cleaned = df_cleaned[df_cleaned['year_of_publication'] > 1000]  # Remove ancient years

    ## C. Text normalization
    text_cols = ['title', 'author', 'publisher']
    for col in text_cols:
        df_cleaned[col] = df_cleaned[col].str.strip()  # Remove whitespace
        df_cleaned[col] = df_cleaned[col].str.title()  # Standardize case

    ## D. Image URL handling
    for img_col in ['image_url_s', 'image_url_m', 'image_url_l']:
        df_cleaned[img_col] = df_cleaned[img_col].apply(
            lambda x: np.nan if 'placeholder' in str(x).lower() else x
        )

    ## E. ISBN validation (basic)
    df_cleaned = df_cleaned[df_cleaned['isbn'].notna()]

    # 6. Debug: Post-cleaning report
    print("\n=== POST-CLEANING REPORT ===")
    print(f"Removed rows: {len(df) - len(df_cleaned)}")
    print("Missing values after cleaning:")
    print(df_cleaned.isna().sum())

    # 7. Save cleaned data
    df_cleaned.to_csv(clean_path, index=False)
    print(f"\n✅ Cleaned data saved to: {clean_path}")
