Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Configuration file for IMDb Automation
... 
... # IMDb URLs
... BASE_URL = "https://www.imdb.com/"
... LOGIN_URL = "https://www.imdb.com/registration/signin"
... 
... # User Credentials (use environment variables for sensitive information in production)
... VALID_EMAIL = "your_email@example.com"
... VALID_PASSWORD = "your_password"
... INVALID_EMAIL = "invalid_email@example.com"
... INVALID_PASSWORD = "wrong_password"
... 
... # Locators (use descriptive names)
... LOCATORS = {
...     "login_button": "imdbHeader-navDrawerOpen--desktop",
...     "sign_in_link": "Sign In",
...     "email_field": "ap_email",
...     "password_field": "ap_password",
...     "submit_button": "signInSubmit",
...     "search_field": "suggestion-search",
...     "search_button": "suggestion-search-button",
...     "watchlist_icon": "ipc-watchlist-ribbon__icon",
...     "review_link": "Write a Review",
...     "review_title": "review-title",
...     "review_text": "review-text",
...     "submit_review": "submit-review",
... }
