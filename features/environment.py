from behave import use_fixture

from features.fixtures import save_screenshot_at_the_end_of_the_failed_tests , web_context
from features.fixtures import config_log


def before_all(context):
    use_fixture(config_log, context)
    print("Starting the tests")

def before_scenario(context, scenario):
    use_fixture(web_context , context, scenario)
    
def after_scenario(context, scenario):
    if scenario.status == "failed":
        use_fixture(save_screenshot_at_the_end_of_the_failed_tests, context, scenario.name)  