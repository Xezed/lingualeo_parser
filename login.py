import os
import pickle

from selenium import webdriver

LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

driver = webdriver.Firefox()


def login():
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        driver.get('http://www.lingualeo.com/ru/')
        driver.delete_all_cookies()

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get('http://www.lingualeo.com/ru/')

    except FileNotFoundError:
        driver.get('http://www.lingualeo.com/ru/login')

        form_email = driver.find_element_by_id('email')
        form_password = driver.find_element_by_id('password')

        form_email.send_keys(LOGIN_EMAIL)
        form_password.send_keys(LOGIN_PASSWORD)
        driver.find_element_by_class_name('btn-upper-orange').click()
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    # else:

