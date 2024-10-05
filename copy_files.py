import os
import shutil
import argparse


def copy_files_recursively(src_dir, dst_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_files_recursively(item_path, dst_dir)

            elif os.path.isfile(item_path):
                file_ext = os.path.splitext(item)[1][1:].lower()
                if not file_ext:
                    file_ext = "no_extension"

                target_dir = os.path.join(dst_dir, file_ext)
                os.makedirs(target_dir, exist_ok=True)

                target_file_path = os.path.join(target_dir, item)
                shutil.copy2(item_path, target_file_path)
                print(f'Копіювання {item_path} до {target_file_path}')

    except Exception as e:
        print(f'Помилка при обробці {src_dir}: {e}')


def main():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання файлів і сортування за розширеннями')
    parser.add_argument('source', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('destination', nargs='?', default='dist', type=str, help='Шлях до директорії призначення (за '
                                                                                 'замовчуванням: dist)')
    args = parser.parse_args()

    if not os.path.exists(args.source):
        print(f'Вихідна директорія {args.source} не існує')
        return

    os.makedirs(args.destination, exist_ok=True)

    copy_files_recursively(args.source, args.destination)


if __name__ == '__main__':
    main()
