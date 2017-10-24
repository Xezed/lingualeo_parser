from time import sleep

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

from login import login


driver = login()


def main():
    while True:
        select_content()
        read_content_until_complete()


def click_next():
    """Find and click next button. Return True if success, False overwise. """
    try:
        driver.find_element_by_class_name('paginator-next-btn').click()

        return True

    except ElementNotInteractableException:

        return False


def complete_page():
    """Complete page and go to next. Return True if success, False overwise."""
    try:
        sleep(1)
        driver.find_element_by_id('pageLearnButton').click()
        sleep(4)
        if driver.find_element_by_css_selector('.paginator-next-btn.disabled'):
            print('Found')
            return False
        sleep(10)

        return True

    except NoSuchElementException:
        print('NoSuchElement')

        return click_next()


def read_content_until_complete():
    """Read content until complete"""
    while True:
        sleep(10)
        scrolling()
        if not complete_page():
            break


def scrolling():
    """Scroll page of content"""
    # Get scroll height
    window_height = driver.execute_script("return document.body.scrollHeight")

    # Get step of scrolling
    scrolling_height = window_height / 50

    scrolled_height = 0

    # Scroll until bottom
    while scrolled_height < window_height:
        driver.execute_script(f"window.scrollTo(0, {scrolled_height});")
        scrolled_height += scrolling_height
        sleep(1)


def select_content():
    """Select content to study"""
    driver.get('https://lingualeo.com/ru/jungle')
    driver.find_element_by_class_name('iconmenu-all').click()
    sleep(3)
    driver.find_elements_by_class_name('content-link')[4].click()


if __name__ == '__main__':
    main()