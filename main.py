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
# Задаємо елементи множин
ListA = ['Катерина', 'Юлія', 'Дарина', 'Оксана', 'Ольга', 'Марія', 'Софія', 'Діана', 'Аліна']
ListB = ['Віталій', 'Сергій', 'Олег', 'Петро', 'Василь', 'Федір', 'Богдан', 'Владислав', 'Віктор']
#вікно 2
def window2():
    root = Tk()
    root.geometry("400x300")
    root.title("win2")
    # Створення боксів
    boxA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    boxA.grid(row=1, column=0)
    for i in ListA:
        boxA.insert(END, i)


    boxB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    boxB.grid(row=1, column=1)
    for i in ListB:
        boxB.insert(END, i)

    def elA():
        boxA['state'] = NORMAL
        boxB['state'] = DISABLED
    def elB():
        boxA['state'] = DISABLED
        boxB['state'] = NORMAL


    var = IntVar()
    var.set(1)
    rad1 = Radiobutton(root, text="Множина А", variable=var, value=0, command= elA) # створюємо перемикач зі значенням 1
    rad1.grid(row=0, column=0)
    rad2 = Radiobutton(root, text="Множина В", variable=var, value=1, command=elB)    # створюємо перемикач зі значенням 2
    rad2.grid(row=0, column=1)


    root.mainloop()
# Створення вікон 2 3 4
d = Menu(root)
root.config(menu=d)
d.add_cascade(label="Вікно 2", command=window2)
d.add_cascade(label="Вікно 3")
d.add_cascade(label="Вікно 4")
root.mainloop()