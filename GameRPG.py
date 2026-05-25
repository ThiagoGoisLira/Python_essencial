import random

# --- CLASSE BASE ---
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        # Calcula um dano aleatório entre 1 e o ataque máximo
        dano = random.randint(1, self.ataque)
        print(f"\n⚔️ {self.nome} atacou {alvo.nome} e causou {dano} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"❤️  {self.nome} agora tem {self.vida} de vida.")

    def esta_vivo(self):
        return self.vida > 0


# --- SUBCLASSES (HERANÇA) ---
class Guerreiro(Personagem):
    def __init__(self, nome):
        # super() chama o construtor da classe Personagem
        super().__init__(nome, vida=100, ataque=20)

    # Polimorfismo: O Guerreiro tem uma habilidade única
    def golpe_demolidor(self, alvo):
        print(f"\n🔥 {self.nome} usa o GOLPE DEMOLIDOR!")
        dano = self.ataque * 2
        alvo.receber_dano(dano)


class Inimigo(Personagem):
    def __init__(self, nome, tipo):
        super().__init__(nome, vida=50, ataque=10)
        self.tipo = tipo


# --- LOOP DO JOGO (SIMULAÇÃO DE COMBATE) ---
def iniciar_batalha():
    heroi = Guerreiro("Arthur")
    orc = Inimigo("Gro-Gash", "Orc")

    print(f"Um {orc.tipo} chamado {orc.nome} apareceu das sombras!")

    # O combate continua enquanto os dois estiverem vivos
    while heroi.esta_vivo() and orc.esta_vivo():
        print("\n--- Novo Turno ---")

        # Turno do Herói
        acao = input("O que deseja fazer? (1 - Atacar | 2 - Golpe Demolidor): ")
        if acao == '1':
            heroi.atacar(orc)
        elif acao == '2':
            heroi.golpe_demolidor(orc)
        else:
            print("Ação inválida, você perdeu o turno!")

        # Turno do Inimigo (se ele sobreviveu ao ataque do herói)
        if orc.esta_vivo():
            orc.atacar(heroi)

    print("\n--- FIM DE BATALHA ---")
    if heroi.esta_vivo():
        print(f"🏆 {heroi.nome} venceu a batalha!")
    else:
        print("💀 Você foi derrotado...")


# Inicia o jogo
if __name__ == "__main__":
    iniciar_batalha()