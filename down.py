from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Suman:
    driver = webdriver.Chrome()
    url = "https://www.imdb.com/search/title/"

    def select_by_user_ratings(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        user_rating = self.driver.find_element(by=By.NAME, value="user_rating-min")
        time.sleep(3)
        user_rating.click()

    def display_per_page(self):
        user_rating = self.driver.find_element(by=By.NAME, value="user_rating-min")
        user_rating_dropdown = Select(user_rating)
        user_rating_dropdown.select_by_visible_text('10')
        user_display = self.driver.find_element(by=By.ID, value='search-count')
        user_display.click()

    # SELECT BY VALUE
    def select_by_language(self):
        user_display = self.driver.find_element(by=By.ID, value='search-count')
        display_dropdown = Select(user_display)
        display_dropdown.select_by_index('1')
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.select_by_value('hi')

    # SELECT MULTIPLE VALUES
    def select_multiple_values(self):
        user_display = self.driver.find_element(by=By.ID, value='search-count')
        display_dropdown = Select(user_display)
        display_dropdown.select_by_index('1')
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.select_by_value('ab')
        time.sleep(2)
        language_dropdown.select_by_value('qac')
        time.sleep(2)
        language_dropdown.select_by_value('guq')
        time.sleep(2)
        language_dropdown.select_by_value('qam')

    # DIS-SELECT BY VALUE
    def disselect_by_value(self):
        user_display = self.driver.find_element(by=By.ID, value='search-count')
        display_dropdown = Select(user_display)
        display_dropdown.select_by_index('1')
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.deselect_by_value('ab')
        time.sleep(2)
        language_dropdown.deselect_by_value('qac')
        time.sleep(2)
        language_dropdown.deselect_by_value('guq')
        time.sleep(2)
        language_dropdown.deselect_by_value('qam')

    def disselect_by_text(self):
        user_display = self.driver.find_element(by=By.ID, value='search-count')
        display_dropdown = Select(user_display)
        display_dropdown.select_by_index('1')
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.deselect_by_visible_text('Abkhazian')
        time.sleep(2)
        language_dropdown.deselect_by_visible_text('Acholi')
        time.sleep(2)
        language_dropdown.deselect_by_visible_text('Aboriginal')
        time.sleep(2)
        language_dropdown.deselect_by_visible_text('Aché')

    # SELECT EVERYTHING FROM A SELECT ELEMENT OF HTML
    def select_all_languages(self):
        user_display = self.driver.find_element(by=By.ID, value='search-count')
        display_dropdown = Select(user_display)
        display_dropdown.select_by_index('1')
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)

        language_options = language_dropdown.options
        print(language_options)
        for i in language_options:
            i.click()
    def select_input(self):
        user_input=self.driver.find_element(by=By.NAME,value='release_date-min')
        a=input(2022-01-01)
        user_input=self.driver.find_element(by=By.NAME,value='release_date-max')
        b=input(2022-11-11)
        print(a,b)



s = Suman()

s.select_by_user_ratings()

s.display_per_page()

s.select_by_language()

s.select_multiple_values()

s.disselect_by_value()

s.disselect_by_text()

s.select_all_languages()
