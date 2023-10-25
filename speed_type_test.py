import tkinter as tk
import random
import time
#speed typing using python
class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.words = ["hello", "world", "python", "programming", "keyboard", "challenge", "speed", "test", "practice", "coding"]
        self.current_word = None
        self.score = 0
        self.start_time = None
        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.input_entry = tk.Entry(root)
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.time_label = tk.Label(root, text="Time: 0s")
        self.word_label.pack(pady=20)
        self.input_entry.pack(pady=10)
        self.start_button.pack()
        self.score_label.pack()
        self.time_label.pack()
        self.input_entry.bind("<Return>", self.check_word)
    def start_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.input_entry.delete(0, tk.END)
        self.input_entry.config(state=tk.NORMAL)
        self.next_word()
    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
    def check_word(self, event):
        user_input = self.input_entry.get().strip()
        if user_input == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.input_entry.delete(0, tk.END)
            self.next_word()
        if self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text=f"Time: {elapsed_time}s")
    def end_game(self):
        self.input_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.word_label.config(text="Game Over!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
