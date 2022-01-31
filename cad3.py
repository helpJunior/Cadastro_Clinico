
import locale
import sys
import tkinter as tk
from tkinter.constants import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import DataCadastro

class Clinica1:
    def __init__(self):

########################  TELA CADASTRO  ##############################
        self.cad1 = tk.Tk()
        self.cad1.geometry("1132x536+24+49")
        self.cad1.minsize(120, 1)
        self.cad1.maxsize(1370, 749)
        self.cad1.resizable(1,  1)
        self.cad1.title("Clinica")
        self.cad1.configure(background="#54bac2")

        self.Entry_Nome_Cadastro = tk.Entry(self.cad1)
        self.Entry_Nome_Cadastro.bind("<Return>", self.pesquisar_bd)
        self.Entry_Nome_Cadastro.place(relx=0.186, rely=0.157, height=30, relwidth=0.746)
        self.Entry_Nome_Cadastro.configure(background="white")
        self.Entry_Nome_Cadastro.configure(font="TkFixedFont")
        self.Entry_Nome_Cadastro.configure(foreground="#000000")

        self.Entry_Estado_Civil = tk.Entry(self.cad1)
        self.Entry_Estado_Civil.place(relx=0.186, rely=0.35, height=30, relwidth=0.216)
        self.Entry_Estado_Civil.configure(background="white")
        self.Entry_Estado_Civil.configure(font="TkFixedFont")
        self.Entry_Estado_Civil.configure(foreground="#000000")

        self.Entry_coisa = tk.Entry(self.cad1)
        self.Entry_coisa.place(relx=0.186, rely=0.454, height=30, relwidth=0.216)
        self.Entry_coisa.configure(background="white")
        self.Entry_coisa.configure(disabledforeground="#a3a3a3")
        self.Entry_coisa.configure(font="TkFixedFont")
        self.Entry_coisa.configure(foreground="#000000")
        self.Entry_coisa.configure(insertbackground="black")

        self.Entry_Profissao = tk.Entry(self.cad1)
        self.Entry_Profissao.place(relx=0.186, rely=0.555, height=30, relwidth=0.216)
        self.Entry_Profissao.configure(background="white")
        self.Entry_Profissao.configure(disabledforeground="#a3a3a3")
        self.Entry_Profissao.configure(font="TkFixedFont")
        self.Entry_Profissao.configure(foreground="#000000")
        self.Entry_Profissao.configure(insertbackground="black")

        self.Entry_Endereco = tk.Entry(self.cad1)
        self.Entry_Endereco.place(relx=0.186, rely=0.654, height=30, relwidth=0.216)
        self.Entry_Endereco.configure(background="white")
        self.Entry_Endereco.configure(font="TkFixedFont")
        self.Entry_Endereco.configure(foreground="#000000")

        self.Entry_Cidade_Estado = tk.Entry(self.cad1)
        self.Entry_Cidade_Estado.place(relx=0.186, rely=0.756, height=30, relwidth=0.216)
        self.Entry_Cidade_Estado.configure(background="white")
        self.Entry_Cidade_Estado.configure(font="TkFixedFont")
        self.Entry_Cidade_Estado.configure(foreground="#000000")

        self.label_cadastro = tk.Label(self.cad1)
        self.label_cadastro.place(relx=0.177, rely=0.056, height=51, width=751)
        self.label_cadastro.configure(background="#54bac2")
        self.label_cadastro.configure(compound='left')
        self.label_cadastro.configure(font="-family {Arial Black} -size 28 -weight bold")
        self.label_cadastro.configure(foreground="#ffffff")
        self.label_cadastro.configure(text='C A D A S T R O')

        self.Label2 = tk.Label(self.cad1)
        self.Label2.place(relx=0.265, rely=0.933, height=41, width=870)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#54bac2")
        self.Label2.configure(compound='left')
        self.Label2.configure(font="-family {Arial} -size 12")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='CLÍNICA NOME QUALQUER - Dr. Qualquer 1')

        self.label_nome_completo = tk.Label(self.cad1)
        self.label_nome_completo.place(relx=0.014, rely=0.157, height=31, width=192)
        self.label_nome_completo.configure(anchor='e')
        self.label_nome_completo.configure(background="#54bac2")
        self.label_nome_completo.configure(compound='left')
        self.label_nome_completo.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_nome_completo.configure(foreground="#ffffff")
        self.label_nome_completo.configure(text='Nome Completo:')

        self.label_nascimento = tk.Label(self.cad1)
        self.label_nascimento.place(relx=0.014, rely=0.249, height=31, width=192)
        self.label_nascimento.configure(anchor='e')
        self.label_nascimento.configure(bg="#54bac2")
        self.label_nascimento.configure(compound='left')
        self.label_nascimento.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_nascimento.configure(foreground="#ffffff")
        self.label_nascimento.configure(text='Data Nascimento:')

        self.label_cpf_rg = tk.Label(self.cad1)
        self.label_cpf_rg.place(relx=0.027, rely=0.35, height=31, width=175)
        self.label_cpf_rg.configure(anchor='e')
        self.label_cpf_rg.configure(background="#54bac2")
        self.label_cpf_rg.configure(compound='left')
        self.label_cpf_rg.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_cpf_rg.configure(foreground="#ffffff")
        self.label_cpf_rg.configure(text='Estado Civil:')

        self.label_estado_civil = tk.Label(self.cad1)
        self.label_estado_civil.place(relx=0.028, rely=0.454, height=31, width=174)
        self.label_estado_civil.configure(anchor='e')
        self.label_estado_civil.configure(background="#54bac2")
        self.label_estado_civil.configure(compound='left')
        self.label_estado_civil.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_estado_civil.configure(foreground="#ffffff")
        self.label_estado_civil.configure(text='CPF/RG:')


        self.label_profissao = tk.Label(self.cad1)
        self.label_profissao.place(relx=0.028, rely=0.555, height=31, width=174)
        self.label_profissao.configure(anchor='e')
        self.label_profissao.configure(background="#54bac2")
        self.label_profissao.configure(compound='left')
        self.label_profissao.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_profissao.configure(foreground="#ffffff")
        self.label_profissao.configure(text='Profissão:')

        self.label_endereco = tk.Label(self.cad1)
        self.label_endereco.place(relx=0.027, rely=0.654, height=31, width=175)
        self.label_endereco.configure(anchor='e')
        self.label_endereco.configure(background="#54bac2")
        self.label_endereco.configure(compound='left')
        self.label_endereco.configure(cursor="fleur")
        self.label_endereco.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_endereco.configure(foreground="#ffffff")
        self.label_endereco.configure(text='Endereço:')

        self.label_cidade_estado = tk.Label(self.cad1)
        self.label_cidade_estado.place(relx=0.027, rely=0.75, height=31, width=175)
        self.label_cidade_estado.configure(anchor='ne')
        self.label_cidade_estado.configure(background="#54bac2")
        self.label_cidade_estado.configure(compound='left')
        self.label_cidade_estado.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_cidade_estado.configure(foreground="#ffffff")
        self.label_cidade_estado.configure(text='Cidade/Estado:')

        self.Text1 = tk.Text(self.cad1)
        self.Text1.place(relx=0.424, rely=0.336, relheight=0.455, relwidth=0.507)
        self.Text1.configure(background="#54bac2")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="#ffffff")
        self.Text1.configure(font="-family {Arial Black} -size 20 -weight bold")
        self.Text1.configure(wrap="word")

        self.Label9 = tk.Label(self.cad1)
        self.Label9.place(relx=0.512, rely=0.259, height=41, width=344)
        self.Label9.configure(background="#54bac2")
        self.Label9.configure(compound='center')
        self.Label9.configure(font="-family {Arial Black} -size 20 -weight bold")
        self.Label9.configure(foreground="#ffffff")
        self.Label9.configure(text='OBSERVAÇÕES')

        ########################## BOTÕES ###########################################
        self.Button_Cadastro = tk.Button(self.cad1, command=self.cadastro_bd)
        self.Button_Cadastro.place(relx=0.186, rely=0.84, height=44, width=177)
        self.Button_Cadastro.configure(activebackground="#ececec")
        self.Button_Cadastro.configure(activeforeground="#000000")
        self.Button_Cadastro.configure(background="#004040")
        self.Button_Cadastro.configure(compound='left')
        self.Button_Cadastro.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button_Cadastro.configure(foreground="#ffffff")
        self.Button_Cadastro.configure(pady="0")
        self.Button_Cadastro.configure(text='CADASTRAR')

        self.Button_Pesquisar = tk.Button(self.cad1, command=self.pesquisar_bd)
        self.Button_Pesquisar.place(relx=0.504, rely=0.84, height=44, width=177)
        self.Button_Pesquisar.configure(background="#004040")
        self.Button_Pesquisar.configure(compound='left')
        self.Button_Pesquisar.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button_Pesquisar.configure(foreground="#ffffff")
        self.Button_Pesquisar.configure(pady="0")
        self.Button_Pesquisar.configure(text='PESQUISAR')

        self.Button_Alterar = tk.Button(self.cad1)
        self.Button_Alterar.place(relx=0.804, rely=0.84, height=44, width=177)
        self.Button_Alterar.configure(background="#004040")
        self.Button_Alterar.configure(compound='left')
        self.Button_Alterar.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button_Alterar.configure(foreground="#ffffff")
        self.Button_Alterar.configure(pady="0")
        self.Button_Alterar.configure(text='ALTERAR')

        self.Button_Sair = tk.Button(self.cad1, command=self.sair)
        self.Button_Sair.place(relx=0.875, rely=0.019, height=24, width=127)
        self.Button_Sair.configure(background="#54bac2")
        self.Button_Sair.configure(compound='left')
        self.Button_Sair.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_Sair.configure(foreground="#FFFFFF")
        self.Button_Sair.configure(pady="0")
        self.Button_Sair.configure(text='SAIR')

