import os

# Lista global para armazenar o histórico de leituras
historico = []


def limpar_tela():
    os.system('cls') #limpar a tela toda vez q rodar


def inserir_dados():
    limpar_tela()
    print("CADASTRAR DADOS DOS SENSORES")
    try:
        temp = float(input("Digite a temperatura da nave (°C): "))
        energia = float(input("Digite a porcentagem de energia (0-100): "))
        print("")
        print("Status da comunicação:")
        print(" [1] Online / Estável")
        print(" [0] Offline / Falha")
        comunicacao = int(input("Escolha (1 ou 0): "))

        leitura = {
            "temperatura": temp,
            "energia": energia,
            "comunicacao": comunicacao
        }
        historico.append(leitura)
        print("\n\033[92mDados cadastrados com sucesso!\033[0m") #Cor verde
    except ValueError:
        print("\n\033[91mErro: Digite valores numéricos válidos.\033[0m")#91m cor vermelha
    input("\nPressione Enter para voltar ao menu...")


def visualizar_status():
    limpar_tela()
    print("STATUS OPERACIONAL DA MISSÃO")
    if not historico:
        print("\033[93mNenhum dado cadastrado.\033[0m")
    else:
        ultima = historico[-1] #usei o exemplo da ultima cp
        status_com = "ONLINE" if ultima["comunicacao"] == 1 else "OFFLINE"
        print(f"Temperatura Atual: {ultima['temperatura']}°C")
        print(f"Nível de Energia:  {ultima['energia']}%")
        print(f"Comunicação:       {status_com}")
    input("\nPressione Enter para voltar ao menu...")


def executar_analise():
    limpar_tela()
    print("=== ANÁLISE DO SISTEMA E ALERTAS ===")
    if not historico:
        print("\033[93mNão há dados para analisar. Cadastre as informações primeiro.\033[0m") #93m deixa a cor amarela
    else:
        ultima = historico[-1]
        alertas = 0
        if ultima["temperatura"] > 80:
            print("\033[91m[ALERTA] Superaquecimento detectado!\033[0m")
            alertas += 1
        if ultima["energia"] < 20:
            print("\033[93m[ALERTA] Energia crítica! Ativando modo de economia.\033[0m")
            alertas += 1
        if ultima["comunicacao"] == 0:
            print("\033[91m[ALERTA] Falha de comunicação com a base!\033[0m")
            alertas += 1
        if alertas == 0:
            print("\033[92mSistemas operando dentro da normalidade. Missão segura.\033[0m")
    input("\nPressione Enter para voltar ao menu...")


def exibir_historico():
    limpar_tela()
    print("=== HISTÓRICO DE LEITURAS ===")
    if not historico:
        print("\033[93mHistórico vazio.\033[0m")
    else:
        for i, leitura in enumerate(historico, 1):
            status_com = "OK" if leitura["comunicacao"] == 1 else "FALHA"
            print(
                f"Leitura #{i} | Temp: {leitura['temperatura']}°C | Energia: {leitura['energia']}% | Comms: {status_com}")
    input("\nPressione Enter para voltar ao menu...")


def menu_principal():
    while True:
        limpar_tela()
        print("-----------------------------------------")
        print("  MONITORAMENTO DE MISSÃO ESPACIAL GS2026 ")
        print("-----------------------------------------")
        print(" [1] Inserir dados dos sensores")
        print(" [2] Visualizar status atual")
        print(" [3] Executar análise de alertas")
        print(" [4] Histórico das leituras")
        print(" [5] Encerrar sistema")
        print("-----------------------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            visualizar_status()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            exibir_historico()
        elif opcao == "5":
            print("\nEncerrando sistema de monitoramento. Boa viagem, astronauta!")
            break
        else:
            print("\n\033[91mOpção inválida!\033[0m")
            import time
            time.sleep(1)


# Chama e roda o menu principal diretamente
menu_principal()