import os
import subprocess

# 1. SPECIFIC TO YOUR CASE
dataset = "saurabhbagchi/books-dataset"  # The exact dataset you want
destination = "./raw_books_data"          # Custom folder name for your project

# 2. CREATE FOLDER (Won't fail if exists)
os.makedirs(destination, exist_ok=True) 

# 3. DOWNLOAD WITH CLEAR FEEDBACK
try:
    print("⌛ Downloading dataset...")
    result = subprocess.run(
        ["kaggle", "datasets", "download", "-d", dataset, "-p", destination, "--unzip"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"✅ Success! Files saved to: {os.path.abspath(destination)}")
        print("📂 Files downloaded:", "\n- ".join(os.listdir(destination)))
    else:
        print("❌ Failed to download. Common fixes:")
        print("- Run 'kaggle competitions list' to test API")
        print("- Check ~/.kaggle/kaggle.json exists")
        print("Full error:\n", result.stderr)

except Exception as e:
    print(f"🔥 Critical error: {str(e)}")