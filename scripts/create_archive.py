import os
from os.path import basename
from zipfile import ZipFile
import zipfile


def create_archive(path_with_files, path_save_archive):
    file_directory = os.listdir(path_with_files)
    with zipfile.ZipFile(path_save_archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_directory:
            add_file = os.path.join(path_with_files, file)
            zf.write(add_file, basename(add_file))
    contains_zip = ZipFile(path_save_archive).namelist()
    assert file_directory == contains_zip, 'Содержимое архива не соответствует исходным файлам'
