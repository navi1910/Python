import tkinter as tk

window = tk.Tk()

window.title('This is the title')

def button_click():
    print('Button was Clicked')

button = tk.Button(window, text = 'This is the Button',
                   command = button_click)

button.pack()

button2 = tk.Button(window, text = 'Stop', 
                    command = window.destroy,
                    width=25,
                    height=10,
                    bg = 'Yellow',
                    activeforeground = 'Red',
                    activebackground = "orange",
                    font= 'Calibri')
button2.pack()

window.mainloop()