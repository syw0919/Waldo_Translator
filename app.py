from googletrans import Translator
from selenium import webdriver
import time
import asyncio
import discord
import os

client = discord.Client()

mode = 1

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    global mode
    channel = message.channel
    
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    #if message.author.bot:
    #    return None

    if message.content.startswith('!waldohelp') or message.content.startswith('!help'):
        await channel.send('''
```
!waldohelp(!help) : 이것은 보여주다 너에게 도움말

!waldolink(!link) : 이것은 보여주다 연락 수단 에게 개발자 의 왈도 번역기
                    그리고 초대 연결 의 왈도 번역기

!waldohello(!hello) : 이것은 하다 인사

!waldotrans(!trans) <한국어 문장> : 이것은 번역하다 너의 언어 를 나의 언어 로

!waldomode(!mode) [1/2] : 이것은 번역하다 다양한 말투
    1(기본의) : 자연스러운
    2 : 역겨운
```
        ''')

        date = message.created_at
        print('[ {} ]'.format(message.author))
        print('[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        print(message.content)

    if message.content.startswith('!waldohello') or message.content.startswith('!hello'):
        await channel.send('안녕하신가! 힘세고 강한 아침, 만일 내게 물어보면,\n나는 왈도.')

        date = message.created_at
        print('[ {} ]'.format(message.author))
        print('[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        print(message.content)

    if message.content.startswith('!waldolink') or message.content.startswith('!link'):
        await channel.send('연락 수단 에게 개발자 의 왈도 번역기: https://discord.gg/UQMPMpGcbG')
        await channel.send('초대 연결 의 왈도 번역기: http://bit.ly/번역하다왈도체')

        date = message.created_at
        print('[ {} ]'.format(message.author))
        print('[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        print(message.content)

    if message.content.startswith('!waldotrans ') or message.content.startswith('!trans '):
        await channel.send('하다 번역 작업, 제발 기다리다...')

        translator = Translator()
            
        if mode == 1:
            textlist = message.content.split(' ')[1:]
            text = ' '.join(textlist)

            etextlist = []
            for translation in translator.translate(textlist, src='ko', dest='en'):
                etextlist.append(translation.text)
            etext = ' '.join(etextlist)

            ktext = translator.translate(etext, src='en', dest='ko').text
        
            await channel.send(f'```\n{ktext}\n```')

        if mode == 2:
            textlist = message.content.split(' ')[1:]
            text = ' '.join(textlist)
            
            etext = translator.translate(text, src='ko', dest='en').text
            etextlist = etext.split(' ')
            
            ktextlist = []
            for translation in translator.translate(etextlist, src='en', dest='ko'):
                ktextlist.append(translation.text)
            ktext = ' '.join(ktextlist).replace('...', '').replace('ㅏ', '하나의')
        
            await channel.send(f'```\n{ktext}\n```')

        date = message.created_at
        print('[ {} ]'.format(message.author))
        print('[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        print(message.content)

    if message.content.startswith('!waldomode') or message.content.startswith('!mode'):
        messagelist = message.content.split(' ')
        
        if len(messagelist) > 1:
            val = messagelist[1]

            if val == '1':
                mode = 1
                await channel.send('바꾸다 말투 자연스러운')
                
            elif val == '2':
                mode = 2
                await channel.send('바꾸다 말투 역겨운')
                
            else:
                await channel.send('그 입력 은 잘못된 형태의!')
        else:
            await channel.send('지금 말투: {}'.format('자연스러운' if mode == 1 else '역겨운'))

        date = message.created_at
        print('[ {} ]'.format(message.author))
        print('[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        print(message.content)

    if message.content.startswith('!자가진단'):
        ret = 1
        while ret != 0:
            ret = 0

            print('자가진단 매크로가 시작되었습니다.')

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

        date = message.created_at
        print('[ {} ]'.format(message.author))
        print('[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        print(message.content)

client.run(os.environ['token'])
