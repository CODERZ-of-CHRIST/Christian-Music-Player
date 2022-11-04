from tkinter import messagebox
#filename = PhotoImage(file = "pics\dovy.gif")
#background_label = Label(window, image=filename)
#background_label.place(x=0, y=100, relwidth=1, relheight=1)
from tkinter import *
from tkinter.tix import COLUMN
import webbrowser
from pygame import *
import random
import time
def here():
        output.delete(0.0, END)
        message = "Loading Music..."
        output.insert(0.0, message)
        time.sleep(1)
        mixer.init()
        mixer.music.load('music\here-i-am.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
                #Play the music
        mixer.music.play()

def congrats():
        output.delete(0.0, END)
        message = "Loading Music..."
        output.insert(0.0, message)
        time.sleep(1)
        mixer.init()
        mixer.music.load('music\congrats.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
                #Play the music
        mixer.music.play()

def surrender():
        output.delete(0.0, END)
        message = "Loading Music..."
        output.insert(0.0, message)
        time.sleep(1)
        mixer.init()
        mixer.music.load('music\i-surrender.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
                #Play the music
        mixer.music.play()

def github():
        import webbrowser
        webbrowser.open("www.github.com/coderifeanyi")

def sky():
        output.delete(0.0, END)
        message = "Loading Music..."
        output.insert(0.0, message)
        time.sleep(1)
        mixer.init()
        mixer.music.load('music\i-the-lord.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
                #Play the music
        mixer.music.play()

def able():
        output.delete(0.0, END)
        message = "Loading Music..."
        output.insert(0.0, message)
        time.sleep(1)
        mixer.init()
        mixer.music.load('music\you-are-able.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
                #Play the music
        mixer.music.play()
win = Tk()
win.title("Christian Music: By Ifeanyi Onuama")
win.geometry("400x500")
photo = PhotoImage(file = "pics\logo.ico")
win.iconphoto(False, photo)
Button(win, text="Follow me on Github", width=25, command=github) .grid(row=1, column=0, sticky=W)


Label (win, text="Choose a song you would like to listen to:", bg="white", fg="black", font="none 14 bold") .grid(row=2, column=0, sticky=W)
#songs
Button(win, text="Here I am to worship", width=55, command=here) .grid(row=3, column=0, sticky=W)
Button(win, text="Congartualtions, By Ada Ehi", width=55, command=congrats) .grid(row=4, column=0, sticky=W)
Button(win, text="I Surrender by HillSong", width=55, command=surrender) .grid(row=5, column=0, sticky=W)
Button(win, text="I the Lord of sea and sky", width=55, command=sky) .grid(row=6, column=0, sticky=W)
Button(win, text="You are able, By Ada Ehi", width=55, command=able) .grid(row=7, column=0, sticky=W)


Label (win, text="New songs are coming soon", bg="white", fg="black", font="none 10 bold") .grid(row=9, column=0, sticky=W)
Label (win, text="© Copyright 2022 Ifeanyi Onuama. All rights reserved", bg="white") .grid(row=10, column=0, sticky=W)


output = Text(win, width=75, height=6, wrap=WORD, background="grey")
output.grid(row=8, column=0, columnspan=2, sticky=W)
win.mainloop()

