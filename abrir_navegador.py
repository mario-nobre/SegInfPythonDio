from tkinter import *
import webbrowser

root = Tk()
root.title('Abrir Navegador')
root.geometry('300x200')


def google():
    webbrowser.open('www.google.com.br')


myGoogle = Button(root, text='Abrir Google', command=google).pack(pady=20)
root.mainloop()
