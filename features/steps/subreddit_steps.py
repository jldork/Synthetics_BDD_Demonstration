import time
from behave import given, when, then

@given("The user is on Reddit")
def user_on_reddit(context):
    context.browser.get("http://www.reddit.com")

@when('He or she searches for Dublin')
def user_searches_for_dublin(context):
    search_bar = context.browser.find_element_by_id('header-search-bar')
    search_bar.send_keys("dublin")
    search_bar.send_keys(u'\ue007') # Hit the enter key

@then('/r/Dublin should be the first search result')
def r_dublin_is_first_result(context):
    time.sleep(1)
    subreddits = context.browser.find_elements_by_partial_link_text('r/')
    assert 'r/Dublin' in subreddits[0].text