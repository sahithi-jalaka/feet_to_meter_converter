
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Feet to Meter Converter",
              font=("Arial", 16, "bold")).grid(
                  row=0, column=0, columnspan=2, pady=10)

        Label(self, text="Enter feet:").grid(
            row=1, column=0, padx=5, pady=5)

        self.feet = StringVar()
        Entry(self, textvariable=self.feet).grid(
            row=1, column=1, padx=5, pady=5)

        Button(self, text="Convert",
               command=self.convert).grid(
                   row=2, column=0, columnspan=2, pady=10)

        self.result = StringVar()
        Label(self, textvariable=self.result,
              font=("Arial", 12)).grid(
                  row=3, column=0, columnspan=2, pady=5)

    def convert(self):
        try:
            feet = float(self.feet.get())
            meters = feet * 0.3048
            self.result.set(f"{feet} feet = {meters:.4f} meters")
        except ValueError:
            self.result.set("Please enter a valid number!")


root = Tk()
root.title("Feet to Meter Converter")
root.geometry("350x200")

app = Application(root)
root.mainloop()
