import pyttsx3
from datetime import *

if(datetime.now().hour >0 and datetime.now().hour <12):
    print("Good Morning , Kumkum")
    pyttsx3.speak("Good Morning,Kumkum")
elif(datetime.now().hour >=2 and datetime.now().hour <=15):
    print("Good Afternoon, Kumkum")
    pyttsx3.speak("Good Afternoon,Kumkum")
elif(datetime.now().hour >15 and datetime.now().hour <=20):
    print("Good Evening,Kumkum")
    pyttsx3.speak("Good Evening,Kumkum")
elif(datetime.now().hour >20 and datetime.now().hour <=24):
    print("Good Night,Kumkum")
    pyttsx3.speak("Good Night,Kumkum")
