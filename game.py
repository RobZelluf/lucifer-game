import random

class Game:
    def __init__(self, num_lucifers):
        self.num_lucifers = num_lucifers
        self.lucifers = num_lucifers
        self.drink_chance = 0.5

    def reset_game(self):
        self.lucifers = self.num_lucifers

    def print_game(self):
        print("Number of lucifers:", self.lucifers)
        print("| " * self.lucifers,"\n")

    def verify_move(self, number):
        if len(number) != 1:
            return False
        if not number.isdigit():
            return False
        else:
            number = int(number)

        if number < 1 or number > 3:
            return False
        if number > self.lucifers:
            return False

        return True

    def take_lucifers(self):
        number = input("Take 1-3 lucifers:")

        if not self.verify_move(number):
            print("Invalid move!")
            return self.take_lucifers()
        else:
            number = int(number)
            self.lucifers -= number

    def computer_turn(self):
        number = (self.lucifers - 1) % 4
        if number == 0:
            number = random.randint(1, 3)

        self.lucifers -= number
        print("Computer took", number, "lucifers")

    def drink(self):
        if random.random() < self.drink_chance:
            print("DRINK!")
            input("Press any key to continue")

        self.drink_chance += 0.025


def main():
    game = Game(15)
    won = False
    while True:
        game.reset_game()
        while True:
            game.print_game()
            game.take_lucifers()

            if game.lucifers == 1:
                game.print_game()
                print("You won!")
                won = True
                break

            if game.lucifers == 0:
                print("You lost!")
                game.drink()
                break

            game.print_game()
            game.computer_turn()

        if won:
            break


if __name__ == '__main__':
    main()
