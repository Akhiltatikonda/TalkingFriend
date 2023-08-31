import pyttsx3
TTV=pyttsx3.init()
#voice speed
rate=TTV.getProperty('rate')
TTV.setProperty('rate',150)
#create function
def TTV_speak(text):
    print('speaking....')
    TTV.say(text)
    TTV.runAndWait()
text='hey, I am your virtual talking friend'
TTV_speak(text)
while text!='bye':
    text=input('What should i say:')
    text=text.lower()
    if text!='bye':
        TTV_speak(text)
    else:
        TTV_speak("see you again bye")