from selenium import webdriver
import time
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

f = open("tempmail", "a")

path = r"C:\Users\Killly\Desktop\python selenium\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.temp-mail.org")
print(driver.title)
time.sleep(10)

#id click-to-copy

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "click-to-copy"))
    )
    element.click()
    paste = pyperclip.paste()
    print(paste)
    f.write(paste)
    f.write("\n")
    f.close()
except:
    driver.quit()


