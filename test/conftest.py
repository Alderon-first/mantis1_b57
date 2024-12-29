from fixture.application import Application
from fixture.sesion import SessionHelper
import pytest
import json
import os.path

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file) # # ищу путь к файлу и поднимаюсь к родительской директории (но путь не универсален для разных ОС) затем os.path.abspath(parent) преобразует путь так, чтобы он склеился правильным образом
        print(config_file)
        with open(config_file) as f:
            target = json.load(f)
            print(target)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    # перехват значений из командной строки
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

