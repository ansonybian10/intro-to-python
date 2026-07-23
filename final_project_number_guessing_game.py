import random

difficulties = {
    "1": ("Easy", 1, 10, 5),
    "2": ("Medium", 1, 50, 7),
    "3": ("Hard", 1, 100, 9),
    "4": ("Impossible", 1, 500, 8)
}

stats = {
    "Easy": {"games": 0, "wins": 0, "best": None},
    "Medium": {"games": 0, "wins": 0, "best": None},
    "Hard": {"games": 0, "wins": 0, "best": None},
    "Impossible": {"games": 0, "wins": 0, "best": None}
}


class GuessingGame:

    def __init__(self, difficulty, low, high, attempts):
        self.difficulty = difficulty
        self.low = low
        self.high = high
        self.max_attempts = attempts
        self.num = random.randint(low, high)
        self.tries = 0
        self.used = set()

    def play(self):
        print(f"\n{self.difficulty} Mode")
        print(f"Guess a number from {self.low} to {self.high}")
        print(f"You get {self.max_attempts} guesses.\n")

        while self.tries < self.max_attempts:

            while True:
                guess = input("Your guess: ")

                try:
                    guess = int(guess)
                except ValueError:
                    print("Enter a number.")
                    continue

                if guess < self.low or guess > self.high:
                    print("That number isn't in the range.")
                    continue

                if guess in self.used:
                    print("You already guessed that.")
                    continue

                break

            self.used.add(guess)
            self.tries += 1

            if guess == self.num:
                print(f"You got it in {self.tries} guesses! Nice job.\n")
                return True

            elif guess < self.num:
                print("Higher!\n")

            else:
                print("Lower!\n")

        print(f"You lost. The number was {self.num}.\n")
        return False


def choose_difficulty():
    print("Choose a difficulty:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 9 attempts)")
    print("4. Impossible (1-500, 8 attempts)")

    while True:
        choice = input("Enter choice (1-4): ")

        if choice in difficulties:
            return difficulties[choice]

        print("Pick a number from 1-4.")


def show_stats():
    print("\nSession Stats")

    for level in stats:
        games = stats[level]["games"]
        wins = stats[level]["wins"]

        if games == 0:
            rate = 0
        else:
            rate = wins / games * 100

        if stats[level]["best"] is None:
            best = "N/A"
        else:
            best = stats[level]["best"]

        print(f"{level}:")
        print(f" Games: {games}")
        print(f" Wins: {wins}")
        print(f" Win Rate: {rate:.0f}%")
        print(f" Best: {best}")
        print()


print("Welcome to the Number Guessing Game!")

while True:
    print("1. Play")
    print("2. View Stats")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        difficulty, low, high, attempts = choose_difficulty()

        game = GuessingGame(difficulty, low, high, attempts)
        won = game.play()

        stats[difficulty]["games"] += 1

        if won:
            stats[difficulty]["wins"] += 1

            if stats[difficulty]["best"] is None or game.tries < stats[difficulty]["best"]:
                stats[difficulty]["best"] = game.tries

    elif choice == "2":
        show_stats()

    elif choice == "3":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice.")