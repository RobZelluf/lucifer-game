import random

class Game:
    def __init__(self, num_matches):
        self.num_matches = num_matches
        self.matches = num_matches
        self.drink_chance = 0.3

    def reset_game(self):
        self.matches = self.num_matches

    def print_game(self):
        print("Number of matches:", self.matches)
        print("| " * self.matches,"\n")

    def verify_move(self, number):
        if len(number) != 1:
            return False
        if not number.isdigit():
            return False
        else:
            number = int(number)

        if number < 1 or number > 3:
            return False
        if number > self.matches:
            return False

        return True

    def take_matches(self):
        number = input("Take 1-3 matches:")

        if not self.verify_move(number):
            print("Invalid move!")
            return self.take_matches()
        else:
            number = int(number)
            self.matches -= number

    def computer_turn(self):
        number = (self.matches - 1) % 4
        if number == 0:
            number = random.randint(1, 3)

        self.matches -= number
        print("Computer took", number, "matches")

    def drink(self):
        if random.random() < self.drink_chance:
            print("DRINK!")
            input("Press any key to continue")

        self.drink_chance += 0.05


def main():
    game = Game(15)
    won = False
    while True:
        game.reset_game()
        while True:
            game.print_game()
            game.take_matches()

            if game.matches == 1:
                game.print_game()
                print("You won!")
                won = True
                break

            if game.matches == 0:
                print("You lost!")
                game.drink()
                break

            game.print_game()
            game.computer_turn()

        if won:
            break


if __name__ == '__main__':
    main()
