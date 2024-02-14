# Importação do tkinter
import tkinter as tk

# Cores usadas na janela
cor0 = "#f0f3f5"# Branco
cor1 = "#323233"# Preto
cor2 = "#42426F"# Roxo
cor3 = "#3d3b3b"# Cinza

janela = tk.Tk() # Incio da janela
janela.title("Login")# Cria uma janela
janela.geometry("800x400")# Tamanho da tela
janela.resizable(width=False, height=False)# Impossivel mudar tamanho da tela
janela.configure(background=cor2) # Definindo cor do fundo

tmp = 12 # Tamanho Padrão da fonte
contador = 0 # Contador de usuarios
usuarios_registrados = {}

def mostrar_login(): # Função para mostrar apenas o Login e esquecer o Registro
    frame_login.pack() # Iniciar o Frame do Login
    frame_registro.pack_forget() # Esquecer o Frame do Registro

def mostrar_registro(): # Função para mostrar apenas o Registro e esquecer o Login
    frame_login.pack_forget() # Esquecer o Frame do Login
    frame_registro.pack() # Iniciar o Frame do Registro

def fazer_login(): # Função para o botão ir para o proximo Frame
    pass

def fazer_registro(): # Função para o botão ir para o proximo Frame
    pass

def completar_registro(): # Função para criar o registro

    global contador
    nome = nome_entry.get()
    sobrenome = sobrenome_entry.get()
    email = email_entry.get()
    senha = senhar_entry.get()
    
    contador += 1
    
    usuarios_registrados[contador] = {"nome": nome, "senha": senha}
    
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"ID: {contador}\n")
        arquivo.write(f"Nome:{nome} ")
        arquivo.write(f"Sobrenome:{sobrenome}\n")
        arquivo.write(f"email:{email}\n")
        arquivo.write(f"Senha:{senha}\n")
        arquivo.write("\n") 
    
    nome_entry.delete(0, 'end')
    sobrenome_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    senhar_entry.delete(0,'end')

def verificar_login(): # Teste com a verificação de Login
    login = login_entry.get()
    senha = senha_entry.get()

    # Verifique as respostas
    for id, usuario in usuarios_registrados.items():
        if usuario["nome"] == login and usuario["senha"] == senha:
            resultado_label.config(text="Login bem-sucedido!")
            return

    # Se não encontrar o usuário ou a senha estiver incorreta
    resultado_label.config(text="Usuário ou senha incorretos")

    # Limpa os campos de entrada após o login
    login_entry.delete(0, "end")
    login_entry.delete(0, "end")

frame_login = tk.Frame(janela, background=cor2)
frame_registro = tk.Frame(janela, background=cor2)

#login -----------------------------------------------------

espaço = tk.Label(frame_login, text="", background=cor2)
espaço.pack()
espaço = tk.Label(frame_login, text="Mavs", background=cor2, font=("Helvetica", 15))
espaço.pack()
espaço = tk.Label(frame_login, text="", background=cor2)
espaço.pack()

login_label = tk.Label(frame_login, text="Login", background=cor2, font=("Helvetica", tmp))
login_label.pack()
login_entry = tk.Entry(frame_login, width=30, background= cor1,font=("Helvetica", tmp))
login_entry.pack()  

senha_label = tk.Label(frame_login, text="Senha", background=cor2, font=("Helvetica", tmp))
senha_label.pack()
senha_entry = tk.Entry(frame_login, width=30, show="*", background= cor1,font=("Helvetica", tmp))
senha_entry.pack()

logar_button = tk.Button(frame_login, text="Logar", background=cor3, command= verificar_login,font=("Helvetica", tmp) )
logar_button.pack()

resultado_label = tk.Label(frame_login, text="", background= cor2,font=("Helvetica", tmp))
resultado_label.pack()

#registro ------------------------------------

espaço = tk.Label(frame_registro, text="", background=cor2)
espaço.pack()
espaço = tk.Label(frame_registro, text="Mavs", background=cor2,  font=("Helvetica", 15))
espaço.pack()
espaço = tk.Label(frame_registro, text="", background=cor2)
espaço.pack()

nome_label = tk.Label(frame_registro, text="Nome", background= cor2, font=("Helvetica", tmp))
nome_label.pack()
nome_entry = tk.Entry(frame_registro, width=30, background=cor1,font=("Helvetica", tmp))
nome_entry.pack()

sobrenome_label = tk.Label(frame_registro, text="Sobrenome", background= cor2, font=("Helvetica", tmp))
sobrenome_label.pack()
sobrenome_entry = tk.Entry(frame_registro, width=30, background=cor1,font=("Helvetica", tmp))
sobrenome_entry.pack()

email_label = tk.Label(frame_registro, text="Email", background= cor2, font=("Helvetica", tmp))
email_label.pack()
email_entry = tk.Entry(frame_registro, width=30, background=cor1, font=("Helvetica", tmp))
email_entry.pack()

senhar_label = tk.Label(frame_registro, text="Senha", background= cor2, font=("Helvetica", tmp))
senhar_label.pack()
senhar_entry = tk.Entry(frame_registro, width=30, background=cor1,font=("Helvetica", tmp))
senhar_entry.pack()

registrar_button = tk.Button(frame_registro, text= "Registrar", background= cor3, command= completar_registro, font=("Helvetica", tmp))
registrar_button.pack()

# Botões para mudar de tela
botao_mostrar_login = tk.Button(frame_registro, text="Fazer login", command=mostrar_login, background=cor3,font=("Helvetica", tmp))
botao_mostrar_registro = tk.Button(frame_login, text="Fazer registro", command=mostrar_registro, background=cor3,font=("Helvetica", tmp))

botao_mostrar_login.pack()
botao_mostrar_registro.pack()
# Inicia a janela principal
mostrar_login()
janela.mainloop()