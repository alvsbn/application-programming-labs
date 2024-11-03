import csv
import os

def create_annotation(img_dir: str, csv_file: str) -> None:
    """
    Создает файл аннотации с относительными и абсолютными путями к изображениям.
    :param img_dir: путь к директории с изображениями
    :param csv_file: путь к файлу аннотации
    """
    with open(csv_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['relative path', 'absolute path'])
        img_list = os.listdir(img_dir)

        for i in img_list:
            relative_path = os.path.relpath(os.path.join(img_dir, i))
            absolute_path = os.path.abspath(os.path.join(img_dir, i))
            writer.writerow([relative_path,absolute_path])
