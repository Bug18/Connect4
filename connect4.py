from copy import *
movesX = [0, 1, 1, 1]
movesY = [1, 1, 0, -1]

# scores = [0, 0, 5, 15, 1000]

"""
s0 = [0, 0, 0, 0, 0, 0]
s1 = [0, 0, 0, 0, 0, 0]
s2 = [2, 0, 0, 0, 0, 0]
s3 = [1, 2, 0, 0, 0, 0]
s4 = [1, 1, 2, 0, 0, 0]
s5 = [1, 1, 1, 0, 0, 0]
s6 = [0, 0, 0, 0, 0, 0]
m = [s0, s1, s2, s3, s4, s5, s6]


s0 = [0, 0, 0, 0, 0, 0]
s1 = [2, 0, 0, 0, 0, 0]
s2 = [1, 0, 0, 0, 0, 0]
s3 = [1, 0, 0, 0, 0, 0]
s4 = [1, 0, 0, 0, 0, 0]
s5 = [0, 0, 0, 0, 0, 0]
s6 = [0, 0, 0, 0, 0, 0]
m = [s0, s1, s2, s3, s4, s5, s6]
"""

points = {
    0: 0,
    1: 1,
    2: 10,
    3: 200,
    4: 200,
    5: 200,
    6: 200,
    7: 200
}


def AI(M):
    povoljnosti = []
    for i in range(7):
        M2 = deepcopy(M)
        index = get_free(M2[i])
        if index == -1:
            povoljnosti.append(-1000)
            continue
        M2[i][index] = 2
        if checkWin(M2, i):
            return i
        if checkWinPlayer(M2, i):
            return i
        p = povoljnost(M2)
        povoljnosti.append(p)
    maximum = -100000000000000000
    indexmaximum = 3
    test = False
    print(povoljnosti)

    for j in range(7):
        if povoljnosti[j] > maximum:
            maximum = povoljnosti[j]
            indexmaximum = j
            test = True

    if test:
        return indexmaximum
    else:
        for k in range(7):
            new_index = get_free(M[k])
            if new_index != -1:
                return new_index


def povoljnost(M):
    s = 0
    for i in range(7):
        s = s + povoljnostStupca(M, i)

    return s


def get_free(s):
    for i in range(6):
        if s[i] == 0:
            return i
    return -1


def checkWin(m, i):
    x = i
    y = get_free(m[i])
    if y == -1:
        y = 5
    y -= 1
    movesX = [0, 1, 1, 1]
    movesY = [1, 1, 0, -1]
    for i in range(4):
        streak = findRow(m, x, y, movesX[i], movesY[i], 2) + findRow(m, x, y, -movesX[i], -movesY[i], 2) + 1
        if streak >= 4:
            return True
    return False


def checkWinPlayer(m, i):
    x = i
    y = get_free(m[i])
    if y == -1:
        y = 5
    y -= 1
    movesX = [0, 1, 1, 1]
    movesY = [1, 1, 0, -1]
    for i in range(4):
        streak = findRow(m, x, y, movesX[i], movesY[i], 1) + findRow(m, x, y, -movesX[i], -movesY[i], 1) + 1
        if streak >= 4:
            return True
    return False


def povoljnostStupca(m, i):
    stupac = m[i]
    y0 = get_free(stupac)
    if y0 == -1:
        return 0
    x0 = i
    movesX = [0, 1, 1, 1]
    movesY = [1, 1, 0, -1]
    rez = 0
    for p in range(1, 3):
        for i in range(4):
            streak = findRow(m, x0, y0, movesX[i], movesY[i], p) + findRow(m, x0, y0, -movesX[i], -movesY[i], p)
            if p == 2:
                rez += points[streak]
            else:
                rez -= points[streak] * 3
    return rez


def findRow(m, x, y, sx, sy, player):
    streak = 0

    for i in range(7):
        x += sx
        y += sy
        if isValid(x, y) and m[x][y] == player:
            streak += 1
        else:
            break

    return streak


def isValid(x, y):
    return 0 <= x <= 6 and 0 <= y <= 5