###############################  DATA LOCAL  ########################
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        self.dia_atual = (datetime.today().strftime('Goiânia, %d de %B de %Y'))

        self.hj = tk.Label(self.cad1, bg="#54bac2", fg="#ffffff", text=f'{self.dia_atual}',
                           font='-family {Arial Black} -size 13 -weight bold')
        self.hj.place(relx=0.01, rely=0.00, height=51, width=350)

        self.bt_calendario = tk.Button(self.cad1, text="DATA", command=self.calendario)
        self.bt_calendario.place(relx=0.186, rely=0.249, height=30, width=50)
        self.Entry_Data = tk.Entry(self.cad1, width=10, font=('arial', '10', 'bold'))
        self.Entry_Data.place(relx=0.230, rely=0.248, height=30, width=70)

        self.cad1.mainloop()

##################### CALENDARIO #############################
    def calendario(self):
        self.calendario1 = Calendar(self.cad1, fg='gray75', bg='blue', font=('arial', '9', 'bold'), locale='pt_br')
        self.calendario1.place(relx=0.230, rely=0.298)
        self.calData = tk.Button(self.cad1, text=' INSERIR', font=('arial', '8', 'bold'), command=self.mostra_idade)
        self.calData.place(relx=0.186, rely=0.246, height=30, width=50)

    def mostra_idade(self):
        dataNasc = self.calendario1.get_date()

        a = (datetime.strptime(dataNasc, '%d/%m/%Y').date())
        b = (datetime.today().strftime('%Y-%m-%d'))
        c = (datetime.strptime(b, '%Y-%m-%d').date())

        self.idade = int((c - a).days / 365.25)

        self.calendario1.destroy()

        self.Entry_Data.delete(0, END)
        self.Entry_Data.insert(END, dataNasc)

        self.calData.destroy()

        self.data = tk.Label(self.cad1)
        self.data.place(relx=0.328, rely=0.249, height=31, width=80)
        self.data.configure(anchor='e')
        self.data.configure(bg="#54bac2")
        self.data.configure(compound='center')
        self.data.configure(font='-family {Arial Black} -size 16 -weight bold')
        self.data.configure(foreground="#ffffff")
        self.data.configure(text='anos:')

        self.idade = tk.Label(self.cad1, bg="#54bac2", fg= "red", text=f'{self.idade}', font='-family {Arial Black} -size 16 -weight bold' )
        self.idade.place(relx=0.310, rely=0.249, height=31, width=30)

