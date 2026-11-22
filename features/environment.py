"""Behave hooks: browser setup/teardown and screenshots on failure.

Settings come from behave.ini [behave.userdata] and can be overridden on the
command line, e.g.:  behave -D browser=chrome -D headless=true
"""
from selenium import webdriver

try:
    import allure
except ImportError:  # allure-behave is optional
    allure = None

TRUE_VALUES = ("1", "true", "yes", "on")


def _flag(userdata, key, default=False):
    return str(userdata.get(key, default)).strip().lower() in TRUE_VALUES


def _create_driver(userdata):
    browser = userdata.get("browser", "firefox").strip().lower()
    headless = _flag(userdata, "headless")
    binary = userdata.get("browser_binary", "").strip()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        # Needed when running inside containers / CI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if binary:
            options.binary_location = binary
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        if binary:
            options.binary_location = binary
        return webdriver.Firefox(options=options)

    raise ValueError("Unsupported browser '%s' (use chrome or firefox)" % browser)


def before_all(context):
    userdata = context.config.userdata
    context.base_url = userdata.get("base_url", "").rstrip("/")
    context.implicit_wait = int(userdata.get("implicit_wait", 10))


def before_scenario(context, scenario):
    context.driver = _create_driver(context.config.userdata)
    if not _flag(context.config.userdata, "headless"):
        context.driver.maximize_window()
    context.driver.implicitly_wait(context.implicit_wait)


def after_step(context, step):
    if step.status != "failed" or not getattr(context, "driver", None):
        return
    try:
        png = context.driver.get_screenshot_as_png()
    except Exception as exc:  # browser may already be gone
        print("Could not take screenshot: %s" % exc)
        return
    if allure:
        allure.attach(png, name="failure - %s" % step.name,
                      attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    # Always quit, even if a step failed before "close browser" ran.
    driver = getattr(context, "driver", None)
    if driver:
        try:
            driver.quit()
        except Exception:
            pass  # already closed by the "close browser" step
        context.driver = None
