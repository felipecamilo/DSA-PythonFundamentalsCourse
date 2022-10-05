# Hangman Game (Jogo da Forca) 
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
        self.painel1 = None
        self.word = word
        self.acertos = 0
        self.erros = 0
        self.endgame = False
        self.letras_erradas = []
        self.letras_corretas = []
        self.won = False
        self.painel = ''

    # Método para adivinhar a letra
    def guess(self, letter):
        self.painel1 = list(self.painel)
        cont = 0
        index = 0
        for i in self.word:
            if letter == i:
                self.acertos += 1
                cont += 1
                self.painel1[index] = letter
                self.painel = ''.join(self.painel1)

            if letter == i and letter not in self.letras_corretas:
                self.letras_corretas.append(letter)

            index += 1

        if cont == 0 and letter not in self.letras_erradas and letter not in self.letras_corretas:
            self.erros += 1
            self.letras_erradas.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.acertos == len(self.word) or self.erros == 6:
            self.endgame = True
        return self.endgame

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.acertos == len(self.word):
            self.won = True
        return self.won

    # Método para não mostrar a letra no board

    def hide_word(self):

        for i in self.word:
            self.painel += '_'

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

        print(board[self.erros])
        print('Palavra: ', self.painel)
        print('\nLetras erradas: ')
        for erros in self.letras_erradas:
            print(erros)
        print('\nLetras corretas: ')
        for corretos in self.letras_corretas:
            print(corretos)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    f = open('palavras.txt', 'r')
    data = f.read()
    rows = data.split('\n')
    randomword = random.choice(rows)
    return randomword


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Métodos
    game.hide_word()
    game.print_game_status()

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while game.hangman_over() is False:
        game.guess(letter=input('\nDigite uma letra:'))
        game.print_game_status()

    # Verifica o status do jogo

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won() is True:
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
