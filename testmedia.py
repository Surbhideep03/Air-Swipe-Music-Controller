from MusicController import MusicController
import time

music = MusicController()

print("Testing in 3 seconds...")
time.sleep(3)

music.playPause()