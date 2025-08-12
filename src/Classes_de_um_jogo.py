class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()  # garante que o tipo seja sempre minúsculo
    
    def atacar(self):
        # Mapeamento de tipo para ataque
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        
        # Verifica se o tipo existe no dicionário
        ataque = ataques.get(self.tipo, "um ataque desconhecido")
        
        # Exibe a mensagem final
        print(f"O {self.tipo} atacou usando {ataque}.")

# Exemplo de uso
if __name__ == "__main__":
    # Criando alguns heróis para demonstrar
    herois = [
        Heroi("Arthur", 30, "guerreiro"),
        Heroi("Merlin", 150, "mago"),
        Heroi("Shifu", 60, "monge"),
        Heroi("Hanzo", 25, "ninja")
    ]
    
    # Cada herói ataca
    for h in herois:
        h.atacar()
