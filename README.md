# Book Data Pipeline

**Downloads and cleans the Kaggle Books Dataset**  
*(saurabhbagchi/books-dataset)*

**Installation and running**
1. Install: `pip install pandas kaggle`
2. Add `kaggle.json` to `~/.kaggle/`
3. Run:
   ```bash
   python download_books.py  # Downloads to ./raw_books_data/
   python clean_books.py     # Cleans to ./cleaned_data/
