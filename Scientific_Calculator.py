import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#0000FF')
root.resizable(width=False, height=False)


ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25),
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=6, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def Square_Root(self):
        try:
            self.current = str(math.sqrt(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')

    def Power_Of_Two(self):
        try:
            self.current = str(eval(ent_field.get())**2)
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Power_Of_Y(self):
        try:
            self.current = ent_field.get() + '**'
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Sin_Func(self):
        try:
            self.current = str(math.sin(math.radians(float(ent_field.get()))))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')

    def Cos_Func(self):
        try:
            self.current = str(math.cos(math.radians(float(ent_field.get()))))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')

    def Tan_Func(self):
        try:
            self.current = str(math.tan(math.radians(float(ent_field.get()))))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')



sc_app = SC_Calculator()


numberpad = "7894561230"
i = 0
button = []
for j in range(2, 6):  
    for k in range(3): 
        if i < len(numberpad):
            button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                   fg="red", width=6, height=2,
                                   highlightbackground='#ADD8E6', highlightthickness=2))
            button[i].grid(row=j, column=k, sticky='nsew', padx=10, pady=10)
            button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
            i += 1


btn_decimal = tk.Button(root, text='.', command=lambda: sc_app.Enter_Num('.'),
                        font=FONT, width=6, height=2, fg="#000000",
                        highlightbackground='#ADD8E6', highlightthickness=2)
btn_decimal.grid(row=5, column=1, sticky='nsew', padx=10, pady=10)


btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_add.grid(row=2, column=3, sticky='nsew', padx=10, pady=10)

btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sub.grid(row=3, column=3, sticky='nsew', padx=10, pady=10)

btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_mul.grid(row=4, column=3, sticky='nsew', padx=10, pady=10)

btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_div.grid(row=5, column=3, sticky='nsew', padx=10, pady=10)

btn_mod = tk.Button(root, text='%', command=lambda: sc_app.Standard_Ops('%'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_mod.grid(row=1, column=3, sticky='nsew', padx=10, pady=10)


btn_CE = tk.Button(root, text='CE', command=sc_app.Clear_Entry,
                   font=FONT, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_equal.grid(row=5, column=2, sticky='nsew', padx=10, pady=10)


btn_sqrt = tk.Button(root, text='√', command=sc_app.Square_Root,
                     font=FONT, width=6, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_sqrt.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

btn_pow2 = tk.Button(root, text='x²', command=sc_app.Power_Of_Two,
                     font=FONT, width=6, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_pow2.grid(row=2, column=4, sticky='nsew', padx=10, pady=10)

btn_powY = tk.Button(root, text='x^y', command=sc_app.Power_Of_Y,
                     font=FONT, width=6, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_powY.grid(row=3, column=4, sticky='nsew', padx=10, pady=10)

btn_sin = tk.Button(root, text='sin', command=sc_app.Sin_Func,
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sin.grid(row=4, column=4, sticky='nsew', padx=10, pady=10)

btn_cos = tk.Button(root, text='cos', command=sc_app.Cos_Func,
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_cos.grid(row=5, column=4, sticky='nsew', padx=10, pady=10)

btn_tan = tk.Button(root, text='tan', command=sc_app.Tan_Func,
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_tan.grid(row=1, column=4, sticky='nsew', padx=10, pady=10)

if __name__ == '__main__':
    root.mainloop()