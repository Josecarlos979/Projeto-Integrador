from tkinter import Label, Entry, Button, Listbox, END, messagebox, Toplevel
from controllers.funcionario_controller import (
    cadastrar_funcionario,
    listar_funcionarios,
)

class FuncionarioView:
    def __init__(self, master: Toplevel):
        self.root = master
        self.root.title("Cadastro de Funcionários")

        # --- Formulário ---
        Label(self.root, text="Nome:").grid(row=0, column=0)
        self.nome_entry = Entry(self.root); self.nome_entry.grid(row=0, column=1)

        Label(self.root, text="Email:").grid(row=1, column=0)
        self.email_entry = Entry(self.root); self.email_entry.grid(row=1, column=1)

        Label(self.root, text="Cargo:").grid(row=2, column=0)
        self.cargo_entry = Entry(self.root); self.cargo_entry.grid(row=2, column=1)

        Button(self.root, text="Cadastrar", command=self.cadastrar)\
            .grid(row=3, column=0, columnspan=2, pady=4)

        # --- Lista ---
        self.lista = Listbox(self.root, width=50)
        self.lista.grid(row=4, column=0, columnspan=2, pady=4)
        self.atualizar_lista()

    def cadastrar(self):
        try:
            cadastrar_funcionario(
                self.nome_entry.get(),
                self.email_entry.get(),
                self.cargo_entry.get()
            )
            messagebox.showinfo("Sucesso", "Funcionário cadastrado.")
            for e in (self.nome_entry, self.email_entry, self.cargo_entry):
                e.delete(0, END)
            self.atualizar_lista()
        except ValueError as err:
            messagebox.showerror("Erro", str(err))

    def atualizar_lista(self):
        self.lista.delete(0, END)
        for fun in listar_funcionarios():
            self.lista.insert(
                END,
                f"{fun.id} - {fun.nome} ({fun.cargo})"
            )
