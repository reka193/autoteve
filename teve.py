from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


usernameStr = 'USERNAME'
passwordStr = 'PASSWORD'

browser = webdriver.Chrome('/media/reka/Data/prog/teveclub/chromedriver')
browser.get('https://teveclub.hu')

username = browser.find_element_by_name('tevenev')
username.send_keys(usernameStr)
password = browser.find_element_by_name('pass')
password.send_keys(passwordStr)

form = browser.find_element_by_name('loginform')
form.submit()

browser.get('https://teveclub.hu/myteve.pet')
try:
    etet = browser.find_element_by_xpath('//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[3]/td[1]/center/div/form/input')
    etet.click()
except NoSuchElementException:
    pass

browser.get('https://teveclub.hu/tanit.pet')
try:
    learn = browser.find_element_by_xpath('//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[1]/td/font/b/div/form[1]/div/input')
    learn.click()
except NoSuchElementException:
    pass

browser.get('https://teveclub.hu/logout.pet')


