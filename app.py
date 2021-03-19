from googletrans import Translator
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
    if message.author.bot:
        return None

    if message.content.startswith('!waldohelp') or message.content.startswith('!help'):
        await channel.send('''```
!waldohelp(!help) : 이것은 보여주다 너에게 도움말

!waldohello(!hello) : 이것은 하다 인사

!waldotrans(!trans) <한국어 문장> : 이것은 번역하다 너의 언어 를 나의 언어 로

!waldomode(!mode) [1/2] : 이것은 번역하다 다양한 말투
    1(기본의) : 역겨운
    2 : 자연스러운
```''')

    if message.content.startswith('!waldohello') or message.content.startswith('!hello'):
        await channel.send('안녕하신가! 힘세고 강한 아침, 만일 내게 물어보면,\n나는 왈도.')

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

    if message.content.startswith('!waldomode ') or message.content.startswith('!mode '):
        val = message.content.split(' ')[1]

        if val == '1':
            mode = 1
            await channel.send('바꾸다 말투 자연스러운')
            
        elif val == '2':
            mode = 2
            await channel.send('바꾸다 말투 역겨운')
            
        else:
            await channel.send('그 입력 은 잘못된 형태의!')

client.run(os.environ['token'])
