Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... from selenium.webdriver.chrome.service import Service
... from selenium.webdriver.chrome.options import Options
... import pytest
... 
... class BaseTest:
...     @pytest.fixture(scope="function")
...     def setup(self):
...         # Configure Chrome options
...         options = Options()
...         options.add_argument("--start-maximized")
...         options.add_argument("--disable-extensions")
...         options.add_argument("--incognito")
...         
...         # Initialize WebDriver
...         service = Service("path/to/chromedriver")  # Replace with your ChromeDriver path
...         driver = webdriver.Chrome(service=service, options=options)
...         driver.get("https://www.imdb.com/")
...         
...         yield driver
