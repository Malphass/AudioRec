
import pygame
import tkinter as tk
import sounddevice as sd
from scipy.io.wavfile import write
from PIL import Image, ImageTk 

pygame.mixer.init()
launched = True


def warning():
    warn = tk.Tk()
    warn.title("warning")
    warn.geometry("300x100+660+420") # largeur x hauteur
    warn.iconbitmap('alert.ico')
    
    warni = tk.Label(warn, text = ("aucun fichier choisi ! \n ou mauvais format"), font = ('Impact', 24) )

    warni.pack(side = 'top')
    warn.mainloop()

    


# fonction de lecture audio

# fonction de lecture des fichiers audio
def playAudio():
    file = zoneSaisie.get()
    if zoneSaisie.get() == "":
        warning()
        print('lol')
        file = 'Sound.wav'

    verify = file.rsplit('.', 1 )[1]
    if verify != "png" or verify != "wav":
        warning()
    
    pygame.mixer_music.load(file)
    pygame.mixer_music.play()

# fonction de mise en pause de fichiers audio
def pauseAudio():
    pygame.mixer_music.pause()

# fonction d'arret de lecture des fichiers audio
def stopAudio():
    pygame.mixer_music.fadeout(2000)

# fonction permettant de regler le volume via un slider horizontal basique
def setVol(vol):
    vol2 = int(vol)/100     # fait la conversion de 0 - 100 à 0 - 1
    pygame.mixer_music.set_volume(vol2)     # met le volume entre 0 et 1 -> 0.77 ect


# fonction d'enregistrement
def recAudio():
   
    fs = 44100 # sample rate
    seconds = 5 # duree d'enregistrement

    myRec = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()   # attente du fin d'enregistrement
    write('rec.mp3', fs, myRec) # sauvegarde du fichier
    

def ecouteRec():
    filename = 'rec.mp3'
    pygame.mixer_music.load(filename)
    pygame.mixer_music.play()
    
# fenetre de vue

# color app
backColor1 = '#222222'
frontColor1 = '#FFFFFF'

# création de fénêtre
window = tk.Tk()
window.title("audioRec")
window.geometry("720x480+600+300") # hauteur x largeur
window.minsize(480,360)

window.maxsize(1440,960)
window.iconbitmap('LGBT_Mic.ico')
logo = tk.PhotoImage(file = 'LGBT_Mic.png')
window.iconphoto(False, logo)
window.config(background=backColor1)


#boite 1 : bienvenue et param

frame  = tk.Frame(window, bg=backColor1, bd=1, relief='sunken', width = 300)

text1 = tk.Label(frame, text="Bienvenue", font=('Calibri', 42), bg=backColor1, fg = frontColor1)

sliderSound = tk.Scale(frame, from_=0, to=100, orient='horizontal',bg = '#660000',fg = '#99FFFF', command = setVol)
sliderSound.set(10)


# boite 2 : jouer son (play,, pause, stop)

frame2 = tk.Frame(window, bg=backColor1, bd = 2, relief='groove', height = 80)

playButton = tk.PhotoImage(file = "playButton.png ")
pauseButton = tk.PhotoImage(file = "pauseButton.png ")
stopButton = tk.PhotoImage(file = "stopButton.png ")

buttonStartAudio = tk.Button(frame2, text="play ", image = playButton, width = 50, height= 50, bg=backColor1, command = playAudio)
buttonPauseAudio = tk.Button(frame2, text="pause", image = pauseButton, width =50, height= 50, bg=backColor1, fg= 'gray', command = pauseAudio)
buttonStopAudio  = tk.Button(frame2, text='Stop' , image = stopButton, width = 50, height= 50, bg=backColor1, fg='red',   command = stopAudio)

zoneSaisie = tk.Entry(frame2, text= "saisie de chanson", font=('calibri', 14), bg='gray',fg='white', width = 50)


# boite 3 : enregistrement audio

frame3 = tk.Frame(window, bg=backColor1, bd=1, relief='sunken')

recButton = tk.PhotoImage(file = "recButton.png")

buttonRec = tk.Button(frame3, text = "rec", image = recButton, width = 40, height = 40, bg=backColor1, fg='red', command = recAudio)




# boite 4 : jouer enregistrement

frame4 = tk.Frame(window, bg = '#442222', bd = 1)

listenRec = tk.PhotoImage(file = "listenRec.png")

buttonListenRec = tk.Button(frame4, text = "Listen rec", image = listenRec, width = 40, height = 40, bg=backColor1, fg='white', command = ecouteRec)




# affichage
frame.pack()
frame2.pack(pady=30)
frame3.pack(pady=30)
frame4.pack(pady=30)


#boite 1 

text1.grid(row = 0, column=0, columnspan = 3)

sliderSound.grid(row=0, column=1,)


# boite 2


buttonStartAudio.grid(row=0, column=0, sticky=tk.W+tk.E)
buttonPauseAudio.grid(row=0, column=1, sticky=tk.W+tk.E)
buttonStopAudio.grid( row=0, column=2, sticky=tk.W+tk.E)
zoneSaisie.grid(row = 1, column = 0, columnspan= 3 , sticky = tk.W+tk.E)

#boite 3 
buttonRec.grid(row=0, column=3, sticky=tk.W+tk.E)


#boite 4

buttonListenRec.grid(row = 0, column = 0, sticky=tk.W+tk.E)




window.mainloop()



    
    





