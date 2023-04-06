import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-3].id)

engine.say("Eu sou a Eilietta")
engine.runAndWait()