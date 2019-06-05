@fixture.browser.chrome
Feature: Filter Resources by Tags
    Scenario: Filter just to Case Studies
    Given The user is on Datadog's resource page
    When she clicks the case study filter
    Then the container orchestration blog should not appear