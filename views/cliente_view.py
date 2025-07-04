from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox, Toplevel
from controllers.cliente_controller import cadastrar_cliente, listar_clientes

class ClienteView:
    def __init__(self, master: Toplevel):
        self.root = master
        self.root.title("Cadastro de Clientes")

        # Formulário
        Label(self.root, text="Nome:").grid(row=0, column=0)
        self.nome_entry = Entry(self.root); self.nome_entry.grid(row=0, column=1)

        Label(self.root, text="Email:").grid(row=1, column=0)
        self.email_entry = Entry(self.root); self.email_entry.grid(row=1, column=1)

        Label(self.root, text="Telefone:").grid(row=2, column=0)
        self.tel_entry = Entry(self.root); self.tel_entry.grid(row=2, column=1)

        Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=3, column=0, columnspan=2, pady=4)

        # Lista
        self.lista = Listbox(self.root, width=50); self.lista.grid(row=4, column=0, columnspan=2, pady=4)
        self.atualizar_lista()

    def cadastrar(self):
        try:
            cadastrar_cliente(self.nome_entry.get(), self.email_entry.get(), self.tel_entry.get())
            messagebox.showinfo("Sucesso", "Cliente cadastrado.")
            for e in (self.nome_entry, self.email_entry, self.tel_entry): e.delete(0, END)
            self.atualizar_lista()
        except ValueError as err:
            messagebox.showerror("Erro", str(err))

    def atualizar_lista(self):
        self.lista.delete(0, END)
        for cli in listar_clientes():
            self.lista.insert(END, f"{cli.id} - {cli.nome} ({cli.telefone})")
