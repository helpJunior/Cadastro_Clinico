from tkinter import *
from tkinter import ttk
import sqlite3
import locale
from datetime import datetime
import sys
from tkinter.constants import *
import webbrowser
from pynput.keyboard import Key, Controller

keyb = Controller()

keyb.press(Key.caps_lock)

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
        self.lbl_anos.destroy()

    def db_conect(self):
        self.conexao = sqlite3.connect('//DESKTOP-ORPBP8A/Users/Manuel/Cadastro_Clinico/clientes2_bd.sqlite') # clientes2_bd.sqlite')
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
        self.observacao = self.entry_observacao.get('1.0', END)
        self.receita = self.entry_receita.get('1.0', END)

    def click(self, event):
        self.limpar_campos()
        self.lista_grid.selection()

        for x in self.lista_grid.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = self.lista_grid.item(x, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_nascimento.insert(END, col3)
            self.entry_civil.insert(END, col4)
            self.entry_religiao.insert(END, col5)
            self.entry_profissao.insert(END, col6)
            self.entry_endereco.insert(END, col7)
            self.entry_cidade.insert(END, col8)
            self.entry_anos.insert(END, col9)
            self.entry_dataConsulta.insert(END, col10)
            #self.entry_telefone.insert(END, col11)
            self.entry_observacao.insert(END, col11)
            self.entry_receita.insert(END, col12)

            self.diames = self.entry_nascimento.get()

            dia = self.diames[0:2]
            mes = self.diames[3:5]

            if dia >= '20' and dia <= '31' and mes == '03' or dia >= '01' and dia <= '20' and mes == '04':
                self.lbl_anos = Label(self.frame1, text="Signo de ÁRIES", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '21' and dia <= '30' and mes == '04' or dia >= '01' and dia <= '20' and mes == '05':
                self.lbl_anos = Label(self.frame1, text="Signo de TOURO", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '21' and dia <= '31' and mes == '05' or dia >= '01' and dia <= '20' and mes == '06':
                self.lbl_anos = Label(self.frame1, text="Signo de GÊMEOS", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '21' and dia <= '30' and mes == '06' or dia >= '01' and dia <= '21' and mes == '07':
                self.lbl_anos = Label(self.frame1, text="Signo de CÂNCER", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '22' and dia <= '31' and mes == '07' or dia >= '01' and dia <= '22' and mes == '08':
                self.lbl_anos = Label(self.frame1, text="Signo de LEÃO", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '22' and dia <= '31' and mes == '08' or dia >= '01' and dia <= '22' and mes == '09':
                self.lbl_anos = Label(self.frame1, text="Signo de VIRGEM", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '22' and dia <= '30' and mes == '09' or dia >= '01' and dia <= '22' and mes == '10':
                self.lbl_anos = Label(self.frame1, text="Signo de LIBRA", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '23' and dia <= '31' and mes == '10' or dia >= '01' and dia <= '21' and mes == '11':
                self.lbl_anos = Label(self.frame1, text="Signo de ESCORPIÃO", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '22' and dia <= '30' and mes == '11' or dia >= '01' and dia <= '21' and mes == '12':
                self.lbl_anos = Label(self.frame1, text="Signo de SARGITÁRIO", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '22' and dia <= '31' and mes == '12' or dia >= '01' and dia <= '20' and mes == '01':
                self.lbl_anos = Label(self.frame1, text="Signo de CAPRICÓRNIO", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '21' and dia <= '31' and mes == '01' or dia >= '01' and dia <= '18' and mes == '02':
                self.lbl_anos = Label(self.frame1, text="Signo de AQUÁRIO", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            elif dia >= '19' and dia <= '29' and mes == '02' or dia >= '01' and dia <= '19' and mes == '03':
                self.lbl_anos = Label(self.frame1, text="Signo de PEIXES", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=300)

            else:
                self.lbl_anos = Label(self.frame1, text="Data inválida", bg='#356A6A', fg='yellow', font=('arial', 20, 'bold'))
                self.lbl_anos.place(x=815, y=320, height=30, width=290)

    def deletar(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""DELETE FROM clientes2 WHERE id = ?""", self.codigo)
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.listar_dados()

    def atualizar(self):
        self.lbl_anos.destroy()
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE clientes2 SET receita = ? 
        WHERE id = ?;
        """, (self.receita, self.codigo))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        #self.listar_dados()
        self.enviar_email()

    def atualizar_sistema(self):
        principal()

    def enviar_email(self):
        self.lbl_anos.destroy()
        import smtplib
        from email.mime.text import MIMEText

        cabeçalho = self.nome
        corpo = self.receita
        # conexão com os servidores do google
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        # username ou email para logar no servidor
        username = 'seuemail@gmail.com'
        password = 'suasenha'

        from_addr = 'seuemail@gmail.com'
        to_addrs = ['destino@gmail.com']

        message = MIMEText(corpo) #enviar somente texto
        message['subject'] = cabeçalho
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()

        self.atualizar_sistema()

    def pesquisar(self):
        self.db_conect()
        self.lista_grid.delete(*self.lista_grid.get_children())

        self.entry_nome.insert(END, '%')
        nome = '%' + self.entry_nome.get()

        self.cursor.execute("""SELECT id,nome,nascimento,civil,religiao,profissao,endereco,cidade,idade,data,observacao,receita FROM clientes2 WHERE Nome LIKE '%s' COLLATE NOCASE ORDER BY Nome ASC""" % nome)
        Resultado_busca = self.cursor.fetchmany()

        for cliente in Resultado_busca:
            self.lista_grid.insert("", END, values=cliente)
        self.db_desconect()
        self.limpar_campos()
        self.db_desconect()

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

        root.mainloop()

    def tela(self):
        self.root.title("Clinica")
        self.root.configure(background='#356A6A')
        self.root.geometry("1250x866+0+0")
        self.root.resizable(True, True)
        self.root.state('zoomed')

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#356A6A", highlightbackground="#356A6A")
        self.frame1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.86)

        self.frame2 = Frame(self.root, bd=4, bg="#356A6A", highlightbackground="#356A6A", highlightthickness=0)
        self.frame2.place(relx=0.02, rely=0.70, relwidth=0.96, relheight=0.145)

    def limpa_receita(self):
        self.entry_receita.delete('1.0', END)

    def widgets_frame1(self):
    # botão limpar
        self.bt_limpar = Button(self.root, text="NOVA\nCONSULTA",  bg="#356A6A", fg="white", font=('verdana', 13, 'bold'), command=self.limpar_campos)
        self.bt_limpar.place(x=480, y=855, width=120, relheight=0.07)

    # botão PESQUISAR
        self.bt_buscar = Button(self.root, text="PESQUISAR", bg="#356A6A", fg="white", font=('verdana', 13, 'bold'), command=self.pesquisar)
        self.bt_buscar.place(x=525, y=89.01, width=120, height=30)

    # botão alterar
        self.bt_alterar = Button(self.root, text="ENVIAR\nRECEITA", bg="#003737", fg="white", font=('verdana', 13, 'bold'), command=self.atualizar)
        self.bt_alterar.place(x=635, y=855, relwidth=0.1, relheight=0.07)

    # botão terra
        self.bt_terra = Button(self.root, text="Terra",  bg="#003737", fg="white", font=('verdana', 13, 'bold'), command=lambda: webbrowser.open('https://mail.terra.com.br/ozone/#/mailList/INBOX'))  # self.tela_consultar)
        self.bt_terra.place(relx=0.915, rely=0.935, relwidth=0.05, relheight=0.05)

        self.bt_terra = Button(self.root, text="MG Sena", bg="#003737", fg="white", font=('verdana', 13, 'bold'), command=lambda: webbrowser.open('https://www.google.com/search?q=mega+sena&oq=mega+sena&aqs=chrome..69i57.2142j0j1&sourceid=chrome&ie=UTF-8'))  # self.tela_consultar)
        self.bt_terra.place(relx=0.775, rely=0.935, relwidth=0.07, relheight=0.05)

        self.bt_terra = Button(self.root, text="Bulário", bg="#003737", fg="white", font=('verdana', 13, 'bold'), command=lambda: webbrowser.open('https://consultaremedios.com.br/bulas'))  # self.tela_consultar)
        self.bt_terra.place(relx=0.845, rely=0.935, relwidth=0.07, relheight=0.05)

    # botão sair
        self.bt_sair = Button(self.root, text='SAIR', bg="#356A6A", fg="#FFFFFF", font="-family {Segoe UI} -size 9 -weight bold", command = self.sair)
        self.bt_sair.place(relx=0.895, rely=0.019, height=24, width=127)

    # botão limpa receita
        self.bt_limpaReceita = Button(self.frame1, text="Limpa Receita", bg="#356A6A", fg="red", font=('verdana', 20, 'bold'), command=self.limpa_receita)
        self.bt_limpaReceita.place(x=500, y=435, height=34, width=250)

    # label e entry codigo
        self.lb_codigo = Label(self.frame1, text="Id:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_codigo.place(x=153, y=45)

        self.entry_codigo = Entry(self.frame1, bg='#356A6A', fg="#ffffff", font=('arial', 15, 'bold'))
        self.entry_codigo.place(x=187, y=45, width=40, height=27)

    # Nome CADASTRO tela principal
        self.lb_cadastro = Label(self.frame1, text="C O N S U L T A", bg="#356A6A", fg="#ffffff", font=('arial black', 40, 'bold'))
        self.lb_cadastro.place(x=450, y=0)

    # label e entry nome
        self.lb_nome = Label(self.frame1, text="Nome Completo:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_nome.place(x=20, y=85)

        self.entry_nome = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_nome.place(x=185, y=85, width=450, height=30)

    # label e entry Nascimento
        self.lb_nascimento = Label(self.frame1, text="Data de Nascimento:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_nascimento.place(x=590, y=280)

        self.entry_nascimento = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_nascimento.place(x=815, y=280, width=140, height=25)

    # label e entry Estado Civil
        self.lb_civil = Label(self.frame1, text="Estado Civil:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_civil.place(x=57, y=155)

        self.entry_civil = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_civil.place(x=185, y=155, width=450, height=30)

    # label e entry Religião
        self.lb_religiao = Label(self.frame1, text="Religião:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_religiao.place(x=93, y=225)

        self.entry_religiao = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_religiao.place(x=185, y=225, width=450, height=30)

    # label e entry Data Consulta
        self.lb_dataConsulta = Label(self.frame1, text='Data da Consulta', bg="#356A6A", fg="#ffffff", font=('arial', 13, 'bold'))  # , relief=RAISED)
        self.lb_dataConsulta.place(x=30, y=280, width=145)

    # doido = 'muitodoido'
        self.entry_dataConsulta = Entry(self.frame1, bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))#, relief=FLAT)
        self.entry_dataConsulta.place(x=180, y=283, height=30, width=110)

    # label e entry Profissão
        self.lb_profissao = Label(self.frame1, text="Profissão:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_profissao.place(x=690, y=85)

        self.entry_profissao = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_profissao.place(x=800, y=85, width=400, height=30)

    # label e entry Endereço
        self.lb_endereco = Label(self.frame1, text="Endereço.:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_endereco.place(x=685, y=155)

        self.entry_endereco = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_endereco.place(x=800, y=155, width=400, height=30)

    # label e entry Cidade
        self.lb_cidade = Label(self.frame1, text="Cidade/UF:", bg="#356A6A", fg="#ffffff", font=('arial', 15, 'bold'))
        self.lb_cidade.place(x=685, y=225)

        self.entry_cidade = Entry(self.frame1, bg="white", fg="#000000", font=('arial', 20, 'bold'))
        self.entry_cidade.place(x=800, y=225, width=400, height=30)

    # label e entry Observação
        self.lb_observacao = Label(self.frame1, text="Observação:", bg="#356A6A", fg="#ffffff", font=('verdana', 20, 'bold'))
        self.lb_observacao.place(x=39, y=325, width=185)

        self.entry_observacao = Text(self.frame1, bg="#356A6A", fg="#ffffff", font=('arial', 25, 'bold'))
        self.entry_observacao.place(x=23, y=360, height=70, width=1200)

    # label e entry Receita
        self.lb_receita = Label(self.frame1, text="Receita:", bg="#356A6A", fg="#ffffff", font=('verdana', 20, 'bold'))
        self.lb_receita.place(x=1, y=440, width=187)

        self.entry_receita = Text(self.frame1, bg="#356A6A", fg="#FFFFFF", font=('arial', 25, 'bold'))
        self.entry_receita.place(x=25, y=475, height=120, width=1200)

    # data local
        self.dia_atual = (datetime.today().strftime('Goiânia, %d de %B de %Y'))

        self.hj = Label(self.root, bg="#356A6A", fg="#ffffff", text=f'{self.dia_atual}', font=('arial', 10, 'bold'))
        self.hj.place(x=0, y=0, height=51, width=220)

    # label e entry anos
        self.lbl_anos = Label()
        self.lbl_anos1 = Label(self.frame1, text='      anos de idade', bg="#356A6A", fg="#ffffff", font=('arial', 13, 'bold'))
        self.lbl_anos1.place(x=1004, y=273, height=54, width=150)

        self.entry_anos = Entry(self.frame1, bg="#356A6A", fg='#ffffff', font=('arial', 17, 'bold'), relief=FLAT)
        self.entry_anos.place(x=990, y=273, height=45, width=50)

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
        self.lista_grid.heading("#11", text='OBSERVAÇÃO\n')
        self.lista_grid.heading("#12", text='RECEITA\n')

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
        self.lista_grid.column("#11", width=180)
        self.lista_grid.column("#12", width=150)
        self.lista_grid.place(x=1, rely=0.1, relwidth=0.99, relheight=0.90)

        # self.scrol_lista = Scrollbar(self.frame2, orient='vertical')
        # self.lista_grid.configure(yscroll=self.scrol_lista.set)
        # self.scrol_lista.place(relx=0.984, rely=0.009, relwidth=0.02, relheight=100)
        self.lista_grid.bind("<Double-1>", self.click)

    def tela_consultar(self):
        self.root.destroy()
        import consultas

    def sair(self):
        self.root.destroy()
        sys.exit()

    def Menus(self):
        Menubar = Menu(self.root)

        self.root.config(menu=Menubar)
        filemenu = Menu(Menubar)
        filemenu2 = Menu(Menubar)

        def Quit():
            self.root.destroy()

########################  MENU BAR  #########################
        '''Menubar.add_cascade(label="opções",menu=filemenu)
        Menubar.add_cascade(label="Funções", menu=filemenu2)

        filemenu.add_command(label="Sair",command=Quit)
        filemenu2.add_command(label="Limpar campos", command=self.limpar_campos)
        #filemenu2.add_command(label="Gerar Relatório", command=self.Gerar_Ficha)'''

principal()