import tkinter
from tkinter import messagebox

root = tkinter.Tk()

#GLOBAL VARIABLES
screen_var = tkinter.StringVar()
screen_var.set('0')
operation = ""
result = 0

#General settings
root.title("Calculadora")
root.geometry('400x400')
root.resizable(False, False)

screen = tkinter.Entry(root, justify="right", width=30, textvariable=screen_var, state="readonly")

#--------------Start calculator functionality----------------------
def clear_screen():
	global operation
	global result
	screen_var.set('0')
	operation = ""
	result = 0

def do_operation(sign, number):
	global result

	if operation == "+":
		result = result + number
	elif operation == "-":
		result = result - number
	elif operation == "*":
		result = result * number
	elif operation == "/":
		try:
			result = result / number
		except:
			messagebox.showerror("Error", "No puedes dividir por cero")

	return result			

def push_number(num):

	if screen_var.get().startswith('0') and '.' not in screen_var.get():
		screen_var.set(num)	
	else:
		screen_var.set(screen_var.get() + num )

def push_comma():
	if '.' not in screen_var.get():
		screen_var.set(screen_var.get() + '.')

def push_operation(sign):
	global result
	global operation
	operation = sign

	if "." not in screen_var.get():
		result = int(screen_var.get())
	else:
		result = float(screen_var.get())	

	screen_var.set("0")	

def push_equal():
	global operation
	result = 0

	if "." in screen_var.get():
		result = do_operation(operation, float(screen_var.get()))
	else:
		result = do_operation(operation, int(screen_var.get()))	

	screen_var.set(str(result))
	
	operation=""

#--------------------End calculator functionality--------------------------					

#-------Start creating buttons------------

btn_9= tkinter.Button(root, text="9", command=lambda:push_number('9'))
btn_8= tkinter.Button(root, text="8", command=lambda:push_number('8'))
btn_7= tkinter.Button(root, text="7", command=lambda:push_number('7'))
btn_add= tkinter.Button(root, text="+", command=lambda:push_operation("+"))

btn_6= tkinter.Button(root, text="6", command=lambda:push_number('6'))
btn_5= tkinter.Button(root, text="5", command=lambda:push_number('5'))
btn_4= tkinter.Button(root, text="4", command=lambda:push_number('4'))
btn_minus= tkinter.Button(root, text="-", command=lambda:push_operation("-")) 

btn_3= tkinter.Button(root, text="3", command=lambda:push_number('3'))
btn_2= tkinter.Button(root, text="2", command=lambda:push_number('2'))
btn_1= tkinter.Button(root, text="1", command=lambda:push_number('1'))
btn_mult= tkinter.Button(root, text="*", command=lambda:push_operation("*"))

btn_0= tkinter.Button(root, text="0", command=lambda:push_number('0'))
btn_comma= tkinter.Button(root, text=".", command=push_comma)
btn_equal= tkinter.Button(root, text="=", command=push_equal )
btn_div= tkinter.Button(root, text="/", command=lambda:push_operation("/"))

btn_erase = tkinter.Button(root, text="Borrar", command=clear_screen)

#-----Finish creating buttons-----

#--------Start Placing widgets--------------

screen.grid(row=0, column=0, columnspan=4, padx=55)

btn_9.grid(row=1, column=0, pady=5, padx=5)
btn_8.grid(row=1, column=1, pady=5, padx=5)
btn_7.grid(row=1, column=2, pady=5, padx=5)
btn_add.grid(row=1, column=3, pady=5, padx=5)

btn_6.grid(row=2, column=0, pady=5, padx=5)
btn_5.grid(row=2, column=1, pady=5, padx=5)
btn_4.grid(row=2, column=2, pady=5, padx=5)
btn_minus.grid(row=2, column=3, pady=5, padx=5)

btn_3.grid(row=3, column=0, pady=5, padx=5)
btn_2.grid(row=3, column=1, pady=5, padx=5)
btn_1.grid(row=3, column=2, pady=5, padx=5)
btn_mult.grid(row=3, column=3, pady=5, padx=5)

btn_0.grid(row=4, column=0, pady=5, padx=5)
btn_comma.grid(row=4, column=1, pady=5, padx=5)
btn_equal.grid(row=4, column=2, pady=5, padx=5)
btn_div.grid(row=4, column=3, pady=5, padx=5)

btn_erase.grid(row=5, column=0, pady=5)

#-----Finish Placing buttons--------

root.mainloop()
