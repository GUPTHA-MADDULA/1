from tkinter import Tk, Label
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    greeting = "Hello Guptha!\n"  # Greeting on top
    time_display = f"Time is: {current_time}"  # Time below greeting
    label_greet.config(text=greeting)
    label_time.config(text=time_display)
    label_time.after(1000, update_time)  # Refresh every 1000ms (1 second)

# Create window
window = Tk()
window.title("Personalized Digital Clock")
window.geometry("700x350")
window.configure(bg="#1E1E2E")  # Vibrant background

# Create greeting label
label_greet = Label(window, font=("Arial Black", 36, "bold"), bg="#1E1E2E", fg="#F8C471")
label_greet.pack(pady=20)

# Create time display label
label_time = Label(window, font=("Arial Black", 48, "bold"), bg="#1E1E2E", fg="#85C1E9")
label_time.pack()

# Start the clock update loop
update_time()

window.mainloop()
