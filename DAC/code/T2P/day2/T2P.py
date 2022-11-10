import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
engine.say("Hello. I'm AI chat box")
engine.runAndWait()
