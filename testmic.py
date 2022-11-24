import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening... ")
    r.adjust_for_ambient_noise(source,duration=0.2)
    audio=r.record(source)
    try: 
        statement=r.recognize_google(audio,language="en-in")
        print(f"user said:{statement}\n")

    except Exception:
        print("i didnt hear you, please say that again")
        
    print(statement)

