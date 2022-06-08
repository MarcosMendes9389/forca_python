# Hangman Game (Jogo da forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word: str = word
        self.countError = 0
        self.wrongLetters = []
        self.correctLetters = []
        self.wordGamer = []
        for i in range(0, word.__len__()):
            self.wordGamer.append("_")

    def play(self):
        self.print_game_status()
        letter = input("Digite uma letra: ")
        self.verify_letter(letter)

    def verify_letter(self, letter):
        if (letter not in self.correctLetters) and (letter not in self.wrongLetters):
            if letter in self.word:
                self.correctLetters.append(letter)
                for i in range(0, self.word.__len__()):
                    if self.word[i] == letter:
                        self.wordGamer[i] = letter

            else:
                self.wrongLetters.append(letter)
                self.countError += 1

    def print_game_status(self):
        print(board[self.countError])
        print("\n")
        print("Palavra: " + "".join(self.wordGamer))
        print("\nLetras erradas: ")
        print("".join(self.wrongLetters))
        print("Letras corretas: ")
        print("".join(self.correctLetters))

    def hangman_over(self):
        print("self.countError" + self.countError.__str__())
        print("board.__len__()" + board.__len__().__str__())
        if self.countError >= board.__len__() - 1:
            return True
        else:
            return False

    def gammer_won(self):
        if "_" not in self.wordGamer:
            return True
        else:
            return False


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    game.play()
    while (not game.hangman_over()) and (not game.gammer_won()):
        game.play()

    if game.gammer_won():
        game.print_game_status()
        print('\nParabéns! Você venceu!!')
    else:
        game.print_game_status()
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()

