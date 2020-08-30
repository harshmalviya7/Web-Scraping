from selenium import webdriver

PATH='C:/Users/aarti computer/Desktop/oneday/Selenium/chromedriver.exe'

driver=webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/Wiki")

driver.close()

driver.quit()

print("Test complete")