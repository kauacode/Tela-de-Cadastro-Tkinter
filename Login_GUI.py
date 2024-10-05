from tkinter import *
import customtkinter as ctk
from PIL import Image

# Cores usadas na janela
cor0 = "#f0f3f5"  # Branco
cor1 = "#323233"  # Preto
cor2 = "#323233"  # Roxo
cor3 = "#3d3b3b"  # Cinza
corButton = "#BD632F"  # Laranja
corSucesso = "#28a745"  # Verde
corErro = "#dc3545"  # Vermelho

# Inicialização de tema
tema_claro = True  # Inicia no tema claro

# Carregar as imagens para o botão de alternar tema
light_mode_image = ctk.CTkImage(light_image=Image.open('./assets/images/light_mode.png'), size=(30, 30))  # Ícone para modo claro
dark_mode_image = ctk.CTkImage(light_image=Image.open('./assets/images/dark_mode.png'), size=(30, 30))  # Ícone para modo escuro

# Dicionário de imagens dos times
time_images = {
    "Lakers": './assets/images/lakers.png',
    "GSW": './assets/images/gsw.png',
    "Miami Heat": './assets/images/miami_heat.png',
    "Spurs": './assets/images/spurs.png',
    "MAVS": './assets/images/mavs.png',
    "Chicago Bulls": './assets/images/chicago_bulls.png'
}

# Função para alternar temas
def alternar_tema():
    global tema_claro

    if tema_claro:
        # Muda para tema escuro
        ctk.set_appearance_mode("dark")
        tema_button.configure(image=light_mode_image)  # Troca para a imagem do modo claro
        tema_claro = False
    else:
        # Muda para tema claro
        ctk.set_appearance_mode("light")
        tema_button.configure(image=dark_mode_image)  # Troca para a imagem do modo escuro
        tema_claro = True

# Início da janela
janela = ctk.CTk()
janela.title("Login")  # Cria uma janela
janela.geometry("1000x750")  # Tamanho da tela
janela.resizable(width=False, height=False)  # Impossível mudar tamanho da tela

# Inicializando frames antes de usá-los
frame_login = ctk.CTkFrame(janela)
frame_registro = ctk.CTkFrame(janela)
frame_usuario = ctk.CTkFrame(janela)  # Novo frame para exibir informações do usuário

tmp = 12  # Tamanho Padrão da fonte
contador = 0  # Contador de usuários
usuarios_registrados = {}

# Funções de navegação entre telas
def mostrar_login():  # Função para mostrar apenas o Login e esquecer o Registro
    frame_login.pack(fill='both', expand=True)  # Iniciar o Frame do Login
    frame_registro.pack_forget()  # Esquecer o Frame do Registro
    frame_usuario.pack_forget()  # Esquecer o Frame de usuário

def mostrar_registro():  # Função para mostrar apenas o Registro e esquecer o Login
    frame_login.pack_forget()  # Esquecer o Frame do Login
    frame_registro.pack(fill='both', expand=True)  # Iniciar o Frame do Registro

# Função para mostrar a tela de usuário logado com a imagem personalizada
def mostrar_usuario_logado(nome, sobrenome, time_favorito):  # Função para mostrar a tela de usuário logado
    frame_login.pack_forget()
    frame_registro.pack_forget()

    # Mostrar frame com dados do usuário
    frame_usuario.pack(fill="both", expand=True)

    # Limpa os widgets existentes se houver
    for widget in frame_usuario.winfo_children():
        widget.destroy()

    usuario_label = ctk.CTkLabel(frame_usuario, text="Informações do Usuário", font=("MS Sans Serif", 44, "bold"))
    usuario_label.pack(pady=20)

    # Criar uma caixa para os dados
    user_data_frame = ctk.CTkFrame(frame_usuario, corner_radius=10, width=400, height=200)
    user_data_frame.pack(pady=20)

    nome_label = ctk.CTkLabel(user_data_frame, text=f"Nome: {nome}", font=("Ubuntu", 20, "bold"))
    nome_label.pack(pady=10)

    sobrenome_label = ctk.CTkLabel(user_data_frame, text=f"Sobrenome: {sobrenome}", font=("Ubuntu", 20, "bold"))
    sobrenome_label.pack(pady=10)

    time_favorito_label = ctk.CTkLabel(user_data_frame, text=f"Time Favorito: {time_favorito}", font=("Ubuntu", 20, "bold"))
    time_favorito_label.pack(pady=10)

    # Carregar a imagem do time selecionado
    if time_favorito in time_images:
        team_image_path = time_images[time_favorito]
        show_image = ctk.CTkImage(light_image=Image.open(team_image_path),
                                  dark_image=Image.open(team_image_path),
                                  size=(400, 200))

        image_label = ctk.CTkLabel(frame_usuario, image=show_image, text="")
        image_label.pack(pady=20)

    # Botão para voltar ao login
    voltar_button = ctk.CTkButton(frame_usuario, text="Voltar ao Login", fg_color=corButton, command=mostrar_login, font=("Ubuntu", 20, "bold"))
    voltar_button.pack(pady=(20, 0))  # Adiciona espaçamento superior e inferior

