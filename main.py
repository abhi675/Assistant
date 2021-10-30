import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import pywhatkit
from selenium import webdriver
from wikipedia.wikipedia import search

Master='Abhishek'
# speak function will pronounce the speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

contactlist={"adity":"+919575545185","deepansh":"+919907219994","ankit":"9826142186","nikita":"+917067579876","aastha":"+91","shruti":"=917766554433"}
def speak(text):
    engine.say(text)
    engine.runAndWait(),

#Function function will wish you on the initializing of jarvis
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning '+Master) 
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon '+ Master)

    else:
        speak('Good Evening' + Master)
    

#Function will take command from microphone
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        audio=r.listen(source)

    try:
        print('Recognizing..')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print('Say that again please')
        query=None

    return query 

#Food items according to day and time
fooditems={"Monday":{"Breakfast":"Sprouts","Lunch":"Rice with sabji and daal with chapati as well","Dinner":"Milk and khichadi"},
"Tuesday":{"Breakfast":"Boil Eggs","Lunch":"Fish with rice","Dinner":"Sweet potatao"},
"Wednesday":{"Breakfast":"Poha","Lunch":"Rice with sabji and peanut butter as well","Dinner":"Nuts and soy products"},
"Thursday":{"Breakfast":"Bananas","Lunch":"Garbanzo beans with fruit juice","Dinner":"Milk and khichadi"},
"Friday":{"Breakfast":"Oatmeal","Lunch":"Oatmeal with mango","Dinner":"Salaad and brocoli"},
"Saturday":{"Breakfast":"Chia seeds","Lunch":"brown rice with milk","Dinner":"Quino and corn"},
"Sunday":{"Breakfast":"Fried Eggs","Lunch":"vegetables with beans"}}

#Daily routine remider function
def dailyRoutine():
    now=datetime.datetime.today().strftime("%Y:%B:%d:%A:%H:%M:%p")
    year,month,day,week,hour,min,temp=now.split(":")
    hour=int(hour)

    if hour<=12:
        pass
    elif hour>12:
        hour=str((hour-12))
   
    speak("It is {} {} {} and today date is {} and {} month is going on".format(hour,min,temp,day,month))
    if int(day)==13 and month=="februrary":
        speak("Happy Birhtday Abhishek...")
    if (int(day)==1 or int(day)==15) and int(hour)==10 and temp=="AM":
        speak("Today is your appointment with doctor at 10 30 PM... You need to get ready and will have to go to doctor's clinic.")
    if hour=="8" and temp=="AM":
        speak("Abhishek it is {} {} {} and you need to take your morning medicine with milk".format(hour,min,temp))
    elif hour=="2" and temp=="PM":
        speak("Abhishek it is {} {} {} so you need to take your afternoon medicine with water".format(hour,min,temp))
    elif int(hour)==8 and temp=="PM":
        speak("Abhishek it is {} {} {} so you need to take you last medicine of the day with hot water".format(hour,min,temp))
    elif (int(hour)>=9 and temp=="PM") or (int(hour)<=6 and temp=="AM"):
        speak("Abhishek it is {} {} {}, you will have to got to bed, Good Night".format(hour,min,temp))
    elif int(hour)==7 and temp=="AM":
        speak("Abhishek it is {} {} {}, you need to wake up and should take your breakfast after shover".format(hour,min,temp))
    elif int(hour)==7 and int(min)==30 and temp=="AM":
        speak("It is your breakfast time")
        speak("Today is {} ... You need to have {} in your breakfast".format(week,fooditems[week]["breakfast"]))
    elif int(hour)==1 and temp=="PM":
        speak("It is your lunch time")
        speak("Today is {} ....You need to have {} in your lunch".format(week,fooditems[week]["Lunch"]))
    elif int(hour)==5 and temp=="PM":
        speak("It is your evening breakfast time")
        speak("You should take fruit juice")
    elif int(hour)==7 and temp=="PM":
        speak("It is your dinner time")
        speak("Have your dinner and in your dinner add {}... Have a nice meal".format(fooditems[week]["Dinner"]))


speak('Initializing Assistant...')
wishMe()
dailyRoutine()



speak("Sir do your want something.......")
feedback=takeCommand()


if "yes" in feedback.lower():

    query=takeCommand()


    if query is None:
        speak('Whenever you need me you can call me sir')

    elif 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak(results)

    elif 'open youtube' in query.lower():
       driver=webdriver.Firefox()
       speak("What do you want to search in youtube")
       something=takeCommand()
       driver.get("https://www.youtube.com/results?search_query="+something)

    elif "search" in query.lower():
        
        driver = webdriver.Chrome()
        search=takeCommand()
        driver.get('search')
       
    elif 'the time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{Master} the time is {strTime}")

    elif 'send message' in query.lower():
        speak("Tell me the name of the person you want to send message")
        name=takeCommand()
        number=-1
        if name.lower() in contactlist:
            number=contactlist[name]
            speak("Speak out the the message you wanna send ....")
            message=takeCommand()
            h=int(datetime.datetime.now().hour)
            m=int(datetime.datetime.now().minute)
            if m==59:
                m=1
                h=(h+1)%24
            else:
                m=m+1
            pywhatkit.sendwhatmsg(number,message,h,m)

        else:
            speak("name is not present in the contact list")
    
    

else:
    speak("Thank you for your time {} ... Have a nice day".format(Master))


