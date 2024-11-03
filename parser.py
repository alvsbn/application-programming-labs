import argparse

def parse() -> tuple[str, int, str, str]:
    """
    Получает аргументы командной строки.
    :return: кортеж, содержащий ключевое слово для поиска, количество изображений, путь к директории для изображений, путь к файлу аннотации
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='Input keyword: ')
    parser.add_argument('number', type=int, help='Input number of images: ')
    parser.add_argument('img_dir', type=str, help='Input path to the folder for images: ')
    parser.add_argument('annotation_path', type=str, help='Input path to the annotation file')
    arguments = parser.parse_args()

    if not (50 <= arguments.number <= 1000):
        raise ValueError("Необходимо указать количество изображений от 50 до 1000.")
    return arguments.keyword, arguments.number, arguments.img_dir, arguments.annotation_path