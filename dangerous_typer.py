import tkinter as tk


class Dangerous_Typer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Most Dangerous Typer")
        self.geometry("800x800")
        self.timer = 5
        self.timer_running = False

        # UI
        self.header = tk.Label(self, text="Start Typing", font=("Arial", 24))
        self.header.pack(pady=20)

        self.timer_label = tk.Label(
            self, text=f"Time left: {self.timer} seconds", font=("Arial", 16)
        )
        self.timer_label.pack(pady=10)

        self.input_frame = tk.Text(self)
        self.input_frame.pack(pady=20)
        self.input_frame.bind("<Key>", self.on_key_press)

        self.reset_button = tk.Button(
            self, text="Reset", command=self.reset_game, font=("Arial", 16)
        )
        self.reset_button.pack(pady=10)

        self.start_button = tk.Button(
            self, text="Start", command=self.start_game, font=("Arial", 16)
        )
        self.start_button.pack(pady=10)

    def on_key_press(self, event):
        self.timer = 6  # Reset timer to 5 seconds when a key is pressed

    def start_game(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()  # Start countdown

    def countdown(self):
        if self.timer > 0:
            self.timer -= 1
            self.timer_label.config(text=f"Time left: {self.timer} seconds")
            self.after(1000, self.countdown)
        else:
            self.input_frame.delete(1.0, tk.END)
            self.input_frame.config(state="disabled")
            self.timer_label.config(text="Time's up!")
            self.header.config(text="Game Over", fg="red")
            self.input_frame.delete(1.0, tk.END)

    def reset_game(self):
        self.timer = 5
        self.timer_label.config(text=f"Time left: {self.timer} seconds")
        self.header.config(text="Start typing!", fg="black")
        self.input_frame.config(state="normal")
        self.input_frame.delete(1.0, tk.END)
        self.timer_running = False
