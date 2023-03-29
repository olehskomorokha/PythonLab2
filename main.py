from tkinter import *
import random

# MAINMENU
root = Tk()
root.geometry("400x400")
root.title("MainWindow")


# Мій варіант
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


# вікно 2
def window2():
    root = Tk()
    root.geometry("600x600")
    root.title("win2")
    var = IntVar()
    var.set(1)
    # Creat and Pull LIST
    boxA = Listbox(root, height=10, width=10, selectmode=MULTIPLE)
    boxA.grid(row=1, column=0)
    for i in ListA:
        boxA.insert(END, i)

    boxB = Listbox(root, height=10, width=10, selectmode=MULTIPLE)
    boxB.grid(row=1, column=1)
    for i in ListB:
        boxB.insert(END, i)


    # Creat label and setA,B

    def elA():
        boxA['state'] = NORMAL
        boxB['state'] = DISABLED

    def elB():
        boxA['state'] = DISABLED
        boxB['state'] = NORMAL

    def save():
        with open('resA.txt', 'a') as f:
            f.write(str())
            f.write('\n')
            f.write(str())
            f.write('\n')
        Label(root, text='результати збережено в файл').grid(sticky=W, row=6, column=0)


    #Save the result into file
    saveA = Button(root, text='Записати результати в файл', command=save)
    saveA.grid(sticky=W, row=5, column=0)


    # radiobutton
    rad1 = Radiobutton(root, text="Множина А", variable=var, value=0, command=elA)
    rad1.grid(row=0, column=0)
    rad2 = Radiobutton(root, text="Множина В", variable=var, value=1, command=elB)
    rad2.grid(row=0, column=1)
    root.configure(bg='#6E6E6E')
    root.mainloop()




def window3():
    root = Tk()
    root.geometry("800x800")
    root.title("win3")

    # Creat and Pull sets A and B
    Label(root, text='Множина А').grid(row=0, column=0)

    setA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setA.grid(row=1, column=0)
    for i in adA:
        setA.insert(END, i)

    Label(root, text='Множина B').grid(row=0, column=1)

    setB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setB.grid(row=1, column=1)
    for i in adB:
        setB.insert(END, i)

# Створення вікон 2 3 4
d = Menu(root)
root.config(menu=d)
d.add_cascade(label="Вікно 2", command=window2)
d.add_cascade(label="Вікно 3", command=window3)
d.add_cascade(label="Вікно 4")
root.configure(bg='#6E6E6E')
root.mainloop()
