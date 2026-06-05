import cv2
import time
from collections import deque

from HandTrackingModule import HandDetector
from GestureDetector import GestureDetector
from MusicController import MusicController

cap = cv2.VideoCapture(0)

detector = HandDetector()
gesture = GestureDetector()
music = MusicController()

positions = deque(maxlen=10)

status = "Ready"

lastAction = 0
cooldown = 1.5

lastGesture = None

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition(img)

    currentTime = time.time()

    if len(lmList) != 0:

        fingers = gesture.fingersUp(lmList)

        currentGesture = tuple(fingers)

        # Debug
        print(fingers)

        # Index finger x-coordinate
        x = lmList[8][1]

        positions.append(x)



        # Gesture Detection
        if (
            currentTime - lastAction > cooldown
            and currentGesture != lastGesture
        ):
            # Thumbs Up = Next Song
            if gesture.isThumbsUp(lmList):
                music.nextSong()
                status = "NEXT SONG"
                lastAction = currentTime

            elif gesture.isThumbsDown(lmList):
                music.previousSong()
                status = "PREVIOUS SONG"
                lastAction = currentTime
            # Open Palm = Play/Pause
            if fingers == [1, 1, 1, 1, 1]:
                music.playPause()
                status = "PLAY / PAUSE"
                lastAction = currentTime
                lastGesture = currentGesture



            # Index Finger = Volume Up
            elif fingers == [0, 1, 0, 0, 0]:
                music.volumeUp()
                status = "VOLUME UP"
                lastAction = currentTime
                lastGesture = currentGesture

            # Index + Middle = Volume Down
            elif fingers == [0, 1, 1, 0, 0]:
                music.volumeDown()
                status = "VOLUME DOWN"
                lastAction = currentTime
                lastGesture = currentGesture

    else:
        lastGesture = None
        positions.clear()

    # UI Text
    cv2.putText(
        img,
        f"Status: {status}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    instructions = [
        "Thumbs Up : Next Song",
        "Thumbs Down : Previous Song",
        "Open Palm : Play/Pause",
        "Index Finger : Volume Up",
        "Index + Middle : Volume Down",

        "ESC : Exit"
    ]

    y = 100

    for text in instructions:
        cv2.putText(
            img,
            text,
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )
        y += 30

    cv2.imshow("AirSwipe Music Controller", img)

    key = cv2.waitKey(1)

    if key & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()