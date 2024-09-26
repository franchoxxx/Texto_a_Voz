import pyttsx3

book = open(r"book.txt")

book_text = book.readlines()

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate
print (rate)                        # printing current voice rate

"""VOICE"""
voices = engine.getProperty('voices')        #getting details of current voice
engine.setProperty('voice', voices[0].id)    #changing index, changes voices. o for English
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for Espanish

"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.5)

for line in book_text:
    engine.say(line)
    engine.runAndWait()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(book_text, 'test.mp3')
engine.runAndWait()
