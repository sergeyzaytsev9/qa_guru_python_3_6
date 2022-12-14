import os
from os.path import basename
from zipfile import ZipFile
import zipfile


def create_archive(path_with_files, path_save_archive):
    """
    Функция создает архив принимая в качестве аргументов путь до файлов и путь сохранения архива с его именем
    :param path_with_files:  Путь до файлов для архивации
    :param path_save_archive: Путь сохранения архива с указанием его имени, например 'D:\test\archive.zip'
    :return:
    """
    file_directory = os.listdir(path_with_files)
    with zipfile.ZipFile(path_save_archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_directory:
            add_file = os.path.join(path_with_files, file)
            zf.write(add_file, basename(add_file))
    contains_zip = ZipFile(path_save_archive).namelist()
    assert file_directory == contains_zip, 'Содержимое архива не соответствует исходным файлам'
