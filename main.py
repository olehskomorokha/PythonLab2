from tkinter import *
import random
import copy

# MAINMENU
root = Tk()
root.geometry("400x400")
root.title("MainWindow")


# Мій варіант
def AboutMe():
    root = Tk()
    root.title('Варіант')
    root.configure(bg='#4B4B55')
    root.geometry("300x300")
    G = 25
    N = 27
    Variant = (N + G % 60) % 30 + 1
    label = Label(root, text=f'Скомороха Олег Ігорович\n'
                             f'Група ІО - {G}\n'
                             f'Номер в списку - {N}\n'
                             f'Варіант - {Variant}\n', font="arial 14", fg='white', bg='#4B4B55')
    label.grid()
    mainloop()


InfoB = Button(root, text='Виконав', command=AboutMe)
InfoB.grid()

# Задаємо елементи множин
set_A = ['Анна', 'Марія', 'Юлія', 'Катерина', 'Софія', 'Ольга', 'Емма', 'Ава', 'Єва', 'Лена']
set_B = ['Іван', 'Петро', 'Олександр', 'Василь', 'Андрій', 'Михайло', 'Віктор', 'Дмитро', 'Олег', 'Сергій']


# вікно 2
def window2():
    global a, b

    root = Tk()
    root.title('Window 2')
    root.configure(bg='#4B4B55')
    var = IntVar()
    var.set(0)
    a = set()
    b = set()

    def women(event):
        if var.get() == 1:
            b.add(set_B[event.widget.curselection()[0]])
        if var.get() == 0:
            a.add(set_A[event.widget.curselection()[0]])

        lbl_a['text'] = f'A = {a}'
        lbl_b['text'] = f'B = {b}'

    def men(event):
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
                             , variable=var, value=0, bg='#4B4B55', fg='white')
    radiobtn_A.grid(row=1, column=0)
    radiobtn_B = Radiobutton(root, text='Множина B', font='arial14', variable=var, value=1, bg='#4B4B55', fg='white')
    radiobtn_B.grid(row=1, column=2)

    lst1 = Listbox(root, font=('Garamond', 14), selectmode=EXTENDED)
    lst1.bind("<<ListboxSelect>>", women)
    lst1.grid(row=2, column=0)
    for i in set_A:
        lst1.insert(END, i)

    lst2 = Listbox(root, font=('Garamond', 14), selectmode=EXTENDED)
    lst2.bind("<<ListboxSelect>>", men)
    lst2.grid(row=2, column=2)
    for i in set_B:
        lst2.insert(END, i)

    lbl_a = Label(root, text='A =', font='arial14', bg='#4B4B55', fg='white')
    lbl_a.grid(row=3, columnspan=3, sticky='w')
    lbl_b = Label(root, text='B =', font='arial14', bg='#4B4B55', fg='white')
    lbl_b.grid(row=4, columnspan=3, sticky='w')

    save_btn = Button(root, text='Зберегти множини', font='arial14', bg='black', fg='white', command=save)
    save_btn.grid(row=5, column=0)
    del_btn = Button(root, text='Очистити множини', font='arial14', bg='black', fg='white', command=del_set)
    del_btn.grid(row=5, column=2)


def window3():
    global S, R
    root = Tk()
    root.geometry("450x650")
    root.title("window3")
    root.configure(bg='#4B4B55')
    # Creat and Pull sets A and B
    Label(root, text='Множина А', bg='#4B4B55', fg='white').grid(row=0, column=0, sticky=W)

    setA = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setA.grid(row=1, column=0, sticky=W)
    for i in a:
        setA.insert(END, i)

    Label(root, text='Множина B', bg='#4B4B55', fg='white').grid(row=0, column=1, sticky=W)

    setB = Listbox(root, height=10, width=10, selectmode=EXTENDED)
    setB.grid(row=1, column=1, sticky=W)
    for i in b:
        setB.insert(END, i)

    # mainFunction

    def a_MAMA_b():
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

    def a_TESHA_b():
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

    S = a_MAMA_b()
    R = a_TESHA_b()

    aSb = Canvas(root, width=300, height=200, bg='#4B4B55')
    dict_SA = {}
    dict_SB = {}

    Label(root, text='aSb, якщо a мати b:', font='arial16', bg='#4B4B55', fg='white').grid(row=2, column=0, sticky=W)
    for i in range(len(a)):
        aSb.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
        aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
        dict_SA.update({list(a)[i]: [30 + i * 50, 80]})
    for j in range(len(b)):
        aSb.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
        aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
        dict_SB.update({list(b)[j]: [30 + j * 50, 160]})
    for k in S:
        aSb.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow=LAST)
    aSb.grid(row=3, column=0, columnspan=3, rowspan=2)

    aRb = Canvas(root, width=300, height=200, bg='#4B4B55')
    RA = {}
    RB = {}
    Label(root, text='aRb, якщо a теща b:', font='arial16', bg='#4B4B55', fg='white').grid(row=5, column=0, sticky=W)
    for i in range(len(a)):
        aRb.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
        aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
        RA.update({list(a)[i]: [30 + i * 50, 80]})
    for j in range(len(b)):
        aRb.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
        aRb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
        RB.update({list(b)[j]: [30 + j * 50, 160]})

    for k in R:
        aRb.create_line(RA[k[0]], RB[k[1]], arrow=LAST)
    aRb.grid(row=6, column=0, columnspan=3, rowspan=2)


