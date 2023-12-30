import speech_recognition as sr
import pyttsx3
import pygame
import webbrowser as web


path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

r=sr.Recognizer()
def SpeakText(command):
    engine=pyttsx3.init()
    #rate = engine.getProperty('rate')   # getting details of current speaking rate
    #print (rate)                        #printing current voice rate
    engine.setProperty('rate', 175)
    #volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    #print (volume)                          #printing current volume level
    voices = engine.getProperty('voices')
    engine.setProperty('volume',1.0)
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. [1] for female [0] for male 1 for female
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:

    pygame.init()
    musicFile=r'C:\Users\dell\Desktop\Projects\AI Charbot\Speech-to-text\1640676121_sshksh.mp3'
    pygame.mixer.music.load(musicFile)
    pygame.mixer.music.play()

    
    r.adjust_for_ambient_noise(source2,duration=0.2)
    audio2=r.listen(source2)

    pygame.init()
    musicFile=r"C:\Users\dell\Desktop\Projects\AI Charbot\Speech-to-text\1640676150_siri.mp3"
    pygame.mixer.music.load(musicFile)
    pygame.mixer.music.play()

    MyText=r.recognize_google(audio2)
    MyText=MyText.lower()

    print("Did you say " + MyText)
    SpeakText(MyText)

    web.open(MyText)








    
