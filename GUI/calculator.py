from tkinter import*
import tkinter

win = Tk()

win.title("Hello")
# win.geometry('600x450+50+50')

# Window_width = 600
# window_height = 400

# # get the screen dimension
# screen_width = win.winfo_screenwidth()
# screen_height = win.winfo_screenheight()

# # find the center point

# center_x = int(screen_width / 2 - Window_width/2)
# center_y = int(screen_height / 2 - window_height/2)

# win.geometry(f'{Window_width}x{window_height}+{center_x}+{center_y}')

# mylabel = Label(win, text="hello world")
# mylabel.pack()
e = Entry(win, width = 45 , borderwidth = 5)
e.grid(row=0 , column = 0 , columnspan = 3 , padx = 10 , pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_addition():
    first_num = e.get()
    global f_num 
    f_num = int(first_num)
    global math 
    math = "addition"
    e.delete(0,END)

def button_subtraction():

    global f_num
    f_num = int(e.get())
    global math
    math = "subtaraction"

    e.delete(0,END)

def button_multiplication():
    global  f_num

    f_num = int(e.get())
    global math
    math ="multiplication"
    e.delete(0,END)

def button_division():
    global f_num 
    f_num = int(e.get())
    global math
    math = "division"

    e.delete(0,END)

def button_equality():
    second_num = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_num + int(second_num))

    if math == "subtraction":
        e.insert(0,f_num - int(second_num))
    
    if math == "multiplication":
        e.insert(0,f_num * int(second_num))

    if math == "division":
        e.insert(0,f_num / int(second_num))
       




button_1 = Button(win, text = "1",padx =40 , pady = 20 , command = lambda:button_click(1))
button_2 = Button(win, text = "2",padx =40 , pady = 20 , command = lambda:button_click(2))
button_3 = Button(win, text = "3",padx =40 , pady = 20 , command = lambda:button_click(3))
button_4 = Button(win, text = "4",padx =40 , pady = 20 , command = lambda:button_click(4))
button_5 = Button(win, text = "5",padx =40 , pady = 20 , command = lambda:button_click(5))
button_6 = Button(win, text = "6",padx =40 , pady = 20 , command = lambda:button_click(6))
button_7 = Button(win, text = "7",padx =40 , pady = 20 , command = lambda:button_click(7))
button_8 = Button(win, text = "8",padx =40 , pady = 20 , command = lambda:button_click(8))
button_9 = Button(win, text = "9",padx =40 , pady = 20 , command = lambda:button_click(9))
button_0 = Button(win, text = "0",padx =40 , pady = 20 , command = lambda:button_click(0))
button_Add = Button(win, text ="+" , padx = 40 , pady = 20, command = button_addition)
button_sub = Button(win, text ="-" , padx = 40 , pady = 20, command = button_subtraction)
button_mul = Button(win, text ="*" , padx = 40 , pady = 20, command = button_multiplication)
button_div = Button(win, text ="/" , padx = 40 , pady = 20, command = button_division)
button_clear = Button(win, text ="Clear" , padx = 40 , pady = 20, command = button_clear)
button_equal = Button(win, text ="=" , padx = 40 , pady = 20, command = button_equality)






button_1.grid(row = 3, column =0 )
button_2.grid(row =3 , column = 1)
button_3.grid(row =3, column = 2)
button_Add.grid(row = 3, column = 3)

button_4.grid(row =2 , column =0)
button_5.grid(row =2, column =1 )
button_6.grid(row =2, column =2)
button_sub.grid(row = 2 , column = 3)


button_7.grid(row =1 , column =0 )
button_8.grid(row =1 , column =1)
button_9.grid(row =1 , column =2)
button_mul.grid(row = 1 , column = 3)

button_0.grid(row =4 , column =0 )
button_div.grid(row = 4 , column = 3)
button_equal.grid(row = 4, column = 1)
button_clear.grid(row = 4 , column = 2)



win.mainloop()

