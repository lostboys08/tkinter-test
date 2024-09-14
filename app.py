import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random


class NumberGuessingGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        self.root.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

        main_frame = tk.Frame(root)
        main_frame.pack(expand=True, fill=tk.BOTH)

        frame = tk.Frame(main_frame)
        frame.pack(expand=True)

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(frame, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(frame)
        self.entry.pack(pady=5)

        self.entry.bind('<Return>', self.handle_return)
        self.entry.bind('<KP_Enter>', self.handle_return)

        self.guess_button = tk.Button(frame, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(frame, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.target_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess> self.target_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"Congradulations! You guess the number in {self.attempts} attempts.")
                self.reset_game()

            self.root.after(100, self.focus_entry)
        
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid integer.")
            self.root.after(100, self.focus_entry)

    def handle_return(self, event):
        self.check_guess()

    def focus_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
    
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()