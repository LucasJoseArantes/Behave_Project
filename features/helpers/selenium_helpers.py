import logging as log
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_element(webdriver, selector, wait_time=60):
    """Wait for an element to be visible and return it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        log.info(f"Element with selector '{selector}' found and visible.")
        return element
    except TimeoutException:
        log.error(f"Element with selector '{selector}' was not found or not visible.")
        return None


def click_element(webdriver, selector, wait_time=60):
    """Wait for an element to be clickable and click on it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
        time.sleep(1)
        element.click()
        log.info(f"Clicked element with selector '{selector}'.")
    except TimeoutException as e:
        log.error(f"Element with selector '{selector}' was not clickable.")
        raise e


def assert_redirect_url(webdriver, expected_url):
    """Asserts if the current URL of the driver matches the expected URL within the specified timeout."""
    current_url = webdriver.current_url
    try:
        assert (
            current_url == expected_url
        ), f"Redirection failed. Expected URL: {expected_url}, Actual URL: {current_url}"
        log.info(f"Redirected to URL: {expected_url}")
    except AssertionError as e:
        log.error(f"Assertion failed: {e}")
        raise e


def assert_message_matches(webdriver, selector, expected_message, wait_time=60):
    """Verifies if the expected message matches the currently displayed message on the page."""
    try:
        time.sleep(1)
        message_element = wait_element(webdriver, selector, wait_time)
        assert message_element.text == expected_message, (
            f"Expected message '{expected_message}' does not match the actual message: " f"'{message_element.text}'"
        )
        log.info(f"Message '{expected_message}' matches the actual message.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Expected message '{expected_message}' was not found or did not match.")
        raise e


def assert_word_in_message(webdriver, selector, expected_word, wait_time=60):
    """Verifies if the expected word is present within the currently displayed message on the page."""
    try:
        message_element = wait_element(webdriver, selector, wait_time)
        assert expected_word in message_element.text, (
            f"Expected word '{expected_word}' is not found in the displayed message: " f"'{message_element.text}'"
        )
        log.info(f"Expected word '{expected_word}' found in the message.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Expected word '{expected_word}' was not found in the message.")
        raise e


def assert_element_displayed(webdriver, selector, wait_time=60):
    """Verifies if the element is displayed on the page."""
    try:
        element = wait_element(webdriver, selector, wait_time)
        assert element.is_displayed(), f"Element with selector '{selector}' is not displayed."
        log.info(f"Element with selector '{selector}' is displayed.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Element with selector '{selector}' is not displayed.")
        raise e


def save_screenshot(webdriver, file_name):
    """Save a screenshot using the WebDriver instance."""
    try:
        webdriver.save_screenshot(file_name)
        log.info(f"Screenshot saved as {file_name}")
    except Exception as e:
        log.error(f"Error saving screenshot: {e}")
        raise e


def check_element_exists(webdriver, selector, wait_time=60):
    """Check the existence of an element within a specified time using WebDriver instance."""
    try:
        exists = wait_element(webdriver, selector, wait_time) is not None
        if exists:
            log.info(f"Element with selector '{selector}' exists.")
        return exists
    except Exception as e:
        log.error(f"Error checking element existence: {e}")
        return False


def click_element_if_visible(webdriver, element_selector, close_element_selector, wait_time=60):
    """Checks if an element is visible; if visible, clicks on another specified element."""
    try:
        element_visible = is_element_visible(webdriver, element_selector, wait_time)
        if element_visible:
            click_element(webdriver, close_element_selector, wait_time)
            log.info(f"Clicked close element with selector '{close_element_selector}'.")
    except Exception as e:
        log.error(f"Error handling element visibility: {e}")
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


def is_element_visible_inside_iframe(webdriver, iframe_selector, selector, wait_time=10):
    """
    Checks if an element inside an iframe is visible without generating an error log.
    Use for elements that may or may not be visible inside the specified iframe.
    """
    try:
        iframe = WebDriverWait(webdriver, wait_time).until(EC.presence_of_element_located((By.XPATH, iframe_selector)))
        webdriver.switch_to.frame(iframe)
        element = WebDriverWait(webdriver, wait_time).until(EC.visibility_of_element_located((By.XPATH, selector)))
        is_visible = element.is_displayed()
        log.info(f"Element located by '{selector}' is {'visible' if is_visible else 'not visible'} inside the iframe.")
        return is_visible
    except TimeoutException:
        return False
    except NoSuchElementException:
        return False
    finally:
        webdriver.switch_to.default_content()


def click_element_inside_iframe(webdriver, iframe_selector, element_selector, wait_time=60):
    """Clicks an element inside an iframe identified by the provided selector."""
    try:
        iframe = WebDriverWait(webdriver, wait_time).until(EC.presence_of_element_located((By.XPATH, iframe_selector)))
        webdriver.switch_to.frame(iframe)
        element = WebDriverWait(webdriver, wait_time).until(EC.element_to_be_clickable((By.XPATH, element_selector)))
        element.click()
    except TimeoutException as e:
        log.error(f"Timeout occurred: {e}")
    except NoSuchElementException as e:
        log.error(f"Element not found inside the iframe: {e}")
    finally:
        webdriver.switch_to.default_content()


def select_option_from_list(webdriver, option_name, selector_button, selector_list):
    """Selects an option from a list."""
    try:
        click_element(webdriver, selector_button)
        time.sleep(1)
        options = webdriver.find_elements(By.XPATH, selector_list)
        for option in options:
            if option.text == option_name:
                option.click()
                log.info(f"Selected option '{option_name}' from list.")
                break
        else:
            assert False, f"Unable to find {option_name} select option"
    except Exception as e:
        log.error(f"Error selecting option from list: {e}")
        raise e


