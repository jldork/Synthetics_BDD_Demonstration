import time
from behave import given, when, then

@given("The user is on Datadog's resource page")
def user_on_datadog_resources(context):
    context.browser.get("https://www.datadoghq.com/resources/")

@when('she clicks the case study filter')
def user_clicks_case_study_filter(context):
    greys = context.browser.find_elements_by_class_name("grayscale")
    
    assert len(greys) == 0

    case_study_button = context.browser.find_element_by_xpath("//button[@data-filter='category-case-study']")
    case_study_button.click()

@then('the container orchestration blog should not appear')
def missing_orchestration_blog_post(context):
    time.sleep(1)
    # Check Greyscale
    greys2 = context.browser.find_elements_by_class_name("grayscale")
    assert len(greys2) > 0