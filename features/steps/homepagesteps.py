from behave import when, then
from selenium.webdriver.common.by import By

from features.helpers import wait_visible
from features.pages.homepage import (
    homepage_button, homepage_title, about_button, about_page_title)


def not_implemented(page):
    raise NotImplementedError(
        "%s page step has no locators yet - add them to features/pages/homepage.py" % page)


@when('I click the Home button')
def click_home_page_button(context):
    context.driver.find_element_by_css_selector(homepage_button).click()


@then('Home Page shows up')
def home_page_is_displayed(context):
    wait_visible(context, By.XPATH, homepage_title, "Home page title is not displayed")


@when('I click the About button')
def click_about_button(context):
    context.driver.find_element_by_css_selector(about_button).click()


@then('About Page shows up')
def about_page_is_displayed(context):
    wait_visible(context, By.XPATH, about_page_title, "About page title is not displayed")


# --- Not implemented yet: scenarios are tagged @wip and skipped by default ---

@when('I click the Results button')
def click_results_button(context):
    not_implemented('Results')


@then('Results Page shows up')
def results_page_shows_up(context):
    not_implemented('Results')


@when('I click the FAQ button')
def click_faq_button(context):
    not_implemented('FAQ')


@then('FAQ Page shows up')
def faq_page_shows_up(context):
    not_implemented('FAQ')


@when('I click the Resources button')
def click_resources_button(context):
    not_implemented('Resources')


@then('Resources Page shows up')
def resources_page_shows_up(context):
    not_implemented('Resources')


@when('I click the Our Partners button')
def click_partners_button(context):
    not_implemented('Our Partners')


@then('Our Partners Page shows up')
def partners_page_shows_up(context):
    not_implemented('Our Partners')


@when('I click the Contact US button')
def click_contact_button(context):
    not_implemented('Contact US')


@then('Our Contact US Page shows up')
def contact_page_shows_up(context):
    not_implemented('Contact US')
