from time import sleep

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

from login import login

driver = login()


def select_content():
    driver.get('https://lingualeo.com/ru/jungle')
    driver.find_element_by_class_name('iconmenu-all').click()
    sleep(3)
    driver.find_element_by_class_name('content-link').click()


def read_content():
    while True:
        sleep(10)
        if not success_clicked_next_btn():
            break


def success_clicked_next_btn():
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    window_height = driver.execute_script("return document.body.scrollHeight")

    scrolling_height = window_height / 50

    scrolled_height = 0

    while scrolled_height < window_height:
        driver.execute_script(f"window.scrollTo(0, {scrolled_height});")

        scrolled_height += scrolling_height

        sleep(SCROLL_PAUSE_TIME)

    try:
        driver.find_element_by_id('pageLearnButton').click()
        driver.find_element_by_class_name('paginator-next-btn').click()
        sleep(10)

        return True
        
    except ElementNotInteractableException:

        return False


while True:
    select_content()
    read_content()