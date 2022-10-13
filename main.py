# Modules externes

import speech_recognition as sr
import pyttsx3 as pt
import datetime
import shutil
import os
import random
import subprocess

#Cet     c5%5%

engine = pt.init()
voices = engine.getProperty('voices')

# Changement de voix en francais ou en anglais
engine.setProperty('voice', voices[0].id) # Ave
def speak(audio):

    engine.say(audio)
    engine.runAndWait()
# la salutation varie en fonction du
def salutation ():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("Bonjour")
    elif hour>= 12 and hour<18:
        speak("Bonne après midi!")

    else:
        speak("Bonsoir !")

    khadijaa=("Ka di djaa")
    speak("je suis  Ka di djaa votre assistance vocale ")
   # ##########################
   # la creation de dictionnaire
dict_hello =['bonjour', "Bonsoir", "Salut "]
dict_good = [ "Oui ça va bien", "J'ai pete le feu aujourd'hui", "je vais bien merci  "]
responses =['ça va', "tu vas ",""]

choi_ord =random.choice(dict_good)
def speak_text():
    re = sr.Recognizer()
    # Le micro est foncti
    with sr.Microphone() as source:
        print("En écoute....")
        re.pause_threshold = 1 # la pause d'entente
        audio = re.listen(source)  # En ecoute
        try :

            print("Reconnaissance....")
            data = re.recognize_google(audio, language='fr-FR') # la reconnaisnce de langue grace à google donc il
            # faut bien connes=xion internet
            speak("Vous avez dit {}".format(data))
            print("Vous avez :{}".format(data))


        except Exception as exp:
            print(exp)
            print("Je n'ai pas bien compris ")
        except RuntimeError:
            print("Error de reconnaissance")

    return  data



def tri_ordi():

    ordi =["ça va ", " tu vas "]
    pass
def userName ():
    name_user = "Quelle est votre nom ?"

    speak("{}".format(name_user))

    name = speak_text()
    speak("Enchanté {}".format(name))
    command = shutil.get_terminal_size().columns
    print("#####################".center(command))
    print( "Enchante".format(name.center(command)))
    speak("Que puis-je faire pour vous ")
if __name__ == '__main__':
    salutation()
    userName()
    while True:
        text=speak_text().lower()
        if "{}".format(responses) in text or 'ça va' in text:

            speak("{}".format(choi_ord))
            subprocess.call(["shutdown", "/r"])

        elif  'mets de la musique ' in text or "chanson" in text:
            speak("Ok avec plaisir")
            music_dir = "C:\\Users\\cleme\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0])) # uohid
        elif "heure" in text:
            time_now = datetime.datetime.now().strftime("%H")

            time_now1 = datetime.datetime.now().strftime("%M")
            heure = time_now + "heures" + time_now1 +"minutes"

            speak("Il est {}".format(heure))
        elif "Redémarrer " in text or " l'ordinateur" in text :
            speak("Cela va prendre quelques minutes  ")
            subprocess.call(["shutdown", "/r"])
        elif "sort " in text or "quitte" in text:
            speak("Ok comme vous voulez")
            exit()

