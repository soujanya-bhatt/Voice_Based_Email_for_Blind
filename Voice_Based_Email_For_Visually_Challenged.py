import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time

print("-" * 60)
print("         Project: Voice based Email for blind")
print("                 <--Created by -->")
print("-" * 60)
# pyglet.lib.load_library('avbin')
# pyglet.have_avbin=True

# project name
tts = gTTS(text="Project: Voice based Email for blind", lang='en')
ttsname = ("name.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

# login from os
login = os.getlogin
print("You are logging in from : " + login())

# choices
print("1. compose a mail.")
tts = gTTS(text="option 1. compose a mail.", lang='en')
ttsname = ("hello.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname = ("hello.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)
# voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print("Your choice:")
    tts = gTTS(text="Your choice ", lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)
    audio = r.listen(source)
    print("ok done!!")
    tts = gTTS(text="ok done ", lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

try:
    text = r.recognize_google(audio)
    print("You said : " + text)
    tts = gTTS(text="you said "+text, lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    tts = gTTS(text="Google Speech Recognition could not understand audio. ", lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# choices details
if text == '1' or text == 'one' or text =='won' or text == 'on':
    r = sr.Recognizer()  # recognize
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Your message :")
        tts = gTTS(text=" your message", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        audio = r.listen(source)
        print("ok done!!")
        tts = gTTS(text="ok done ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
    try:
        text1 = r.recognize_google(audio)
        print("You said : " + text1)
        tts = gTTS(text=" You said"+text1, lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        msg = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        tts = gTTS(text="Google Speech Recognition could not understand audio. ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    mail = smtplib.SMTP('smtp.gmail.com', 587)  # host and port area
    mail.ehlo()  # Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls()  # security connection
    mail.login('sou103janyas@gmail.com', 'sou@miniproject')  # login part
    mail.sendmail('sou103janyas@gmail.com', 'sou103janyas@gmail.com', msg)  # send part
    print("Congrats! Your mail has been sent. ")
    tts = gTTS(text="Congrats! Your mail has been sent. ", lang='en')
    ttsname = ("send.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()

if text == '2' or text == 'tu' or text == 'two' or text == 'Tu':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)  # this is host and port area.... ssl security
    unm = ('sou103janyas@gmail.com')  # username
    psw = ('sou@miniproject')  # password
    mail.login(unm, psw)  # login
    stat, total = mail.select('Inbox')  # total number of mails in inbox
    print("Number of mails in your inbox :" + str(total))
    tts = gTTS(text="Total mails are :" + str(total), lang='en')  # voice out
    ttsname = ("total.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    # unseen mails
    unseen = mail.search(None, 'UnSeen')  # unseen count
    print("Number of UnSeen mails :" + str(unseen))

    result, data = mail.uid('search', None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)')  # fetch
    raw_email = email_data[0][1].decode("utf-8")  # decode
    email_message = email.message_from_string(raw_email)
    print("From: " + email_message['From'])
    tts = gTTS(text="From :" + email_message['From'] , lang='en')
    ttsname = ("mail.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("Subject: " + str(email_message['Subject']))
    tts = gTTS(text="And Your subject: " + str(email_message['Subject']), lang='en')
    ttsname = ("mail.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    # Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print("Body :" + txt)
    tts = gTTS(text="Body: " + txt, lang='en')
    ttsname = ("body.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()
    mail.logout()