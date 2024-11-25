Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def test_post_review(setup):
...     driver = setup
...     driver.find_element(By.ID, "suggestion-search").send_keys("Inception")
...     driver.find_element(By.ID, "suggestion-search-button").click()
...     driver.find_element(By.LINK_TEXT, "Inception").click()
...     driver.find_element(By.LINK_TEXT, "Write a Review").click()
...     driver.find_element(By.ID, "review-title").send_keys("Amazing Movie!")
...     driver.find_element(By.ID, "review-text").send_keys("A masterpiece by Christopher Nolan.")
...     driver.find_element(By.ID, "submit-review").click()
...     assert "Review submitted" in driver.page_source
