import os

from icrawler.builtin import GoogleImageCrawler

def download_images(keyword: str, number: int, img_dir: str) -> None:
    """
    Скачивает изображения.
    :param keyword: ключевое слово для поиска
    :param number: количество изображений для скачивания
    :param img_dir: путь к директории с изображениями
    """
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    google_crawler = GoogleImageCrawler(storage={'root_dir': img_dir})
    google_crawler.crawl(keyword = keyword, max_num = number)