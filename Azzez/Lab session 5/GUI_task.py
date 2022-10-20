from tkinter import *


#  The calculator class
class Calculator():

    def __init__(self) -> None:
        super().__init__()

        
        # creating Tk window object
        self.window = Tk()
        self.window.title("Calculator")
        self.window.minsize(width=300, height=300)


        # total sum label 
        # using the grid function for goementry
        self.total_label = Label(text="Total: ", font=("Arial", 12 , "bold"))
        self.total_label.grid(column=0, row=0)

        #  created the calculator output label widget
        self.output = Label(text="0", font=("Arial", 12 , "bold"))
        self.output.grid(column=1, row=0)


        # creating calculator entry widget
        self.input = Entry()
        self.input.grid(column=0, row=1)

        # creating add button widget
        self.add_btn = Button(text="+", command=self.add_input)
        self.add_btn.grid(column=0, row=2)

        # creating substract button widget
        self.substract_btn = Button(text="-", command=self.substract_input)
        self.substract_btn.grid(column=1, row=2, padx=10)

        # creating reset button
        self.reset_btn = Button(text="Reset", command=self.reset)
        self.reset_btn.grid(column=2, row=2)

        # the code below keeps the self.window open
        self.window.mainloop()

    #  function handling addition
    def add_input(self):
        #  the code below gets the current total and adds the input to it
        current_total = int(self.output["text"])
        current_total += int(self.input.get())
        self.output["text"] = current_total


    #  function handling substraction
    def substract_input(self):
        #  the code below gets the current total and substracts the input to it
        current_total = int(self.output["text"])
        current_total -= int(self.input.get())
        self.output.config(text=current_total)

    def reset(self):
        self.output.config(text=0)


# creating the calculator object
calculator = Calculator()
