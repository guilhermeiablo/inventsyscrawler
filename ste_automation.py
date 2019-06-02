from selenium import webdriver
from getpass import getpass
from time import sleep

usr = input('Enter your username or email id: ')
pwd = getpass('Enter your password : ')

driver = webdriver.Safari()
driver.get('https://stesa.inventsys.com.br/10762/item/list')

username_box = driver.find_element_by_name('username_email')
username_box.send_keys(usr)

password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_class_name('btn')
login_btn.submit()

sleep(5)

export_btn = driver.find_element_by_partial_link_text('Exportar')
export_btn.click()                    

sleep(5)

csv_btn = driver.find_element_by_xpath("//input[@value='csv']")
csv_btn.submit()

export_csv = driver.find_element_by_name('submit')
export_csv.submit()

