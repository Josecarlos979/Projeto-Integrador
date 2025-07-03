import tkinter as tk
from tkinter import ttk, messagebox

# Importa funções de negócio
from controllers.cardapio_controller import cadastrar_item


class CardapioView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Cardápio")
        self.root.attributes("-fullscreen", True)

        # ── Frame central ─────────────────────────────────────────────── #
        self.frame = ttk.Frame(self.root, padding=30)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.frame, text="Cadastrar Item no Cardápio",
                  font=("Helvetica", 22, "bold")).grid(row=0, column=0,
                                                       columnspan=2, pady=20)

        # ── Campos de entrada ────────────────────────────────────────── #
        ttk.Label(self.frame, text="Nome do Item:").grid(row=1, column=0,
                                                         sticky="e", padx=5,
                                                         pady=5)
        self.nome_entry = ttk.Entry(self.frame, width=40)
        self.nome_entry.grid(row=1, column=1)

        ttk.Label(self.frame, text="Descrição:").grid(row=2, column=0,
                                                      sticky="e", padx=5,
                                                      pady=5)
        self.desc_entry = ttk.Entry(self.frame, width=40)
        self.desc_entry.grid(row=2, column=1)

        # ── Botões ───────────────────────────────────────────────────── #
        ttk.Button(self.frame, text="Salvar",
                   command=self.salvar_cardapio, width=18)\
            .grid(row=3, column=0, pady=20)
        ttk.Button(self.frame, text="Fechar",
                   command=self.fechar, width=18)\
            .grid(row=3, column=1, pady=20)

        # Atalho ESC para fechar
        self.root.bind("<Escape>", lambda _: self.fechar())

    # ========== Callbacks ========== #
    def salvar_cardapio(self):
        nome = self.nome_entry.get()
        descricao = self.desc_entry.get()

        try:
            cadastrar_item(nome, descricao)
            messagebox.showinfo("Sucesso", "Item cadastrado com sucesso!")
            self.limpar_campos()
        except ValueError as ve:
            messagebox.showwarning("Atenção", str(ve))
        except Exception as e:
            messagebox.showerror("Erro inesperado",
                                 f"Ocorreu um erro: {e}")

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.nome_entry.focus_set()

    def fechar(self):
        self.root.quit()

    # ========== Execução ========== #
    def start(self):
        self.root.mainloop()


# ---------- Execução direta ---------- #
if __name__ == "__main__":
    CardapioView().start()
