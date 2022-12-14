# -*- coding: utf-8 -*-

import datetime
import speech_recognition as sr
import pyttsx3
import requests
from texttotime import speechtodate

#Declaring constants

#Log url
Logurl="http://127.0.0.1:5000/log"

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
        #recording done
        
        try: 
            statement=r.recognize_google(audio,language="en-in")
            print(f"user said:{statement}\n")

        except Exception:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement
    
#log manager for the activitylog
def logManager(var):
    log=dateCalculation()+" " + var
    requests.post(Logurl, data={'log': log}).json()
    
#Information or data to be posted into the api
if __name__=='__main__': 
    while True:
        wake=takeUtterance(3).lower()
        #print("This is the wake word statement")
        if "mark" in wake:
            #Wake word handler hook 
            wake=True
            open=0
            while wake:
                #Openning message event handler
                if open==1:
                    print("What can I do for you set a remainder or access a todo list?")
                if open==0:
                    logManager("Wake word detected program begun")
                    print("Wake word detected.")
                    print(timeSalutation()+" This is the crystal time management platform I can manage a todo list and set a remainder. What would you like to do today?")
                    open+=1
                statement=takeUtterance(5).lower()
                if len(statement)==4:
                    print("You haven't said a thing, how can I help you?")
                    continue
                #This is the todo intent.
                elif "todo" in statement or "list" in statement:
                    #todo list intent handler
                    todoHook=True
                    #reinitializing statement
                    statement=""
                    while todoHook:
                        print("Would you like to add ,check or exit your todo list?")
                        todoTarget=takeUtterance(6).lower()
                        logManager("Accessed todo list")
                        if len(todoTarget)==4:
                            print("I didn't hear you could you repeat")
                        elif "add" in todoTarget:
                            todoTarget=""
                            print("What would you like to add to the todo-list")
                            add=takeUtterance(10).lower()
                            requests.post('http://127.0.0.1:5000/todos', data={'task': add}).json()
                            logManager("Add item to todolist")
                            #Variable to monitor your todo
                            hook=True
                            while hook:
                                print("Is there anything else you would like to add?")
                                addTodo=takeUtterance(10).lower()
                                #Handling some error context
                                if len(addTodo)==4:
                                    addTodo=""
                                    print("I didn't understand could you please repeat answer yes or no?")
                                    continue
                                elif 'yes' in addTodo:
                                    addTodo=""
                                    print("What is it?")
                                    addItem=takeUtterance(6).lower()
                                    requests.post('http://127.0.0.1:5000/todos', data={'task': addItem}).json()
                                    logManager("Add item to todolist")
                                elif 'no' in addTodo:
                                    addTodo=""
                                    print("Okay thats great")
                                    logManager("Exit the todolist")
                                    hook=False
                                    todoHook=False
                        elif "check" in todoTarget:
                            todoTarget=""
                            print("This is your current todo-list")
                            response=requests.get('http://127.0.0.1:5000/todos').json()
                            for todo in response:
                                    print(todo['task'])
                        elif "exit" or "leave" in todoTarget:
                            todoTarget=""
                            todoHook=False
                        
                
                #This is the remainder intent.
                elif "remainder" in statement or "reminder" in statement:
                    logManager("Accessed the Remainder")
                    print("Would you like to set a remainder or check you remainder?")
                    remainder=takeUtterance(6).lower()
                    if len(remainder) ==4:
                        print("You can either set or check you remainders")
                    elif "set" in remainder:
                        print("What day would you like to set your remainder")
                        #Remainder event handler
                        remain=True
                        while remain:
                            day=takeUtterance(6).lower()
                            senddate=speechtodate(day)
                            if senddate!=0:
                                print("What would you like to do?")
                                rem=takeUtterance(6).lower()
                                print("At what time?")
                                time=takeUtterance(6).lower()
                                print("Would you like to set another remainder or no to exit?")
                                nextrem=takeUtterance(6).lower()
                                requests.post('http://127.0.0.1:5000/remainder', data={'remainder': rem,'date':senddate, 'time':time}).json()
                                if "no" in nextrem:
                                    remain=False
                                elif "yes" in nextrem:
                                    continue
                            elif senddate==0 or senddate=="None":
                                print("I didn't get the date well, could you please repeat?")
                            elif 'exit' in senddate:
                                remain=False

                #This is the project intent
                elif "project" in statement:
                    logManager("Accessed the project")
                    print("Would you like to view you projects or add to your project list?")
                    Target=takeUtterance(10).lower()
                    if "add" in Target:
                        logManager("Adding a new project")
                        print("What is the name of the project you would like to add")
                        add=takeUtterance(10).lower()
                        print("What are the first step needed to complete you project?")
                        addProject=takeUtterance(10).lower()
                        logManager("Adding a item new project")
                        while True:  
                            print("Is there next step?")
                            addItem=takeUtterance(10).lower()
                            #Handling yes and no intent.addItem
                            if 'yes' in addItem:
                                print("What is it?")
                                addItem=takeUtterance(10).lower()
                                logManager("Adding a item new project")
                            elif 'no' in addItem:
                                print("Okay thats great")
                                logManager("Close access to the new project")
                                False
                            #Handling some error context
                            else:
                                print("I didn't understand could you please repeat answer yes or no?")

                    if "view" in Target:
                        print("What is the name of the project you would like to view or do you want me to list to your project?")
                
                #This is the calendar intent.
                elif "calendar" in statement:
                    print("Which day would you like to add a task or would you like to view or check task?")
                    date=takeUtterance(10).lower()
                    #add a date converter and validation
                    print("What tasks would you like to add?")
                    calTask=takeUtterance(10).lower()
                    while True:
                        print("Is there anything else you would like to add?")
                        addCalItem=takeUtterance(10).lower()
                        #Handling yes and no intent.addItem
                        if 'yes' in addCalItem:
                            print("What is it?")
                            addCalItem=takeUtterance(10).lower()
                        elif 'no' in addCalItem:
                            print("Okay thats great")
                            False
                        #Handling some error context
                        else:
                            print("I didn't understand could you please repeat answer yes or no?")

                #This is the sleep/ exit command of the program.
                elif "good bye" in statement or "goodbye" in statement or "ok bye" in statement or "turn off" in statement or "quit" in statement:
                    logManager("Exit intent detected program closed.")
                    wake=False
                    open=0
                    print ('Thank you and take care')
                    break
                #Error handler of the program
                else:
                    print("What would you like to access?")
        else:
            print("No wake word detected.")
    