
board = [["[  ]","[  ]","[  ]"],["[  ]","[  ]","[  ]"],["[  ]","[  ]","[  ]"]]

def display_board(current_board):
    for i in current_board:
        for k in i:
            print(k, end="")
        print("\n")
        
def player_input(player, current_board):
    while True:
        if player == "[ X ]":
            print("Player 1's Turn:")
            player1xcoord= input("X Coord:")
            if player1xcoord not in ["1", "2", "3"]:
                print("Out of Bounds")
                continue
            player1xcoord= int(player1xcoord)-1
            
            player1ycoord = input("Y Coord:")
            if player1ycoord not in ["1", "2", "3"]:
                print("Out of Bounds")
                continue
            player1ycoord= int(player1ycoord)-1
            if current_board[player1ycoord][player1xcoord] != "[  ]":
                print("Space Occupied")
                continue
            return [player1xcoord,player1ycoord]
        
        elif player == "[ O ]":
            print("Player 2's Turn:")
            player2xcoord= input("X Coord:")
            if player2xcoord not in ["1", "2", "3"]:
                print("Out of Bounds")
                continue
            player2xcoord= int(player2xcoord)-1
            
            player2ycoord = input("Y Coord:")
            if player2ycoord not in ["1", "2", "3"]:
                print("Out of Bounds")
                continue
            player2ycoord= int(player2ycoord)-1
            if current_board[player2ycoord][player2xcoord] != "[  ]":
                print("Space Occupied")
                continue
            return [player2xcoord,player2ycoord]

def update_board(current_board, player_moves, player):
    current_board[player_moves[1]][player_moves[0]]= player
    return current_board

def check_game_status(current_board, player):
    column =[]
    for i in current_board:
        if all(k == player for k in i):
            return False
    for i in range(len(current_board[0])):
        for k in range(len(current_board)):
            column.append(current_board[k][i])
        if all(cell == player for cell in column):
            return False
    if all(current_board[i][i] == player for i in range(len(current_board))):
        return False
    if all(current_board[i][len(current_board)-i-1] == player for i in range(len(current_board))):
        return False               
    return True                     
   
             

def mainloop():
    while True:
        current_board = board
        display_board(current_board)
        player_1_moves=player_input("[ X ]", current_board)
        current_board=update_board(current_board,player_1_moves,"[ X ]")
        status=check_game_status(current_board,"[ X ]")
        if status== False:
            print("game over")
            break
            
        display_board(current_board)
        player_2_moves=player_input("[ O ]", current_board)
        current_board=update_board(current_board,player_2_moves,"[ O ]")
        status=check_game_status(current_board,"[ O ]")
        if status == False:
            print("game over")
            break
mainloop()