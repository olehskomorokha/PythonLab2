from tkinter import *
#MAINMENU
root = Tk()
root.geometry("800x900")
root.title("MainWindow")
#Мій варіант
def AboutMe():
    root = Tk()
    root.title('Варіант')
    root.geometry("300x300")
    G = 25
    N = 27
    Variant = (N + G % 60) % 30 + 1
    label = Label(root, text=f'Скомороха Олег Ігорович\n'
                             f'Група ІО - {G}\n'
                             f'Номер в списку - {N}\n'
                             f'Варіант - {Variant}\n', font="arial 14")
    label.grid()
    mainloop()

InfoB = Button(root, text='Виконав', command=AboutMe)
InfoB.grid()

#Створення вікон 2 3 4
d = Menu(root)
root.config(menu=d)
d.add_cascade(label="Вікно 2")
d.add_cascade(label="Вікно 3")
d.add_cascade(label="Вікно 4")
root.mainloop()