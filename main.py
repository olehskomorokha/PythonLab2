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
set_A = ['Катерина', 'Юлія', 'Дарина', 'Оксана', 'Ольга', 'Марія', 'Софія', 'Діана', 'Аліна']
set_B = ['Віталій', 'Сергій', 'Олег', 'Петро', 'Василь', 'Федір', 'Богдан', 'Владислав', 'Віктор']


# вікно 2
def window2():
    global a, b

    root = Tk()
    root.title('Window 2')
    var = IntVar()
    var.set(0)
    a = set()
    b = set()

    def add_women(event):
        if var.get() == 1:
            b.add(set_B[event.widget.curselection()[0]])
        if var.get() == 0:
            a.add(set_A[event.widget.curselection()[0]])

        lbl_a['text'] = f'A = {a}'
        lbl_b['text'] = f'B = {b}'

    def add_men(event):
        if var.get() == 1:
            a.add(set_A[event.widget.curselection()[0]])
        if var.get() == 0:
            b.add(set_B[event.widget.curselection()[0]])
        lbl_b['text'] = f'B = {b}'
        lbl_a['text'] = f'A = {a}'

    def save():
        with open('result.txt', 'w', encoding="utf-8") as f:
            f.write(str(a))
            f.write('\n')
            f.write(str(b))
            f.write('\n')
        save_btn.config(state=DISABLED)

    def del_set():
        a = set()
        b = set()
        lbl_a['text'] = f'A = {a}'
        lbl_b['text'] = f'B = {b}'
        save_btn.config(state=NORMAL)
        with open('result.txt', 'w') as f:
            f.write('')

    radiobtn_A = Radiobutton(root, text='Множина А', font='arial14'
                             , variable=var, value=0)
    radiobtn_A.grid(row=1, column=0)
    radiobtn_B = Radiobutton(root, text='Множина B', font='arial14', variable=var, value=1)
    radiobtn_B.grid(row=1, column=2)

    lst1 = Listbox(root, font=('Garamond', 14), selectmode=EXTENDED)
    lst1.bind("<<ListboxSelect>>", add_women)
    lst1.grid(row=2, column=0)
    for i in set_A:
        lst1.insert(END, i)

    lst2 = Listbox(root, font=('Garamond', 14), selectmode=EXTENDED)
    lst2.bind("<<ListboxSelect>>", add_men)
    lst2.grid(row=2, column=2)
    for i in set_B:
        lst2.insert(END, i)

    lbl_a = Label(root, text='A =', font='arial14')
    lbl_a.grid(row=3, columnspan=3, sticky='w')
    lbl_b = Label(root, text='B =', font='arial14')
    lbl_b.grid(row=4, columnspan=3, sticky='w')

    save_btn = Button(root, text='Зберегти множини', font=('Garamond', 12), bg='snow', command=save)
    save_btn.grid(row=5, column=0)
    del_btn = Button(root, text='Очистити множини', font=('Garamond', 12), bg='snow', command=del_set)
    del_btn.grid(row=5, column=2)


def window3():
    root = Tk()
    root.geometry("800x800")
    root.title("win3")

    # Creat and Pull sets A and B
    Label(root, text='Множина А').grid(row=0, column=0)

    setA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setA.grid(row=1, column=0)
    for i in a:
        setA.insert(END, i)

    Label(root, text='Множина B').grid(row=0, column=1)

    setB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setB.grid(row=1, column=1)
    for i in b:
        setB.insert(END, i)

    # mainFunction
    def a_onychka_b():
        A = set()
        for i in a:
            if i in set_A:
                A.add(i)
        B = b
        S = []
        for i in range(min(len(A), len(B))):
            p = random.choice(list(A))
            q = random.choice(list(B))
            if p != q:
                S.append([p, q])
        return S

    def a_khrechshena_b():
        A = set()
        for i in a:
            if i in set_A:
                A.add(i)
        B = b
        R = []
        for i in range(min(len(A), len(B))):
            p = random.choice(list(A))
            q = random.choice(list(B))
            if p != q:
                if [p, q] not in S:
                    R.append([p, q])
        return R

    S = a_onychka_b()
    R = a_khrechshena_b()

    aSb = Canvas(root, width=600, height=200, bg='navy')
    dict_SA = {}
    dict_SB = {}

    aSb = Canvas(root, width=600, height=200, bg='navy')
    dict_SA = {}
    dict_SB = {}

    for i in range(len(a)):
        aSb.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
        aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
        dict_SA.update({list(a)[i]: [30 + i * 50, 80]})
    for j in range(len(b)):
        aSb.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
        aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
        dict_SB.update({list(b)[j]: [30 + j * 50, 160]})
    for k in S:
        aSb.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow=LAST)
    aSb.grid(row=2, column=0, columnspan=3, rowspan=2)

    aRb = Canvas(root, width=600, height=200, bg='navy')
    dict_RA = {}
    dict_RB = {}
    for i in range(len(a)):
        aRb.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
        aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
        dict_RA.update({list(a)[i]: [30 + i * 50, 80]})
    for j in range(len(b)):
        aRb.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
        aRb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
        dict_RB.update({list(b)[j]: [30 + j * 50, 160]})

    for k in R:
        aRb.create_line(dict_RA[k[0]], dict_RB[k[1]], arrow=LAST)
    aRb.grid(row=5, column=0, columnspan=3, rowspan=2)


# Створення вікон 2 3 4
d = Menu(root)
root.config(menu=d)
d.add_cascade(label="Вікно 2", command=window2)
d.add_cascade(label="Вікно 3", command=window3)
d.add_cascade(label="Вікно 4")
root.configure(bg='#6E6E6E')
root.mainloop()
