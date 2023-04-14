
import tkinter as tk

class Calculator:
    
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.display = tk.Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*", "/", "C", "="]
        
        self.create_buttons()
        
        self.equation = ""
    
    def create_buttons(self):
        row_num = 1
        col_num = 0
        for button in self.buttons:
            command = lambda x=button: self.click_button(x)
            
            tk.Button(self.master, text=button, padx=40, pady=20, command=command).grid(row=row_num, column=col_num)
            
            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1
    
    def click_button(self, button):
        if button == "C":
            self.equation = ""
            self.display.delete(0, tk.END)
        elif button == "=":
            try:
                self.result = eval(self.equation)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(self.result))
                self.equation = ""
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.equation = ""
        else:
            self.equation += button
            self.display.insert(tk.END, button)
            

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
