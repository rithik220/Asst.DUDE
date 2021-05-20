import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import wolframalpha
from ecapture import ecapture as ec
from bs4 import BeautifulSoup as soup
import wikipedia
import random
import pyttsx3
import datetime
from bs4 import BeautifulSoup


engine = pyttsx3.init()



def speak(audio):
    print('DUDE: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello .,DUDE at your service.')
speak('Please tell me how can I help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        speak('Sorry .! I didn\'t get that! Try typing the command!')
        command = str(input('Command: '))
    return command

def dudeResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

if __name__ == '__main__':        

    while True:
        command = myCommand()
        command = command.lower()

        if 'reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            try:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
                webbrowser.open(url)
                speak('The Reddit content has been opened for you Sir.')
            except:
                speak('couldn\'t get reddit right now')

        elif 'open' in command:
            reg_ex = re.search('open (.+)', command)
            try :
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                speak('The website you have requested has been opened. ')
            except:
                pass

            
        elif "open camera" in command or "take a photo" in command:
            ec.capture(0, " DUDE Camera ", "img.jpg")


        elif 'nothing more' in command or 'abort' in command or 'stop' in command or 'quit' in command:
            speak('okay')
            speak('Bye ., have a good day.')
            sys.exit()
           
        elif 'hello' in command:
            speak('Hello .')

        elif 'bye' in command or 'exit' in command:
            speak('Bye ., have a good day.')
            sys.exit()
                                    
        elif 'play music' in command:
            speak('Sorry! Only from local disc i can play music! Say okay! if I should play the music I have!')
            local = myCommand()

            if 'ok' in local:
                try:
                    speak('playing')
                    n = random.randint(0,2)
                    print(n)

                    music_dir = r'C:\Users\home\Music'
                    song = os.listdir(music_dir)
                    print(song)

                    os.startfile(os.path.join(music_dir,song[n]))

                except:
                    speak('sorry creater was dumb, cant play music, enjoy asking something else.')

        elif 'send message'  in command:
                try:
                    speak('please type the case sensitve number of a recipent ')
                    contactNumber = str(input('number: ')) 
                    speak(' tell me your message please.')
                    m = myCommand()


                    url = "https://www.fast2sms.com/dev/bulk"

                    payload = {
                        'sender_id' :'CHKSMS',
                        'message':m + '- From Asst.DUDE',
                        'language': 'english',
                        'route':'p',
                        'numbers': contactNumber
                    }
                    headers = {
                    'authorization': "nvpfrtJGwEURSLPXqegb5Kz68QyxDCN79kVdTmOIY3hcFBlis1tUBSQezunjK8LhHI0CdoMsxDVTYl1X",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }
                    response = requests.request("POST", url, data=payload , headers=headers)
                    print(response.text)


                except:
                    speak('creator sucked up. failed to send your mesaage sorry. enjoy asking anything else to your DUDE.')               



        elif  'gmail' in command:
            speak('Who is the recipient?')
            recipient = myCommand()
            try:
                speak('write down the sensitive gmail name of the recipient please')
                name = str(input('receiver_id : '))
                speak('tell me your message to be sent ')
                content = myCommand()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('dudeasst.srgv@gmail.com', '19202223rgsv')
                mail.sendmail('dudeasst.srgv@gmail.com', name, content + ' -Asst. DUDE')
                mail.close()
                speak('Email has been sent successfuly. You can check your inbox.')

            except:

                speak('sorry, couldn\'t process your mail.')





        elif 'news' in command:
            speak('please ask me in which news you are intrested to check now')
            check = myCommand()
            url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en/{check}'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            news = soup.findAll('h3', attrs = {'class':'ipQwMb ekueJc RD0gLb'})
            for n in news:
                print(n.text)
                print('\n')
                engine.say(n.text)
            print('For more information visit: ', url)
            engine.say('For more information visit google news')
            engine.runAndWait()
            words = check.split('news')


        elif 'play video' in command:
            speak(' please tell me which video you want watch')   
            video = myCommand()

            words = video.split('where is')
            print(words[-1])
            link = str(words[-1])
            link = re.sub(' ', '', link)
            engine.say('Locating')
            engine.say(link)
            engine.runAndWait()

            link = f'https://www.youtube.com/results?search_command={link}'
            print(link)
            webbrowser.open(link)



        elif 'maps' in command:
            print('..')
            speak('now please tell me only the place you want to peek into')
            place = myCommand()
            words = place.split('where is')
            print(words[-1])
            link = str(words[-1])
            link = re.sub(' ', '', link)
            engine.say('Locating')
            engine.say(link)
            engine.runAndWait()
            link = f'https://www.google.co.in/maps/place/{link}'
            print(link)
            webbrowser.open(link)



        else:
            command = command
            speak('Searching...')
            try:
                try:
                    app_id = 'J3KPU2-YHYVP56Y68'
                    client = wolframalpha.Client(app_id)
                    res = client.query(command)
                    answer = next(res.results).text
                    speak('Yes.')
                    speak('Wolframalpha says -')
                    speak(answer)
                    
                except:
                    results = wikipedia.summary(command, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(answer)
        
            except:
                webbrowser.open('www.google.com/{command}')
        
        speak('Next Command! Please!')