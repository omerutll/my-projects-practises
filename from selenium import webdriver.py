from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
driver_path = r"C:\Users\omers\OneDrive\Masaüstü\Python kursu\python\drivers\chromedriver.exe"

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

print("login...\n")
name = input("gööndereceginiz kisinin ismini girin: ")
count = int(input("mesaj sayiyis: "))
msg = input("mesajinizi giriniz: ")

user = driver.find_element(By.XPATH, '//span[@title="{}"]'.format(name))
user.click()
msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')
for i in range(count):
    msgBox.send__keys(msg)
    sendButton = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/button')
    sendButton.click()
