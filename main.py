from graphics import *
from math import *
from Connect4.connect4 import *


class Stupac:
    def __init__(self, id):
        self.content = [0] * 6
        self.id = id

    def get_free(self):
        for index in range(len(self.content)):
            if self.content[index] == 0:
                return index
        return -1

    def push(self, player, win):
        free_index = self.get_free()
        if free_index == -1:
            return -1
        self.content[free_index] = player
        cir = Circle(Point(self.id + 0.5, free_index + 0.5), 0.5)
        if player == 1:
            cir.setFill('red')
        elif player == 2:
            cir.setFill('blue')
        cir.draw(win)
        return free_index

    def __getitem__(self, item):
        return self.content[item]

    def __setitem__(self, key, value):
        self.content[key] = value

    def get_player(self, index):
        return self.content[index]


def check_horizontal(stupci, x, y):
    player = stupci[x][y]
    counter = 0

    if x + 3 > 6:
        pom = 6 - x + 1
    else:
        pom = 4

    for i in range(1, pom):
        if stupci[x + i][y] == player:
            counter += 1
        elif stupci[x + i][y] != player:
            break
    if counter == 3:
        return True

    while x >= 0:
        x -= 1
        if stupci[x][y] == player:
            counter += 1
        elif stupci[x][y] != player:
            if counter == 3:
                return True
            elif counter < 3:
                return False
        if counter == 3:
            return True


def check_vertical(stupci, x, y):
    player = stupci[x][y]
    counter = 0

    # test_list.insert(0, 6)

    while y >= 0:
        y -= 1
        if stupci[x][y] == player:
            counter += 1
        elif stupci[x][y] != player:
            if counter == 3:
                return True
            elif counter < 3:
                return False
        if counter == 3:
            return True


def check_diagonal(stupci, x, y):
    player = stupci[x][y]
    counter = 0
    counter2 = 0
    excluded_left = [[0, 0, 1, 2], [1, 0, 1], [2, 0], [4, 5], [5, 4, 5], [6, 3, 4, 5]]
    excluded_right = [[0, 3, 4, 5], [1, 4, 5], [2, 5], [4, 0], [5, 0, 1], [6, 0, 1, 2]]

    state = True
    state2 = True
    state3 = True
    state4 = True

    for k in excluded_left:
        if k[0] == x:
            for l in range(1, len(k)):
                if k[l] == y:
                    state = False
                    state2 = False

    for k in excluded_right:
        if k[0] == x:
            for l in range(1, len(k)):
                if k[l] == y:
                    state3 = False
                    state4 = False

    for j in range(1, 4):
        x2 = x - j
        y2 = y + j
        x3 = x + j
        y3 = y - j
        x4 = x + j
        y4 = y + j
        x5 = x - j
        y5 = y - j

        if x2 >= 0 and y2 <= 5 and state is True:
            if stupci[x2][y2] == player:
                counter += 1
            else:
                state = False

        if x3 <= 6 and y3 >= 0 and state2 is True:
            if stupci[x3][y3] == player:
                counter += 1
            else:
                state2 = False

        if x4 <= 6 and y4 <= 5 and state3 is True:
            if stupci[x4][y4] == player:
                counter2 += 1
            else:
                state3 = False

        if x5 >= 0 and y5 >= 0 and state4 is True:
            if stupci[x5][y5] == player:
                counter2 += 1
            else:
                state4 = False

    if counter == 3 or counter2 == 3:
        return True
    else:
        return False


def check_four(stupci, x, y):
    if check_horizontal(stupci, x, y) is True or check_vertical(stupci, x, y) is True or check_diagonal(stupci, x, y) is True:
        return True


def main():
    state = True
    stupci = []
    for k in range(7):
        stupci.append(Stupac(k))

    win = GraphWin("Connect 4", width=1000, height=800, autoflush=True)
    win.setCoords(0, 0, 7, 6)

    for i in range(1, 6):
        l = Line(Point(0, i), Point(7, i))
        l.draw(win)

    for j in range(1, 7):
        l = Line(Point(j, 6), Point(j, 0))
        l.draw(win)

    ############################################################################################
    counter = 0

    while state:
        illegal_state = False
        mouse_point = win.getMouse()
        x = int(floor(mouse_point.getX()))
        y = stupci[x].push(1, win)
        if y == -1:
            print("Bad move. Play again...")
            illegal_state = True

        p1 = check_four(stupci, x, y)

        if p1:
            state = False
            msg = Text(Point(3.5, 3.5), "Win Player!")
            msg.setSize(36)
            msg.draw(win)

        if state and not illegal_state:
            x2 = AI(stupci)
            y2 = stupci[x2].push(2, win)

            p2 = check_four(stupci, x2, y2)

            if p2 and state:
                state = False
                msg = Text(Point(3.5, 3.5), "Win AI!")
                msg.setSize(36)
                msg.draw(win)
        elif illegal_state:
            continue

        counter += 2

        if counter == 42 and state:
            msg = Text(Point(3.5, 3.5), "Draw!")
            msg.setSize(36)
            msg.draw(win)
            state = False

        if not state:
            win.getMouse()
            win.close()


if __name__ == '__main__':
    main()
