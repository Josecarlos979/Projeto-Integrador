import tkinter as tk
from tkinter import ttk, messagebox
from controller.cardapio_controller import cadastrar_item
from view.tela_principal_view import TelaPrincipal

class CardapioView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Cardápio")
        self.root.attributes('-fullscreen', True)

        self.frame = ttk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        titulo = ttk.Label(self.frame, text="Cadastrar Item no Cardápio", font=("Helvetica", 20, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada
        ttk.Label(self.frame, text="Nome do Item:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.nome_entry = ttk.Entry(self.frame, width=40)
        self.nome_entry.grid(row=1, column=1)

        ttk.Label(self.frame, text="Descrição:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.frame, width=40)
        self.desc_entry.grid(row=2, column=1)

        # Botões
        ttk.Button(self.frame, text="Salvar", command=self.salvar_cardapio, width=20).grid(row=3, column=0, pady=20)
        ttk.Button(self.frame, text="Voltar", command=self.voltar_menu, width=20).grid(row=3, column=1, pady=20)

        self.root.bind("<Escape>", lambda e: self.voltar_menu())

        self.root.mainloop()

    def salvar_cardapio(self):
        nome = self.nome_entry.get().strip()
        descricao = self.desc_entry.get().strip()

        try:
            cadastrar_item(nome, descricao)
            messagebox.showinfo("Sucesso", "Item cadastrado com sucesso!")
            self.limpar_campos()
        except ValueError as ve:
            messagebox.showwarning("Atenção", str(ve))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def voltar_menu(self):
        self.root.destroy()
        TelaPrincipal().executar()
