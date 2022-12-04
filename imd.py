from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import select
import time

class Raj:
    driver=webdriver.Chrome()
    url = "https://www.imdb.com/search/title/"
    def select_by_user_rating(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        user_rating = self.driver.find_element(by=By.NAME, value="user_rating-min")
        time.sleep(2)
        user_rating.click()
    def display_per_page(self):
        user.rating=self.driver.find_element()