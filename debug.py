import pandas as pd
import numpy as np
import os
from datetime import datetime

# 1. Load data with error-tolerant settings
df = pd.read_csv(
    "./raw_books_data/books_data/books.csv",
    encoding='latin1',
    sep=';',
    on_bad_lines='skip',
    quotechar='"',
    engine='python'
)

# 2. Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace('-', '_')

# 3. Convert year to numeric, coercing errors
df['year_of_publication'] = pd.to_numeric(df['year_of_publication'], errors='coerce')

# 4. Clean data (create copy to avoid SettingWithCopyWarning)
clean_df = df[
    df['year_of_publication'].notna() & 
    (df['year_of_publication'] <= datetime.now().year)
].copy()  # Note the .copy() here

# 5. Handle missing values (safe method)
clean_df.loc[:, 'book_author'] = clean_df['book_author'].fillna('Unknown')
clean_df.loc[:, 'publisher'] = clean_df['publisher'].fillna('Unknown')

# 6. Save cleaned data
os.makedirs("./cleaned_data", exist_ok=True)
clean_df.to_csv("./cleaned_data/books_cleaned.csv", index=False)

# 7. Final report
print("\n=== FINAL CLEANING REPORT ===")
print(f"Original rows: {len(df):,}")
print(f"Invalid years removed: {len(df) - len(clean_df):,}")
print(f"Valid rows saved: {len(clean_df):,} ({len(clean_df)/len(df)*100:.1f}%)")
print("\n=== SAMPLE DATA ===")
print(clean_df.head(3))
print(f"\n✅ Success! Cleaned data saved to: ./cleaned_data/books_cleaned.csv")