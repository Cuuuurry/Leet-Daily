from typing import List


class Solution:
    def __init__(self) -> None:
        self.A = None
        self.B = None

    def tictactoe(self, moves: List[List[int]]) -> str:
        Amoves = []
        Bmoves = []
        for i, move in enumerate(moves):
            if i % 2 == 0:
                Amoves.append(move)
            else:
                Bmoves.append(move)
        self.A = Player(Amoves)
        self.A.record()
        self.B = Player(Bmoves)
        self.B.record()
        if self.isDraw():
            return "Draw"
        if self.A.isWinner():
            return "A"
        if self.B.isWinner():
            return "B"
        return "Pending"

    def isDraw(self):
        if not self.A or not self.B:
            raise Exception("Losing Moves of A or B")
        for i in range(3):
            if not self.A.hor[i] or not self.B.hor[i]:
                return False
            if not self.A.ver[i] or not self.B.ver[i]:
                return False
        for direct in ["equal", "reverse"]:
            if not self.A.diag[direct] or not self.B.diag[direct]:
                return False
        return True


class Player(object):
    def __init__(self, moves):
        self.moves = moves
        self.hor = {0: 0, 1: 0, 2: 0}
        self.ver = {0: 0, 1: 0, 2: 0}
        self.diag = {"equal": 0, "reverse": 0}

    def record(self) -> None:
        for move in self.moves:
            self.hor[move[0]] += 1
            self.ver[move[1]] += 1
            self.diag["equal"] += int(move[0] == move[1])
            self.diag["reverse"] += int(move[0] + move[1] == 2)

    def isWinner(self) -> bool:
        for row in self.hor:
            if self.hor[row] == 3:
                return True
        for col in self.ver:
            if self.ver[col] == 3:
                return True
        for dg in self.diag:
            if self.diag[dg] == 3:
                return True

        return False