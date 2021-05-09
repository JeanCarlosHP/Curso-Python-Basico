from pygame import mixer, event

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input()
event.wait()
