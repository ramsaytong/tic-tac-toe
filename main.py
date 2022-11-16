
POSISTION=[[(" "),(" "),(" ")],
           [(" "),(" "),(" ")],
           [(" "),(" "),(" ")]]

def show():
    table = f"{POSISTION[0][0]}|{POSISTION[0][1]}|{POSISTION[0][2]}\n" \
            f"_____\n" \
            f"{POSISTION[1][0]}|{POSISTION[1][1]}|{POSISTION[1][2]}\n" \
            f"_____\n" \
            f"{POSISTION[2][0]}|{POSISTION[2][1]}|{POSISTION[2][2]}\n"
    print(table)

def player1():
    global n
    try:
        row = int(input("Player1(X) , pls choose your row: ")) - 1
        column = int(input("Player1(X) , pls choose your column: ")) - 1
        step = POSISTION[row][column]
        if step == " ":
            n += 1
            POSISTION[row][column] = "X"
            show()
        else:
            print("This step was occupied already")
            show()
            player1()
    except ValueError:
        print("\nYou have not typed anything")
    except IndexError:
        print('\nNumber must be between 1 and 3')


def player2():
    global n
    try:
        row = int(input("Player2(O) , pls choose your row: ")) - 1
        column = int(input("Player2(O) , pls choose your column: ")) - 1
        step = POSISTION[row][column]
        if step == " ":
            n += 1
            POSISTION[row][column] = "O"
            show()
        else:
            print("This step was occupied already")
            show()
            player2()
    except ValueError:
        print("\nYou have not typed anything")
    except IndexError:
        print('\nNumber must be between 1 and 3')

def winning_check():
    global is_game_on,n
    for i in range(0,3):
        column = [f"{POSISTION[0][i]}", f"{POSISTION[1][i]}", f"{POSISTION[2][i]}"]
        skew = [f"{POSISTION[0][0]}", f"{POSISTION[1][1]}", f"{POSISTION[2][2]}"]
        if POSISTION[i] == ['X', 'X', 'X'] \
                or column == ['X', 'X', 'X'] \
                or skew == ['X', 'X', 'X']:
            is_game_on = False
            print("player1(X) win!")
        elif POSISTION[i] == ['O', 'O', 'O'] \
                or column == ['O', 'O', 'O'] \
                or skew == ['O', 'O', 'O']:
            is_game_on = False
            print("player2(O) win!")
    if is_game_on and n == 9:
        is_game_on = False
        print('Match Draw')

is_game_on=True
n = 0

def game():
  print("Welcome to Tic Tac Toe Game!\n")
  show()
  while is_game_on:
      player1()
      winning_check()
      if is_game_on:
          player2()
          winning_check()

game()