def window4():
    root = Tk()
    root.geometry("700x300")
    root.title('Window 4')
    root.configure(bg='#4B4B55')
    win4 = Frame(root, bd=10)
    win4.configure(bg='#4B4B55')
    win4.pack()
    lableTEXT = Label(win4, text='Операції на відношеннях S та R', font='arial14', fg='white', bg='#4B4B55')
    lableTEXT.grid(row=0, columnspan=4)

    def button1():
        canv.delete("all")
        canv.create_text(150, 20, text='R \u222A S', font='Garamond 16')
        b1 = {}
        b2 = {}
        V = R + S
        for i in range(len(a)):
            canv.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
            canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            b1.update({list(a)[i]: [30 + i * 50, 80]})
        for j in range(len(b)):
            canv.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
            canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
            b2.update({list(b)[j]: [30 + j * 50, 160]})
        for k in V:
            canv.create_line(b1[k[0]], b2[k[1]], arrow=LAST)

    def button2():
        canv.delete("all")
        canv.create_text(150, 20, text='R \u2229 S', font='Garamond 16')
        b1 = {}
        b2 = {}
        V = []
        for i in R:
            if i in S:
                V.append(i)

        for i in range(len(a)):
            canv.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
            canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            b1.update({list(a)[i]: [30 + i * 50, 80]})
        for j in range(len(b)):
            canv.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
            canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
            b2.update({list(b)[j]: [30 + j * 50, 160]})

        for k in V:
            if len(V) != 0:
                canv.create_line(b1[k[0]], b2[k[1]], arrow=LAST)

    def button3():
        canv.delete("all")
        canv.create_text(150, 20, text='R \ S', font='Garamond 16')
        b1 = {}
        b2 = {}
        V = copy.deepcopy(R)
        for i in V:
            if i in S:
                V.remove(i)

        for i in range(len(a)):
            canv.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
            canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            b1.update({list(a)[i]: [30 + i * 50, 80]})
        for j in range(len(b)):
            canv.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
            canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
            b2.update({list(b)[j]: [30 + j * 50, 160]})
        for k in V:
            canv.create_line(b1[k[0]], b2[k[1]], arrow=LAST)

    def button4():
        canv.delete("all")
        canv.create_text(150, 20, text='U \ R', font='Garamond 16')
        b1 = {}
        b2 = {}

        V = []
        # a = set()
        for i in a:
            if i in set_B:
                a.add(i)
        for i in a:
            for j in b:
                V.append([i, j])

        for i in V:
            if i in R:
                V.remove(i)

        for i in range(len(a)):
            canv.create_text(30 + i * 50, 50, text=list(a)[i], font='Arial 10')
            canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            b1.update({list(a)[i]: [30 + i * 50, 80]})
        for j in range(len(b)):
            canv.create_text(30 + j * 50, 190, text=list(b)[j], font='Arial 10')
            canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
            b2.update({list(b)[j]: [30 + j * 50, 160]})
        for k in V:
            if len(V) != 0:
                canv.create_line(b1[k[0]], b2[k[1]], arrow=LAST)

    def button5():
        canv.delete("all")
        canv.create_text(150, 20, text='S⁻¹', font='Garamond 16')
        b1 = {}
        b2 = {}
        V = copy.deepcopy(S)
        for i in V:
            i[0], i[1] = i[1], i[0]
        for i in range(len(a)):
            canv.create_text(30 + i * 50, 50, text=list(a)[i], font='Garamond 10')
            canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            b1.update({list(a)[i]: [30 + i * 50, 80]})
        for j in range(len(b)):
            canv.create_text(30 + j * 50, 190, text=list(b)[j], font='Garamond 10')
            canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="red")
            b2.update({list(b)[j]: [30 + j * 50, 160]})
        for k in V:
            canv.create_line(b2[k[0]], b1[k[1]], arrow=LAST)

    unB = Button(win4, text='R ∪ S', bg='black', fg='white', width=9, command=button1)
    unB.grid(row=1, column=0, sticky='w')
    peretinB = Button(win4, text='R ∩ S', bg='black', fg='white', width=9, command=button2)
    peretinB.grid(row=2, column=0, sticky='w')
    difB = Button(win4, text='R \ S', bg='black', fg='white', width=9, command=button3)
    difB.grid(row=3, column=0, sticky='w')
    notB = Button(win4, text='U \ R', bg='black', fg='white', width=9, command=button4)
    notB.grid(row=4, column=0, sticky='w')
    minusB = Button(win4, text='S⁻¹', bg='black', fg='white', width=9, command=button5)
    minusB.grid(row=5, column=0, sticky='w')
    canv = Canvas(win4, width=600, height=250, bg='#4B4B55')
    canv.grid(row=1, rowspan=9, column=3)

    root.mainloop()


# Створення вікон 2 3 4
d = Menu(root)
root.config(menu=d)
d.add_cascade(label="Вікно 2", command=window2)
d.add_cascade(label="Вікно 3", command=window3)
d.add_cascade(label="Вікно 4", command=window4)
root.configure(bg='#4B4B55')
root.mainloop()