def scroll_to_element(webdriver, selector):
    """Scrolls to a specific element on the page."""
    try:
        element = wait_element(webdriver, selector)
        webdriver.execute_script("arguments[0].scrollIntoView();", element)
        log.info(f"Scrolled to the element with selector '{selector}'.")
    except Exception as e:
        log.error(f"Error scrolling to the element with selector '{selector}': {e}")
        raise e


def scroll_and_click_element(webdriver, selector):
    """Scrolls to a specific element on the page and clicks on it."""
    try:
        element = wait_element(webdriver, selector)
        webdriver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()
        log.info(f"Scrolled to and clicked element with selector '{selector}'.")
    except Exception as e:
        log.error(f"Error scrolling to and clicking element with selector '{selector}': {e}")
        raise e


def assert_redirect_url_starts_with(webdriver, expected_url):
    """Asserts if the current URL of the driver starts with the expected URL within the specified timeout."""
    current_url = webdriver.current_url
    try:
        assert current_url.startswith(
            expected_url
        ), f"Redirection failed. Expected URL: {expected_url}, Actual URL: {current_url}"
        log.info(f"Redirected to URL: {expected_url}")
    except AssertionError as e:
        log.error(f"Assertion failed: {e}")
        raise e


def wait_element_and_return_text(webdriver, selector, wait_time=60):
    """Waits for an element identified by XPath to become visible, retrieves its text, and returns it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        log.info(f"Element with selector '{selector}' and '{element.text}' found and visible.")
        return element.text if element else None
    except TimeoutException as e:
        log.error(f"Timeout waiting for element with selector '{selector}': {e}")
        raise e


def get_word_from_element(text, index):
    """Gets the word from an element, use index to select word position."""
    try:
        word = text.split()[index]
        log.info(f"Got word '{word}' from element with text '{text}'.")
        return word
    except Exception as e:
        log.error(f"Error getting word from element with text '{text}': {e}")
        raise e


def assert_element_href_contains_task_id(webdriver, selector, task_id, wait_time=60):
    """Asserts that an element identified by a selector contains an 'href' attribute with the given task_id."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.presence_of_element_located((By.XPATH, selector)))
        href = element.get_attribute("href")
        assert href is not None and f"/task/{task_id}" in href, f"Invalid href attribute: {href}"
        log.info(f"Element's href attribute contains the task ID '{task_id}'.")
    except TimeoutException as e:
        log.error(f"Timeout waiting for element with selector '{selector}': {e}")
        raise e


def wait_for_text_change_and_assert(webdriver, actual_text, selector, expected_text, wait_time=60):
    """Waits for the text of an element identified by the selector to change
    and asserts that it is equal to the expected text."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.presence_of_element_located((By.XPATH, selector)))

        wait.until(lambda webdriver: element.text != actual_text and element.text == expected_text)
        new_text = element.text

        log.info(f"Text of element with selector '{selector}' changed to '{new_text}'. Assertion...")
        assert new_text == expected_text, f"Text did not change to '{expected_text}'."
    except TimeoutException as e:
        log.error(f"Timeout waiting for text change in element with selector '{selector}': {e}")
        raise e


def change_focus_to_iframe(webdriver, selector, wait_time=60):
    """Changes the focus of the WebDriver to an iframe identified by the provided selector."""
    try:
        iframe = WebDriverWait(webdriver, wait_time).until(EC.presence_of_element_located((By.XPATH, selector)))
        webdriver.switch_to.frame(iframe)
        time.sleep(3)
        log.info(f"Switched focus to iframe with selector: {selector}")
    except TimeoutException as e:
        log.error(f"Timeout occurred: {e}")
        raise e


def change_focus_to_default_content(webdriver):
    """Changes the focus of the WebDriver back to default content."""
    try:
        webdriver.switch_to.default_content()
        time.sleep(3)
        log.info("Changed focus to main window")
    except Exception as e:
        log.info(f"n error occurred while changing the focus to main window: {e}")
        raise e


def execute_script(webdriver, script, wait_time=1):
    """Executes a script on the current page."""
    try:
        webdriver.execute_script(script)
        time.sleep(wait_time)
        log.info(f"Executed script: {script}")
    except Exception as e:
        log.error(f"An error occurred while executing script: {e}")
        raise e


def upload_file_with_send_keys(webdriver, selector, file_path):
    """Uploads a file using send keys"""
    try:
        file_input = webdriver.find_element(By.CSS_SELECTOR, selector)
        file_input.send_keys(file_path)
        log.info(f"Uploaded file using send keys: {file_path}")
    except Exception as e:
        log.error(f"An error occurred during file upload: {e}")
        raise e


def press_esc(webdriver):
    """Press ESC key"""
    try:
        ActionChains(webdriver).send_keys(Keys.ESCAPE).perform()
        log.info("Pressed ESC key")
    except Exception as e:
        log.error(f"An error occurred while pressing ESC key: {e}")
        raise e


def navigate_to_url(webdriver, url, wait_time=60):
    """Navigate to the specified URL and set a timeout for page load"""
    try:
        webdriver.set_page_load_timeout(wait_time)
        webdriver.get(url)
        log.info(f"Successfully navigated to URL: {url}")
    except TimeoutException as e:
        log.error(f"Timeout while navigating to URL: {url}")
        raise e
