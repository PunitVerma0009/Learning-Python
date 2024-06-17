from gtts import gTTS
import os
mytext = 'Type the text that you want to make a mp3 file of'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