#################### VARIAVEIS  ##################################

    def variaveis2_bd(self):
        self.Observacao2 = self.obs2.get('1.0', END).upper()

    def variaveis_bd(self):
        self.Nome_Completo = self.Entry_Nome_Cadastro.get().upper()
        self.Estado_Civil = self.Entry_Estado_Civil.get()
        #self.Documento = self.Entry_CPF_RG.get().upper
        self.Profissao = self.Entry_Profissao.get().upper()
        self.Endereco = self.Entry_Endereco.get().upper()
        self.Cidade_Estado = self.Entry_Cidade_Estado.get().upper()
        self.Data_Nascimento = self.Entry_Data.get()
        self.Observacao = self.Text1.get('1.0', END).upper()

        self.Entry_Nome_Cadastro.delete(0, END)
        self.Entry_Estado_Civil.delete(0, END)
        #self.Entry_CPF_RG.delete(0, END)
        self.Entry_Profissao.delete(0, END)
        self.Entry_Endereco.delete(0, END)
        self.Entry_Cidade_Estado.delete(0, END)
        self.Entry_Data.delete(0, END)
        self.Text1.delete('1.0', END)

###################### CADASTRANDO NO BANCO DE DADOS ############################
    def cadastro_bd(self):
        self.variaveis_bd()

        DataCadastro.cursor.execute("""INSERT INTO Cadastros (Nome_Completo, Estado_Civil, Profissao, Endereco, Cidade_Estado, Data_Nascimento, Observacao) VALUES(?, ?, ?, ?, ?, ?, ?)
        """, (self.Nome_Completo, self.Estado_Civil, self.Profissao, self.Endereco, self.Cidade_Estado, self.Data_Nascimento, self.Observacao))
        DataCadastro.conn.commit()
        messagebox.showinfo(title='Cadastro Info', message='Cadastro realizado com sucesso')

