from selenium import webdriver
import time

def macro():
    print('자가진단 매크로가 시작되었습니다.')
    
    ret = 0

    try:
        options = webdriver.chrome.options.Options()
        options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', options=options)

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
            print('Alert창: ' + message)
            time.sleep(3)
            ret = 1

        except Exception as ex:
            print('[ Info ]\n로그인 완료')

        driver.find_element_by_id('survey_q1a1').click() # 코로나 의심 증상 없음
        driver.find_element_by_id('survey_q2a1').click() # 코로나 검사 결과를 기다리고 있지 않음
        driver.find_element_by_id('survey_q3a1').click() # 자가격리가 이루어지고 있지 않음
        driver.find_element_by_id('btnConfirm').click() # 제출 버튼 클릭
        time.sleep(2) if options.headless else time.sleep(5)
        print('[ Info ]\nTask failed successfully')
        
    except Exception as ex:
        print(f"[ Error ]{str(ex).rstrip()}\n\n")
        ret = 1

    finally:
        driver.close()
        time.sleep(3)
        return ret


num = 1
while num != 0:
    num = macro()