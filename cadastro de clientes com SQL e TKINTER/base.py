import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd 
import sqlite3


def cadastrar_cliente():
    conexao = sqlite3.connect('client.db')
    c = conexao.cursor()
    conexao.execute(' INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)',
                    {
                        'nome': entry_nome.get(),
                        'sobrenome' : entry_sobrenome.get(),
                        'email' : entry_email.get(),
                        'telefone' : entry_telefone.get()
                    }
                    )
    conexao.commit()
    conexao.close()

def exportar_clientes():
    conexao = sqlite3.connect('client.db')
    
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM clientes ")
    clientes_cadastrados = c.fetchall()
    print(clientes_cadastrados)
    conexao.commit()

    conexao.close()
    

janela = tk.Tk()
janela.title('cadastro de clientes')

label_nome = tk.Label(janela, text='nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)


#entrys:

entry_nome = tk.Entry(janela, text='nome')
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='sobrenome')
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='email')
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='telefone')
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

#botoes:

botao_cadastrar = tk.Button(janela, text='cadastrar cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=1, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar= tk.Button(janela, text='exportar clientes', command=exportar_clientes)
botao_exportar.grid(row=5, column=1, padx=10, pady=10, columnspan=2, ipadx=80)



janela.mainloop()

