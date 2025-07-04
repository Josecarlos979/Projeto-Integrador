from tkinter import Label, Entry, Button, messagebox, Listbox, END, Toplevel
from tkinter.ttk import Combobox
from controllers.agendamento_controller import agendar_evento, listar_agendamentos
from controllers.cliente_controller import listar_clientes
from controllers.funcionario_controller import listar_funcionarios
from controllers.evento_controller import listar_eventos

class AgendamentoView:
    def __init__(self, master: Toplevel):
        self.root = master
        self.root.title("Agendamento de Eventos")

        # --- Comboboxes com registros existentes ---
        Label(self.root, text="Evento:").grid(row=0, column=0, sticky="e")
        self.evento_cb = Combobox(self.root, state="readonly", width=30)
        self.evento_cb.grid(row=0, column=1)

        Label(self.root, text="Cliente:").grid(row=1, column=0, sticky="e")
        self.cliente_cb = Combobox(self.root, state="readonly", width=30)
        self.cliente_cb.grid(row=1, column=1)

        Label(self.root, text="Funcionário:").grid(row=2, column=0, sticky="e")
        self.func_cb = Combobox(self.root, state="readonly", width=30)
        self.func_cb.grid(row=2, column=1)

        Label(self.root, text="Data/Hora (YYYY-MM-DD HH:MM:SS):").grid(row=3, column=0)
        self.datahora_entry = Entry(self.root, width=30)
        self.datahora_entry.grid(row=3, column=1)

        Button(self.root, text="Agendar", command=self.cadastrar)\
            .grid(row=4, column=0, columnspan=2, pady=4)

        # --- Lista ---
        self.lista = Listbox(self.root, width=65)
        self.lista.grid(row=5, column=0, columnspan=2, pady=4)

        self.carregar_opcoes()
        self.atualizar_lista()

    # Carrega nomes + IDs na Combobox
    def carregar_opcoes(self):
        self.eventos = listar_eventos()          # guarda lista de objetos
        self.clientes = listar_clientes()
        self.funcionarios = listar_funcionarios()

        self.evento_cb["values"] = [
            f"{e.id} - {e.titulo}" for e in self.eventos
        ]
        self.cliente_cb["values"] = [
            f"{c.id} - {c.nome}" for c in self.clientes
        ]
        self.func_cb["values"] = [
            f"{f.id} - {f.nome}" for f in self.funcionarios
        ]

    def cadastrar(self):
        try:
            id_evento = self.eventos[self.evento_cb.current()].id
            id_cliente = self.clientes[self.cliente_cb.current()].id
            id_func = self.funcionarios[self.func_cb.current()].id
            data_hora = self.datahora_entry.get()

            agendar_evento(id_evento, id_cliente, id_func, data_hora)
            messagebox.showinfo("Sucesso", "Evento agendado.")
            self.datahora_entry.delete(0, END)
            self.atualizar_lista()
        except (IndexError, ValueError) as err:
            messagebox.showerror("Erro", f"Dados inválidos: {err}")

    def atualizar_lista(self):
        self.lista.delete(0, END)
        for ag in listar_agendamentos():
            self.lista.insert(
                END,
                f"{ag.id} | Evento:{ag.id_evento} | Cliente:{ag.id_cliente} "
                f"| Funcionário:{ag.id_funcionario} | {ag.data_hora}"
            )
