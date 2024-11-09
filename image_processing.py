import cv2

import matplotlib.pyplot as plt
import numpy as np


def load_image(img_path: str) -> np.ndarray:
    """
    Загружает изображение из указанного пути.
    :param img_path: путь к изображению
    :return: изображение
    """
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Failed to upload image.")
    return img


def get_image_size(img: np.ndarray) -> None:
    """
    Выводит размер изображения.
    :param img: изображение
    """
    print(img.shape)


def create_histogram(img: np.ndarray) -> tuple:
    """
    Создает гистограммы для каждого цветового канала.
    :param img: изображение
    :return: кортеж, состоящий из гистограмм для каждого цветового канала
    """
    blue_hist = cv2.calcHist([img],[0],None,[256],[0,256])
    green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
    red_hist = cv2.calcHist([img], [2], None, [256], [0, 256])
    return blue_hist, green_hist, red_hist


def plot_histogram(hist: tuple) -> None:
    """
    Отображает гистограммы.
    :param hist: кортеж, состоящий из гистограмм для каждого цветового канала
    """
    plt.figure()

    plt.plot(hist[0], color='b', label="Blue channel")
    plt.plot(hist[1], color='g', label="Green channel")
    plt.plot(hist[2], color='r', label="Red channel")
    plt.title("Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Number of pixels")
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim([0, 256])
    plt.legend()

    plt.show()


def create_binary_image(img: np.ndarray) -> np.ndarray:
    """
    Создает бинарное изображение.
    :param img: изображение
    :return: бинарное изображение
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, b_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    return b_img


def save_binary_image(binary_image_path: str, binary_img: np.ndarray) -> None:
    """
    Сохраняет бинарное изображение.
    :param binary_image_path: путь для сохранения бинарного изображения
    :param binary_img: бинарное изображение
    """
    cv2.imwrite(binary_image_path, binary_img)
