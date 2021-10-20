from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

DRIVER_PATH = "..\\chromedriver.exe"
SITE_URL = "https://www.facebook.com/"


def main():
    connector = SeleniumConnector(
        driver_path=DRIVER_PATH,
        site_url=SITE_URL,
    )

    email_input_field = connector.find_element_by_css_id("email")
    expected_email = "my.email@gmail.com"
    enter_text_in_input_field(
        input_field=email_input_field,
        text=expected_email,
    )
    retrieved_email = get_text_from_input_field(
        input_field=email_input_field,
    )
    print(f"Expected email: {expected_email}")
    print(f"Retrieved email: {retrieved_email}")


def enter_text_in_input_field(input_field: WebElement, text: str):
    input_field.clear()
    input_field.send_keys(text)


def get_text_from_input_field(input_field: WebElement):
    return input_field.get_attribute("value")


def submit_input_field(input_field: WebElement):
    input_field.send_keys(Keys.RETURN)


class SeleniumConnector:
    def __init__(self, driver_path: str, site_url: str):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get(site_url)

    @property
    def url(self):
        return self.driver.current_url

    def navigate_url(self, site_url: str):
        self.driver.get(site_url)

    def find_element_by_css_id(self, element_id: str):
        return self.driver.find_element(By.ID, element_id)


if __name__ == '__main__':
    main()
