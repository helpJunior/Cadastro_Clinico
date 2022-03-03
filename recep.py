from tkinter import *
from tkinter import ttk
import sqlite3
#import locale
from datetime import datetime
import sys
from tkinter.constants import *
from tkinter import messagebox
import webbrowser
from pynput.keyboard import Key, Controller

keyb = Controller()
keyb.press(Key.caps_lock)
keyb.release(Key.caps_lock)

root = Tk()

class Funcoes():
    def limpar_campos(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_nascimento.delete(0, END)
        self.entry_civil.delete(0, END)
        self.entry_religiao.delete(0, END)
        self.entry_profissao.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.entry_dataConsulta.delete(0, END)
        self.entry_observacao.delete('1.0', END)
        self.entry_receita.delete('1.0', END)
        self.entry_anos.delete(0, END)
        self.entry_telefone.delete(0, END)

    def db_conect(self):
        self.conexao = sqlite3.connect('//DESKTOP-ORPBP8A/Users/Manuel/Cadastro_Clinico/clientes2_bd.sqlite') # clientes2_bd.sqlite)
        self.cursor = self.conexao.cursor()

    def db_desconect(self):
        self.conexao.close()

    def criar_tabela(self):
        self.db_conect()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT UNIQUE NOT NULL,
            nascimento TEXT UNIQUE NOT NULL,
            civil TEXT  NOT NULL,
            religiao TEXT  NOT NULL,
            profissao TEXT  NOT NULL,
            endereco TEXT  NOT NULL,
            cidade TEXT  NOT NULL,
            idade TEXT ,
            data TEXT ,
            telefone TEXT ,
            observacao TEXT  NOT NULL,
            receita TEXT 
            );""");

        self.conexao.commit()
        self.db_desconect()

    def capturar_campos(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.nascimento = self.entry_nascimento.get()
        self.civil = self.entry_civil.get()
        self.religiao = self.entry_religiao.get()
        self.profissao = self.entry_profissao.get()
        self.endereco = self.entry_endereco.get()
        self.cidade = self.entry_cidade.get()
        self.data = self.entry_dataConsulta.get()
        self.telefone = self.entry_telefone.get()
        self.observacao = self.entry_observacao.get('1.0', END)
        self.receita = self.entry_receita.get('1.0', END)

    def inserir_dados(self):
        self.entry_idade.destroy()
        self.entry_idade.destroy()
        self.capturar_campos()
        self.db_conect()

        if self.entry_nome.get() =="":
            msg= "È necessário preencher o campo Nome Completo\n"
            messagebox.showinfo("Cadastro de Pacientes", msg)

        elif self.entry_nascimento.get() =="":
            msg= "È necessário preencher o campo a data de nascimento\n"
            messagebox.showinfo("Cadastro de Pacientes", msg)

        else:
            self.db_conect()
            self.cursor.execute("""INSERT INTO clientes2 (nome,nascimento,civil,religiao,profissao,endereco,cidade,idade,data,telefone,observacao,receita) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (self.nome, self.nascimento, self.civil, self.religiao, self.profissao, self.endereco, self.cidade,self.idade,self.data, self.telefone, self.observacao, self.receita))

            self.conexao.commit()
            self.db_desconect()
            self.limpar_campos()
            self.entry_idade.destroy()
            self.atualizar_sistema()
            
    def listar_dados(self):
        self.entry_idade.destroy()
        self.lista_grid.delete(*self.lista_grid.get_children())
        self.db_conect()
        lista = self.cursor.execute("""SELECT id , nome,nascimento,civil,religiao,profissao,endereco,cidade,idade,data,telefone,observacao,receita
         FROM clientes2 ORDER BY nome ASC;""")

        for l in lista:
            self.lista_grid.insert("", END, values=l)
        self.db_desconect()

    def click(self, event):
        self.limpar_campos()
        self.lista_grid.selection()

        for x in self.lista_grid.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13= self.lista_grid.item(x, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_nascimento.insert(END, col3)
            self.entry_civil.insert(END, col4)
            self.entry_religiao.insert(END, col5)
            self.entry_profissao.insert(END, col6)
            self.entry_endereco.insert(END, col7)
            self.entry_cidade.insert(END, col8)
            self.entry_anos.insert(END,col9)
            self.entry_dataConsulta.insert(END, col10)
            self.entry_telefone.insert(END, col11)
            self.entry_observacao.insert(END, col12)
            self.entry_receita.insert(END, col13)

    def deletar(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""DELETE FROM clientes2 WHERE id = ?""", self.codigo)
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.listar_dados()

    def atualizar_sistema(self):
        principal()

    def atualizar2(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE clientes2 SET receita = ? 
           WHERE id = ?;
           """, (self.receita, self.codigo))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()

    def atualizar(self):
        self.entry_idade.destroy()
        self.lb_signos.destroy()
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE clientes2 SET nome = ?, nascimento = ?, civil = ?, religiao = ?, profissao = ?, endereco = ?, cidade = ?, idade = ?, data = ?, telefone = ?, observacao = ?, receita = ?
        WHERE id = ?;
        """, (self.nome, self.nascimento, self.civil, self.religiao, self.profissao, self.endereco, self.cidade, self.idade, self.data, self.telefone, self.observacao, self.receita, self.codigo))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.entry_idade.destroy()

    def pesquisar(self):
        self.db_conect()
        self.lista_grid.delete(*self.lista_grid.get_children())

        self.entry_nome.insert(END, '%')
        nome = '%' + self.entry_nome.get()

        self.cursor.execute("""SELECT * FROM clientes2  WHERE Nome LIKE '%s' COLLATE NOCASE ORDER BY Nome ASC""" % nome)
        Resultado_busca = self.cursor.fetchmany()
        self.limpar_campos()

        for cliente in Resultado_busca:
            self.lista_grid.insert("", END, values=cliente)
            self.db_desconect()

            if Resultado_busca != False:

                self.db_desconect()
                self.limpar_campos()
                self.click()
                self.limpar_campos()
        else:
            self.db_desconect()
            slice = nome[1:-1].upper()

            msg = f" O nome {slice} não está cadastrado\n"
            messagebox.showerror("                    Localizar Pacientes", msg)

            self.db_desconect()
            self.limpar_campos()

class principal(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.grid_cliente()
        self.widgets_frame1()
        self.Menus()
        self.criar_tabela()
        self.limpar_campos()
        self.cor_widgets()

        root.mainloop()

    def tela(self):
        self.root.title("Clinica")
        self.root.configure(background='#54bac2')
        self.root.geometry("990x600+0+0")
        self.root.resizable(1, 1)
        self.root.state('zoomed')
        self.root.maxsize(1370, 749)
        self.root.minsize(120, 1)

########################################### TEMPORIZADOR  em TESTE #################################################################
    '''def temp(self):

            temporizador = '15/03'

            a = (datetime.strptime(temporizador, '%d/%m').date())
            b = (datetime.today().strftime('%m-%d'))
            c = (datetime.strptime(b, '%m-%d').date())

            dia = int((a - c).days)

            if dia == 0:
                msg = "Teste do SISTEMA CLÍNICAS EXPIRADO\n\nFavor entrar em contato (62) 6666-6666"
                messagebox.showerror("Cadastro de Pacientes", msg)
                self.sair()
            else:

                msg = f"Faltam {dia} dias para EXPIRAR o SISTEMA CLÍNICAS\n"
                messagebox.showinfo("Cadastro de Pacientes", msg)'''
#########################################################################################
    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#54bac2")
        self.frame1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.86)

        self.frame2 = Frame(self.root, bd=4, bg="#fff")
        self.frame2.place(relx=0.02, rely=0.74, relwidth=0.96, relheight=0.180)

    def cor_widgets(self):
    #Botões
        self.bt_bg = '#54bac2'
        self.bt_fg = 'white'
        self.bt_font = ('verdana', 13, 'bold')

    #Label
        self.lb_bg = '#54bac2'
        self.lb_fg = 'white'
        self.lb_font = ('arial', 15, 'bold')

    #Entradas
        self.et_bg = "#54bac2"
        self.et_bg_branco = "#ffffff"
        self.et_fg_branco = "#ffffff"
        self.et_fg_preto = "#000000"
        self.et_font = ('arial', 15, 'bold')

    def widgets_frame1(self):
        self.cor_widgets()

    # botão limpar
        self.bt_limpar = Button(self.root, text="LIMPAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.atualizar_sistema)
        self.bt_limpar.place(relx=0.05, rely=0.925, relwidth=0.10, relheight=0.07)

    # botão PESQUISAR
        self.bt_buscar = Button(self.root, text="PESQUISAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.pesquisar)
        self.bt_buscar.place(relx=0.255, rely=0.925, relwidth=0.15, relheight=0.07)

    # botão cadastrar
        self.bt_novo = Button(self.root, text="CADASTRAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.inserir_dados)
        self.bt_novo.place(relx=0.455, rely=0.925, relwidth=0.15, relheight=0.07)

    # botão alterar
        self.bt_alterar = Button(self.root, text="ALTERAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.atualizar)
        self.bt_alterar.place(relx=0.655, rely=0.925, relwidth=0.1, relheight=0.07)

    # botão Gmail
        self.bt_consultar = Button(self.root, text="Gmail",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=lambda: webbrowser.open('https://gmail.com'))#self.tela_consultar)
        self.bt_consultar.place(relx=0.850, rely=0.935, relwidth=0.07, relheight=0.05)

    # botão Terra
        self.bt_consultar2 = Button(self.root, text="Terra", bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=lambda: webbrowser.open('https://mail.terra.com.br/ozone/#/mailList/INBOX'))  # self.tela_consultar)
        self.bt_consultar2.place(relx=0.920, rely=0.935, relwidth=0.07, relheight=0.05)

    # botão google
        self.bt_consultar = Button(self.root, text="Google", bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=lambda: webbrowser.open('https://google.com'))  # self.tela_consultar)
        self.bt_consultar.place(relx=0.770, rely=0.935, relwidth=0.08, relheight=0.05)

    # Nome CADASTRO tela principal
        self.lb_cadastro = Label(self.frame1, text="C A D A S T R O", bg=self.lb_bg, fg=self.lb_fg, font=('arial black', 40, 'bold'))
        self.lb_cadastro.place(x=380, y=0)

    # label e entry codigo
        self.lb_codigo = Label(self.frame1, text="Id:", bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_codigo.place(x=153, y=46)

        self.entry_codigo = Entry(self.frame1, bg=self.et_bg, fg=self.et_fg_branco, font=self.et_font)
        self.entry_codigo.place(x=187, y=48, width=40, height=27)

    # label e entry Nome
        self.lb_nome = Label(self.frame1, text="Nome Completo:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_nome.place(x=5, y=85)

        self.entry_nome = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=('arial', 20, 'bold'))
        self.entry_nome.place(x=165, y=85, width=300, height=30)

    # label e entry Estado Civil
        self.lb_civil = Label(self.frame1, text="Estado Civil:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_civil.place(x=40, y=155)

        self.entry_civil = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=('arial', 20, 'bold'))
        self.entry_civil.place(x=165, y=155, width=300, height=30)

    # label e entry Religião
        self.lb_religiao = Label(self.frame1, text="Religião:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_religiao.place(x=75, y=225)

        self.entry_religiao = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=('arial', 20, 'bold'))
        self.entry_religiao.place(x=165, y=225, width=300, height=30)

    # label e entry Profissão
        self.lb_profissao = Label(self.frame1, text="Profissão:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_profissao.place(x=475, y=85)

        self.entry_profissao = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=('arial', 20, 'bold'))
        self.entry_profissao.place(x=580, y=85, width=300, height=30)

    # label e entry Endereço
        self.lb_endereco = Label(self.frame1, text="Endereço.:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_endereco.place(x=470, y=155)

        self.entry_endereco = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font= ('arial', 20, 'bold'))
        self.entry_endereco.place(x=580, y=155, width=300, height=30)

    # label e entry Cidade
        self.lb_cidade = Label(self.frame1, text="Cidade/UF:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_cidade.place(x=470, y=225)

        self.entry_cidade = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font= ('arial', 20, 'bold'))
        self.entry_cidade.place(x=580, y=225, width=300, height=30)

    # label e entry Data Consulta
        self.lb_dataConsulta = Label(self.frame1, text='Dt. Consulta:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)  # , relief=RAISED)
        self.lb_dataConsulta.place(x=940, y=85, width=125)

        self.entry_dataConsulta = Entry(self.frame1, bg=self.et_bg, fg=self.lb_fg, font=self.lb_font) #, relief=FLAT)
        self.entry_dataConsulta.place(x=1070, y=85, height=30, width=110)

    # data de nascimento
        self.lb_nascimento = Label(self.frame1, text="Nasc.:", bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_nascimento.place(x=940, y=155)

        self.bt_calendario = Button(self.frame1, text="DATA", command=self.mostra_idade)  # self.calendario
        self.bt_calendario.place(x=1010, y=155, height=30, width=40)

        self.entry_nascimento = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.entry_nascimento.bind("<Return>")
        self.entry_nascimento.place(x=1050, y=155, height=27, width=108)

    # contato
        self.lb_telefone = Label(self.frame1, text="Telefone:", bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_telefone.place(x=910, y=225, height=30, width=85)

        self.entry_telefone = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.entry_telefone.place(x=1000, y=225, height=27, width=155)

    # label e text Observação
        self.lb_observacao = Label(self.frame1, text="Obs.:", bg=self.lb_bg, fg=self.lb_fg, font=('verdana', 15, 'bold'))
        self.lb_observacao.place(x=1, y=350, relwidth=0.10)

        self.entry_observacao = Text(self.frame1, bg=self.et_bg, fg=self.et_fg_preto, font= ('arial', 25, 'bold'))
        self.entry_observacao.place(x=23, y=383, height=99, width=630)

    # label e text Receita
        self.lb_receita = Label(self.frame1, text="RECOMENDAÇÕES TERAPÊUTICAS:", bg=self.lb_bg, fg=self.lb_fg, font=('verdana', 13, 'bold'))
        self.lb_receita.place(x=660, y=358, width=400)

        self.entry_receita = Text(self.frame1, bg=self.et_bg, fg='#ffffff', font= ('arial', 15, 'bold'))
        self.entry_receita.place(x=695, y=383, height=99, width=630)

    # data local
        self.dia_atual = (datetime.today().strftime('Goiânia, %d de %B de %Y'))
        self.hj = Label(self.frame1, bg=self.lb_bg, fg=self.lb_fg, text=f'{self.dia_atual}', font=('arial', 10, 'bold'))
        self.hj.place(x=0, y=0, height=51, width=220)

    # label e entry anos
        self.entry_anos = Entry()
        self.entry_anos.place()

########################### CALENDARIO EM TESTE ################################################################################################
    #def calendario(self):
        #self.calendario1 = Calendar(self.root, fg='gray75', bg='blue', font=('arial', '9', 'bold'), locale='pt_br')
        #self.calendario1.place(x=1010, y=300)

        #self.calData = Button(self.root, text=' INSERIR', font=('arial', '8', 'bold'), command=self.mostra_idade)
        #self.calData.place(x=810, y=307, height=30, width=50)
##################################################################################################################################################

    def mostra_idade(self):
        try:
            dataNasc = self.entry_nascimento.get()

            a = (datetime.strptime(dataNasc, '%d/%m/%Y').date())
            b = (datetime.today().strftime('%Y-%m-%d'))
            c = (datetime.strptime(b, '%Y-%m-%d').date())

            self.idade = int((c - a).days / 365.25)

            self.entry_anos.delete(0, END)
            self.entry_nascimento.delete(0, END)
            self.entry_nascimento.insert(END, dataNasc)

            self.entry_idade = Label(self.frame1, bg=self.lb_bg, fg="red", text=f'{self.idade} anos', font=self.lb_font)
            self.entry_idade.place(x=1170, y=158, height=27, width=70)

            self.diames = self.entry_nascimento.get()

            dia = self.diames[0:2]
            mes = self.diames[3:5]

            if dia >= '20' and dia <= '31' and mes == '03' or dia >= '01' and dia <= '20' and mes == '04':
                self.lb_signos = Label(self.frame1, text="Signo de ÁRIES", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("aries")
            elif dia >= '21' and dia <= '30' and mes == '04' or dia >= '01' and dia <= '20' and mes == '05':
                self.lb_signos = Label(self.frame1, text="Signo de TOURO", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("touro")
            elif dia >= '21' and dia <= '31' and mes == '05' or dia >= '01' and dia <= '20' and mes == '06':
                self.lb_signos = Label(self.frame1, text="Signo de GÊMEOS", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("gemeos")
            elif dia >= '21' and dia <= '30' and mes == '06' or dia >= '01' and dia <= '21' and mes == '07':
                self.lb_signos = Label(self.frame1, text="Signo de CÂNCER", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("cancer")
            elif dia >= '22' and dia <= '31' and mes == '07' or dia >= '01' and dia <= '22' and mes == '08':
                self.lb_signos = Label(self.frame1, text="Signo de LEÃO", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("leao")
            elif dia >= '22' and dia <= '31' and mes == '08' or dia >= '01' and dia <= '22' and mes == '09':
                self.lb_signos = Label(self.frame1, text="Signo de VIRGEM", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("virgem")
            elif dia >= '22' and dia <= '30' and mes == '09' or dia >= '01' and dia <= '22' and mes == '10':
                self.lb_signos = Label(self.frame1, text="Signo de LIBRA", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("libra")
            elif dia >= '23' and dia <= '31' and mes == '10' or dia >= '01' and dia <= '21' and mes == '11':
                self.lb_signos = Label(self.frame1, text="Signo de ESCORPIÃO", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("escorpiao")
            elif dia >= '22' and dia <= '30' and mes == '11' or dia >= '01' and dia <= '21' and mes == '12':
                self.lb_signos = Label(self.frame1, text="Signo de SARGITÁRIO", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("sagitario")
            elif dia >= '22' and dia <= '31' and mes == '12' or dia >= '01' and dia <= '20' and mes == '01':
                self.lb_signos = Label(self.frame1, text="Signo de CAPRICÓRNIO", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("capricornio")
            elif dia >= '21' and dia <= '31' and mes == '01' or dia >= '01' and dia <= '18' and mes == '02':
                self.lb_signos = Label(self.frame1, text="Signo de AQUÁRIO", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("aquario")
            elif dia >= '19' and dia <= '29' and mes == '02' or dia >= '01' and dia <= '19' and mes == '03':
                self.lb_signos = Label(self.frame1, text="Signo de PEIXES", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

                # print("peixes")
            else:
                self.lb_signos = Label(self.frame1, text="Data inválida", bg=self.lb_bg, fg='yellow', font=self.lb_font)
                self.lb_signos.place(x=1000, y=185, height=30, width=250)

        except:
            msg = "Preencher a data de nascimento\n"
            messagebox.showinfo("Cadastro de Pacientes", msg)

    def grid_cliente(self):
        self.lista_grid = ttk.Treeview(self.frame2, columns=(
        'col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12', 'col13'))
        self.lista_grid.heading("#0", text='\n')
        self.lista_grid.heading("#1", text='CODIGO\n')
        self.lista_grid.heading("#2", text='NOME\n')
        self.lista_grid.heading("#3", text='NASCIMENTO\n')
        self.lista_grid.heading("#4", text='E. CIVIL\n')
        self.lista_grid.heading("#5", text='RELIGIÃO\n')
        self.lista_grid.heading("#6", text='PROFISSÃO\n')
        self.lista_grid.heading("#7", text='ENDEREÇO\n')
        self.lista_grid.heading("#8", text='CIDADE/UF\n')
        self.lista_grid.heading("#9", text='IDADE\n')
        self.lista_grid.heading("#10", text='D. CONSULTA\n')
        self.lista_grid.heading("#11", text='TELEFONE\n')
        self.lista_grid.heading("#12", text='OBSERVAÇÃO\n')
        self.lista_grid.heading("#13", text='RECEITA\n')

        self.lista_grid.column("#0", width=0)
        self.lista_grid.column("#1", width=60)
        self.lista_grid.column("#2", width=120)
        self.lista_grid.column("#3", width=90)
        self.lista_grid.column("#4", width=50)
        self.lista_grid.column("#5", width=60)
        self.lista_grid.column("#6", width=80)
        self.lista_grid.column("#7", width=120)
        self.lista_grid.column("#8", width=80)
        self.lista_grid.column("#9", width=40)
        self.lista_grid.column("#10", width=90)
        self.lista_grid.column("#11", width=70)
        self.lista_grid.column("#12", width=180)
        self.lista_grid.column("#13", width=150)
        self.lista_grid.place(x=1, rely=0.1, relwidth=0.99, relheight=0.90)
        self.lista_grid.bind("<Double-1>", self.click)

    def tela_consultar(self):
        self.db_desconect()
        import consultas

    def sair(self):
        self.root.destroy()
        sys.exit()

    def Menus(self):
        Menubar = Menu(self.root)

        self.root.config(menu=Menubar)
        filemenu1 = Menu(Menubar, tearoff=0)
        filemenu2 = Menu(Menubar, tearoff=0)

        Menubar.add_cascade(label="Funções", menu=filemenu1)
        Menubar.add_cascade(label="Opções", menu=filemenu2)

        filemenu1.add_command(label="Listar Pacientes", command=self.pesquisar)
        filemenu1.add_command(label="Tela de Consulta", command=self.tela_consultar)

        filemenu2.add_command(label="Atualizar Sistema", command=self.atualizar_sistema)
        filemenu2.add_command(label="Deletar Paciente", foreground="red", command=self.deletar)
        filemenu2.add_command(label="Sair do Sistema", command=self.sair)

        def Quit():
            self.root.destroy()

principal()