import pyglet
import time

notif = pyglet.media.load("voice/warningMasker1.mp3",streaming = False)

def mainkan():
    notif.play()
    time.sleep(5)

mainkan()


