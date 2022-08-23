# Author:Gangireddy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://github.com/login")
  return driver

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="login_field").send_keys("nallagondu")
  time.sleep(2)
  driver.find_element(by="id", value="password").send_keys("Ganga@github2" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value='//*[@id="details-ff8bc2"]/summary').click()
  print(driver.current_url)

print(main())