######################### TELA DE CONSULTAS ################################################
    def pesquisar_bd(self):
        self.cad2 = tk.Tk()
        self.cad2.geometry("1132x536+24+49")
        self.cad2.minsize(120, 1)
        self.cad2.maxsize(1370, 749)
        self.cad2.resizable(1, 1)
        self.cad2.title("Toplevel2")
        self.cad2.configure(background="#54bac2")

        self.Entry_Nome_Pesquisa = tk.Entry(self.cad2)
        self.Entry_Nome_Pesquisa.bind("<Return>", self.pesquisar_bd)
        self.Entry_Nome_Pesquisa.place(relx=0.186, rely=0.187, height=30, relwidth=0.746)
        self.Entry_Nome_Pesquisa.configure(background="white")
        self.Entry_Nome_Pesquisa.configure(font="TkFixedFont")
        self.Entry_Nome_Pesquisa.configure(foreground="#000000")

        self.label_nome_completo = tk.Label(self.cad2)
        self.label_nome_completo.place(relx=0.014, rely=0.187, height=31, width=192)
        self.label_nome_completo.configure(anchor='e')
        self.label_nome_completo.configure(background="#54bac2")
        self.label_nome_completo.configure(compound='left')
        self.label_nome_completo.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.label_nome_completo.configure(foreground="#ffffff")
        self.label_nome_completo.configure(text='Nome Completo:')

        self.obs_pesquisa = tk.Label(self.cad2)
        self.obs_pesquisa.place(relx=0.05, rely=0.280, relheight=0.100, relwidth=0.350)
        self.obs_pesquisa.configure(background="#54bac2")
        self.obs_pesquisa.configure(compound='center')
        self.obs_pesquisa.configure(font="-family {Arial Black} -size 20 -weight bold")
        self.obs_pesquisa.configure(foreground="#FFFFFF")
        self.obs_pesquisa.configure(text='DADOS PACIENTE')

        self.obs_alterar = tk.Label(self.cad2)
        self.obs_alterar.place(relx=0.612, rely=0.280, relheight=0.100, width=350)
        self.obs_alterar.configure(background="#54bac2")
        self.obs_alterar.configure(compound='center')
        self.obs_alterar.configure(font="-family {Arial Black} -size 20 -weight bold")
        self.obs_alterar.configure(foreground="#ffffff")
        self.obs_alterar.configure(text='DIAGNÓSTICO ATUAL.')

        self.label_cadastro = tk.Label(self.cad2)
        self.label_cadastro.place(relx=0.205, rely=0.075, height=51, width=751)
        self.label_cadastro.configure(background="#54bac2")
        self.label_cadastro.configure(compound='left')
        self.label_cadastro.configure(font="-family {Arial Black} -size 28 -weight bold")
        self.label_cadastro.configure(foreground="#ffffff")
        self.label_cadastro.configure(text='P E S Q U I S A R  P A C I E N T E')

        self.frame = tk.Frame(self.cad2)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.place(relx=0.05, rely=0.370, relheight=0.055, relwidth=0.050)
        self.obs1 = tk.Text(self.cad2, bg='#54bac2', font=('Courier', '13', 'bold'), fg='#ffffff')
        self.obs1.place(relx=0.05, rely=0.370, relheight=0.455, relwidth=0.350)

        self.obs2 = tk.Text(self.cad2)
        self.obs2.place(relx=0.6, rely=0.370, relheight=0.455, relwidth=0.350)
        self.obs2.configure(background="#54bac2")
        self.obs2.configure(font="TkTextFont")
        self.obs2.configure(foreground="#ffffff")
        self.obs2.configure(font="-family {Arial Black} -size 10 -weight bold")
        self.obs2.configure(wrap="word")

        self.Button_Pesquisar = tk.Button(self.cad2, command=self.localisar_cliente)
        self.Button_Pesquisar.place(relx=0.425, rely=0.35, height=44, width=177)
        self.Button_Pesquisar.configure(background="#004040")
        self.Button_Pesquisar.configure(compound='left')
        self.Button_Pesquisar.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button_Pesquisar.configure(foreground="#ffffff")
        self.Button_Pesquisar.configure(pady="0")
        self.Button_Pesquisar.configure(text='PESQUISAR')

        self.Button_Alterar = tk.Button(self.cad2, command=self.alterar_dados)
        self.Button_Alterar.place(relx=0.425, rely=0.55, height=44, width=177)
        self.Button_Alterar.configure(background="#004040")
        self.Button_Alterar.configure(compound='left')
        self.Button_Alterar.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button_Alterar.configure(foreground="#ffffff")
        self.Button_Alterar.configure(pady="0")
        self.Button_Alterar.configure(text='ALTERAR')

        self.Button_Consultar = tk.Button(self.cad2)
        self.Button_Consultar.place(relx=0.425, rely=0.78, height=44, width=177)
        self.Button_Consultar.configure(background="#004040")
        self.Button_Consultar.configure(compound='left')
        self.Button_Consultar.configure(font="-family {Arial Black} -size 14 -weight bold")
        self.Button_Consultar.configure(foreground="#ffffff")
        self.Button_Consultar.configure(pady="0")
        self.Button_Consultar.configure(text='CONSULTAR')

        self.rodape2 = tk.Label(self.cad2)
        self.rodape2.place(relx=0.265, rely=0.933, height=41, width=870)
        self.rodape2.configure(anchor='w')
        self.rodape2.configure(background="#54bac2")
        self.rodape2.configure(compound='left')
        self.rodape2.configure(font="-family {Arial} -size 12")
        self.rodape2.configure(foreground="#ffffff")
        self.rodape2.configure(text='CLÍNICA NOME QUALQUER - Dr. Qualquer 1')

