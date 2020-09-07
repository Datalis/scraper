from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from shutil import which


class HeadlessChrome():
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver_path = which('chromedriver')
        self.driver = webdriver.Chrome(options=options, executable_path=self.driver_path)

    def __del__(self):
        self.driver.quit()

    def take_screenshot(self, url):
        print('-> getting url', url)
        self.driver.get(url)
        print('-> taking screenshot of', url)
        self.driver.save_screenshot("screenshot.png")

    def try_get_until_elem_load(self):
        try:
            timeout = 10
            print('-> get toolbar element with timeout', timeout)
            elem = WebDriverWait(self.driver, timeout)\
                .until(EC.presence_of_element_located((By.CLASS_NAME, 'toolbar')))
            print('-> elem success load')
        except TimeoutException:
            print("Timeout")

