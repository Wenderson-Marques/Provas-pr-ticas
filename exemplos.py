import tkinter as tk
from pymongo import MongoClient

def cadastrar_fazenda():
    nome = entry_nome.get()
    tamanho = entry_tamanho.get()
    localizacao = entry_localizacao.get()

    fazenda = {
        "nome": nome,
        "tamanho": tamanho,
        "localizacao": localizacao
    }

    # Conectando ao MongoDB
    client = MongoClient('localhost', 27017)
    db = client['agro_db']
    fazendas = db['fazendas']

    # Inserindo a fazenda no banco de dados
    fazendas.insert_one(fazenda)

    label_status['text'] = "Fazenda cadastrada com sucesso!"

# Interface
root = tk.Tk()
root.title("Cadastro de Fazendas")

label_nome = tk.Label(root, text="Nome da Fazenda:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_tamanho = tk.Label(root, text="Tamanho da Fazenda:")
label_tamanho.grid(row=1, column=0)
entry_tamanho = tk.Entry(root)
entry_tamanho.grid(row=1, column=1)

label_localizacao = tk.Label(root, text="Localização da Fazenda:")
label_localizacao.grid(row=2, column=0)
entry_localizacao = tk.Entry(root)
entry_localizacao.grid(row=2, column=1)

button_cadastrar = tk.Button(root, text="Cadastrar Fazenda", command=cadastrar_fazenda)
button_cadastrar.grid(row=3, columnspan=2)

label_status = tk.Label(root, text="")
label_status.grid(row=4, columnspan=2)

root.mainloop()