###########################  DATA LOCAL  ########################
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        self.dia_atual = (datetime.today().strftime('Goiânia, %d de %B de %Y'))

        self.hj = tk.Label(self.cad2, bg="#54bac2", fg="#ffffff", text=f'{self.dia_atual}', font='-family {Arial Black} -size 13 -weight bold')
        self.hj.place(relx=0.00, rely=0.00, height=51, width=350)

####################### VOLTAR ##########################################
        self.Button_Voltar = tk.Button(self.cad2, command=self.voltar)
        self.Button_Voltar.place(relx=0.875, rely=0.019, height=24, width=127)
        self.Button_Voltar.configure(background="#54bac2")
        self.Button_Voltar.configure(compound='left')
        self.Button_Voltar.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_Voltar.configure(foreground="#FFFFFF")
        self.Button_Voltar.configure(pady="0")
        self.Button_Voltar.configure(text='VOLTAR')

    def alterar_dados(self):
        self.variaveis2_bd()

        DataCadastro.cursor.execute(""" UPDATE Cadastros SET Observacao = ? 
                WHERE Observacao = ? """, (self.obs2))

        DataCadastro.conn.commit()

    def localisar_cliente(self):
        self.obs1.delete(0.0, END)
        pesquisa_nome = self.Entry_Nome_Pesquisa.get().upper()
        DataCadastro.cursor.execute("SELECT * FROM Cadastros WHERE Nome_Completo = '%s'" % pesquisa_nome)
        self.consulta = DataCadastro.cursor.fetchall()
        for i in self.consulta:
            self.obs1.insert(END, f'''Nome:{i[1]}
Nascido:{i[6]}
Estado Civil:{i[2]}
Profissão:{i[3]}
Endereço:{i[4]}
Cidade/Estado:{i[5]}
____________________________
Obs.: {i[7]} '''.upper())

        self.cad2.mainloop()

    def voltar(self):
        self.cad2.destroy()

        #self.sair()
        #import pesquisa

    def sair(self):
        sys.exit()
        #self.cad1.destroy()

Clinica1()

