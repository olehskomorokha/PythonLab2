from tkinter import *

# MAINMENU
root = Tk()
root.geometry("800x900")
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
    global A, B
    root = Tk()
    root.geometry("400x300")
    root.title("win2")
    var = IntVar()
    var.set(1)
    # Creat and Pull LIST
    boxA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    boxA.grid(row=1, column=0)
    for i in ListA:
        boxA.insert(END, i)

    boxB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    boxB.grid(row=1, column=1)
    for i in ListB:
        boxB.insert(END, i)
    A = set()
    B = set()

    # Creat label and setA,B
    def A_A():
        A = boxA.get(boxA.curselection())
        Label(root, text=f'A = {A}').grid(row=3, column=0)

    def B_B():
        B = boxB.get(boxB.curselection())
        Label(root, text=f'B = {B}').grid(row=3, column=1)

    butA = Button(root, text='запистаи A в множину', command=A_A)
    butA.grid(row=2, column=0, sticky=W)
    butB = Button(root, text='запистаи B в множину', command=B_B)
    butB.grid(row=2, column=1, sticky=W)

    def elA():
        boxA['state'] = NORMAL
        boxB['state'] = DISABLED

    def elB():
        boxA['state'] = DISABLED
        boxB['state'] = NORMAL

    def saveA():
        fA = open('resA.txt', 'w')
        fA.write(str(A))
        fA.close()
        Label(root, text='результат A збережено в файл').grid(sticky=W, row=6, column=0)

    def saveB():
        fB = open('resB.txt', 'w')
        fB.write(str(B))
        fB.close()
        Label(root, text='результат B збережено в файл').grid(sticky=W, row=6, column=1)

    saveA = Button(root, text='Записати результат A в файл', command=saveA)
    saveA.grid(sticky=W, row=5, column=0)
    saveB = Button(root, text='Записати результат B в файл', command=saveB)
    saveB.grid(sticky=W, row=5, column=1)
    # radiobutton

    rad1 = Radiobutton(root, text="Множина А", variable=var, value=0, command=elA)
    rad1.grid(row=0, column=0)
    rad2 = Radiobutton(root, text="Множина В", variable=var, value=1, command=elB)
    rad2.grid(row=0, column=1)
    root.configure(bg='#6E6E6E')
    root.mainloop()

    # вікно 3


def window3():
    root = Tk()
    root.geometry("400x300")
    root.title("win3")
    A = {'Катерина', 'Дарина', 'Оксана', 'Марія', 'Софія', 'Аліна'}
    B = {'Віталій', 'Олег', 'Василь', 'Богдан', 'Владислав', 'Віктор'}
    # Creat and Pull sets A and B
    setA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setA.grid(row=0, column=0)
    for i in A:
        setA.insert(END, i)

    setB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setB.grid(row=0, column=1)
    for i in B:
        boxB.insert(END, i)
    root.configure(bg='#6E6E6E')
    root.mainloop()


# Створення вікон 2 3 4
d = Menu(root)
root.config(menu=d)
d.add_cascade(label="Вікно 2", command=window2)
d.add_cascade(label="Вікно 3", command=window3)
d.add_cascade(label="Вікно 4")
root.configure(bg='#6E6E6E')
root.mainloop()
