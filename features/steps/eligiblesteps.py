from behave import given, when, then
from selenium.webdriver.common.by import By
from features.helpers import wait_visible


@given('I go to start page')
def open_start_page(context):
    context.driver.get(context.base_url + '/')


@when('I click on start button')
def click_start_button(context):
    context.driver.find_element_by_css_selector('a.cta.cta-start.mt-20.mb-20').click()


@then('I select yes in all answers')
def select_yes_all_answers(context):
    context.driver.find_element_by_css_selector('label[for="affected_covid_19-yes"]').click()
    context.driver.find_element_by_css_selector('label[for="country-yes"]').click()
    context.driver.find_element_by_css_selector('label[for="age-yes"]').click()


@then('I select no in an answer')
def select_no_in_an_answer(context):
    context.driver.find_element_by_css_selector('label[for="affected_covid_19-yes"]').click()
    context.driver.find_element_by_css_selector('label[for="country-yes"]').click()
    context.driver.find_element_by_css_selector('label[for="age-no"]').click()


@then('I select next')
def click_next_button(context):
    context.driver.find_element_by_css_selector("div.form-group button").click()


@then('verify user not eligible text shows up')
def verify_user_not_eligible_text(context):
    wait_visible(context, By.CSS_SELECTOR, '#general-not-eligible',
                 "'Not eligible' message is not displayed")


@then('verify consent to participate shows up')
def verify_consent_shows_up(context):
    wait_visible(context, By.CSS_SELECTOR, 'h2[class="page-title uppercase"]',
                 "Consent to participate page is not displayed")


@then('close browser')
def close_browser(context):
    context.driver.close()
