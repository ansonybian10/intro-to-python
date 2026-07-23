import random
import tkinter as tk
 
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
 
FONT = ("Arial", 20)
 
class GuessingGame:
 
    def __init__(self, difficulty, low, high, attempts):
        self.difficulty = difficulty
        self.low = low
        self.high = high
        self.max_attempts = attempts
        self.num = random.randint(low, high)
        self.tries = 0
        self.used = set()
 
    def check_guess(self, guess):
        # returns a string message, and whether the game is over
        if guess in self.used:
            return "You already guessed that.", False
 
        self.used.add(guess)
        self.tries += 1
 
        if guess == self.num:
            return f"Correct! You got it in {self.tries} guesses.", True
 
        elif guess < self.num:
            remaining = self.max_attempts - self.tries
            if remaining == 0:
                return f"Higher! Out of attempts. The number was {self.num}.", True
            return f"Higher! {remaining} attempts left.", False
 
        else:
            remaining = self.max_attempts - self.tries
            if remaining == 0:
                return f"Lower! Out of attempts. The number was {self.num}.", True
            return f"Lower! {remaining} attempts left.", False
 
# rest of this stuff is tkinter gui code 
 
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x650")
root.update_idletasks()
width = 500
height = 650
x = (root.winfo_screenwidth() // 2) - (width // 2)      # this centers the windows on your screen. i did this because not all
y = (root.winfo_screenheight() // 2) - (height // 2)    # screens are the same size, so it will center on all devices
root.geometry(f"{width}x{height}+{x}+{y}")
 
game = None
 
difficulty_label = tk.Label(root, text="Choose a difficulty:", font=FONT)
difficulty_label.pack(pady=5)
 
difficulty_var = tk.StringVar(value="1")
 
for key in difficulties:
    name = difficulties[key][0]
    rb = tk.Radiobutton(root, text=name, variable=difficulty_var, value=key, font=FONT)
    rb.pack()
 
info_label = tk.Label(root, text="", font=FONT, wraplength=450)
info_label.pack(pady=5)
 
guess_entry = tk.Entry(root, font=FONT)
 
result_label = tk.Label(root, text="", font=FONT, wraplength=450)
 
def start_game():
    global game
 
    choice = difficulty_var.get()
    name, low, high, attempts = difficulties[choice]
    game = GuessingGame(name, low, high, attempts)
 
    info_label.config(text=f"Guess a number from {low} to {high} ({attempts} attempts)")
    guess_entry.pack(pady=5)
    submit_button.pack(pady=5)
    result_label.pack(pady=5)
    result_label.config(text="")
    guess_entry.config(state="normal")
    submit_button.config(state="normal")
    guess_entry.delete(0, tk.END)
 
def submit_guess():
    guess = guess_entry.get()
 
    try:
        guess = int(guess)
    except ValueError:
        result_label.config(text="Enter a number.")
        return
 
    if guess < game.low or guess > game.high:
        result_label.config(text="That number isn't in the range, you probably made a typo.")
        return
 
    message, game_over = game.check_guess(guess)
    result_label.config(text=message)
    guess_entry.delete(0, tk.END)
 
    if game_over:
        stats[game.difficulty]["games"] += 1
        won = "Correct" in message
 
        if won:
            stats[game.difficulty]["wins"] += 1
            best = stats[game.difficulty]["best"]
            if best is None or game.tries < best:
                stats[game.difficulty]["best"] = game.tries
 
        # stops the game, no more guesses are allowed unless the user starts a new game
        guess_entry.config(state="disabled")
        submit_button.config(state="disabled")
 
 
start_button = tk.Button(root, text="Start Game", command=start_game, font=FONT)
start_button.pack(pady=5)
 
submit_button = tk.Button(root, text="Submit Guess", command=submit_guess, font=FONT)
 
stats_window_open = None
 
def view_stats():
    global stats_window_open
 
    # if a stats window is already open, close it first, only then can you open a new one, this prevents multiple stats windows
    # from opening, I tested this and having multiple windows open was pretty annoying
    if stats_window_open is not None:
        stats_window_open.destroy()
 
    stats_window = tk.Toplevel(root)
    stats_window.title("Session Stats")
    stats_window.geometry("400x300")
    stats_window_open = stats_window
 
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
 
        text = f"{level}: {games} games, {wins} wins, {rate:.0f}% win rate, best: {best}"
        label = tk.Label(stats_window, text=text, font=FONT, wraplength=380, justify="left")
        label.pack(pady=3)
 
stats_button = tk.Button(root, text="View Stats", command=view_stats, font=FONT)
stats_button.pack(pady=5)
 
root.mainloop()