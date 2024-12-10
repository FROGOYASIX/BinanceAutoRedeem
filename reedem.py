from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random

def create_driver():
    # Configure Chrome Options
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection by disabling automation flag
    options.add_argument("--disable-infobars")
    options.add_argument("--incognito")  # Use incognito mode
    options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

    # Initialize WebDriver with updated settings
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.binance.com/en/login")
    time.sleep(random.uniform(25, 35))  # Longer random delay for manual login
    
    return driver

def random_delay(base=2, variance=3):
    """Introduce a random delay to simulate human behavior."""
    time.sleep(base + random.uniform(0, variance))

def human_typing(element, text):
    """Simulate human typing by adding a small random delay between keystrokes."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

def redeem_red_packet(packet_code, driver):
    try:
        # Navigate to Red Packet redemption page
        driver.get("https://www.binance.com/en/my/wallet/account/payment/cryptobox")
        random_delay(2, 3)

        # Input the Red Packet code
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bn-textField-input"))
        )
        human_typing(code_input, packet_code)

        # Click the "Claim" button
        redeem_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'bn-button') and text()='Claim']")
            )
        )
        random_delay(1, 2)
        redeem_button.click()
        random_delay(2, 3)

        # Click the "Open" button
        open_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'bn-button') and text()='Open']")
            )
        )
        random_delay(1, 2)
        open_button.click()
        random_delay(3, 5)

        print("Redemption successful!")
    except Exception as e:
        print(f"Error redeeming code")

# Main execution
if __name__ == "__main__":
    driver = create_driver()
    try:
        redeem_red_packet("your_red_packet_code_here", driver)
    finally:
        driver.quit()
