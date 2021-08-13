from selenium import webdriver
import time
import os

options = webdriver.chrome.options.Options()
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', options=options)

num = 1

while num != 0:
    print('System restarting...')
    
    ret = 0

    try:
        driver.get('https://id.heroku.com/login')
        time.sleep(1)
        driver.find_element_by_id('email').send_keys(os.environ['herokuemail'])
        driver.find_element_by_id('password').send_keys(os.environ['herokupass'])
        driver.find_element_by_name('commit').click()
        print('login succeed')
        time.sleep(30)
        print('select "waldo-translator"')
        driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div[2]/div[3]/div[1]/a/div/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div[1]/div[1]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        print('select "Restart all dynos"')
        driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/li[9]/a').click()
        time.sleep(3)
        print('execute')
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div[3]/button[2]').click()
        time.sleep(10)

    except Exception as ex:
        print(f'[ Error ]\n{str(ex).strip()}\n\n')
        ret = 1

    finally:
        num = ret

driver.close()