from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fixture.sesion import SessionHelper


class Application:
    # класс Application предназначен для создания сессии и методов взаимодействия с ней
    def __init__(self, browser, base_url):
        if browser == "firefox":
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.wd = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', options=options)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browzer %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def is_valid(self):
        # сессия валидна: проверяем, что браузер еще существует, проверяя наличие урла
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
