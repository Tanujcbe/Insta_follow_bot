from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import instapi
import time
import random
i=0
j=0
driver=webdriver.Chrome(executable_path="G:\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.instagram.com")
time.sleep(2)
elem=driver.find_element_by_name('username')
elem.send_keys("YOUR_EMAIL")
el=driver.find_element_by_name('password')
el.send_keys("YOUR_PASSWORD")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[3]/div[1]/a/div').click()
time.sleep(2)
for i in range (100):
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(int(2)+int(i))+']/div[3]/button').click()
        i+=1
        print(i)
        a=random.randint(0,3)
        time.sleep(a)
    except:
        j+=1
        print(j)
    time.sleep(1)
    if i% random.randint(1,5)==0:
        b=random.randint(0,10)
        time.sleep(b)

