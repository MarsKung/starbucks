from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
import http.client
import os
from dotenv import load_dotenv

load_dotenv()

PASSWD = os.getenv("PASSWD", "Test@1234")

class tmpmail():
    def __init__(self):
        self.conn = http.client.HTTPSConnection("mailsac.com")
        self.headers = { 'Mailsac-Key': os.getenv("MAILSAC_KEY") }
        # self.address = "itakxraxbstmkosxtdsv"
        

    def create_address(self):
        self.address = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=20))
        self.conn.request("GET", f"/api/addresses/{self.address}@mailsac.com/message-count", headers=self.headers)

        res = self.conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        #print(data)
        if data["count"] >= 1:
            self.create_address()
        
        
        return self.address

    def get_message(self):

        conn = http.client.HTTPSConnection("mailsac.com")

        conn.request("GET", f"/api/addresses/{self.address}@mailsac.com/messages", headers=self.headers)

        res = conn.getresponse()
        data = res.read()

        #print(data.decode("utf-8"))
        return data.decode("utf-8")

# 設定 Chrome 選項
chrome_options = Options()
#chrome_options.add_argument("--headless")  # 啟用無頭模式
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

# 初始化 WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 開啟網頁
driver.get('https://myotgcard.starbucks.com.tw/StarbucksMemberWebsite/RegisterTerms.html')
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[4]/p[1]/a[2]'))
)
mail = tmpmail()
mail_address = mail.create_address()
button.click()
mail_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[3]/div/div[2]/input'))
)
mail_input.send_keys(mail_address + "@mailsac.com")
pwd_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[3]/div/input')
pwd_input.send_keys(PASSWD)
cpwd_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[4]/div/input')
cpwd_input.send_keys(PASSWD)
name_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[5]/input')
name_input.send_keys(mail_address)
y_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[6]/ul[1]/li[1]/input')
y_input.send_keys("1999")
m_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[6]/ul[1]/li[2]/input')
m_input.send_keys("01")
d_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[6]/ul[1]/li[3]/input')
d_input.send_keys("01")
phone_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[7]/input')
phone_input.send_keys("0999999999")
hint_select = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[8]/select')
hint_select.send_keys("第一個手機型號是？ What was the model of your first cell phone?")
hint_input = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[8]/input')
hint_input.send_keys("nokia")
news_click = driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div/div[9]/ul/li[2]/input')
news_click.click()
button = driver.find_element(By.XPATH, '/html/body/form/div/div[4]/a[2]')
button.click()
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[4]/div/p/a[3]'))
)
button.click()
driver.implicitly_wait(10)
time.sleep(5)
while 1:
    messages = json.loads(mail.get_message())
    print(len(messages))
    for message in messages:
        # print(message)
        if "星巴克" in message['subject']:
            #print("找到驗證信")
            verification_link = message["links"][0] 
            driver.get(verification_link)
            driver.implicitly_wait(10)
            driver.quit()
            input(mail_address + "@mailsac.com\npress Enter to exit")
            exit(0)
    time.sleep(5)



