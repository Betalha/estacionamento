from datetime import datetime
from estac import Estacionamento
from placas import IdentificadorEstado
def main():
    estacionamento = Estacionamento(10, 10)
    identificador = IdentificadorEstado()

    while True:
        print("\n1. Entrada de veículo")
        print("2. Saída de veículo")
        print("3. Mostrar matriz de estacionamento")
        print("4. Identificar estado pela placa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa do veículo: ")
            hora_entrada = datetime.strptime(input("Digite a hora de entrada (HH:MM): "), "%H:%M")
            print(estacionamento.entrada_veiculo(placa, hora_entrada))

        elif opcao == "2":
            placa = input("Digite a placa do veículo: ")
            hora_saida = datetime.strptime(input("Digite a hora de saída (HH:MM): "), "%H:%M")
            valor_hora = float(input("Digite o valor por até 3 horas: "))
            valor_adicional = float(input("Digite o valor adicional por hora extra: "))
            print(estacionamento.saida_veiculo(placa, hora_saida, valor_hora, valor_adicional))

        elif opcao == "3":
            estacionamento.mostrar_matriz()

        elif opcao == "4":
            placa = input("Digite a placa do veículo: ")
            print(f"Estado de origem: {identificador.identificar_estado(placa)}")

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
