import customtkinter as ctk

# 1. Configurações de Aparência
ctk.set_appearance_mode("dark")  # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (padrão), "green", "dark-blue"

class MeuApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Meu Primeiro Projeto Moderno")
        self.geometry("400x240")

        # 2. Criando os Widgets (Componentes)
        self.label = ctk.CTkLabel(self, text="Olá! Este é o CustomTkinter", font=("Roboto", 20))
        self.label.pack(pady=20)

        self.botao = ctk.CTkButton(self, text="Clique Aqui", command=self.evento_clique)
        self.botao.pack(pady=10)

    # 3. Lógica do Evento
    def evento_clique(self):
        self.label.configure(text="Botão Pressionado!")
        print("O usuário interagiu com a interface.")

if __name__ == "__main__":
    app = MeuApp()
    app.mainloop() # O "coração" da interface que mantém a janela aberta