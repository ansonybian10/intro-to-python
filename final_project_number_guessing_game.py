import random
 
Difficulties = {
    "1": ("Easy", 1, 10, 5),
    "2": ("Medium", 1, 50, 7),
    "3": ("Hard", 1, 100, 9),
    "4": ("Impossible", 1, 500, 8)
}
 
# tracks stats for the current run of the program
session_stats = {
    "Easy": {"games": 0, "wins": 0, "best": None},
    "Medium": {"games": 0, "wins": 0, "best": None},
    "Hard": {"games": 0, "wins": 0, "best": None},
    "Impossible": {"games": 0, "wins": 0, "best": None}
}
 
 
class GuessingGame:
 
    def __init__(self, name, min_num, max_num, max_attempts):
        self.name = name
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.target = random.randint(min_num, max_num)
        self.attempts = 0
        self.guessed_numbers = set()
 
    def get_valid_guess(self):
        """Ask the user for a guess until they give a valid one."""
        while True:
            raw_guess = input(f"Guess a number ({self.min_num}-{self.max_num}): ")
            try:
                guess = int(raw_guess)
            except ValueError:
                print("That's not even a number, try again.")
                continue
 
            if guess < self.min_num or guess > self.max_num:
                print(f"You're guess has to be between {self.min_num} and {self.max_num}.")
                continue
 
            return guess
 
    def play(self):
        print(f"\nStarting {self.name} mode! Guess the number between "
              f"{self.min_num} and {self.max_num}.")
        print(f"You have {self.max_attempts} attempts. Good luck!\n")
 
        while self.attempts < self.max_attempts:
            guess = self.get_valid_guess()
 
            if guess in self.guessed_numbers:
                print("You already guessed that number, try a different one.\n")
                continue
 
            self.guessed_numbers.add(guess)
            self.attempts += 1
 
            if guess < self.target:
                print("Higher!\n")
            elif guess > self.target:
                print("Lower!\n")
            else:
                print(f"Correct! You got it in {self.attempts} attempts.\n")
                return True
 
        print(f"Game over, you ran out of attempts! The number was {self.target}.\n")
        return False
 
 
def get_difficulty():
    ## ask the user to pick a difficulty, game (obviously) gets harder as difficulty increases
    print("Choose a difficulty:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 9 attempts)")
    print("4. Impossible (1-500, 8 attempts)")
 
    while True:
        choice = input("Enter choice (1-4): ")
        if choice in Difficulties:
            return Difficulties[choice]
        print("Invalid choice. Please enter a number from 1 to 4.")
 
 
def save_score(difficulty, won, attempts):
    session_stats[difficulty]["games"] += 1
 
    if won:
        session_stats[difficulty]["wins"] += 1
        current_best = session_stats[difficulty]["best"]
        if current_best is None or attempts < current_best:
            session_stats[difficulty]["best"] = attempts
 
 
def show_stats():
    print("\n--- STATS (this session) ---")
    for difficulty, data in session_stats.items():
        games = data["games"]
        wins = data["wins"]
        best = data["best"] if data["best"] is not None else "N/A"
 
        win_rate = (wins / games * 100) if games > 0 else 0
 
        print(f"{difficulty}: {games} games played, {wins} wins, "
              f"{win_rate:.0f}% win rate, best score: {best} attempts")
    print()
 
 
def play_game():
    name, min_num, max_num, max_attempts = get_difficulty()
    game = GuessingGame(name, min_num, max_num, max_attempts)
    won = game.play()
    save_score(name, won, game.attempts)
 
 
def main_menu():
    print("Welcome to the Number Guessing Game!")
 
    while True:
        print("\n1. Play Game")
        print("2. View Stats")
        print("3. Quit")
        choice = input("Choose an option (1-3): ")
 
        if choice == "1":
            play_game()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
 
 
if __name__ == "__main__":
    main_menu()