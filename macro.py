from selenium import webdriver
import time
import socket
import os


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except:
        return False


while internet() is False:
    print('Please connect the internet...')
    time.sleep(1)
    os.system('cls')
    time.sleep(1)

print('자가진단 매크로가 시작되었습니다.')

ret = 0

try:
    options = webdriver.chrome.options.Options()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome('chromedriver.exe', options=options)

    wait = .5

    driver.get('https://hcs.eduro.go.kr/') # 사이트 접속
    time.sleep(1)
    driver.find_element_by_id('btnConfirm2').click() # 자가진단 참여하기 버튼 클릭
    time.sleep(wait)
    driver.find_element_by_class_name('searchBtn').click() # 학교 검색
    time.sleep(wait)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[7]').click() # 대전광역시 선택
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]').click() # 고등학교 선택
    driver.find_element_by_class_name('searchArea').send_keys('대덕소프트웨어마이스터고등학교\n') # 대덕소프트웨어마이스터고등학교 검색
    time.sleep(wait)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click() # 검색 결과 선택
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click() # 학교선택 버튼 클릭
    time.sleep(wait)
    driver.find_element_by_id('user_name_input').send_keys('손영웅') # 이름 입력
    driver.find_element_by_id('birthday_input').send_keys('030919\n') # 생년월일 입력
    time.sleep(wait*4)
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys('1234\n') # 암호 입력
    time.sleep(wait*6)
    driver.find_element_by_class_name('name').click() # 손영웅 클릭
    time.sleep(wait*4)
    try:
        alert = driver.switch_to.alert
        message = alert.text
        alert.accept()
        driver.close()
        os.system('taskkill /f /im chromedriver.exe')
        print('Alert창: ' + message)
        time.sleep(3)

    except Exception as ex:
        print('[ Info ]\n로그인 완료')
    driver.find_element_by_id('survey_q1a1').click() # 코로나 의심 증상 없음
    driver.find_element_by_id('survey_q2a1').click() # 코로나 검사 결과를 기다리고 있지 않음
    driver.find_element_by_id('survey_q3a1').click() # 자가격리가 이루어지고 있지 않음
    driver.find_element_by_id('btnConfirm').click() # 제출 버튼 클릭
    time.sleep(2) if options.headless else time.sleep(5)
    print('[ Info ]\nTask failed successfully')

except Exception as ex:
    with open('error.log', 'a+t') as f:
        f.write(f"[ {time.strftime('%c', time.localtime(time.time()))} ]\n{str(ex).rstrip()}\n\n")
        print(f"[ Error ]{str(ex).rstrip()}\n\n")
    ret = 1

finally:
    driver.close()
    os.system('taskkill /f /im chromedriver.exe')
    time.sleep(3)
    exit(ret)
