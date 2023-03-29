from tkinter import *
import random, copy


class Main:
    def __init__(self, main):
        self.main = main
        main.title('Window 1')
        main.geometry('250x154')
        self.set_A = ['Катерина', 'Юлія', 'Дарина', 'Оксана', 'Ольга', 'Марія', 'Софія', 'Діана', 'Аліна']
        self.set_B = ['Віталій', 'Сергій', 'Олег', 'Петро', 'Василь', 'Федір', 'Богдан', 'Владислав', 'Віктор']

        self.frame_main = Frame(main, bg='DeepPink4', bd=10)
        self.frame_main.pack()
        self.name = Label(self.frame_main, text="Підчасюк Ганна\nГрупа ІВ-71\nНомер у списку - 12\nНомер варіанту - 24",
                          bg='DeepPink4', font=('Garamond', 16), fg='white')
        self.name.grid(row=0, columnspan=3)

        self.btn_win2 = Button(self.frame_main, text='Window 2', bg='HotPink4', font=('Garamond', 12), fg='white',
                               command=self.window2)
        self.btn_win2.grid(row=1, column=0)
        self.btn_win3 = Button(self.frame_main, text='Window 3', bg='HotPink4', font=('Garamond', 12), fg='white',
                               command=self.window3)
        self.btn_win3.grid(row=1, column=1)
        self.btn_win4 = Button(self.frame_main, text='Window 4', bg='HotPink4', font=('Garamond', 12), fg='white',
                               command=self.window4)
        self.btn_win4.grid(row=1, column=2)

    def window2(self):
        self.win2 = Toplevel(self.main)
        self.win2.title('Window 2')
        self.var = IntVar()
        self.var.set(0)
        self.a = set()
        self.b = set()

        def add_women(event):
            if self.var.get() == 0:
                self.a.add(self.set_A[event.widget.curselection()[0]])
            if self.var.get() == 1:
                self.b.add(self.set_A[event.widget.curselection()[0]])
            self.lbl_a['text'] = 'A = {}'.format(self.a)
            self.lbl_b['text'] = 'B = {}'.format(self.b)

        def add_men(event):
            if self.var.get() == 0:
                self.a.add(self.set_B[event.widget.curselection()[0]])
            if self.var.get() == 1:
                self.b.add(self.set_B[event.widget.curselection()[0]])
                self.lbl_b['text'] = 'B = {}'.format(self.b)
                self.lbl_a['text'] = 'A = {}'.format(self.a)

        def save():
            with open('result.txt', 'a') as f:
                f.write(str(self.a))
                f.write('\n')
                f.write(str(self.b))
                f.write('\n')
            self.save_btn.config(state=DISABLED)

        def del_set():
            self.a = set()
            self.b = set()
            self.lbl_a['text'] = 'A = {}'.format(self.a)
            self.lbl_b['text'] = 'B = {}'.format(self.b)
            self.save_btn.config(state=NORMAL)
            with open('result.txt', 'w') as f:
                f.write('')

        self.frm_win2 = Frame(self.win2, bg='red4', bd=10)
        self.frm_win2.pack()
        self.choose_set = Label(self.frm_win2, text='Оберіть до якої множини додавати елементи:', bg='red4',
                                font=('Garamond', 14), fg='white')
        self.choose_set.grid(row=0, columnspan=3)
        self.radiobtn_A = Radiobutton(self.frm_win2, text='Множина А', font=('Garamond', 12), bg='red4',
                                      activebackground='red4', variable=self.var, value=0)
        self.radiobtn_A.grid(row=1, column=0)
        self.radiobtn_B = Radiobutton(self.frm_win2, text='Множина B', font=('Garamond', 12), bg='red4',
                                      activebackground='red4', variable=self.var, value=1)
        self.radiobtn_B.grid(row=1, column=2)
        self.lbl_fr1 = LabelFrame(self.frm_win2, text='Жіночі імена', font=('Garamond', 12), bg='red4', fg='white')
        self.lbl_fr1.grid(row=2, column=0)
        self.lst1 = Listbox(self.lbl_fr1, font=('Garamond', 14), selectmode=EXTENDED)
        self.lst1.bind("<<ListboxSelect>>", add_women)
        self.lst1.grid(row=2, column=0)
        for i in self.set_A:
            self.lst1.insert(END, i)

        self.lbl_fr2 = LabelFrame(self.frm_win2, text='Чоловічі імена', font=('Garamond', 12), bg='red4', fg='white')
        self.lbl_fr2.grid(row=2, column=2)
        self.lst2 = Listbox(self.lbl_fr2, font=('Garamond', 14), selectmode=EXTENDED)
        self.lst2.bind("<<ListboxSelect>>", add_men)
        self.lst2.grid(row=2, column=2)
        for i in self.set_B:
            self.lst2.insert(END, i)

        self.lbl_a = Label(self.frm_win2, text='A =', bg='red4', font=('Garamond', 14), fg='white')
        self.lbl_a.grid(row=3, columnspan=3, sticky='w')
        self.lbl_b = Label(self.frm_win2, text='B =', bg='red4', font=('Garamond', 14), fg='white')
        self.lbl_b.grid(row=4, columnspan=3, sticky='w')

        self.save_btn = Button(self.frm_win2, text='Зберегти множини', font=('Garamond', 12), bg='snow', command=save)
        self.save_btn.grid(row=5, column=0)
        self.del_btn = Button(self.frm_win2, text='Очистити множини', font=('Garamond', 12), bg='snow', command=del_set)
        self.del_btn.grid(row=5, column=2)

    def window3(self):
        self.win3 = Toplevel(self.main)
        self.win3.title('Window 3')

        self.frm_win3 = Frame(self.win3, bg='navy')
        self.frm_win3.pack()
        self.lbl_fr3 = LabelFrame(self.frm_win3, bg='navy', text='A', font=('Garamond', 14), fg='white')
        self.lbl_fr3.grid(row=0, column=0)
        self.lbl_fr4 = LabelFrame(self.frm_win3, bg='navy', text='B', font=('Garamond', 14), fg='white')
        self.lbl_fr4.grid(row=0, column=1)
        self.list_a = Listbox(self.lbl_fr3, font=('Garamond', 14))
        self.list_a.grid()
        for i in self.a:
            self.list_a.insert(END, i)
        self.list_b = Listbox(self.lbl_fr4, font=('Garamond', 14))
        self.list_b.grid()
        for i in self.b:
            self.list_b.insert(END, i)
        self.lbl_aSb = Label(self.frm_win3, text='Множина aSb, якщо a внучка b:', font=('Garamond', 14), bg='navy',
                             fg='white')
        self.lbl_aSb.grid(row=1, columnspan=3)
        self.lbl_aRb = Label(self.frm_win3, text='Множина aRb, якщо a хрещена мати b:', font=('Garamond', 14),
                             bg='navy', fg='white')
        self.lbl_aRb.grid(row=4, columnspan=3)

        def a_onychka_b():
            A = set()
            for i in self.a:
                if i in self.set_A:
                    A.add(i)
            B = self.b
            S = []
            for i in range(min(len(A), len(B))):
                p = random.choice(list(A))
                q = random.choice(list(B))
                if p != q:
                    S.append([p, q])
            return S

        def a_khrechshena_b():
            A = set()
            for i in self.a:
                if i in self.set_A:
                    A.add(i)
            B = self.b
            R = []
            for i in range(min(len(A), len(B))):
                p = random.choice(list(A))
                q = random.choice(list(B))
                if p != q:
                    if [p, q] not in self.S:
                        R.append([p, q])
            return R

        self.S = a_onychka_b()
        self.R = a_khrechshena_b()

        aSb = Canvas(self.frm_win3, width=600, height=200, bg='navy')
        dict_SA = {}
        dict_SB = {}
        for i in range(len(self.a)):
            aSb.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Garamond 10')
            aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            dict_SA.update({list(self.a)[i]: [30 + i * 50, 80]})
        for j in range(len(self.b)):
            aSb.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Garamond 10')
            aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
            dict_SB.update({list(self.b)[j]: [30 + j * 50, 160]})
        for k in self.S:
            aSb.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow=LAST)
        aSb.grid(row=2, column=0, columnspan=3, rowspan=2)

        aRb = Canvas(self.frm_win3, width=600, height=200, bg='navy')
        dict_RA = {}
        dict_RB = {}
        for i in range(len(self.a)):
            aRb.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Garamond 10')
            aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            dict_RA.update({list(self.a)[i]: [30 + i * 50, 80]})
        for j in range(len(self.b)):
            aRb.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Garamond 10')
            aRb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
            dict_RB.update({list(self.b)[j]: [30 + j * 50, 160]})

        for k in self.R:
            aRb.create_line(dict_RA[k[0]], dict_RB[k[1]], arrow=LAST)
        aRb.grid(row=5, column=0, columnspan=3, rowspan=2)

    def window4(self):
        self.win4 = Toplevel(self.main)
        self.win4.title('Window 4')

        self.frm_win4 = Frame(self.win4, bg='dark slate gray', bd=10)
        self.frm_win4.pack()
        self.lbl_oper = Label(self.frm_win4, text='Операції над відношеннями', font=('Garamond', 16),
                              bg='dark slate gray',
                              fg='white')
        self.lbl_oper.grid(row=0, columnspan=4)

        def btn1():
            self.canv.delete("all")
            self.canv.create_text(150, 20, text='R \u222A S', font='Garamond 16')
            dict_b1 = {}
            dict_b2 = {}
            V = self.R + self.S
            for i in range(len(self.a)):
                self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Garamond 10')
                self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
            for j in range(len(self.b)):
                self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Garamond 10')
                self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
                dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
            for k in V:
                self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def btn2():
            self.canv.delete("all")
            self.canv.create_text(150, 20, text='R \u2229 S', font='Garamond 16')
            dict_b1 = {}
            dict_b2 = {}
            V = []
            for i in self.R:
                if i in self.S:
                    V.append(i)

            for i in range(len(self.a)):
                self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Garamond 10')
                self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
            for j in range(len(self.b)):
                self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Garamond 10')
                self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
                dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})

            for k in V:
                if len(V) != 0:
                    self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def btn3():
            self.canv.delete("all")
            self.canv.create_text(150, 20, text='R \ S', font='Garamond 16')
            dict_b1 = {}
            dict_b2 = {}
            V = copy.deepcopy(self.R)
            for i in V:
                if i in self.S:
                    V.remove(i)

            for i in range(len(self.a)):
                self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Garamond 10')
                self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
            for j in range(len(self.b)):
                self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Garamond 10')
                self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
                dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
            for k in V:
                self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def btn4():
            self.canv.delete("all")
            self.canv.create_text(150, 20, text='U \ R', font='Garamond 16')
            dict_b1 = {}
            dict_b2 = {}

            V = []
            a = set()
            for i in self.a:
                if i in self.set_B:
                    a.add(i)
            b = copy.deepcopy(self.b)
            for i in a:
                for j in b:
                    V.append([i, j])

            for i in V:
                if i in self.R:
                    V.remove(i)

            for i in range(len(self.a)):
                self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
                self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
            for j in range(len(self.b)):
                self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
                self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
                dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
            for k in V:
                if len(V) != 0:
                    self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def btn5():
            self.canv.delete("all")
            self.canv.create_text(150, 20, text='S⁻¹', font='Garamond 16')
            dict_b1 = {}
            dict_b2 = {}
            V = copy.deepcopy(self.S)
            for i in V:
                i[0], i[1] = i[1], i[0]
            for i in range(len(self.a)):
                self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Garamond 10')
                self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
            for j in range(len(self.b)):
                self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Garamond 10')
                self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow2")
                dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
            for k in V:
                self.canv.create_line(dict_b2[k[0]], dict_b1[k[1]], arrow=LAST)

        self.union_btn = Button(self.frm_win4, text='R ∪ S', bg='slate gray', fg='white', width=5, command=btn1)
        self.union_btn.grid(row=1, column=0, sticky='w')
        self.intersection_btn = Button(self.frm_win4, text='R ∩ S', bg='slate gray', fg='white', width=5, command=btn2)
        self.intersection_btn.grid(row=2, column=0, sticky='w')
        self.difference_btn = Button(self.frm_win4, text='R \ S', bg='slate gray', fg='white', width=5, command=btn3)
        self.difference_btn.grid(row=3, column=0, sticky='w')
        self.not_btn = Button(self.frm_win4, text='U \ R', bg='slate gray', fg='white', width=5, command=btn4)
        self.not_btn.grid(row=4, column=0, sticky='w')
        self.reverse_btn = Button(self.frm_win4, text='S⁻¹', bg='slate gray', fg='white', width=5, command=btn5)
        self.reverse_btn.grid(row=5, column=0, sticky='w')
        self.canv = Canvas(self.frm_win4, width=600, height=250, bg='dark slate gray')
        self.canv.grid(row=1, rowspan=6, column=3)


root = Tk()
window = Main(root)
root.mainloop()
