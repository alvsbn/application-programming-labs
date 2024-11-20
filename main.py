import argparse

from data_frame import create_data_frame, add_columns, compute_stat_info, filter_h_w, add_area_col, sort_area, \
    create_hist


def parse() -> tuple[str, int, int]:
    """
    Получает аргументы командной строки.
    :return: кортеж, содержаший путь к аннотации, значения максимальных высоты и длины изображения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('annotation_path', type=str, help='Input path to the annotation file')
    parser.add_argument('max_height', type=int, help='Input max height of image:')
    parser.add_argument('max_width', type=int, help='Input max width of image:')
    arguments = parser.parse_args()
    return arguments.annotation_path, arguments.max_height, arguments.max_width


def main():
    annotation_path, max_height, max_width = parse()
    try:
        data_frame = create_data_frame(annotation_path)
        add_columns(data_frame)
        compute_stat_info(data_frame)

        filtered_data_frame = filter_h_w(data_frame, max_height, max_width)
        print(filtered_data_frame)

        add_area_col(filtered_data_frame)

        sorted_data_frame = sort_area(filtered_data_frame)
        print(sorted_data_frame)

        create_hist(sorted_data_frame)

    except Exception as e:
        print(e)


if __name__=="__main__":
    main()



