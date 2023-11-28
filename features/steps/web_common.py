"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""

from selenium import webdriver
from configs import urlconfig
from webdriver_manager.firefox import GeckoDriverManager


def go_to(context, location):

    """
    Function to start an instance of the specified browser and navigate to the specified URL.
    :param location: the location or key in URLCONFIG for the URL to navigate to
    """

    gecko_path = GeckoDriverManager().install()
    context.driver = webdriver.Firefox(executable_path=gecko_path)

    # If the location does not start with 'http', assume it's a key in URLCONFIG
    if not location.startswith('http'):
        _url = urlconfig.URLCONFIG.get(location)
        base_url = urlconfig.URLCONFIG.get('base_url')
        url = base_url + _url

    # Navigate to the URL
    context.driver.get(url)

    return context.driver

def assert_page_title(context, expected_title):
    """
    Function to assert title of current page.
    :param expected_title:
    :param context:
    """

    actual_title = context.driver.title

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected.")

def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context:
    :param expected_url:
    """

    # get the current url
    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print("The page url is as expected.")

#======================================================================================#
def url_contains(context, text):

    current_url = context.driver.current_url
    if text in current_url:
        return True
    else: return False
aaa
def assert_url_contains(context, text):

    contains = url_contains(context, text)
    assert contains, f"Current url '{context.driver.current_url}' does not contain test '{text}'."

#======================================================================================#
def find_element(context, locator_attribute, locator_text):
    """
    Finds an element and returns the element object.
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)
    
#======================================================================================#
def find_elements(context, locator_attribute, locator_text):
    """
    Finds an element and returns the element object.
    :param context:
    :param locator_attribute: what to use to locate (example, id, class, xpath,....)
    :param locator_text: the locator text (ex. the id, the class, the name,...)
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_elements(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)

#======================================================================================#
def is_element_visible(element):
    '''
    Checks if element is visible and returns True or False
    '''

    if element.is_displayed():
        return True
    else:
        return False
#======================================================================================#
def assert_element_visible(context_or_element, locator_att=None, locator_text=None):
    '''
    Function to check if the passed in element is visible.
    Raises and exception if it is not exception.
    '''
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    if not element.is_displayed():
        raise AssertionError('The element is not displayed')

def type_into_element(context, input_value, locator_attribute, locator_text):

    input_filed = context.driver.find_element(locator_attribute, locator_text)
    input_filed.send_keys(input_value)

def click(context_or_element, locator_att=None, locator_text=None):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element.click()

# def element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):

#     if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
#         element = context_or_element
#     else:
#         element = context_or_element.driver.find_element(locator_att, locator_text)

#     element_text = element.text
#     if not case_sensitive:
#         if expected_text.lower() in element_text.lower():
#             return True
#         else:
#             return False
#     else:
#         return True if expected_text in element_text else False


# def assert_element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):

#     max_try = 5
#     sleep_bn_try = 2
#     for i in range(max_try):
#         try:
#             contains = element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive)
#             assert contains, "Element does not contain text"
#             break
#         except AssertionError:
#             print(f"Checking if element contains text. Retry number: {i}")
#             time.sleep(sleep_bn_try)
#     else:
#         raise Exception(f"Element with locator type '{locator_att}', and locator text '{locator_text}', "
#                         f"does not contains the text '{expected_text}'. Retried {max_try * sleep_bn_try} seconds")

# def assert_radio_is_selected(context_or_element, locator_att=None, locator_text=None):

#     if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
#         element = context_or_element
#     else:
#         element = context_or_element.driver.find_element(locator_att, locator_text)

#     is_checked = element.get_attribute('checked')
#     assert is_checked, f"The radio is not selected {element.get_attribute('name')}"
#     # import pdb; pdb.set_trace()

def get_element_text(context_or_element, locator_att=None, locator_text=None):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element_text = context_or_element.text
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)
        element_text = element.text

    return element_text
