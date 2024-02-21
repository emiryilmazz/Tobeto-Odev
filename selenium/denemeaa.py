from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class TobetoGirisYap:

    def __init__(self) -> None:
           # her test başında çalışır chrome ve tam ekran yapmayı sağlar yani ön ayar için
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        


       
        

    def test_tobeto_giris_yap(self):
        self.driver.get("https://tobeto.com/giris")

        email = self.driver.find_element(By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']")
        email.send_keys("denemehesabi292@outlook.com")
        sleep(1)
        password =self.driver.find_element(By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']") 
        password.send_keys("987654")
        sleep(4)
        giris_yap_button = self.driver.find_element(By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']")
        giris_yap_button.click()
        sleep(1)

        self.driver.save_screenshot("tobetogiris.png")
        sleep(1)

        text_info = WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[role='alert'] > .toast-body")))
        assert text_info.text == "• Giriş başarılı."


    def tearDown(self):# her test  sonunda çalışır  ve tarayıcı kapanır.
        self.driver.quit()




deneme=TobetoGirisYap()
deneme.test_tobeto_giris_yap()
deneme.tearDown()