import csv
import os
import shutil

from utils.progress_bar import print_progress_bar

def convert(path: str, target_dir: str = "exports", image_path: str = "exports"):
    filename, file_extension = os.path.splitext(os.path.basename(path))
    fieldnames = ['id', 'image_1920', 'extra']
    correct_files = []
    with open(os.path.join(target_dir, f"{filename}.raw{file_extension}"), 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        output_rows = []
        with open(path) as source_csvfile:
            csvreader = csv.reader(source_csvfile, delimiter=',')

            # TODO: check if csv container 'id' and 'name'

            next(csvreader)
            progress_counter = 0
            progress_total = sum(1 for r in csvreader)
            source_csvfile.seek(0)
            next(csvreader)
            for row in csvreader:
                line = {}
                id, name = row[0], row[1]
                line['id'] = id

                # TODO: find compressed image_1920
                main_file_path = os.path.join(image_path, "main", f"{name}-SQ.jpg")
                if os.path.isfile(main_file_path):
                    line['image_1920'] = main_file_path
                    correct_files.append(main_file_path)

                # TODO: find compressed extra
                extra_file_path = os.path.join(image_path, "extra", f"{name}-Edit1.jpg")
                if os.path.isfile(extra_file_path):
                    line['extra'] = extra_file_path
                    correct_files.append(extra_file_path)

                if any(key in list(line.keys()) for key in ['image_1920', 'extra']):
                    output_rows.append(line)

                progress_counter += 1
                print_progress_bar(progress_counter, progress_total)
        csvwriter.writerows(output_rows)

    fieldnames = ["image"]
    with open(os.path.join(target_dir, f"{filename}.remain{file_extension}"), 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        output_rows = []
        for subdir, dirs, files in os.walk("/home/odoo/Desktop/python/otools/exports"):
            for file in files:
                filepath = subdir + os.sep + file
                output_path = filepath.replace("/home/odoo/Desktop/python/otools/exports", "/home/odoo/Desktop/python/otools/exports/remain")
                if filepath.endswith(".jpg") and filepath.replace('/home/odoo/Desktop/python/otools/', '') not in correct_files:
                    output_rows.append({'image': file})
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    shutil.copy2(filepath, output_path)
        csvwriter.writerows(output_rows)
