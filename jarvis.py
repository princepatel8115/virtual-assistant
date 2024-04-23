from platform import win32_edition
#from signal import alarm
from tkinter import *
from winsound import PlaySound
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman
import pywhatkit as wk
import pyscreenshot
import requests
from bs4 import BeautifulSoup


#from Class1 import Student
#import pytesseract
from PIL import Image
from pathlib import Path
#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mridu\AppData\Local\Tesseract-OCR\tesseract.exe"




    

def sendEmail(to , content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("200510101105@paruluniversity.ac.in","Gopalparul1")
    server.sendmail("200510101105@paruluniversity.ac.in",to,content)
    server.close()


def alarm(Timing):
    alttime = str(datetime.datetime.now().strptime(Timing,'%I:%M %p'))
    alttime = alttime[11:-3]
    hour_in_time = alttime[:2]
    hour_in_time = int(hour_in_time) 
    min_in_time = alttime[3:5]
    min_in_time = int(min_in_time)
    print(f'Alarm has been set at {Timing}')
    var.set('Alarm has been set')
    window.update()
    #var.set("alarm has been set at")
    while True:
        if hour_in_time == datetime.datetime.now().hour:
            if  min_in_time == datetime.datetime.now().minute:
                print('Turn off your Alarm')

                from pydub import AudioSegment
                from pydub.playback import play

                song = AudioSegment.from_wav("3.wav")
                play(song)

        elif min_in_time<datetime.datetime.now().minute:
            break


numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'name':'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def send_Message():
    root=Tk()
    root.title("Send Whatsapp")

    n1=Label(root, text="Number")
    n1.grid(column=0,row=0)
    n2=Entry(root, width="50")
    n2.grid(column=1,row=0)

    m1=Label(root, text="Message")
    m1.grid(column=0,row=1)
    m2=Entry(root, width="50")
    m2.grid(column=1,row=1)

    current=datetime.datetime.now().time()
    hour=current.strftime("%H")
    minu=current.strftime("%M")
    hour=int(hour)
    minu=int(minu)
    minu+=2

    def send():
        wk.sendwhatmsg("+91"+n2.get(),m2.get(),hour,minu)
        send=Button(root,text="SEND")

    send_msg=Button(root, text="Send",command=send)
    send_msg.grid(column=1,row=4)

    def quit():
        exit()

    end=Button(root,text="Exit",command=quit)
    end.grid(column=1,row=5)

    root.mainloop()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        var.set('good morning sir')
        window.update()
        speak("Good Morning Sir, How may I help you!")
    elif hour>=12 and hour<18:
        var.set('good afternoon')
        window.update()
        speak("Good Afternoon Sir, How may I help you!") 
    else:
        var.set('good evening sir')
        window.update()
        speak("Good Evening Sir, How may I help you!")  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course error' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'temperature' in query:
            search='temperature in vadodara'
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div", attrs={'class':'BNeawe'}).text
            speak(f"current {search} is {temp}")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("https://www.google.com")


        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'open github' in query:
            var.set('opening github')
            window.update()
            speak("opening github") 
            webbrowser.open("https://www.github.com")

        elif 'open facebook' in query:
            var.set('opening facebook')
            window.update()
            speak("opening facebook") 
            webbrowser.open("https://www.facebook.com")

        elif 'news' in query:
            var.set('opening news')
            window.update()
            speak("opening news") 
            webbrowser.open("https://zeenews.india.com/live-tv")

        elif 'open parul university' in query or 'take me to parul university' in query:
            var.set('opening parul university')
            window.update()
            speak("opening parul university")
            webbrowser.open('https://paruluniversity.ac.in')
        
        elif 'open exam portal' in query:
            var.set('opening exam portal')
            window.update()
            speak('opening exam portal')
            webbrowser.open("https://exams.paruluniversity.ac.in")
             

        elif 'open instagram' in query:
            var.set('opening instagram')
            window.update()
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'take me to bank' in query:
            var.set('opening bank')
            window.update()
            speak('opening hdfc bank')
            webbrowser.open('https://netbanking.hdfcbank.com/netbanking/')

        elif 'phone number of teacher' in query or 'mobile number of faculity' in query or 'contact number' in query or 'can you provide me phone number of faculties' in query:
            ans_no = "Dr. Priya Swaminaryan 9427857621 \nHOD Hina Choksi 9227873387 \nProf. Dharmendra Sinh 9510406252 \nProf. Abhishek Kumar 9898735028 \nProf. Bhavika Vaghela 7600025348 \nProf. Anjali Mahavar 9712303497 \nProf. Arpan Kumar 9408404954 \nProf. Bindi Bhatt 8460168246 \nProf. Manish Joshi 9898530753 \nProf. Karuna Patel 9033542599 \nProf. Nishant Khatri 7016200184 \nProf. Priya Patel 7359162174 \nProf. Sohil Parmar 6352559859"
            var.set(ans_no)
            window.update()
            speak('here are phone number of your faculties')
        
        elif "can you suggest me some movie" in query or 'any movie recommendation' in query:
            sent = ['you must watch Interstellar which is based on space and time travel', 'you must match current trending series Money Heist', 'have you watched Inception','you should watch Who Am I or Snowden coz its relates to your field','spider man far from home','she Hulk','bhramastra']
            ans_q = random.choice(sent)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'Okay' in ans_take_from_user_how_are_you or 'I will watch' in ans_take_from_user_how_are_you or 'I m watching' in ans_take_from_user_how_are_you:
                speak('Okay..')  
            elif 'No' in ans_take_from_user_how_are_you or 'not yet' in ans_take_from_user_how_are_you or 'na' in ans_take_from_user_how_are_you:
                speak('You should watch') 

        elif "whats up" in query or "how are you" in query:
            sentmsg = ['I am fine! what about you', 'Nice! what about you', 'Great what about you','I am Okay! what about you']
            ans_q = random.choice(sentmsg)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'Great' in ans_take_from_user_how_are_you or 'Okay' in ans_take_from_user_how_are_you:
                speak('Okay..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('Oh sorry..') 
        

        elif "shutdown" in query:
            var.set('shutting down')
            window.update()
            speak("shutting down")
            os.system('shutdown -s')

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'Bye Have a nice day'
            speak(ex_exit)
            exit()
            
               
			
        elif 'open stack overflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('https://stackoverflow.com')

        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'C:\\Users\\tiwar\\Music\\Playlists' # Enter the Path of Music Library
            songs = os.listdir(music_dir)
            # n = random.randint(0,27)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'what is the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'what can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'how old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Jarvis Sir")
            window.update()
            speak('myself Jarvis sir')

        elif 'who created you' in query or 'who developed you' in query:
            var.set('My Creator is Jaynil , amanda and prince')
            window.update()
            speak('My Creator is jaynil , amanda and prince')

        elif ' hello' in query:
            var.set('Hello Everyone! My self Jarvis')
            window.update()
            speak('Hello Everyone! My self Jarvis')
        
        elif 'how are you feeling' in query:
            var.set('feeling great after meeting you')
            window.update()
            speak('feeling great after meeting you')

        elif 'email to ram' in query:
            try:
                speak("what should i say");
                content=takeCommand()
                to='200510101105@paruluniversity.ac.in'
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry you email has not been sent")


		
        elif "open amazon" in query or 'shop online' in query :
            var.set("Opening amazon")
            window.update()
            speak('opening amazon')
            webbrowser.open("https://www.amazon.in")

        elif 'open whatsapp' in query or 'check whatsapp messages' in query:
            var.set('opening whatsup')
            window.update()
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com")
        
        elif 'send message' in query or 'send a message' in query:
            var.set('sending message')
            window.update()
            speak("Sending Whatsapp Message")
            send_Message()
        
        elif 'set alarm' in query:
            var.set('at what time do you want to set an alarm')
            window.update()
            speak('At what time you want to set alarm')
            tt = takeCommand()
            tt= tt.replace('.','')
            tt = tt.upper()
            alarm(tt)



        
        elif 'open gmail' in query:
            var.set('opening gmail')
            window.update();
            speak('opening gmail')
            webbrowser.open('https://mail.google.com')

        elif "take a screenshot" in query :
                    speak("taking screenshot")
                    #time.sleep(2.4)
                    image = pyscreenshot.grab()
                    image.show()
                    
        
        elif 'calculation' in query:
            sum = 0
            var.set('Yes Sir, please tell the numbers')
            window.update()
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    var.set('here is result'+str(sum))
                    window.update()
                    speak('here is result'+str(sum))
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit

        elif 'plus' in query or '+' in query or '-' in query or 'minus' in query or 'multiply' in query or '*' in query or 'divide' in query or '/' in query:
            opr = query.split()[1]

            if opr == '+' or opr=='plus':
                speak(int(query.split()[0]) + int(query.split()[2]))
            elif opr == '-' or opr=='minus':
                speak(int(query.split()[0]) - int(query.split()[2]))
            elif opr == 'multiply' or '*':
                speak(int(query.split()[0]) * int(query.split()[2]))
            elif opr == 'divide':
                speak(int(query.split()[0]) / int(query.split()[2]))
            elif opr == 'power':
                speak(int(query.split()[0]) ** int(query.split()[2]))
            else:
                speak("Wrong Operator")


        '''
        elif 'enter student details' in query:
            s = Student()
            var.set('Name of the student')
            window.update()
            speak('Name of the student')
            name = takeCommand()
            var.set('standard in which he/she study')
            window.update()
            speak('standard in which he/she study')
            standard = takeCommand()
            var.set('Role Number')
            window.update()
            speak('Role number')
            rollno = takeCommand()
            s.Enterdetalis(name,standard,rollno)
            var.set('Details are saved')
            window.update()
            speak('Details are saved')

        elif 'show me details' in query:
            var.set('Name: '+name+' Standard: '+ standard+' Roll No.: '+ rollno)
            window.update()'''

        '''elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg',frame)
            stream.release()

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        
        elif 'read the photo' in query: #If you have Pytesseract installed for Optical Character Recognition
            try:
                im = Image.open('pic.jpg')
                text = pytesseract.image_to_string(im)
                speak(text)
            except Exception as e:
                print("Unable to read the data")
                print(e) '''
            
                

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Virtual Assistant')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