def completar_registro():  # Função para criar o registro
    global contador
    nome = nome_entry.get()
    sobrenome = sobrenome_entry.get()
    email = email_entry.get()
    senha = senhar_entry.get()
    time_favorito = nba_combo.get()
    
    contador += 1
    
    usuarios_registrados[contador] = {"nome": nome, "sobrenome": sobrenome, "email": email, "senha": senha, "time_favorito": time_favorito}
    
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"ID: {contador}\n")
        arquivo.write(f"Nome: {nome} ")
        arquivo.write(f"Sobrenome: {sobrenome}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write(f"Senha: {senha}\n")
        arquivo.write(f"Time Favorito: {time_favorito}\n")
        arquivo.write("\n") 
    
    nome_entry.delete(0, 'end')
    sobrenome_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    senhar_entry.delete(0,'end')

def verificar_login():  # Teste com a verificação de Login
    login = login_entry.get()
    senha = senha_entry.get()

    # Verifique as respostas
    for id, usuario in usuarios_registrados.items():
        if usuario["nome"] == login and usuario["senha"] == senha:
            resultado_label.configure(text="Login bem-sucedido!", text_color=corSucesso)

            # Após 1 segundo, redirecionar para a tela do usuário
            janela.after(1000, lambda: mostrar_usuario_logado(usuario["nome"], usuario["sobrenome"], usuario["time_favorito"]))
            return

    # Se não encontrar o usuário ou a senha estiver incorreta
    resultado_label.configure(text="Usuário ou senha incorretos", text_color=corErro)

    # Limpa os campos de entrada após o login
    login_entry.delete(0, "end")
    senha_entry.delete(0, "end")

# Tela de Login -----------------------------------------------------

title_font = ctk.CTkFont(family="MS Sans Serif", size=44, weight="bold")
misc_font = ctk.CTkFont(family="Ubuntu", size=20, weight="bold")

espaço = ctk.CTkLabel(frame_login, text="")
espaço.pack()
espaço = ctk.CTkLabel(frame_login, text="Tela de Login", font=title_font)
espaço.pack()
espaço = ctk.CTkLabel(frame_login, text="")
espaço.pack()

# Criando um frame menor para os campos de login e senha
login_frame = ctk.CTkFrame(frame_login, corner_radius=10, width=400, height=300)
login_frame.pack(pady=20, padx=40)

login_label = ctk.CTkLabel(login_frame, text="Login", font=misc_font)
login_label.pack(pady=(20, 10))  # Adiciona espaçamento superior e inferior
login_entry = ctk.CTkEntry(login_frame, width=280)
login_entry.pack(pady=(0, 10))  # Adiciona espaçamento inferior

senha_label = ctk.CTkLabel(login_frame, text="Senha", font=misc_font)
senha_label.pack(pady=(0, 10))  # Adiciona espaçamento inferior
senha_entry = ctk.CTkEntry(login_frame, width=280, show="*")
senha_entry.pack(pady=(0, 10))  # Adiciona espaçamento inferior

resultado_label = ctk.CTkLabel(login_frame, text="")
resultado_label.pack(pady=10)

login_button = ctk.CTkButton(login_frame, text="Login", fg_color=corButton, command=verificar_login, font=misc_font)
login_button.pack(pady=10)

# Botão para registrar-se
registro_button = ctk.CTkButton(login_frame, text="Registre-se", fg_color=corButton, command=mostrar_registro, font=misc_font)
registro_button.pack(pady=20)


# Tema toggle button
tema_button = ctk.CTkButton(frame_login, text="", image=dark_mode_image, width=30, height=30, fg_color=corButton, command=alternar_tema)
tema_button.place(x=10, y=10)  # Posiciona o botão no canto superior esquerdo


# Tela de Registro -----------------------------------------------------

title_font = ctk.CTkFont(family="MS Sans Serif", size=44, weight="bold")
misc_font = ctk.CTkFont(family="Ubuntu", size=20, weight="bold")

espaço = ctk.CTkLabel(frame_registro, text="")
espaço.pack()
espaço = ctk.CTkLabel(frame_registro, text="Tela de Registro", font=title_font)
espaço.pack()
espaço = ctk.CTkLabel(frame_registro, text="")
espaço.pack()

# Criando um frame menor para os campos de registro
registro_frame = ctk.CTkFrame(frame_registro, corner_radius=10, width=400, height=300)
registro_frame.pack(pady=20, padx=40)

nome_label = ctk.CTkLabel(registro_frame, text="Nome", font=misc_font)
nome_label.pack(pady=(20, 10))
nome_entry = ctk.CTkEntry(registro_frame, width=280)
nome_entry.pack()

sobrenome_label = ctk.CTkLabel(registro_frame, text="Sobrenome", font=misc_font)
sobrenome_label.pack(pady=(10, 10))
sobrenome_entry = ctk.CTkEntry(registro_frame, width=280)
sobrenome_entry.pack()

email_label = ctk.CTkLabel(registro_frame, text="Email", font=misc_font)
email_label.pack(pady=(10, 10))
email_entry = ctk.CTkEntry(registro_frame, width=280)
email_entry.pack()

senhar_label = ctk.CTkLabel(registro_frame, text="Senha", font=misc_font)
senhar_label.pack(pady=(10, 10))
senhar_entry = ctk.CTkEntry(registro_frame, width=280, show="*")
senhar_entry.pack()

# Combobox para o time favorito
nba_combo = ctk.CTkComboBox(registro_frame, values=["Lakers", "GSW", "Miami Heat", "Spurs", "MAVS", "Chicago Bulls"])
nba_combo.pack(pady=(20, 10))

registrar_button = ctk.CTkButton(registro_frame, text="Registrar", fg_color=corButton, command=completar_registro, font=misc_font)
registrar_button.pack(pady=20)

# Botão para voltar ao login
voltar_button = ctk.CTkButton(registro_frame, text="Voltar ao Login", fg_color=corButton, command=mostrar_login, font=misc_font)
voltar_button.pack(pady=20)

mostrar_login()  # Mostrar tela de login inicialmente

janela.mainloop()
