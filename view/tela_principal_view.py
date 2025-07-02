import tkinter as tk
from tkinter import ttk

class TelaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Restaurante")
        self.root.attributes('-fullscreen', True)

        self.frame = ttk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        titulo = ttk.Label(self.frame, text="Sistema de Restaurante", font=("Helvetica", 24, "bold"))
        titulo.pack(pady=20)

        botoes = [
            ("Cardápio", self.abrir_cardapio),
            ("Clientes", self.abrir_clientes),
            ("Funcionários", self.abrir_funcionarios),
            ("Mesas", self.abrir_mesas),
            ("Eventos", self.abrir_eventos),
            ("Sair", self.sair)
        ]

        for texto, comando in botoes:
            btn = ttk.Button(self.frame, text=texto, command=comando, width=30)
            btn.pack(pady=10)

        self.root.bind("<Escape>", lambda e: self.sair()) 

    def abrir_cardapio(self):
        import view.cardapio_view as cardapio
        self.root.destroy()
        cardapio.CardapioView()

    def abrir_clientes(self):
        pass 

    def abrir_funcionarios(self):
        pass 

    def abrir_mesas(self):
        pass 

    def abrir_eventos(self):
        pass  

    def sair(self):
        self.root.destroy()

    def executar(self):
        self.root.mainloop()
