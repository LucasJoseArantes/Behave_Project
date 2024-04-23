import logging as log
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(webdriver, selector, wait_time=60):
    """Waits for an element to become visible and returns it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        log.info(f"Found visible element with selector '{selector}'.")
        return element
    except TimeoutException:
        log.error(f"Element with selector '{selector}' was not found or not visible.")
        return None


def click_on_element(webdriver, selector, wait_time=60):
    """Waits for an element to become clickable and clicks on it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
        time.sleep(1)
        element.click()
        log.info(f"Clicked on element with selector '{selector}'.")
    except TimeoutException as e:
        log.error(f"Element with selector '{selector}' was not clickable.")
        raise e


def confirm_redirected_url(webdriver, expected_url):
    """Confirms if the current URL of the driver matches the expected URL within the specified timeout."""
    current_url = webdriver.current_url
    try:
        assert (
            current_url == expected_url
        ), f"Redirection failed. Expected URL: {expected_url}, Actual URL: {current_url}"
        log.info(f"Successfully redirected to URL: {expected_url}")
    except AssertionError as e:
        log.error(f"Assertion failed: {e}")
        raise e


def verify_message_matches(webdriver, selector, expected_message, wait_time=60):
    """Verifies if the expected message matches the currently displayed message on the page."""
    try:
        time.sleep(1)
        message_element = wait_for_element(webdriver, selector, wait_time)
        assert message_element.text == expected_message, (
            f"Expected message '{expected_message}' does not match the actual message: " f"'{message_element.text}'"
        )
        log.info(f"Message '{expected_message}' matches the displayed message.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Expected message '{expected_message}' was not found or did not match.")
        raise e


def verify_word_in_message(webdriver, selector, expected_word, wait_time=60):
    """Verifies if the expected word is present within the currently displayed message on the page."""
    try:
        message_element = wait_for_element(webdriver, selector, wait_time)
        assert expected_word in message_element.text, (
            f"Expected word '{expected_word}' is not found in the displayed message: " f"'{message_element.text}'"
        )
        log.info(f"Expected word '{expected_word}' found in the message.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Expected word '{expected_word}' was not found in the message.")
        raise e


def verify_element_displayed(webdriver, selector, wait_time=60):
    """Verifies if the element is displayed on the page."""
    try:
        element = wait_for_element(webdriver, selector, wait_time)
        assert element.is_displayed(), f"Element with selector '{selector}' is not displayed."
        log.info(f"Element with selector '{selector}' is displayed.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Element with selector '{selector}' is not displayed.")
        raise e


def take_screenshot(webdriver, file_name):
    """Takes a screenshot using the WebDriver instance."""
    try:
        webdriver.save_screenshot(file_name)
        log.info(f"Screenshot saved as {file_name}")
    except Exception as e:
        log.error(f"Error occurred while saving screenshot: {e}")
        raise e


def check_element_existence(webdriver, selector, wait_time=60):
    """Checks the existence of an element within a specified time using WebDriver instance."""
    try:
        exists = wait_for_element(webdriver, selector, wait_time) is not None
        if exists:
            log.info(f"Element with selector '{selector}' exists.")
        return exists
    except Exception as e:
        log.error(f"Error occurred while checking element existence: {e}")
        return False


def click_on_element_if_visible(webdriver, element_selector, close_element_selector, wait_time=60):
    """Checks if an element is visible; if visible, clicks on another specified element."""
    try:
        element_visible = is_element_visible(webdriver, element_selector, wait_time)
        if element_visible:
            click_on_element(webdriver, close_element_selector, wait_time)
            log.info(f"Clicked on close element with selector '{close_element_selector}'.")
    except Exception as e:
        log.error(f"Error occurred while handling element visibility: {e}")
        raise e


def is_element_visible(webdriver, selector, wait_time=10):
    """Checks if an element is visible, without generating an error log.
    Use for elements that may or may not be visible."""
    try:
        element = WebDriverWait(webdriver, wait_time).until(EC.visibility_of_element_located((By.XPATH, selector)))
        is_visible = element.is_displayed()
        log.info(f"Element located by '{selector}' is {'visible' if is_visible else 'not visible'} on the page.")
        return is_visible
    except TimeoutException:
        log.info(f"Timeout occurred while waiting for element located by '{selector}' to be visible.")
        return None


def navigate_to_url(webdriver, url, wait_time=60):
    """Navigates to the specified URL and sets a timeout for page load"""
    try:
        webdriver.set_page_load_timeout(wait_time)
        webdriver.get(url)
        log.info(f"Successfully navigated to URL: {url}")
    except TimeoutException as e:
        log.error(f"Timeout occurred while navigating to URL: {url}")
        raise e
