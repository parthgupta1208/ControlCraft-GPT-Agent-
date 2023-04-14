
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]

        row_index = 1
        col_index = 0

        for button in buttons:
            command = lambda x=button: self.handle_button_click(x)
            tk.Button(master, text=button, width=7, height=2, command=command)\
                .grid(row=row_index, column=col_index, padx=5, pady=5)
            col_index += 1
            if col_index > 3:
                row_index += 1
                col_index = 0

        tk.Button(master, text="=", width=16, height=2, command=self.calculate)\
            .grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def handle_button_click(self, button_text):
        current_text = self.display.get()
        new_text = current_text + button_text
        self.display.delete(0, tk.END)
        self.display.insert(0, new_text)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
