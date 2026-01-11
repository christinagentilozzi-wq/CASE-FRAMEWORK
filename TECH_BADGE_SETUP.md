# Tech Badge Asset Management

## Local Development Setup

If you have Tech Badge assets stored locally (e.g., `C:\Users\RAC\OneDrive\MAST\mASTERSHEETS\TECHBADE`), follow these steps:

### Option 1: Using the Extraction Script

1. Copy your `Design Concept for Tech Badge.zip` file to `/mnt/data/` (or update the path in the script)
2. Run the extraction script:
   ```bash
   python3 extract_badge_assets.py
   ```

### Option 2: Direct File Access

To modify the `extract_badge_assets.py` script for your local path:

**Windows:**
```python
zip_path = r"C:\Users\RAC\OneDrive\MAST\mASTERSHEETS\TECHBADE\Design Concept for Tech Badge.zip"
extract_dir = r"C:\Users\RAC\OneDrive\MAST\mASTERSHEETS\TECHBADE\extracted"
```

**Linux/Mac:**
```python
zip_path = "/path/to/your/Design Concept for Tech Badge.zip"
extract_dir = "/path/to/your/badge_assets"
```

### Option 3: Configuration File

You can also create a `config.py` file to manage paths:

```python
# config.py
import os

# Adjust these paths based on your system
if os.name == 'nt':  # Windows
    BADGE_ZIP_PATH = r"C:\Users\RAC\OneDrive\MAST\mASTERSHEETS\TECHBADE\Design Concept for Tech Badge.zip"
    BADGE_EXTRACT_DIR = r"C:\Users\RAC\OneDrive\MAST\mASTERSHEETS\TECHBADE\badge_assets"
    PDF_OUTPUT_PATH = r"C:\Users\RAC\OneDrive\MAST\mASTERSHEETS\UI_UX_Case_Study_Master_System_v1.pdf"
else:  # Linux/Mac
    BADGE_ZIP_PATH = "/mnt/data/Design Concept for Tech Badge.zip"
    BADGE_EXTRACT_DIR = "/mnt/data/badge_assets"
    PDF_OUTPUT_PATH = "/mnt/data/UI_UX_Case_Study_Master_System_v1.pdf"
```

Then update your scripts to import from `config.py`.

## Notes

- Use raw strings (prefix with `r`) for Windows paths to handle backslashes correctly
- Ensure the ZIP file exists at the specified location before running the extraction script
- The extracted files will be placed in the `badge_assets` subdirectory
