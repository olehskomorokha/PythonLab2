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
    win2 = Toplevel(root)
    win2.title('Window 2')
    var = IntVar()
    var.set(0)
    a = set()
    b = set()

    def add_women(event):
        if var.get() == 0:
            a.add(set_A[event.widget.curselection()[0]])
        if var.get() == 1:
            b.add(set_A[event.widget.curselection()[0]])
        lbl_a['text'] = 'A = {}'.format(a)
        lbl_b['text'] = 'B = {}'.format(b)

    def add_men(event):
        if var.get() == 0:
            a.add(set_B[event.widget.curselection()[0]])
        if var.get() == 1:
            b.add(set_B[event.widget.curselection()[0]])
            lbl_b['text'] = 'B = {}'.format(b)
            lbl_a['text'] = 'A = {}'.format(a)

    def save():
        with open('result.txt', 'a') as f:
            f.write(str(a))
            f.write('\n')
            f.write(str(b))
            f.write('\n')
        save_btn.config(state=DISABLED)

    def del_set():
        a = set()
        b = set()
        lbl_a['text'] = 'A = {}'.format(a)
        lbl_b['text'] = 'B = {}'.format(b)
        save_btn.config(state=NORMAL)
        with open('result.txt', 'w') as f:
            f.write('')

    frm_win2 = Frame(win2, bg='red4', bd=10)
    frm_win2.pack()
    choose_set = Label(frm_win2, text='Оберіть до якої множини додавати елементи:', bg='red4',
                            font=('Garamond', 14), fg='white')
    choose_set.grid(row=0, columnspan=3)
    radiobtn_A = Radiobutton(frm_win2, text='Множина А', font=('Garamond', 12), bg='red4',
                                  activebackground='red4', variable=var, value=0)
    radiobtn_A.grid(row=1, column=0)
    radiobtn_B = Radiobutton(frm_win2, text='Множина B', font=('Garamond', 12), bg='red4',
                                  activebackground='red4', variable=var, value=1)
    radiobtn_B.grid(row=1, column=2)
    lbl_fr1 = LabelFrame(frm_win2, text='Жіночі імена', font=('Garamond', 12), bg='red4', fg='white')
    lbl_fr1.grid(row=2, column=0)
    lst1 = Listbox(lbl_fr1, font=('Garamond', 14), selectmode=EXTENDED)
    lst1.bind("<<ListboxSelect>>", add_women)
    lst1.grid(row=2, column=0)
    for i in set_A:
        lst1.insert(END, i)

    lbl_fr2 = LabelFrame(frm_win2, text='Чоловічі імена', font=('Garamond', 12), bg='red4', fg='white')
    lbl_fr2.grid(row=2, column=2)
    lst2 = Listbox(lbl_fr2, font=('Garamond', 14), selectmode=EXTENDED)
    lst2.bind("<<ListboxSelect>>", add_men)
    lst2.grid(row=2, column=2)
    for i in set_B:
        lst2.insert(END, i)

    lbl_a = Label(frm_win2, text='A =', bg='red4', font=('Garamond', 14), fg='white')
    lbl_a.grid(row=3, columnspan=3, sticky='w')
    lbl_b = Label(frm_win2, text='B =', bg='red4', font=('Garamond', 14), fg='white')
    lbl_b.grid(row=4, columnspan=3, sticky='w')

    save_btn = Button(frm_win2, text='Зберегти множини', font=('Garamond', 12), bg='snow', command=save)
    save_btn.grid(row=5, column=0)
    del_btn = Button(frm_win2, text='Очистити множини', font=('Garamond', 12), bg='snow', command=del_set)
    del_btn.grid(row=5, column=2)


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
