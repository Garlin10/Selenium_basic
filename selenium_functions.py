import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re  # Import the regular expressions module

def start_browser():
    # Function to start a Selenium WebDriver browser instance
    # Automatically download and install the latest compatible ChromeDriver
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    return driver
def open_url(driver, url):
    # Function to navigate to a specified URL
    driver.get(url)
def is_element_visible(driver, locator, by=By.XPATH):
    # Function to check if an element is visible
    try:
        return driver.find_element(by, locator).is_displayed()
    except:
        return False

def wait_for_element(driver, locator, timeout=10, by=By.XPATH):
    # Function to wait until an element is visible
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((by, locator)))

def click_button(driver, locator, by=By.XPATH):
    # Function to click on a button
    button = driver.find_element(by, locator)
    button.click()

def write_text_in_field(driver, locator, text, by=By.XPATH):
    # Function to write text in an input field
    input_field = driver.find_element(by, locator)
    input_field.clear()
    input_field.send_keys(text)

def get_current_url(driver):
    # Function to return the current URL
    return driver.current_url

if __name__ == "__main__":
    # Example usage
    driver = start_browser()
    # Replace 'your_locator_here' with actual JS path or XPath
    # Example: wait_for_element(driver, 'your_locator_here', by=By.XPATH)
    url_to_open = "https://www.example.com"
    open_url(driver, url_to_open)
    click_button(driver, '/html/body/div/p[2]/a',By.XPATH)