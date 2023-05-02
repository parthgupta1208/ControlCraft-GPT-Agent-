
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.master.geometry('300x250')
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=True, fill='both')
        self.display = tk.Entry(self.frame, width=25, font=('Arial', 12))
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=5)
        self.buttons = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '.', 'C', '/']
        self.row, self.col = 1, 0
        for button in self.buttons:
            if button in ['+', '-', '*', '/']:
                tk.Button(self.frame, text=button, width=5, height=2, font=('Arial', 12), fg='blue', bd=0,
                          command=lambda x=button: self.display.insert(tk.END, x)).grid(row=self.row, column=self.col)
            elif button == 'C':
                tk.Button(self.frame, text=button, width=5, height=2, font=('Arial', 12), fg='white', bg='red', bd=0,
                          command=lambda: self.display.delete(0, tk.END)).grid(row=self.row, column=self.col)
            else:
                tk.Button(self.frame, text=button, width=5, height=2, font=('Arial', 12), bd=0,
                          command=lambda x=button: self.display.insert(tk.END, x)).grid(row=self.row, column=self.col)
            self.col += 1
            if self.col > 3:
                self.row += 1
                self.col = 0

def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
