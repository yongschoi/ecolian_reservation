from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=options)
driver.implicitly_wait(1)

driver.get(url='http://localhost:8081')

login_link = driver.find_element_by_xpath('//*[@id="inspire"]/div/nav/div[1]/div/a[2]/div[2]/div')
login_link.click()

id_input = driver.find_element_by_id('input-22')
id_input. send_keys('yongs@naver.com')

pass_input = driver.find_element_by_id('input-25')
pass_input.send_keys('123')

login_btn = driver.find_element_by_xpath('//*[@id="inspire"]/div/main/div/div/div/div/div/div/button/span[1]')
login_btn.click()

date_input = driver.find_element_by_id('input-31')
date_input.send_keys('20210518')

name_input = driver.find_element_by_id('input-34')
name_input.send_keys('홍민수')

phone_input = driver.find_element_by_id('input-37')
phone_input.send_keys('010-5555-4522')

people_input = driver.find_element_by_id('input-40')
people_input.send_keys('4')

