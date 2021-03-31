from selenium import webdriver
import time
import os

num = 1

while num != 0:
    ret = 0

    try:
        options = webdriver.chrome.options.Options()
        options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome('chromedriver.exe', options=options)

        driver.get('https://id.heroku.com/login')
        time.sleep(1)
        driver.find_element_by_id('email').send_keys(os.environ['herokuemail'])
        driver.find_element_by_id('password').send_keys(os.environ['herokupass'])
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div[2]/div[3]/div[1]/a/div/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div[1]/div[1]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/li[9]/a').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div[3]/button[2]').click()
        time.sleep(10)

    except Exception as ex:
        print(f"[ Error ]{str(ex).rstrip()}\n\n")
        ret = 1

    finally:
        driver.close()
        time.sleep(3)
        num = ret
