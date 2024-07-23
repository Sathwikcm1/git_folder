from tkinter import * #importing tkinter module.

win = Tk() # making an object of the class Tk
win.title('Calculator') #adding the title of the window.
win.geometry('550x750+100+100') #setting the window size, that is 400*600 pixel and 100,100 pixels from the left corner of the screen.
# win.resizable(0,0) # making the window fixed.
win.config(bg = 'black') # configuring the background color of the window to black.
label_result = Label(win, width = 16, height = 3, background = 'grey', font=('arial', 30, 'bold') , text = "Enter Expression") # label_result is the name of the object of the class lebel. we set the background color to grey and set the font size width and height and everything .
label_result.grid(row = 0, column = 0, columnspan = 4, padx = 1, pady = 20) # placing the label_result in the grid., this is the first row and the first column.




eqn = '' # this is the equation for the calculator.

def clear():
    global eqn
    eqn = '' # setting the eqn to empty because we want to clear the equation.
    label_result.config(text = eqn) # displaying the equation which is now empty.
def disp(val):  # taking the val as an argument , it is the current eneterd value.
    global eqn
    eqn = eqn + val # addin the value to the equation to feed it to the eval function.
    label_result.config(text = eqn) # displaying the updated equation.

def delete():
    global eqn
    eqn = eqn[:-1] # deleting last character from the string(splicing operation.) 
    label_result.config(text = eqn ) # displaying the updated equation.

def calculate():
    global eqn # accessing the global variable eqn.
    result = ''  # setting the result to empty.
    if eqn  != '':  # checking if the equation is not empty.
        try : 
            result = eval(eqn) # eval is built in function to evaluate the equation.
        except: 
            result = 'error' # if the equation is not valid  , we print error.
            eqn = ''        # hence we set the eqn to empty.
    label_result.config(text = result) # displaying the reuslt.

button_config = {'width': 5, 'height': 2, 'font': ('arial', 20), 'bg': '#333', 'fg': 'white', 'activebackground': '#555', 'activeforeground': 'white'}
# the above line is a dictionary which contains all the configurations for the buttons.


buttons = [
    ('C', 1, 0, clear),
    ('/', 1, 1, lambda: disp('/')),
    ('*', 1, 2, lambda: disp('*')),
    ('-', 1, 3, lambda: disp('-')),
    ('7', 2, 0, lambda: disp('7')),
    ('8', 2, 1, lambda: disp('8')), 
    ('9', 2, 2, lambda: disp('9')), 
    ('+', 2, 3, lambda: disp('+')),
    ('4', 3, 0, lambda: disp('4')),
    ('5', 3, 1, lambda: disp('5')), 
    ('6', 3, 2, lambda: disp('6')), 
    ('=', 3, 3, calculate),           # call the function calculate when equal button is pressed.
    ('1', 4, 0, lambda: disp('1')),
    ('2', 4, 1, lambda: disp('2')), 
    ('3', 4, 2, lambda: disp('3')),
    ('0', 5, 0, lambda: disp('0')),
    ('.', 5, 1, lambda: disp('.')), 
    ('Del', 5, 2, delete)            # calls the function delete when the delete buttton is pressed.
]
# the above line is a list of tuples, that 

for (text, row, col, cmd) in buttons:
    Button(win, text=text, command=cmd, **button_config).grid(row=row, column=col, padx=5, pady=5, sticky="nsew") # sticky = nsew, makes the button stick to the north, south, east and west.
# the above for loop goes over each button tupe in the buttons list and it creates a button widget with the specified text, command and style options.


for i in range(6):
    win.grid_rowconfigure(i, weight=1)
for i in range(4):
    win.grid_columnconfigure(i, weight=1)
# the above lines are configuring the weights of the rows and columns of the grids.

win.mainloop() # running the mainloop, this is used to display the window.