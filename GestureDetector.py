class GestureDetector:

    def fingersUp(self, lmList):

        if len(lmList) == 0:
            return []

        fingers = []

        # Thumb Open
        fingers.append(
            1 if lmList[4][1] > lmList[3][1] else 0
        )

        # Index
        fingers.append(
            1 if lmList[8][2] < lmList[6][2] else 0
        )

        # Middle
        fingers.append(
            1 if lmList[12][2] < lmList[10][2] else 0
        )

        # Ring
        fingers.append(
            1 if lmList[16][2] < lmList[14][2] else 0
        )

        # Pinky
        fingers.append(
            1 if lmList[20][2] < lmList[18][2] else 0
        )

        return fingers

    def isThumbsUp(self, lmList):

        return (
            lmList[4][2] < lmList[3][2] < lmList[2][2] and
            lmList[8][2] > lmList[6][2] and
            lmList[12][2] > lmList[10][2] and
            lmList[16][2] > lmList[14][2] and
            lmList[20][2] > lmList[18][2]
        )

    def isThumbsDown(self, lmList):

        return (
            lmList[4][2] > lmList[3][2] > lmList[2][2] and
            lmList[8][2] > lmList[6][2] and
            lmList[12][2] > lmList[10][2] and
            lmList[16][2] > lmList[14][2] and
            lmList[20][2] > lmList[18][2]
        )
