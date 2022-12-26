from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import math


r = sr.Recognizer()
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source) #sesi dinliyor
        voice="" # sese boş değer atıyor
        try:
            voice= r.recognize_google(audio, language="tr-TR") # eğer google asistan sesi algılarsa 
        except sr.UnknownValueError:  # except programda bir istisna meydana gelirse yapılacak işlemi tanımlar
            speak("dediğinizi anlayamadım")
        except sr.RequestError:
            speak("Sistem Çalışmıyor")
        return voice # sesi döndürüyor

#%%
def response(voice):
    
    if "merhaba" in voice:
        speak('sana da merhaba')
    if 'nasılsın' in voice:
          speak('teşekkür ederim, sen nasılsın ?')     
    if 'görüşürüz' in voice or 'hoşçakal' in voice:
        speak('kendine çok iyi bak, görüşürüz.')
    if 'hangi gündeyiz' in voice or "bugün günlerden ne" in voice or "bugün hangi gün" in voice:
        today = time.strftime("%A")
        if today == "Saturday":
            speak("Cumartesi")
        elif today == "Sunday":
            speak("Pazar")    
        elif today == "Monday":
            speak("Pazartesi")
        elif today == "Tuesday":
            speak("Salı")
        elif today == "Wednesday":
            speak("Çarşamba")
        elif today == "Thursday":
            speak("Perşembe")
        elif today == "Friday":
            speak("Cuma")
    if 'saat kaç' in voice or 'bana saati söyler misin' in voice  or 'saat' in voice:
            print(datetime.now().strftime("%H:%M:%S"))
   
    if 'program açık mı' in voice or 'program' in voice:   
        speak("program açık")
    if 'programı kapat' in voice or "kapat" in voice:
        speak("program kapatılıyor")
        exit()
                        
  #  if 'adın ne' in voice:
   #     speak('Bana henüz bir isim verilmedi, bana bir isim vermek ister misin?')  
        
def speak(string):
    tts = gTTS(text=string, lang="tr" , slow=False) #google'ye bağlanmamızı sağlayan köprü
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

while True:
    voice = record() # voice ye recorddan gelen değerleri atadık 
    if voice != '':
     voice = voice.lower()
     print(voice.capitalize())
     response(voice)
   



