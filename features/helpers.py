"""Shared helpers for step definitions."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_visible(context, by, locator, message, timeout=10):
    """Wait for an element to be visible; fail the step with `message` if it never is."""
    try:
        return WebDriverWait(context.driver, timeout).until(
            EC.visibility_of_element_located((by, locator)))
    except Exception:
        raise AssertionError(message)
