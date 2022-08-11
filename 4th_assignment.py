from selenium import webdriver

PATH = "/Users/zachra/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ynet.co.il")

