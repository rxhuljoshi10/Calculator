from tkinter import *

class Calculator:
    def __init__(self,root):
        self.root = root
        self.themeColor = "DodgerBlue"
        self.rowCounter = 1
        self.colCounter = 0
        self.calcButtons = ['C','%','<=','÷',7,8,9,'x',4,5,6,'-',1,2,3,'+','00',0,'.','=']

        self.screen = Entry(self.root, fg=self.themeColor, bg="black", highlightthickness=2, highlightbackground=self.themeColor, font=("Courier",22), width=13)
        self.screen.grid(sticky=N, padx=5, pady=10, ipadx=10, ipady=5)
        
        self.buttonArea = Frame(self.root, bg="grey", height=200)
        self.buttonArea.grid(padx=5)

        for button in self.calcButtons:
            button = self.createButton(button)
            button.bind("<Enter>",lambda event, arg=button : self.onButton(arg))
            button.bind("<Leave>",lambda event, arg=button : self.offButton(arg))

    def createButton(self, text):
        b = Button(self.buttonArea, text=text, command=lambda: self.click(text), relief="raised", bg="black", fg=self.themeColor, font=("Courier",22), width=3, highlightthickness=2, highlightcolor="red",highlightbackground="red")
        b.grid(row=self.rowCounter, column=self.colCounter)

        self.colCounter += 1
        if self.colCounter > 3:
            self.rowCounter += 1
            self.colCounter = 0
        return b

    def onButton(self, b):
        b.config(bg="#0a1715")

    def offButton(self, b):
        b.config(bg="black")

    def click(self,val):
        if val == "=":
            self.calculate()

        elif val == 'C':
            self.screen.delete('0',END)

        elif val == '<=':
            screenVal = self.screen.get()
            updatedVal = screenVal[:-1]
            self.screen.delete('0',END)
            self.screen.insert('0',updatedVal)

        else:
            self.screen.insert(END, val)

    def calculate(self):
        exp = self.screen.get()
        try:
            exp = exp.replace('x','*')
            exp = exp.replace('÷','/')
            result = eval(exp)
            self.screen.delete('0',END)
            self.screen.insert('0',result)
        except:
            pass
        

root = Tk()
root.geometry("262x365")
root.title("Calculator")
root.iconbitmap("Calculator\CalcIcon.ico")
root.resizable(0,0)
root.config(bg="black", highlightthickness=1, highlightcolor="DodgerBlue")
Calculator(root)
root.mainloop()