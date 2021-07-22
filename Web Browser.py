import tkinter as tk
from tkinter import *
import webbrowser


def google():
    webbrowser.open("www.google.com")

def facebook():
    webbrowser.open("www.facebook.com")

def whatsapp():
    webbrowser.open("www.whatsapp.com")

def youtube():
    webbrowser.open("www.youtube.com")

def twitter():
    webbrowser.open("www.twitter.com")

def gmail():
    webbrowser.open("www.gmail.com")

def snapchat():
    webbrowser.open("www.snapchat.com")

def instagram():
    webbrowser.open("www.instagram.com")



win = tk.Tk()
win.title("MY WebBrowser")
win.geometry("1000x500")

ifacebook = PhotoImage(file="facebook.png")
facebook = tk.Button(win,image=ifacebook,command=facebook)
facebook.grid(row=1,column=3)

iyoutube = PhotoImage(file="youtube.png")
youtube = tk.Button(win,image=iyoutube,command=youtube)
youtube.grid(row=1,column=2)


iinstagram = PhotoImage(file="instagram.png")
instagram = tk.Button(win,image=iinstagram,command=instagram)
instagram.grid(row=0,column=1)

itwitter = PhotoImage(file="twitter.png")
twitter = tk.Button(win,image=itwitter,command=twitter)
twitter.grid(row=0,column=2)

isnapchat = PhotoImage(file="snapchat.png")
snapchat = tk.Button(win,image=isnapchat,command=snapchat)
snapchat.grid(row=0,column=3)

iwhatsapp = PhotoImage(file="whatsapp.png")
whatsapp = tk.Button(win,image=iwhatsapp,command=whatsapp)
whatsapp.grid(row=0,column=0)

igmail = PhotoImage(file="gmail.png")
gmail = tk.Button(win,image=igmail,command=gmail)
gmail.grid(row=1,column=0)

igoogle = PhotoImage(file="google.png")
google = tk.Button(win,image=igoogle,command=google)
google.grid(row=1,column=1)



win.mainloop()