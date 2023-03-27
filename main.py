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
    root.geometry("800x800")
    root.title("win3")
    A = {'Катерина', 'Дарина', 'Оксана', 'Марія', 'Софія', 'Аліна'}
    B = {'Віталій', 'Олег', 'Василь', 'Богдан', 'Владислав', 'Віктор'}
    # Creat and Pull sets A and B
    Label(root, text='Множина А').grid(row=0, column=0)
    setA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setA.grid(row=1, column=0)
    for i in A:
        setA.insert(END, i)

    Label(root, text='Множина B').grid(row=0, column=1)
    setB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setB.grid(row=1, column=1)
    for i in B:
        setB.insert(END, i)

    frm_win3 = Frame(root, bg='navy')
    frm_win3.grid()
    lbl_fr3 = LabelFrame(frm_win3, bg='navy', text='A', font=('Garamond', 14), fg='white')
    lbl_fr3.grid(row=0, column=0)
    lbl_fr4 = LabelFrame(frm_win3, bg='navy', text='B', font=('Garamond', 14), fg='white')
    lbl_fr4.grid(row=0, column=1)


    lbl_aSb = Label(frm_win3, text='Множина aSb', font=('Garamond', 14), bg='navy',
                    fg='white')
    lbl_aSb.grid(row=1, columnspan=3)
    lbl_aRb = Label(frm_win3, text='Множина aRb', font=('Garamond', 14),
                         bg='navy', fg='white')
    lbl_aRb.grid(row=4, columnspan=3)

    def a_onychka_b():
        A = set()
        for i in ListA:
            if i in A:
                A.add(i)
        S = []
        for i in range(min(len(A), len(B))):
            p = random.choice(list(A))
            q = random.choice(list(B))
            if p != q:
                S.append([p, q])
        return S

    def a_khrechshena_b():
        A = set()
        for i in ListA:
            if i in A:
                A.add(i)
        b = B
        R = []
        for i in range(min(len(A), len(b))):
            p = random.choice(list(b))
            q = random.choice(list(b))
            if p != q:
                if [p, q] not in S:
                    R.append([p, q])
        return R
    S = a_onychka_b()
    R = a_khrechshena_b()

    aSb = Canvas(frm_win3, width=600, height=200, bg='navy')
    dict_SA = {}
    dict_SB = {}

    for i in range(len(A)):
        aSb.create_text(30 + i * 50, 50, text=list(A)[i], font='Garamond 10')
        aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
        dict_SA.update({list(A)[i]: [30 + i * 50, 80]})
    for j in range(len(B)):
        aSb.create_text(30 + j * 50, 190, text=list(B)[j], font='Garamond 10')
        aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
        dict_SB.update({list(B)[j]: [30 + j * 50, 160]})
    for k in S:
        aSb.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow=LAST)
    aSb.grid(row=2, column=0, columnspan=3, rowspan=2)

    aRb = Canvas(frm_win3, width=600, height=200, bg='navy')
    dict_RA = {}
    dict_RB = {}
    aRb = Canvas(frm_win3, width=600, height=200, bg='navy')
    dict_RA = {}
    dict_RB = {}
    for i in range(len(A)):
        aRb.create_text(30 + i * 50, 50, text=list(A)[i], font='Garamond 10')
        aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
        dict_RA.update({list(A)[i]: [30 + i * 50, 80]})
    for j in range(len(B)):
        aRb.create_text(30 + j * 50, 190, text=list(B)[j], font='Garamond 10')
        aRb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
        dict_RB.update({list(B)[j]: [30 + j * 50, 160]})
    for k in R:
        aRb.create_line(dict_RA[k[0]], dict_RB[k[1]], arrow=LAST)
        aRb.grid(row=6, column=0, columnspan=3, rowspan=2)

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
