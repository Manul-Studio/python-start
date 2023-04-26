'''Command Line Emailer

Write a program that takes an email address and
string of text on the command line and then, using selenium,
logs in to your email account and sends an email of the string
to the provided address. (You might want to set up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook or Twitter account.'''

import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

install_dir = "/snap/firefox/current/usr/lib/firefox"
driver_loc = os.path.join(install_dir, "geckodriver")
binary_loc = os.path.join(install_dir, "firefox")

service = FirefoxService(driver_loc)
opts = webdriver.FirefoxOptions()
opts.binary_location = binary_loc
driver = webdriver.Firefox(service=service, options=opts)

driver.get('https://mail.google.com')

login = driver.find_element(By.ID, 'identifierId')
login.send_keys('tgestowyolczi@gmail.com')
loginNext = driver.find_element(By.ID, 'identifierNext')
loginNext.click()
haslo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type=password]')))
haslo.send_keys('Olczi123!')
hasloNext = driver.find_element(By.ID, 'passwordNext')
hasloNext.click()
send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.T-I-KE')))
send.click()
addr = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#\:65')))
addr.send_keys('dupa@gmail.com')