import subprocess
from pathlib import Path

print("🔄 Starting conversion of all notebooks to .qmd files...\n")

# Get all .ipynb files in the notebooks folder
notebooks_dir = Path("notebooks")
book_dir = Path("book")
book_dir.mkdir(exist_ok=True)

notebook_files = sorted(notebooks_dir.glob("*.ipynb"))

if not notebook_files:
    print("❌ No .ipynb files found in notebooks/ folder!")
    exit(1)

print(f"Found {len(notebook_files)} notebook(s) to convert:\n")

for nb_path in notebook_files:
    nb_name = nb_path.name
    qmd_name = nb_path.stem + ".qmd"
    qmd_path = book_dir / qmd_name
    
    print(f"Converting: {nb_name} → {qmd_name}")
    
    try:
        # Use nbconvert to markdown first
        result = subprocess.run([
            "jupyter", "nbconvert",
            "--to", "markdown",
            "--output", nb_path.stem,
            "--output-dir", str(book_dir),
            str(nb_path)
        ], check=True, capture_output=True, text=True)
        
        # Rename .md to .qmd
        md_file = book_dir / (nb_path.stem + ".md")
        if md_file.exists():
            md_file.rename(qmd_path)
            print(f"  ✅ Success: {qmd_name}")
        else:
            print(f"  ⚠️  Warning: No .md file generated for {nb_name}")
            
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed: {nb_name}")
        print(f"     Error: {e.stderr.strip()}")
    except Exception as e:
        print(f"  ❌ Error converting {nb_name}: {e}")

print("\n🎉 Conversion process completed!")
print(f"   .qmd files are in: {book_dir}/")
print(f"   Original .ipynb files remain in: notebooks/")
