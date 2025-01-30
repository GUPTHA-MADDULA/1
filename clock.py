from tkinter import Tk, Label

window = Tk()
window.title("Clock")
window.geometry("600x300")  # Corrected the geometry string
window.configure(bg="steelblue")

label = Label(window, text="Welcome", font=("Arial Black", 78, "bold"), bg="steelblue", fg="white")  # Fixed font syntax
label.pack(pady=100)

window.mainloop()
