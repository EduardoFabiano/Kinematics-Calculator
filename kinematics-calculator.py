import math

def calcular_mru():
    print("\nMovimento Retilíneo Uniforme (MRU)")
    print("O que você deseja calcular?")
    print("1 - Distância (d)")
    print("2 - Velocidade (v)")
    print("3 - Tempo (t)")
    opcao = input("Escolha uma opção (1-3): ")

    if opcao == '1':
        v = float(input("Velocidade (m/s): "))
        t = float(input("Tempo (s): "))
        d = v * t
        print(f"\nDistância calculada: {d:.2f} metros")
    elif opcao == '2':
        d = float(input("Distância (m): "))
        t = float(input("Tempo (s): "))
        if t == 0:
            print("\nErro: O tempo não pode ser zero!")
            return
        v = d / t
        print(f"\nVelocidade calculada: {v:.2f} m/s (ou {v*3.6:.2f} km/h)")
    elif opcao == '3':
        d = float(input("Distância (m): "))
        v = float(input("Velocidade (m/s): "))
        if v == 0:
            print("\nErro: A velocidade não pode ser zero!")
            return
        t = d / v
        print(f"\nTempo calculado: {t:.2f} segundos")
    else:
        print("\nOpção inválida!")

def calcular_muv():
    print("\nMovimento Uniformemente Variado (MUV)")
    print("O que você deseja calcular?")
    print("1 - Velocidade Final (v) usando o Tempo")
    print("2 - Distância / Deslocamento (Δs) usando o Tempo")
    print("3 - Velocidade Final (v) usando Torricelli (sem Tempo)")
    print("4 - Aceleração (a)")
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        v0 = float(input("Velocidade Inicial (v0 em m/s): "))
        a = float(input("Aceleração (a em m/s²): "))
        t = float(input("Tempo (t em s): "))
        v = v0 + (a * t)
        print(f"\nVelocidade Final calculada: {v:.2f} m/s")
    elif opcao == '2':
        v0 = float(input("Velocidade Inicial (v0 em m/s): "))
        a = float(input("Aceleração (a em m/s²): "))
        t = float(input("Tempo (t em s): "))
        d = (v0 * t) + (a * (t ** 2) / 2)
        print(f"\nDistância percorrida calculada: {d:.2f} metros")
    elif opcao == '3':
        v0 = float(input("Velocidade Inicial (v0 em m/s): "))
        a = float(input("Aceleração (a em m/s²): "))
        d = float(input("Distância percorrida (Δs em metros): "))
        v_quadrado = (v0 ** 2) + (2 * a * d)
        if v_quadrado < 0:
            print("\nErro: O resultado dentro da raiz quadrada deu negativo. Verifique os valores.")
            return
        v = math.sqrt(v_quadrado)
        print(f"\nVelocidade Final calculada (Torricelli): {v:.2f} m/s")
    elif opcao == '4':
        v = float(input("Velocidade Final (v em m/s): "))
        v0 = float(input("Velocidade Inicial (v0 em m/s): "))
        t = float(input("Tempo (t em s): "))
        if t == 0:
            print("\nErro: O tempo não pode ser zero!")
            return
        a = (v - v0) / t
        print(f"\nAceleração calculada: {a:.2f} m/s²")
    else:
        print("\nOpção inválida!")

def menu_principal():
    while True:
        print("\nCALCULADORA DE CINEMÁTICA")
        print("1 - Movimento Retilíneo Uniforme (MRU)")
        print("2 - Movimento Uniformemente Variado (MUV)")
        print("0 - Sair")
        escolha = input("Selecione o tipo de movimento: ")
        
        if escolha == '1':
            calcular_mru()
        elif escolha == '2':
            calcular_muv()
        elif escolha == '0':
            print("\nObrigado por usar a calculadora! Encerrando script.")
            break
        else:
            print("\nOpção inválida! Escolha 1, 2 ou 0.")

if __name__ == "__main__":
    menu_principal()
