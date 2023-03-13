import os
import sys
import pytest
from os.path import abspath, dirname, join

root_dir = dirname(dirname(abspath(__file__)))
print(root_dir)
sys.path.append(root_dir)
infra_dir_path = join(root_dir, 'infra')

pytest_plugins = [
]

@pytest.fixture(scope="session", autouse=True)
def set_env():
    print("HELLLO SET ENV")
    os.environ["DB_ENGINE"] = "django.db.backends.postgresql" # указываем, что работаем с postgresql
    os.environ["DB_NAME"]="postgres" # имя базы данных
    os.environ["POSTGRES_USER"]="postgres" # логин для подключения к базе данных
    os.environ["POSTGRES_PASSWORD"]="postgres" # пароль для подключения к БД (установите свой)
    os.environ["DB_HOST"]="db" # название сервиса (контейнера)
    os.environ["DB_PORT"]="5432" # порт для подключения к БД
