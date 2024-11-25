Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pytest
... from selenium import webdriver
... from selenium.webdriver.common.by import By
... 
... @pytest.fixture(scope="function")
... def setup():
...     driver = webdriver.Chrome()  # Replace with your ChromeDriver path
...     driver.get("https://www.imdb.com/")
...     yield driver
...     driver.quit()
... 
... def test_valid_login(setup):
...     driver = setup
...     driver.find_element(By.ID, "imdbHeader-navDrawerOpen--desktop").click()
...     driver.find_element(By.LINK_TEXT, "Sign In").click()
...     driver.find_element(By.ID, "ap_email").send_keys("your_email@example.com")
...     driver.find_element(By.ID, "ap_password").send_keys("your_password")
...     driver.find_element(By.ID, "signInSubmit").click()
...     assert "Your Watchlist" in driver.page_source
... 
... def test_invalid_login(setup):
...     driver = setup
...     driver.find_element(By.ID, "imdbHeader-navDrawerOpen--desktop").click()
...     driver.find_element(By.LINK_TEXT, "Sign In").click()
...     driver.find_element(By.ID, "ap_email").send_keys("invalid_email@example.com")
...     driver.find_element(By.ID, "ap_password").send_keys("wrong_password")
...     driver.find_element(By.ID, "signInSubmit").click()
...     assert "incorrect" in driver.page_source
