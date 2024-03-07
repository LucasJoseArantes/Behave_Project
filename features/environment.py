from behave import use_fixture

from features.configs.webdriver import get_webdriver
from features.fixtures import save_screenshot_at_the_end_of_the_failed_tests


def before_all(context):
    print("Starting the tests")
    context.webdriver = get_webdriver()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        use_fixture(save_screenshot_at_the_end_of_the_failed_tests, context, scenario.name)  

def after_all(context):
    context.webdriver.quit()
    print("Tests Finished")