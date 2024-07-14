# Visit the URL https://www.saucedemo.com/ and login with the following credentials :-
# Username: standard_user
# Password: secret_sauce
# Try to fetch the following using Python Selenium :-
# 1.) Title of the webpage
# 2.) Current URL of the webpage
# 3.) Extract the entire contents of the webpage and save it in a Text file whose name will be "Webpage_task_11.txt"

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

user_name=driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")
time.sleep(2)

password=driver.find_element(By.NAME,"password")
password.send_keys("secret_sauce")
time.sleep(2)

title = driver.title
print("Title:", title)


current_url = driver.current_url
print("Current URL:", current_url)

page_source=driver.page_source

with open("Webpage_task.txt","w",encoding="utf-8")as file:
    file.write(page_source)

driver.quit()