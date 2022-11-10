import playsound
from gtts import gTTS  #module cua googl
import os

# myText = "Hello my name is Linh"

fh = open("test.txt", "r")
myText = fh.read().replace("/n", " ")

language = 'en'

output = gTTS(text= myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()
playsound.playsound('output.mp3', True)
