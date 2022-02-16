from tkinter import *
from tkinter import ttk
import sqlite3
import locale
from datetime import datetime
from tkcalendar import Calendar
import sys
from tkinter.constants import *
from tkinter import messagebox

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

    def db_conect(self):
        self.conexao = sqlite3.connect('clientes26_bd.bd')
        self.cursor = self.conexao.cursor()

    def db_desconect(self):
        self.conexao.close()

    def criar_tabela(self):
        self.db_conect()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes26 (
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

    def inserir_dados(self):
        #self.atualizar_sistema()
        # obter dados dos campos
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
            self.cursor.execute("""INSERT INTO clientes26 (nome,nascimento,civil,religiao,profissao,endereco,cidade,idade,data,observacao,receita) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (self.nome, self.nascimento, self.civil, self.religiao, self.profissao, self.endereco, self.cidade,self.idade,self.data, self.observacao, self.receita))

            self.conexao.commit()
            self.db_desconect()
            self.listar_dados()
            self.limpar_campos()
            self.atualizar_sistema()

    def listar_dados(self):
        self.lista_grid.delete(*self.lista_grid.get_children())
        self.db_conect()
        lista = self.cursor.execute("""SELECT id , nome,nascimento,civil,religiao,profissao,endereco,cidade,idade,data,observacao,receita
         FROM clientes26 ORDER BY nome ASC;""")

        for l in lista:
            self.lista_grid.insert("", END, values=l)
        self.db_desconect()

    def click(self, event):
        self.limpar_campos()
        self.lista_grid.selection()

        for x in self.lista_grid.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12= self.lista_grid.item(x, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_nascimento.insert(END, col3)
            self.entry_civil.insert(END, col4)
            self.entry_religiao.insert(END, col5)
            self.entry_profissao.insert(END, col6)
            self.entry_endereco.insert(END, col7)
            self.entry_cidade.insert(END, col8)
            self.entry_anos.insert(END,col9)
            self.entry_receita.insert(END, col12)
            self.entry_dataConsulta.insert(END, col10)
            self.entry_observacao.insert(END, col11)

    def deletar(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""DELETE FROM clientes26 WHERE id = ?""", self.codigo)
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.listar_dados()

    def atualizar_sistema(self):
        principal()

    def atualizar2(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE clientes26 SET receita = ? 
           WHERE id = ?;
           """, (self.receita, self.codigo))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()

    def atualizar(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE clientes26 SET nome = ?, nascimento = ?, civil = ?, religiao = ?, profissao = ?, endereco = ?, cidade = ?, data = ?, observacao = ?, receita = ?
        WHERE id = ?;
        """, (self.nome, self.nascimento, self.civil, self.religiao, self.profissao, self.endereco, self.cidade, self.data, self.observacao, self.receita, self.codigo))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()

    def pesquisar(self):
        self.db_conect()
        self.lista_grid.delete(*self.lista_grid.get_children())

        self.entry_nome.insert(END, '%')
        nome = '%' + self.entry_nome.get()

        self.cursor.execute("""SELECT * FROM clientes26  WHERE Nome LIKE "%s" COLLATE NOCASE ORDER BY Nome ASC""" % nome)
        Resultado_busca = self.cursor.fetchall()

        for cliente in Resultado_busca:
            self.lista_grid.insert("", END, values=cliente)
        self.db_desconect()
        self.limpar_campos()
        self.db_desconect()

############################################################################
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
        self.root.geometry("1332x666+20+1")
        self.root.resizable(1, 1)
        self.root.maxsize(1370, 749)
        self.root.minsize(120, 1)

########################################### TEMPORIZADOR  em TESTE #################################################################
        '''temporizador = '15/03'

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
            messagebox.showinfo("Cadastro de Pacientes", msg)
            self.frames()'''
###########################################################################################################################

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#54bac2")
        self.frame1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.86)

        self.frame2 = Frame(self.root, bd=4, bg="#fff")
        self.frame2.place(relx=0.02, rely=0.65, relwidth=0.96, relheight=0.265)

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
        self.bt_limpar = Button(self.root, text="LIMPAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.limpar_campos)
        self.bt_limpar.place(relx=0.05, rely=0.925, relwidth=0.10, relheight=0.07)

    # botão PESQUISAR
        self.bt_buscar = Button(self.root, text="PESQUISAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.pesquisar)
        self.bt_buscar.place(relx=0.255, rely=0.925, relwidth=0.10, relheight=0.07)

    # botão cadastrar
        self.bt_novo = Button(self.root, text="CADASTRAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.inserir_dados)
        self.bt_novo.place(relx=0.455, rely=0.925, relwidth=0.10, relheight=0.07)

    # botão alterar
        self.bt_alterar = Button(self.root, text="ALTERAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.atualizar)
        self.bt_alterar.place(relx=0.655, rely=0.925, relwidth=0.1, relheight=0.07)

    # botão ConsultarE
        self.bt_consultar = Button(self.root, text="CONSULTAR",  bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command='')#self.tela_consultar)
        self.bt_consultar.place(relx=0.855, rely=0.925, relwidth=0.1, relheight=0.07)

    # label e entry codigo
        self.lb_codigo = Label(self.frame1, text="Id:", bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_codigo.place(x=153, y=46)

        self.entry_codigo = Entry(self.frame1, bg=self.et_bg, fg=self.et_fg_branco, font=self.et_font)
        self.entry_codigo.place(x=187, y=48, width=40, height=27)

    # Nome CADASTRO tela principal
        self.lb_cadastro = Label(self.frame1, text="C A D A S T R O", bg=self.lb_bg, fg=self.lb_fg, font=('arial black', 40, 'bold'))
        self.lb_cadastro.place(x=450, y=0)

    # label e entry Nome
        self.lb_nome = Label(self.frame1, text="Nome Completo:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_nome.place(x=20, y=85)

        self.entry_nome = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=self.et_font)
        self.entry_nome.place(x=185, y=85, width=450, height=30)

    # label e entry Nascimento
        self.lb_nascimento = Label(self.frame1, text="Nascimento:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_nascimento.place(x=670, y=280)

        self.entry_nascimento = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=self.et_font)
        self.entry_nascimento.place(x=815, y=285, width=124, height=25)

    # label e entry Estado Civil
        self.lb_civil = Label(self.frame1, text="Estado Civil:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_civil.place(x=57, y=155)

        self.entry_civil = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=self.et_font)
        self.entry_civil.place(x=185, y=155, width=450, height=30)

    # label e entry Religião
        self.lb_religiao = Label(self.frame1, text="Religião:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_religiao.place(x=93, y=225)

        self.entry_religiao = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font=self.et_font)
        self.entry_religiao.place(x=185, y=225, width=450, height=30)

    # label e entry Data Consulta
        self.lb_dataConsulta = Label(self.frame1, text='Dt. Consulta:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)#, relief=RAISED)
        self.lb_dataConsulta.place(x=54, y=280, width=125)

        self.entry_dataConsulta = Entry(self.frame1, bg=self.et_bg, fg=self.lb_fg, font= self.lb_font)#, relief=FLAT)
        self.entry_dataConsulta.place(x=188, y=283, height=30, width=110)

    # label e entry Profissão
        self.lb_profissao = Label(self.frame1, text="Profissão:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_profissao.place(x=690, y=85)

        self.entry_profissao = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font= self.lb_font)
        self.entry_profissao.place(x=800, y=85, width=450, height=30)

    # label e entry Endereço
        self.lb_endereco = Label(self.frame1, text="Endereço.:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_endereco.place(x=685, y=155)

        self.entry_endereco = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font= self.lb_font)
        self.entry_endereco.place(x=800, y=155, width=450, height=30)

    # label e entry Cidade
        self.lb_cidade = Label(self.frame1, text="Cidade/UF:", bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lb_cidade.place(x=685, y=225)

        self.entry_cidade = Entry(self.frame1, bg=self.et_bg_branco, fg=self.et_fg_preto, font= self.lb_font)
        self.entry_cidade.place(x=800, y=225, width=450, height=30)

    # label e text Observação
        self.lb_observacao = Label(self.frame1, text="Obs.:", bg=self.lb_bg, fg=self.lb_fg, font=('verdana', 20, 'bold'))
        self.lb_observacao.place(x=1, y=325, relwidth=0.10)

        self.entry_observacao = Text(self.frame1, bg=self.et_bg, fg=self.et_fg_preto, font= self.lb_font)
        self.entry_observacao.place(x=23, y=360, height=60, width=727)

    # label e text Receita
        self.lb_receita = Label(self.frame1, text="Visualizar Receita:", bg=self.lb_bg, fg=self.lb_fg, font=('verdana', 20, 'bold'))
        self.lb_receita.place(x=750, y=335, relwidth=0.40)

        self.entry_receita = Text(self.frame1, bg=self.et_bg, fg=self.et_fg_preto, font= self.lb_font)
        self.entry_receita.place(x=810, y=370, height=50, width=450)

    # data local
        locale.setlocale(locale.LC_ALL, 'pt_BR')

        self.dia_atual = (datetime.today().strftime('Goiânia, %d de %B de %Y'))
        self.hj = Label(self.root, bg=self.lb_bg, fg=self.lb_fg, text=f'{self.dia_atual}', font=('arial', 10, 'bold'))
        self.hj.place(x=0, y=0, height=51, width=220)

        self.bt_calendario = Button(self.frame1, text="DATA", command=self.mostra_idade) # self.calendario
        self.bt_calendario.place(x=810, y=284, height=30, width=50)

        self.entry_nascimento = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.entry_nascimento.bind("<Return>")
        self.entry_nascimento.place(x=860, y=284, height=27, width=105)

    # label e entry anos
        self.lbl_anos = Label(self.frame1, text = 'anos:', bg=self.lb_bg, fg=self.lb_fg, font= self.lb_font)
        self.lbl_anos.place(x=1005, y=285, height=31, width=100)

        self.entry_anos = Entry(self.root, bg=self.et_bg, fg='red', font= self.lb_font, relief=FLAT)
        self.entry_anos.place(x=998, y=291, height=27, width=30)

########################### EM TESTE ################################################################################################
    '''def data_consultas(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        self.dia_atual = (datetime.today().strftime('%d/%m/%Y'))

        self.entry_dataConsulta = Entry(self.frame1, text=self.dia_atual,  bg="#54bac2", fg="#ffffff", font=('arial', 15, 'bold'))
        self.entry_dataConsulta.place(x=200, y=285, height=30, width=130)
    def data_consulta(self):

       # self.limpar_campos()

        locale.setlocale(locale.LC_ALL, 'pt_BR')

        self.dia_atual = (datetime.today().strftime('%d/%m/%Y'))

        self.entry_dataConsulta = Entry(self.frame1, text=self.dia_atual, bg="#54bac2", fg="#ffffff",  font=('arial', 15, 'bold'), relief=FLAT)
        self.entry_dataConsulta.place(x=180, y=283, height=30, width=110)
        self.entry_dataConsulta.insert(0, self.dia_atual)'''

    #def calendario(self):
        #self.calendario1 = Calendar(self.root, fg='gray75', bg='blue', font=('arial', '9', 'bold'), locale='pt_br')
        #self.calendario1.place(x=1010, y=300)

        #self.calData = Button(self.root, text=' INSERIR', font=('arial', '8', 'bold'), command=self.mostra_idade)
        #self.calData.place(x=810, y=307, height=30, width=50)
##################################################################################################################################################

    def mostra_idade(self):
        #dataNascimento = self.calendario1.get_date()
        dataNasc = self.entry_nascimento.get()

        a = (datetime.strptime(dataNasc, '%d/%m/%Y').date())
        b = (datetime.today().strftime('%Y-%m-%d'))
        c = (datetime.strptime(b, '%Y-%m-%d').date())

        self.idade = int((c - a).days / 365.25)

        #self.calendario1.destroy()
        self.entry_anos.delete(0, END)
        self.entry_nascimento.delete(0, END)
        self.entry_nascimento.insert(END, dataNasc)

    # Mostra a palavra 'anos:' após apertar o botão 'DATA'
        self.data = Label(self.root)
        self.data.place(x=1009, y=289, height=31, width=100)
        self.data.configure(bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.data.configure(text='anos:')

        self.entry_idade = Label(self.root, bg=self.lb_bg, fg="red", text=f'{self.idade}', font=self.lb_font)
        self.entry_idade.place(x=985, y=287, height=31, width=33)

    def grid_cliente(self):
        self.lista_grid = ttk.Treeview(self.frame2, height=120, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12'))
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
        self.lista_grid.heading("#10", text='DATA CONSULTA\n')
        self.lista_grid.heading("#11", text='OBSERVAÇÃO\n')
        self.lista_grid.heading("#12", text='RECEITA\n')

        self.lista_grid.column("#0", width=0)
        self.lista_grid.column("#1", width=55)
        self.lista_grid.column("#2", width=80)
        self.lista_grid.column("#3", width=85)
        self.lista_grid.column("#4", width=70)
        self.lista_grid.column("#5", width=80)
        self.lista_grid.column("#6", width=80)
        self.lista_grid.column("#7", width=110)
        self.lista_grid.column("#8", width=70)
        self.lista_grid.column('#9', width=60)
        self.lista_grid.column('#10', width=120)
        self.lista_grid.column('#11', width=100, minwidth=50)
        self.lista_grid.place(x=1, rely=0.1, relwidth=0.99, relheight=0.86)

        #self.scrol_lista = Scrollbar(self.frame2, orient='vertical')
        #self.lista_grid.configure(yscroll=self.scrol_lista.set)
        #self.scrol_lista.place(relx=0.984, rely=0.009, relwidth=0.02, relheight=100)
        self.lista_grid.bind("<Double-1>", self.click)

########################################################
    def tela_consultar(self):
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

        filemenu2.add_command(label="Atualizar Sistema", command=self.atualizar_sistema)
        filemenu2.add_command(label="Deletar Paciente", foreground="red", command=self.deletar)
        filemenu2.add_command(label="Sair do Sistema", command=self.sair)

        def Quit():
            self.root.destroy()

principal()