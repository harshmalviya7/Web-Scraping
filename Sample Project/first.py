from selenium import webdriver

PATH='C:/Users/Desktop/Selenium/chromedriver.exe'

driver=webdriver.Chrome(executable_path=PATH)

driver.get("https://en.wikipedia.org/wiki/Wiki")
#opens the wikipedia

driver.close()
#closes the chrome

driver.quit()
#quits the driver

print("Test complete")
#output generated in cmd prompt
