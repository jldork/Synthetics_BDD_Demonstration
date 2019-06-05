from selenium import webdriver

def browser_chrome(context, timeout=30, **kwargs):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.notifications" : 2
        }
    )
    # -- SETUP-FIXTURE PART:
    browser = webdriver.Chrome(options=chrome_options)
    context.browser = browser
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    browser.quit()