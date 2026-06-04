import ctypes

VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1

def press_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    ctypes.windll.user32.keybd_event(key, 0, 2, 0)

def play_pause():
    press_key(VK_MEDIA_PLAY_PAUSE)

def next_track():
    press_key(VK_MEDIA_NEXT_TRACK)

def previous_track():
    press_key(VK_MEDIA_PREV_TRACK)