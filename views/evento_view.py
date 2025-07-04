from tkinter import Label, Entry, Button, Text, Listbox, END, messagebox, Toplevel
from controllers.evento_controller import cadastrar_evento, listar_eventos

class EventoView:
    def __init__(self, master: Toplevel):
        self.root = master
        self.root.title("Cadastro de Eventos")

        # --- Formulário ---
        Label(self.root, text="Título:").grid(row=0, column=0)
        self.titulo_entry = Entry(self.root, width=40)
        self.titulo_entry.grid(row=0, column=1)

        Label(self.root, text="Descrição:").grid(row=1, column=0, sticky="n")
        self.desc_text = Text(self.root, width=30, height=4)
        self.desc_text.grid(row=1, column=1)

        Label(self.root, text="Data (YYYY-MM-DD):").grid(row=2, column=0)
        self.data_entry = Entry(self.root)
        self.data_entry.grid(row=2, column=1)

        Button(self.root, text="Cadastrar", command=self.cadastrar)\
            .grid(row=3, column=0, columnspan=2, pady=4)

        # --- Lista ---
        self.lista = Listbox(self.root, width=50)
        self.lista.grid(row=4, column=0, columnspan=2, pady=4)
        self.atualizar_lista()

    def cadastrar(self):
        try:
            cadastrar_evento(
                self.titulo_entry.get(),
                self.desc_text.get("1.0", END).strip(),
                self.data_entry.get()
            )
            messagebox.showinfo("Sucesso", "Evento cadastrado.")
            for e in (self.titulo_entry, self.data_entry): e.delete(0, END)
            self.desc_text.delete("1.0", END)
            self.atualizar_lista()
        except ValueError as err:
            messagebox.showerror("Erro", str(err))

    def atualizar_lista(self):
        self.lista.delete(0, END)
        for ev in listar_eventos():
            self.lista.insert(
                END,
                f"{ev.id} - {ev.titulo} ({ev.data})"
            )
