import time
import random
import string
import itertools


#joaodark esteve aqui <3
def exibir_banner():
   


    banners = [
        """
        JOAODARK ESTAVA AQUI!!!!!
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀@joaodarkofc
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """,
        """
    Famous error message]

                                           \ / _
                                      ___,,,
                                      \_[o o]
     @joaodarkofc      !              C\  _\/
             /                     _____),_/__
        ________                  /     \/   /
      _|       .|                /      o   /
     | |       .|               /          /
      \|       .|              /          /
       |________|             /_        \/
       __|___|__             _//\        \
 _____|_________|____       \  \ \        \
                    _|       ///  \        \
                   |               \       /
                   |               /      /
                   |              /      /
 ________________  |             /__    /_
 b'ger        ...|_|.............. /______\.......
        """,
        """
      .======================================.
      | ___ ___ ___               _   _   _  |
      | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
      | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
      '===================================== ,sSSSs
                JOAODARKOFC                 SSSS "(
           .:.                              SSS@ =/  \~/
          C|||'                             SSSS_(_  _Y_
        ___|||______________________________SS/ _)_) /.-
       [____________________________________] \   /\//
        |   ____    ____    ____    ____   | \|==(\_/
        |  (____)  (____)  (____)  (____)  | (/   ;
        |  |    |  |    |  |    |  |    |  | |____|
        |  |    |  |    |  |    |  |    |  |  \  |\
        |  |    |  |    |  |    |  |    |  |   ) ) )
        |  |____|  |____|  |____|  |____|  |  (  |/
        |  I====I  I====I  I====I  I====I  |  /\ |
       jgs |    |  |    |  |    |  |    |  | /.(=\
                                               Y\_\
        """
    ]

   
    banner = random.choice(banners)

    


    animacao = itertools.cycle(["|", "/", "-", "\\"])
    intervalo_animacao = 0.01  




   
    for char in banner:
        print(char, end='', flush=True)
        if char in ["=", "\n"]:
            time.sleep(intervalo_animacao)  
        else:
            time.sleep(intervalo_animacao / 2)
    print("\n")
def gerar_senha(tamanho, caracteres):
    return ''.join(random.choice(caracteres) for _ in range(tamanho))


def gerar_wordlist_wifi(nome, sobrenome, data_nascimento, nome_pet):
    wordlist = set()
    base_senhas = [
        nome.lower(),
        sobrenome.lower(),
        nome_pet.lower(),
        data_nascimento,
        f"{nome}{sobrenome}",
        f"{sobrenome}{nome}",
        f"{nome_pet}123",
        f"{data_nascimento[:2]}-{data_nascimento[2:4]}-{data_nascimento[4:]}",  # formato de data
        f"{nome}_wifi",
        f"{sobrenome}_wifi",
    ]
    for senha in base_senhas:
        variacoes = [
            senha,
            f"{senha}!",
            f"{senha}123",
            senha.capitalize(),
            senha.upper(),
        ]
        wordlist.update(variacoes)
    return list(wordlist)
def gerar_wordlist_rede_social(nome_usuario, email, numero_telefone):
    wordlist = set()
    base_senhas = [
        nome_usuario.lower(),
        email.split("@")[0],  
        numero_telefone[-4:],  
        f"{nome_usuario}123",
        f"{email.split('@')[0]}123",
    ]   
    for senha in base_senhas:
        variacoes = [
            senha,
            f"{senha}!",
            f"{senha}123",
            senha.capitalize(),
            senha.upper(),
        ]
        wordlist.update(variacoes)   
    return list(wordlist)
def exibir_menu():
    menu = """
    Escolha uma opção para gerar wordlist ou senha:
    1. Gerar wordlist para Wi-Fi
    2. Gerar wordlist para redes sociais (Instagram, Facebook, Twitter)
    3. Gerar senha apenas com números
    4. Gerar senha com letras e números
    5. Gerar senha complexa (letras, números e caracteres especiais)
    6. Sair
    """
    print(menu)
def gerenciar_menu(opcao):
    if opcao == 1:
        print("Gerar wordlist para Wi-Fi:")
        nome = input("Digite o nome do dono do Wi-Fi: ")
        sobrenome = input("Digite o sobrenome do dono do Wi-Fi: ")
        data_nascimento = input("Digite a data de nascimento (DDMMYYYY): ")
        nome_pet = input("Digite o nome do pet: ")
        wordlist = gerar_wordlist_wifi(nome, sobrenome, data_nascimento, nome_pet)
        print("Wordlist gerada:")
        for senha in wordlist:
            print(senha)
def gerenciar_menu(opcao):
    if opcao == 2:
        print("Gerar wordlist para redes sociais:")
        nome_usuario = input("Digite o nome de usuário: ")
        email = input("Digite o email: ")
        numero_telefone = input("Digite o número de telefone: ")
        wordlist = gerar_wordlist_rede_social(nome_usuario, email, numero_telefone)
        print("Wordlist gerada:")
        
        
        for senha in wordlist:
            print(senha)  

    elif opcao == 1:
        print("Gerar wordlist para Wi-Fi:")
        nome = input("Digite o nome do dono do Wi-Fi: ")
        sobrenome = input("Digite o sobrenome do dono do Wi-Fi: ")
        data_nascimento = input("Digite a data de nascimento (DDMMYYYY): ")
        nome_pet = input("Digite o nome do pet: ")
        wordlist = gerar_wordlist_wifi(nome, sobrenome, data_nascimento, nome_pet)
        print("Wordlist gerada:")
        
        for senha in wordlist:  
            print(senha)

   
    elif opcao == 3:
        print("Gerar senha apenas com números:")
        tamanho = int(input("Digite o tamanho da senha: "))
        print(gerar_senha(tamanho, string.digits))
    
    elif opcao == 4:
        print("Gerar senha com letras e números:")
        tamanho = int(input("Digite o tamanho da senha: "))
        print(gerar_senha(tamanho, string.ascii_letters + string.digits))
    
    elif opcao == 5:
        print("Gerar senha complexa:")
        tamanho = int(input("Digite o tamanho da senha: "))
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
        print(gerar_senha(tamanho, caracteres))

    elif opcao == 6:
        print("Saindo...")

    else:
        print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    exibir_banner()
    while True:
        exibir_menu()
        opcao_usuario = int(input("Escolha uma opção do menu: "))
        gerenciar_menu(opcao_usuario)
        if opcao_usuario == 6:
            break
