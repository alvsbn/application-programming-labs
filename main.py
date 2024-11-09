import argparse

import cv2

from image_processing import load_image, get_image_size, create_histogram, plot_histogram, create_binary_image, \
    save_binary_image


def parse() -> tuple[str, str]:
    """
    Получает аргументы командной строки.
    :return: кортеж, содержаший путь к изображению и путь для сохранения бинарного изображения
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='Input path to the image: ')
    parser.add_argument('binary_image_path', type=str, help='Input path to save the binary image:')
    arguments = parser.parse_args()
    return arguments.image_path, arguments.binary_image_path


def main() -> None:
    image_path, binary_image_path = parse()
    try:
        image = load_image(image_path)

        get_image_size(image)

        histogram = create_histogram(image)
        plot_histogram(histogram)

        binary_image = create_binary_image(image)

        cv2.imshow("Original image", image)
        cv2.waitKey(0)
        cv2.imshow("Binary image", binary_image)
        cv2.waitKey(0)

        save_binary_image(binary_image_path, binary_image)

    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
