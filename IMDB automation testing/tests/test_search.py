Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def test_search_movie(setup):
...     driver = setup
...     driver.find_element(By.ID, "suggestion-search").send_keys("Inception")
...     driver.find_element(By.ID, "suggestion-search-button").click()
...     results = driver.find_elements(By.CLASS_NAME, "result_text")
...     assert len(results) > 0, "No results found for the search term"
... 
