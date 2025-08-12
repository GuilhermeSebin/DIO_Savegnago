def calculadora_partidas_ranqueadas():
    print("=== Calculadora de Partidas Ranqueadas ===")
    
    # Entrada de dados
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))
    
    # Cálculo do saldo
    saldo = vitorias - derrotas
    
    # Determinando o rank
    if saldo <= 10:
        nivel = "Ferro"
    elif saldo <= 20:
        nivel = "Bronze"
    elif saldo <= 50:
        nivel = "Prata"
    elif saldo <= 80:
        nivel = "Ouro"
    elif saldo <= 90:
        nivel = "Diamante"
    elif saldo <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    # Exibindo resultado
    print(f"O Herói tem um saldo de {saldo} e está no nível de {nivel}.")

# Executa a função
if __name__ == "__main__":
    calculadora_partidas_ranqueadas()
