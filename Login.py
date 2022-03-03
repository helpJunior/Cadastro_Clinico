import sys
import tkinter as tk
from tkinter import messagebox
import locale
from datetime import datetime

class Toplevel1:
    def __init__(self):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        # ------------------------- TELA DE LOGIN --------------------------------------
        self.top = tk.Tk()
        self.top.geometry("505x321+351+155")
        self.top.minsize(120, 1)
        self.top.maxsize(1370, 749)
        self.top.resizable(1, 1)
        self.top.title("Toplevel 0")
        self.top.configure(bg="#54bac2")

        self.Entry_Nome_Login = tk.Entry(self.top)
        self.Entry_Nome_Login.place(relx=0.232, rely=0.355, height=30, relwidth=0.622)
        self.Entry_Nome_Login.configure(bg="white")
        self.Entry_Nome_Login.configure(font="TkFixedFont")
        self.Entry_Nome_Login.configure(fg="#000000")

        self.Entry_Senha = tk.Entry(self.top, show='*')
        self.Entry_Senha.place(relx=0.234, rely=0.511, height=30, relwidth=0.622)
        self.Entry_Senha.configure(bg="white")
        self.Entry_Senha.configure(font="TkFixedFont")
        self.Entry_Senha.configure(fg="#000000")

        self.Button1 = tk.Button(self.top, command=self.bd_login)
        self.Button1.place(relx=0.376, rely=0.685, height=34, width=147)
        self.Button1.configure(bg="#54bac2")
        self.Button1.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button1.configure(fg="#ffffff")
        self.Button1.configure(text='ACESSO')

        self.label_cadastro = tk.Label(self.top)
        self.label_cadastro.place(relx=0.05, rely=0.377, height=25, width=88)
        self.label_cadastro.configure(bg="#54bac2")
        self.label_cadastro.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_cadastro.configure(fg="#ffffff")
        self.label_cadastro.configure(text='Login:')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.05, rely=0.533, height=25, width=88)
        self.Label2.configure(bg="#54bac2")
        self.Label2.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Label2.configure(fg="#ffffff")
        self.Label2.configure(text='Senha:')

        self.label_nome_completo = tk.Label(self.top)
        self.label_nome_completo.place(relx=0.297, rely=0.125, height=46, width=248)
        self.label_nome_completo.configure(bg="#54bac2")
        self.label_nome_completo.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_nome_completo.configure(fg="#ffffff")
        self.label_nome_completo.configure(text='A U T E N T I C A Ç Ã O')

        self.top.mainloop()

    def bd_login(self):
        '''temporizador = '25/03'

        a = (datetime.strptime(temporizador, '%d/%m').date())
        b = (datetime.today().strftime('%m-%d'))
        c = (datetime.strptime(b, '%m-%d').date())

        dia = int((a - c).days)

        if dia <= 0:
            msg = "Teste do SISTEMA CLÍNICAS EXPIRADO\n\nFavor entrar em contato (62) 6666-6666"
            messagebox.showerror("Cadastro de Pacientes", msg)
            sys.exit()
        else:

            msg = f"Uso gratuito no período de 30 dias\nFaltam {dia} dias para encerrar o uso trial\n"
            messagebox.showinfo("Cadastro de Pacientes", msg)

            if dia == 0:
                sys.exit()'''

        Nome = self.Entry_Nome_Login.get()
        Senha = self.Entry_Senha.get()

        no = 'Eli'
        se = '123'

        nom = 'Nogueira'
        sen = '123'

        try:
            if (Nome == no and Senha == se):
                messagebox.showinfo(title='Login Info', message='Autenticação aceita')
                self.top.destroy()
                import recep

            if (Nome == nom and Senha == sen):
                messagebox.showinfo(title='Login Info', message='Autenticação aceita')
                self.top.destroy()
                import consultas

            else:
                messagebox.showerror(title='Login Info', message='Login ou Senha não Existe')

        except:
            pass

Toplevel1()