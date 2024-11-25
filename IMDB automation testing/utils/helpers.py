Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium.webdriver.common.by import By
... from selenium.webdriver.support.ui import WebDriverWait
... from selenium.webdriver.support import expected_conditions as EC
... 
... class Helpers:
...     @staticmethod
...     def login(driver, email, password, locators):
...         """Logs in to IMDb with the provided credentials."""
...         driver.find_element(By.ID, locators["login_button"]).click()
...         driver.find_element(By.LINK_TEXT, locators["sign_in_link"]).click()
...         driver.find_element(By.ID, locators["email_field"]).send_keys(email)
...         driver.find_element(By.ID, locators["password_field"]).send_keys(password)
...         driver.find_element(By.ID, locators["submit_button"]).click()
... 
...     @staticmethod
...     def search_movie(driver, movie_name, locators):
...         """Searches for a movie on IMDb."""
...         driver.find_element(By.ID, locators["search_field"]).send_keys(movie_name)
...         driver.find_element(By.ID, locators["search_button"]).click()
... 
...     @staticmethod
...     def wait_for_element(driver, locator_type, locator, timeout=10):
...         """Waits for an element to be visible on the page."""
