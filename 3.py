import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

class CadastroFazendasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Fazendas")

        self.label_nome = tk.Label(root, text="Nome da Fazenda:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)

        self.label_tamanho = tk.Label(root, text="Tamanho da Fazenda:")
        self.label_tamanho.grid(row=1, column=0)
        self.entry_tamanho = tk.Entry(root)
        self.entry_tamanho.grid(row=1, column=1)

        self.label_localizacao = tk.Label(root, text="Localização da Fazenda:")
        self.label_localizacao.grid(row=2, column=0)
        self.entry_localizacao = tk.Entry(root)
        self.entry_localizacao.grid(row=2, column=1)

        self.button_cadastrar = tk.Button(root, text="Cadastrar Fazenda", command=self.cadastrar_fazenda)
        self.button_cadastrar.grid(row=3, columnspan=2)

    def cadastrar_fazenda(self):
        nome = self.entry_nome.get()
        tamanho = self.entry_tamanho.get()
        localizacao = self.entry_localizacao.get()

        if nome == "" or tamanho == "" or localizacao == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        fazenda = {
            "nome": nome,
            "tamanho": tamanho,
            "localizacao": localizacao
        }

#respostas da prova de tecnicas de programção 



        # Conectando ao MongoDB
        client = MongoClient('localhost', 27017)
        db = client['agro_db']
        fazendas = db['fazendas']

        # Inserindo a fazenda no banco de dados
        fazendas.insert_one(fazenda)

        messagebox.showinfo("Sucesso", "Fazenda cadastrada com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroFazendasApp(root)
    root.mainloop()
