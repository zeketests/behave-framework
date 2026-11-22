# Selenium with Python Behave (BDD) Framework

![image](https://user-images.githubusercontent.com/67669609/103450271-6f3ae900-4c92-11eb-9a77-05e816d020fe.png)

## Introduction
A BDD test automation framework that uses [Behave](https://behave.readthedocs.io/) (Gherkin) and Selenium WebDriver, with [Allure](https://pypi.org/project/allure-behave/) reports.

## Project structure
```
behave-framework/
├── behave.ini              # Behave settings + test configuration (userdata)
├── requirements.txt        # Python dependencies
└── features/
    ├── *.feature           # Scenarios written in Gherkin
    ├── environment.py      # Hooks: browser setup/teardown, screenshots on failure
    ├── helpers.py          # Shared helpers (e.g. wait_visible)
    ├── pages/              # Page locators
    └── steps/              # Step definitions
```

## Setup
### 1. Install Python
Download Python 3.8 or newer from the [Python webpage](https://www.python.org/downloads/).

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
```
Activate it on Windows:
```bash
venv\Scripts\activate
```
Activate it on macOS / Linux:
```bash
source venv/bin/activate
```

### 3. Install the requirements
This installs Behave, Selenium and Allure Behave:
```bash
pip install -r requirements.txt
```

### 4. Install a browser driver
Selenium 3 needs the driver for your browser on your `PATH`:
- Firefox (default): [geckodriver](https://github.com/mozilla/geckodriver/releases)
- Chrome: [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/). Its major version must match your Chrome version.

## Running tests
Run the whole suite:
```bash
behave
```
Run one feature file:
```bash
behave features/login.feature
```
Run in headless Chrome:
```bash
behave -D browser=chrome -D headless=true
```

## Configuration
Settings live in `behave.ini` under `[behave.userdata]`. Override any of them from the command line with `-D key=value`.

| Setting | Default | Description |
|---|---|---|
| `browser` | `firefox` | `firefox` or `chrome` |
| `headless` | `false` | Run without opening a browser window |
| `base_url` | QA site URL | Site under test |
| `implicit_wait` | `10` | Seconds Selenium waits when looking for elements |
| `browser_binary` | *(empty)* | Optional path to a specific browser executable |

How the framework behaves:
- The browser is always closed after each scenario, even when a step fails.
- When a step fails, a screenshot is attached to the Allure report.
- Verification steps wait for the element to be visible and fail with a clear message if it isn't.

## Tags
Scenarios tagged `@wip` are work in progress and are skipped by default (`default_tags = -@wip` in `behave.ini`).
Run only them:
```bash
behave --tags=@wip
```

## Allure reports
Run the tests with the Allure formatter. This example saves the results in a folder named after the run date:
```bash
behave -f allure_behave.formatter:AllureFormatter -o results/2026-11-22
```
Then open the HTML report:
```bash
allure serve results/2026-11-22
```
The `results/` folder is ignored by git.

### Report example:
![allure-report](https://user-images.githubusercontent.com/67669609/103218166-1c131000-48f9-11eb-9c64-bdbbd8383765.png)

Reports can be uploaded to [Netlify](https://www.netlify.com/) so other team members can see them.

## Known issues
### `'allure' is not recognized as an internal or external command...`
The Allure command-line tool is separate from the `allure-behave` Python package. Install it with npm:
```bash
npm install -g allure-commandline
```
Or download it from the [Allure website](https://allurereport.org/docs/install/) and add its `bin` folder to your `PATH`.

### `ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.`
The Allure command-line tool needs Java. Install a [JDK](https://adoptium.net/) and set `JAVA_HOME` to its folder, for example `C:\Program Files\Java\jdk-17`.

### `This version of ChromeDriver only supports Chrome version X`
Your ChromeDriver and Chrome versions don't match. Download the ChromeDriver that matches your Chrome version.

## References
- [Behave docs](https://behave.readthedocs.io/en/latest/index.html)
- [Selenium documentation](https://www.selenium.dev/documentation/)
- [Gherkin reference](https://cucumber.io/docs/gherkin/reference/)
- [Allure Behave](https://pypi.org/project/allure-behave/)
- [Behavior-driven Python - Opensource.com](https://opensource.com/article/18/5/behavior-driven-python)

## Cool videos
- [Behavior-Driven Python - PyCon 2018](https://www.youtube.com/watch?v=EtIAbfCrsFI&t=344s&ab_channel=PyCon2018)
- [Gherkin Tutorial](https://www.youtube.com/watch?v=KP0vpVLatMc&ab_channel=RevalGovender)

## Contributing
Pull requests and new ideas are always welcome.

## To Do
- Add locators for the Results, FAQ, Resources, Our Partners and Contact US pages (currently `@wip`).
- Add integration with Slack.
