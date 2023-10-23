from random import randint


class Rocket:
    def __init__(self, x: int = 2) -> None:
        self.distance = x

    def __str__(self) -> str:
        return "jestem rakietą"


class Board:
    def __init__(self, x: int = 1) -> None:
        self.rockets = []
        for i in range(x):
            self.rockets.append(Rocket())

        for i in self.rockets:
            i.distance = randint(1,6)

    def __len__(self):
        return len(self.rockets)

    @staticmethod
    def get_distance(rocket1: Rocket, rocket2: Rocket) -> int:
        return rocket1.distance - rocket2.distance

board = Board(3)
for i in board.rockets:
    print(i, i.distance)

print(Board.get_distance(board.rockets[1], board.rockets[2]))
print(len(board))
