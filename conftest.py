import os
import shutil
import pytest
import zipfile

RESOURCES_PATH = os.path.join(os.getcwd(), "tmp")
ZIPPED_PATH = os.path.join(os.getcwd(), "zipped")
ZIPPED_RESOURCES = os.path.join(os.getcwd(), 'zipped', 'zipped_resources.zip')


@pytest.fixture(scope='function', autouse=True)
def given_zip_file():
    if not os.path.exists(ZIPPED_PATH):
        os.mkdir(ZIPPED_PATH)

    with zipfile.ZipFile(ZIPPED_PATH + '/zipped_resources.zip', 'w') as zf:
        for file in os.listdir(RESOURCES_PATH):
            add_file = os.path.join(RESOURCES_PATH, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(ZIPPED_PATH)

