# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:10:52 2022

@author: User
"""
import datetime
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait

def timeSalutation():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    
def takeUtterance():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        #This is for the adjust of the background noise in around the speaker. 
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        
        try: 
            statement=r.recognize_google(audio,language="en-in")
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement

timeSalutation()

# if __name__=='__main__':
    
#     while True:
#         speak("What can I do for you today?")
#         statement=takeUtterance().lower()
#         if statement==0:
#             continue
#         #This is the sleep/ exit command of the program.
#         if "good bye" in statement or "ok bye" in statement or "turn off" in statement or "quit" in statement:
#             speak ('Thank you and take care')
#             break
    