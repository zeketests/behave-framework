from behave import when, then
from selenium.webdriver.common.by import By

from features.helpers import wait_visible


@when('I click log in button')
def click_log_in_button(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Log In')]").click()


@when('I put my email "{user}" and password "{password}"')
def type_user_and_password(context, user, password):
    context.driver.find_element_by_css_selector('#email').send_keys(user)
    context.driver.find_element_by_css_selector('#password').send_keys(password)


@when('I confirm the log in')
def click_confirm_log_in(context):
    context.driver.find_element_by_css_selector('#btn-login').click()


@then('baseline survey shows up')
def baseline_survey_is_displayed(context):
    heading = wait_visible(context, By.XPATH, "//h2[contains(text(),'Eligibility')]",
                           "Baseline survey not showing up")
    assert heading.text.strip() == "Eligibility", \
        "Expected 'Eligibility' heading, got '%s'" % heading.text


@then('please enter a valid mail pop up shows up')
def invalid_mail_message(context):
    wait_visible(context, By.CSS_SELECTOR, '#error-message',
                 "'Please enter a valid email' message is not displayed")


@then('wrong email or password shows up')
def invalid_password_message(context):
    wait_visible(context, By.CSS_SELECTOR, '#error-message',
                 "'Wrong email or password' message is not displayed")
