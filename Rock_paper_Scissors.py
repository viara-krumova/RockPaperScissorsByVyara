import random
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
win_player = 0
win_computer = 0

status ='yes'
while status != 'no':
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'
    player_move = input('Choose [r]ock, [p]aper ot [s]cissors:')
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Try again ...')
    computer_move = ''
    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    prCyan(f'Computer chose {computer_move}')
    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        prRed('You win!')
        win_player += 1
    elif player_move == computer_move:
        prGreen('Draw!')
    else:
        prGreen('You lose!')
        win_computer += 1
    prPurple('Type [yes] to Play Again or [no] to quit:')
    status = input()
prGreen(f'Result: player : computer -> {win_player} : {win_computer}')




