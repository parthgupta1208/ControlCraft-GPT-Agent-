
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

        self.equation = ""

    def create_button(self, text, row, column, columnspan=1, rowspan=1):
        button = tk.Button(self.master, text=text, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.equation = ""
            self.display.delete(0, tk.END)
        elif text == "=":
            answer = str(eval(self.equation))
            self.display.delete(0, tk.END)
            self.display.insert(0, answer)
            self.equation = answer
        else:
            self.equation += text
            self.display.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
