Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def test_add_to_watchlist(setup):
...     driver = setup
...     driver.find_element(By.ID, "suggestion-search").send_keys("Inception")
...     driver.find_element(By.ID, "suggestion-search-button").click()
...     driver.find_element(By.LINK_TEXT, "Inception").click()
...     driver.find_element(By.CLASS_NAME, "ipc-watchlist-ribbon__icon").click()
...     assert "Added to Watchlist" in driver.page_source
... 
... def test_remove_from_watchlist(setup):
...     driver = setup
...     driver.get("https://www.imdb.com/watchlist")
...     driver.find_element(By.CLASS_NAME, "ipc-watchlist-ribbon__icon").click()
...     assert "Removed from Watchlist" in driver.page_source
