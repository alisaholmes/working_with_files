import os
import shutil
import zipfile

import pytest

from script_os import FILES_DIR, ZIP_DIR, ARCHIVE_DIR


@pytest.fixture(scope="session", autouse=True)
def create_archive():
    if not os.path.exists(ARCHIVE_DIR):
        os.mkdir(ARCHIVE_DIR)
        with zipfile.ZipFile(ZIP_DIR, 'w') as zf:  # создаем архив
            for file in os.listdir(FILES_DIR):
                zf.write(os.path.join(FILES_DIR, file), file)  # добавляем файл в архив

    # удаление_файлов_после_архивации
    yield
    shutil.rmtree(ARCHIVE_DIR)
