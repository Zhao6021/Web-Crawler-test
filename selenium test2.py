import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/JieDa/Desktop/selenium test/chromedriver.exe"
driver = webdriver.Chrome(PATH)
my_account = "david.wz.jie@viewsonic.com"
my_password = "$David1206"

driver.get("https://stage.myviewboard.com/signin")
WebDriverWait(driver, 10).until(                                #讓瀏覽器等待(最多10秒)，等到ID為"mat-input-0"的element出現才繼續進行
        EC.presence_of_element_located((By.ID, "mat-input-0"))
    )
account_blank = driver.find_element_by_id("mat-input-0")
account_blank.send_keys(my_account)
login_but = driver.find_element_by_xpath("//*[@id=\"page-top\"]/app-landing/div/div/ng-component/main/div/div/div/div/div/div/form/div[2]/button")
login_but.click()
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pwinput"))
    )
password_blank = driver.find_element_by_id("pwinput")
password_blank.send_keys(my_password)
continue_but = driver.find_element_by_xpath("//*[@id=\"page-top\"]/app-landing/div/div/ng-component/main/div/div/div/div/div/div/form/div[3]/button")
continue_but.click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "footer"))
    )
confirm_but = driver.find_element_by_id("footer")
confirm_but.click()

time.sleep(10)