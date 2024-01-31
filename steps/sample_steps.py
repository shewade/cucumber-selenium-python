from behave import given, when, then
from selenium import webdriver

@given('I open the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('I navigate to "{url}"')
def step_impl(context, url):
    context.driver.get(url)

@then('I should see the title "{expected_title}"')
def step_impl(context, expected_title):
    actual_title = context.driver.title
    assert actual_title == expected_title, f'Expected title "{expected_title}", but got "{actual_title}"'

@then('the browser should be closed')
def step_impl(context):
    context.driver.quit()