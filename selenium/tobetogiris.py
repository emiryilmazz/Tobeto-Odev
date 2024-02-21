from tobetoInfo import username,password
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

class Tobeto:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.username=username
        self.password=password

    def login(self):
        self.driver.get("https://tobeto.com/")
        time.sleep(3)

        giris_yap= self.driver.find_element(By.XPATH,"//div[@id='__next']//section[@class='web-header']/nav//a[@href='/giris']").click()
        time.sleep(3)

        username=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")               
        username.send_keys(self.username)

        password=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
        password.send_keys(self.password)
        time.sleep(3)
        

        self.driver.find_elements(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button").click()
        time.sleep(3)

        self.driver.save_screenshot("tobeto.png")
        time.sleep(3)

        welcome=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")
        print(welcome.text)

        excepted_mesaj="TOBETO'ya hoş geldin"

        # if actual_mesaj==welcome.text:
        #     print("başarili")
        # else:
        #     print("yanlış mesaj")

        # assert(excepted_mesaj,welcome.text)


        
tobeto=Tobeto(username,password)
tobeto.login()