import random

def candy_game(num_candies, player_name):
    player1_candies = 0
    player2_candies = 0
    turn = random.randint(1, 2)
    input('\n\nPress ENTER to find out who takes the candy first\n')
    if turn == 1:
        print('             !!Player goes first!!')
    else:
        print('             !!Bot goes first!!')
    player1_move = 0

    while num_candies > 0:
        if turn == 1:
            while True:
                try:
                    player1_move = int(input(f'{player_name} move: '))
                    if 1 <= player1_move <= 28:
                        break
                    else:
                        print('You can take a maximum of 28')                   
                except:
                    print('Try again')
            num_candies -= player1_move
            player1_candies += player1_move + player2_candies
            player2_candies -= player2_candies
            turn = 2

            print(f'        {num_candies} candies left ')

            if num_candies <= 0:
                print(f'             !!! {player_name} WON!!!')
        else:
            if num_candies <= 57:
                player2_move = num_candies % 28
            else:
                player2_move = random.randint(1,28)
            print('Bot move:', player2_move)
            num_candies -= player2_move
            player2_candies += player2_move + player1_candies
            player1_candies -= player1_candies
            turn = 1
            input(' Press ENTER to continue')
            print(f'        {num_candies} candies left ')

            if num_candies <= 0:
                print('         !!!Bot WON!!!')

def main():
    player_name = input("\nHello, I have a game for you, what's your name?\n Enter your name and press ENTER:  ")
    print('\nThe rules are simple, whoever takes the last\n candy from the table takes everything,\n with the condition that only 28 candies can be taken at a time.')
    while True:
        try:
            total_candies = int(input('\n\nHow many sweets will we put on the table? '))
            break
        except:
            print("Can't have that many candies")
    candy_game(total_candies, player_name)

main()