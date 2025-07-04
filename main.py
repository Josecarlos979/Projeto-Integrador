from tkinter import Tk, Button, Toplevel
from views.cliente_view import ClienteView
from views.funcionario_view import FuncionarioView
from views.evento_view import EventoView
from views.agendamento_view import AgendamentoView

def abrir_janela(classe_view):
    topo = Toplevel(root)
    classe_view(topo)

root = Tk()
root.title("Sistema de Gestão")

Button(root, text="Clientes",     width=20, command=lambda: abrir_janela(ClienteView)).pack(pady=4)
Button(root, text="Funcionários", width=20, command=lambda: abrir_janela(FuncionarioView)).pack(pady=4)
Button(root, text="Eventos",      width=20, command=lambda: abrir_janela(EventoView)).pack(pady=4)
Button(root, text="Agendamentos", width=20, command=lambda: abrir_janela(AgendamentoView)).pack(pady=4)

root.mainloop()
