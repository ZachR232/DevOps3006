from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome()
my_driver.get("file:///Users/zachra/Downloads/tip_calc/index.html")
billamt = my_driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
people = my_driver.find_element(by="id", value="peopleamt")
people.send_keys("5")
music = my_driver.find_element(by="id", value="music")
music.send_keys("5")
my_driver.find_element(by="id", value="calculate").click()
expected = "8.00"
actual = my_driver.find_element(by="id", value="tip").text

assert expected == actual