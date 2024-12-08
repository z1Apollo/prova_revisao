usuario_correto = "z1Apollo"
senha_correta = "237"
max_tentativas = 3

for tentativa in range(max_tentativas):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ao sistema Infinity School!")
        break 
    else:
        tentativas_restantes = max_tentativas - (tentativa + 1)
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você tem {tentativas_restantes} tentativas restantes.")
        else:
            print("Credenciais incorretas. Você não tem mais tentativas restantes.")
            for _ in range(3):
                print("Acesso bloqueado.")