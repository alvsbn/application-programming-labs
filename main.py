from annotation import create_annotation
from downloader import download_images
from iterator import Iterator
from parser import parse


def main() -> None:
    keyword, number, img_dir, annotation_path = parse()
    try:
        download_images(keyword, number, img_dir)
        create_annotation(img_dir, annotation_path)
        img_iterator = Iterator(annotation_path)
        for i in img_iterator:
            print(i)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
