from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import asyncio
import discord
import sys
import os
import re

client = discord.Client()

mode = 1

admin = {}

async def log(message):
    global admin

    date = message.created_at
    try:
        msgtext = '[ USER INFO ]\n{} : {}\n[ SERVER INFO ]\n{} : {}\n[ CHANNEL INFO ]\n{} : {}\n[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]\n{}\n================'.format(
            message.author,
            message.author.id,
            message.channel.guild,
            message.channel.guild.id,
            message.channel,
            message.channel.id,
            date.year,
            date.month,
            date.day,
            (date.hour+9) % 24,
            date.minute,
            date.second,
            message.content
        )
    except:
        msgtext = '[ USER INFO ]\n{} : {}\n[ CHANNEL INFO ]\n{} : {}\n[ {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} ]\n{}\n================'.format(
            message.author,
            message.author.id,
            message.channel,
            message.channel.id,
            date.year,
            date.month,
            date.day,
            (date.hour+9) % 24,
            date.minute,
            date.second,
            message.content
        )
    print(msgtext)
    try:
        await admin.send(msgtext)
    except Exception as ex:
        print('No admin channel :thinking:')
        print(str(ex))

async def selfdiagnosis(channel):
    school = os.environ["school"]
    name = os.environ["name"]
    birth = os.environ["birth"]
    password = os.environ["pass"]
    num = 1
    while num != 0:
        print('자가진단 매크로가 시작되었습니다.')
        await channel.send('자가진단 매크로가 시작되었습니다.')

        ret = 1

        try:
            options = webdriver.chrome.options.Options()
            # options.add_argument('--headless')
            # options.add_argument("--disable-gpu")
            options.add_argument("--start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', options=options)

            wait = .5

            driver.get('https://hcs.eduro.go.kr/')  # 사이트 접속
            print('사이트 접속: https://hcs.eduro.go.kr/')
            await channel.send('사이트 접속: `https://hcs.eduro.go.kr/`')
            
            time.sleep(1)
            
            driver.find_element_by_id('btnConfirm2').click()  # 자가진단 참여하기 버튼 클릭
            
            time.sleep(wait)
            
            driver.find_element_by_class_name('searchBtn').click()  # 학교 검색
            
            time.sleep(wait)
            
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[7]').click()  # 대전광역시 선택
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]').click()  # 고등학교 선택
            driver.find_element_by_class_name('searchArea').send_keys(f'{school}\n')  # 학교 검색
            
            print(f'학교 검색: {school}')
            await channel.send(f'학교 검색: `{school}`')
            
            time.sleep(wait)
            
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()  # 검색 결과 선택
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()  # 학교선택 버튼 클릭
            
            time.sleep(wait)
            
            driver.find_element_by_id('user_name_input').send_keys(f'{name}')  # 이름 입력
            
            print(f'이름 입력: {name}')
            await channel.send(f'이름 입력: `{name}`')
            
            driver.find_element_by_id('birthday_input').send_keys(f'{birth}\n')  # 생년월일 입력
            
            print(f'생년월일 입력: {birth}')
            await channel.send(f'생년월일 입력: `{birth}`')
            
            time.sleep(wait*8)
            
            ##### 암호 입력
            driver.find_element_by_xpath('//input[@id="password"]').click()
            
            for i in password:
                WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, f'//a[@aria-label="{i}"]'))).click()
                
            time.sleep(3)
            
            print('암호 입력: ****')
            await channel.send('암호 입력: `****`')
            
            driver.find_element_by_id('btnConfirm').click()
            
            time.sleep(wait*6)
            
            driver.find_element_by_class_name('name').click()  # 손영웅 클릭
            
            time.sleep(wait*4)
            
            try:
                alert = driver.switch_to.alert
                m = alert.text
                alert.accept()
                driver.close()
                print('Alert창: ' + m)
                await channel.send(f'```\n[ Alert ]\n{m}\n```')
                time.sleep(3)
                ret = 0

            except Exception as ex:
                print('[ Info ]\n로그인 완료')
                await channel.send('로그인 완료')

            driver.find_element_by_id('survey_q1a1').click()  # 코로나 의심 증상 없음
            
            print('코로나 의심 증상 여부: 아니오')
            await channel.send('코로나 의심 증상 여부: `아니오`')
            
            # 코로나 검사 결과를 기다리고 있지 않음
            driver.find_element_by_id('survey_q2a1').click()
            
            print('코로나 검사 결과 대기 여부: 아니오')
            await channel.send('코로나 검사 결과 대기 여부: `아니오`')
            
            driver.find_element_by_id('survey_q3a1').click()  # 자가격리가 이루어지고 있지 않음
            
            print('자가격리 실행 여부: 아니오')
            await channel.send('자가격리 실행 여부: `아니오`')
            
            driver.find_element_by_id('btnConfirm').click()  # 제출 버튼 클릭
            
            print('제출')
            await channel.send('제출')
            
            time.sleep(2) if options.headless else time.sleep(5)
            print('[ Info ]\nTask failed successfully')
            await channel.send('자가진단을 완료하였습니다.')
            ret = 0

        except:
            print(f"[ Error ]", *sys.exc_info(), "\n", sep="\n")
            await channel.send(f"```\n[ Error ]\n{'\\n'.join(sys.exc_info())}\n```")

        finally:
            try:
                driver.close()
            except:
                print('There is no driver to close')
            time.sleep(3)
            num = ret

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    global admin

    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

    admin = client.get_channel(int(os.environ['adminchannel']))

    await admin.send(f"다음으로 로그인합니다\n{client.user.name}\n{client.user.id}\n================")


# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    global mode
    global admin
    channel = message.channel
    author = str(message.author)

    # 메세지를 보낸 사람이 봇일 경우 무시한다
    # if message.author.bot:
    #    return None

    if message.content.startswith('!waldohelp') or message.content.startswith('!help'):
        await log(message)

        await channel.send('''
```
!waldohelp(!help) : 이것은 보여주다 너에게 도움말

!waldolink(!link) : 이것은 보여주다 연락 수단 에게 개발자 의 왈도 번역기
                    그리고 invite link 의 왈도 번역기

!waldohello(!hello) : 이것은 하다 인사

!waldotrans(!trans) <한국어 문장> : 이것은 번역하다 너의 언어 를 나의 언어 로

!waldomode(!mode) [1/2] : 이것은 번역하다 다양한 말투
    1(기본의) : 자연스러운
    2 : 역겨운
```
        ''')

    if message.content.startswith('!waldohello') or message.content.startswith('!hello'):
        await log(message)

        await channel.send('안녕하신가! 힘세고 강한 아침, 만일 내게 물어보면,\n나는 왈도.')

    if message.content.startswith('!waldolink') or message.content.startswith('!link'):
        await log(message)

        await channel.send('연락 수단 에게 개발자 의 왈도 번역기: https://discord.gg/UQMPMpGcbG')
        await channel.send('Invite link 의 왈도 번역기: http://bit.ly/번역하다왈도체')

    if message.content.startswith('!waldotrans ') or message.content.startswith('!trans '):
        await log(message)

        await channel.send('하다 번역 작업, 제발 기다리다...')

        translator = Translator()

        text = re.sub(' +', ' ', message.content)

        if mode == 1:
            textlist = text.split(' ')[1:]
            text = ' '.join(textlist)

            etextlist = []
            for translation in translator.translate(textlist, src='ko', dest='en'):
                etextlist.append(translation.text)
            etext = ' '.join(etextlist)

            ktext = translator.translate(etext, src='en', dest='ko').text

            await channel.send(f'```\n{ktext}\n```')

            if len(text) > 15 and text == ktext:
                await channel.send('Error has been occured!\nSystem restarting(It may take a minute)...')
                await admin.send('Error has been occured!\nSystem restarting(It may take a minute)...')
                os.system('python restart.py')

        if mode == 2:
            textlist = text.split(' ')[1:]
            text = ' '.join(textlist)

            etext = translator.translate(text, src='ko', dest='en').text
            etextlist = etext.split(' ')

            ktextlist = []
            for translation in translator.translate(etextlist, src='en', dest='ko'):
                ktextlist.append(translation.text)
            ktext = ' '.join(ktextlist).replace('...', '').replace('ㅏ', '하나의')

            await channel.send(f'```\n{ktext}\n```')

            if len(text) > 15 and text == ktext:
                await channel.send('Error has been occured!\nSystem restarting(It may take a minute)...')
                await admin.send('Error has been occured!\nSystem restarting(It may take a minute)...')
                os.system('python restart.py')

    if message.content.startswith('!waldomode') or message.content.startswith('!mode'):
        await log(message)

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

    if message.content.startswith('!admin'):
        await log(message)

        if author == os.environ['admin']:
            admin = channel
            await admin.send('This channel is now the admin channel!\nThe command logs will be appear on here!')
        else:
            await channel.send('Who the fuck are you?')

    if message.content.startswith('!restart'):
        await log(message)

        if author == os.environ['admin']:
            await channel.send('System restarting(It may take a minute)...')
            os.system('python restart.py')
        else:
            await channel.send('Who the fuck are you?')

    if message.content.startswith('!자가진단'):
        await log(message)

        if author == os.environ['admin']:
            await selfdiagnosis(channel)
        else:
            await channel.send('당신은 권한을 가지고 있지 않은!')

client.run(os.environ['token'])
