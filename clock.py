import tkinter as tk
from time import strftime


def update_clock():
    """Update the time and date displayed on the clock."""
    current_time = strftime("%I:%M:%S %p")
    current_date = strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Update again after 1 second
    root.after(1000, update_clock)


# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("700x300")
root.configure(bg="#111111")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Arial", 18, "bold"),
    fg="#888888",
    bg="#111111"
)
title_label.pack(pady=(30, 5))

# Time display
time_label = tk.Label(
    root,
    text="00:00:00 AM",
    font=("Courier New", 64, "bold"),
    fg="#00ff88",
    bg="#111111"
)
time_label.pack(pady=10)

# Date display
date_label = tk.Label(
    root,
    text="Loading...",
    font=("Arial", 20),
    fg="#ffffff",
    bg="#111111"
)
date_label.pack(pady=10)

# Start the clock
update_clock()

# Run the application
root.mainloop()
