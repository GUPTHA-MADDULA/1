from tkinter import Tk, Label
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    label.config(text=current_time)  # Update label text
    label.after(1000, update_time)  # Refresh every 1000ms (1 second)

# Create window
window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="steelblue")

# Create label for clock
label = Label(window, font=("Arial Black", 78, "bold"), bg="steelblue", fg="white")
label.pack(pady=60)

# Start the clock update loop
update_time()

window.mainloop()
