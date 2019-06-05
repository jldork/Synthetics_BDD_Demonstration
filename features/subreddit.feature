@fixture.browser.chrome
Feature: Search for subreddit
    Scenario: Search for /r/Dublin
    Given The user is on Reddit
    When He or she searches for Dublin
    Then /r/Dublin should be the first search result