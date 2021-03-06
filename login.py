import os
import pickle

from selenium import webdriver

LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

driver = webdriver.Firefox()


def login():
    """If cookie file exist then use it, else login. Return driver"""
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))

    except FileNotFoundError:
        driver.get('http://.lingualeo.com/ru/login')

        form_email = driver.find_element_by_id('email')
        form_password = driver.find_element_by_id('password')

        form_email.send_keys(LOGIN_EMAIL)
        form_password.send_keys(LOGIN_PASSWORD)

        driver.find_element_by_class_name('btn-upper-orange').click()

        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    else:
        # We can set cookie ONLY on the same domain.
        driver.get('http://www.lingualeo.com')
        # Delete existing cookie before set ours.
        driver.delete_all_cookies()

        for cookie in cookies:
            # Mozilla doesn't support a leading dot in domain names.
            cookie['domain'] = cookie['domain'].strip('.')
            driver.add_cookie(cookie)

    return driver
