import zipfile
import os
import shutil

zip_path = "/mnt/data/Design Concept for Tech Badge.zip"
extract_dir = "/mnt/data/badge_assets"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

os.listdir(extract_dir)
