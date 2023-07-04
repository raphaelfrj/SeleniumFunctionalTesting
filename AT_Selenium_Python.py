from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
servico=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)

# Site Access
browser.get("https://saucedemo.com")
browser.implicitly_wait(5)
browser.maximize_window()

# Login - Part 1
browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
time.sleep(1)
browser.find_element('xpath', '//*[@id="password"]').send_keys('secret_sauce')
time.sleep(1)
browser.find_element('xpath', '//*[@id="login-button"]').click()
time.sleep(1)
assert browser.find_element('xpath', '//*[@id="header_container"]/div[2]/span').is_displayed()

# Add Cart - Part 2
browser.find_element('xpath', '//*[@id="item_4_title_link"]/div').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="back-to-products"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
time.sleep(1)

# Buying the products
browser.find_element('xpath', '//*[@id="checkout"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="first-name"]').send_keys('Raphael')
time.sleep(1)
browser.find_element('xpath', '//*[@id="last-name"]').send_keys('Frajácomo')
time.sleep(1)
browser.find_element('xpath', '//*[@id="postal-code"]').send_keys('00000-0000')
time.sleep(1)
browser.find_element('xpath', '//*[@id="continue"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="finish"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="back-to-products"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="react-burger-menu-btn"]').click()
time.sleep(1)
browser.find_element('xpath', '//*[@id="logout_sidebar_link"]').click()
time.sleep(1)

time.sleep(5)



