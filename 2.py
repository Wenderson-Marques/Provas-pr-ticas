import tkinter as tk
from pymongo import MongoClient

def inserir_dados():
    nome = entry_nome.get()
    idade = int(entry_idade.get())

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    # Conectando ao MongoDB
    client = MongoClient('localhost', 27017)
    db = client['agro_db']
    pessoas = db['pessoas']

    # Inserindo a pessoa no banco de dados
    pessoas.insert_one(pessoa)

    label_status['text'] = "Dados inseridos com sucesso!"

# Interface
root = tk.Tk()
root.title("Inserção de Dados no MongoDB")

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1)

button_inserir = tk.Button(root, text="Inserir Dados", command=inserir_dados)
button_inserir.grid(row=2, columnspan=2)

label_status = tk.Label(root, text="")
label_status.grid(row=3, columnspan=2)

root.mainloop()
