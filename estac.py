class Estacionamento:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matriz = [[None for _ in range(n)] for _ in range(m)]
        self.veiculos = {} 

    def entrada_veiculo(self, placa, hora_entrada):
        for i in range(self.m):
            for j in range(self.n):
                if self.matriz[i][j] is None:
                    self.matriz[i][j] = placa
                    self.veiculos[placa] = {'posicao': (i, j), 'hora_entrada': hora_entrada}
                    return f"Veículo {placa} estacionado na posição ({i}, {j})"
        return "Estacionamento cheio"

    def saida_veiculo(self, placa, hora_saida, valor_hora, valor_adicional):
        if placa in self.veiculos:
            posicao = self.veiculos[placa]['posicao']
            hora_entrada = self.veiculos[placa]['hora_entrada']
            self.matriz[posicao[0]][posicao[1]] = None
            del self.veiculos[placa]
            valor = self.calcular_valor(hora_entrada, hora_saida, valor_hora, valor_adicional)
            return f"Veículo {placa} saiu. Total a pagar: R$ {valor:.2f}"
        return "Veículo não encontrado"

    def calcular_valor(self, hora_entrada, hora_saida, valor_hora, valor_adicional):
        from math import ceil, floor
        tempo_total = (hora_saida - hora_entrada).total_seconds() / 3600
        if tempo_total <= 3:
            if tempo_total > floor(tempo_total) + 0.25:
                return (ceil(tempo_total))*valor_hora
            else: return floor(tempo_total)*valor_hora       
        else:
            horas_extras = tempo_total - 3
            if horas_extras > floor(horas_extras) + 0.25:
                return 3*valor_hora + ceil(horas_extras) * valor_adicional
            else: return 3*valor_hora + floor(horas_extras) * valor_adicional

    def mostrar_matriz(self):
        for linha in self.matriz:
            print(linha)
