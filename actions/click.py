from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Click:
    def click_element(self, driver: webdriver, locator):
        try:
            return WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, locator))).click()
        except Exception as inst:
            print("Error: when click element", inst)
