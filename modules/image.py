import os
from PIL import Image

from utils.progress_bar import print_progress_bar

def compress(rootpath: str, target_dir: str = "exports"):
    progress_count = 0
    progress_total = sum([len(files) for _, _, files in os.walk(rootpath)])
    for subdir, dirs, files in os.walk(rootpath):
        for file in files:
            filepath = subdir + os.sep + file
            output_path = filepath.replace(rootpath, target_dir)
            if filepath.endswith(".jpg"):
                picture = Image.open(filepath)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                picture.save(output_path, optimize=True, quality=15)
            progress_count += 1
            print_progress_bar(progress_count, progress_total)
