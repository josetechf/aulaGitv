import tkinter as tk
from tkinter import ttk


class JanelaBonitaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Minha Janela Bonita")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f8ff")  # Fundo azul claro

        # Label de título
        self.label_titulo = ttk.Label(
            self.master, text="Bem-vindo!", font=("Helvetica", 18, "bold")
        )
        self.label_titulo.pack(pady=10)

        # Campo de entrada
        self.label_nome = ttk.Label(self.master, text="Digite seu nome:")
        self.label_nome.pack(pady=5)
        self.campo_nome = ttk.Entry(self.master, font=("Helvetica", 12))
        self.campo_nome.pack(pady=5)

        # Botão
        self.botao_exibir = ttk.Button(
            self.master, text="Exibir Mensagem", command=self.exibir_mensagem
        )
        self.botao_exibir.pack(pady=10)

        # Label para exibir mensagens dinâmicas
        self.label_mensagem = ttk.Label(
            self.master, text="", font=("Helvetica", 14), foreground="green"
        )
        self.label_mensagem.pack(pady=10)

        # Botão de saída
        self.botao_sair = ttk.Button(
            self.master, text="Sair", command=self.master.quit
        )
        self.botao_sair.pack(pady=20)

    def exibir_mensagem(self):
        nome = self.campo_nome.get()
        if nome.strip():
            self.label_mensagem.config(
                text=f"Olá, {nome}! Espero que tenha um ótimo dia!"
            )
        else:
            self.label_mensagem.config(text="Por favor, insira seu nome.")


if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaBonitaApp(root)
    root.mainloop()
