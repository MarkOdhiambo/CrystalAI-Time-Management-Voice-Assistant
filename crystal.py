# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:10:52 2022

@author: User
"""
import datetime
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
# rate=engine.getProperty('rate')
# engine.setProperty("rate",130)
# voices=engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait

def timeSalutation():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        return"Good Morning!"
    elif hour>12 and hour<18:
        return"Good Afternoon"
    else:
        return"Good evening"
def dateCalculation():
    year=str(datetime.datetime.now().year)
    day=str(datetime.datetime.now().day)
    month=str(datetime.datetime.now().month)
    hour=str(datetime.datetime.now().hour)
    minute=str(datetime.datetime.now().minute)
    return day+"/"+month+"/"+year+" "+hour+":"+minute
    
def takeUtterance(var):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        #This is for the adjust of the background noise in around the speaker. 
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio=r.record(source,duration=var)
        
        try: 
            statement=r.recognize_google(audio,language="en-in")
            print(f"user said:{statement}\n")

        except Exception:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement
    
#log manager for the activitylog
def logManager(var):
    return dateCalculation() +" " + var
#Information or data to be posted into the api
if __name__=='__main__':
    
    while True:
        statement=takeUtterance(5).lower()
        if "crystal" in statement:
            print("Wake word detected.")
            speak(timeSalutation()+" This is the crystal time management platform I can manage a todo list and work on a project what would you like to do today?")
            statement=takeUtterance(10).lower()
            if statement==0:
                continue
            #This is the todo intent.
            elif "todo" in statement:
                speak("Would you like to add or check your todo list?")
                todoTarget=takeUtterance(10).lower()
                if "add" in todoTarget:
                    speak("What would you like to add to the todo-list")
                    add=takeUtterance(10).lower()
                if "check" in todoTarget:
                    speak("This is your current todo-list")
                    
            #This is the project intent
            elif "project" in statement:
                speak("Would you like to view you projects or add to your project list?")
                todoTarget=takeUtterance(10).lower()
                if "add" in todoTarget:
                    speak("WWhat is the name of the project you would like to add")
                    add=takeUtterance(10).lower()
                if "view" in todoTarget:
                    speak("This is your current todo-list")
         
            #This is the sleep/ exit command of the program.
            elif "good bye" in statement or "ok bye" in statement or "turn off" in statement or "quit" in statement:
                speak ('Thank you and take care')
                break
        else:
            print("No wake word detected.")
    