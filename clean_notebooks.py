import os
import json
import glob

# Find all .ipynb files in this folder and all subfolders
notebook_files = glob.glob("**/*.ipynb", recursive=True)
fixed_count = 0

for filepath in notebook_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            notebook = json.load(f)
        except json.JSONDecodeError:
            print(f"Skipping {filepath} (Not valid JSON)")
            continue

    # Look for the bugged 'widgets' metadata and delete it
    if 'metadata' in notebook and 'widgets' in notebook['metadata']:
        del notebook['metadata']['widgets']
        
        # Save the cleaned notebook back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
        
        print(f"✅ Scrubbed bugged metadata from: {filepath}")
        fixed_count += 1

print(f"\n🚀 Done! Successfully cleaned {fixed_count} notebooks.")