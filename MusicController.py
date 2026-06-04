import pyautogui

class MusicController:

    def playPause(self):
        pyautogui.press("playpause")

    def nextSong(self):
        pyautogui.press("nexttrack")

    def previousSong(self):
        pyautogui.press("prevtrack")

    def volumeUp(self):
        pyautogui.press("volumeup")

    def volumeDown(self):
        pyautogui.press("volumedown")

    def mute(self):
        pyautogui.press("volumemute")