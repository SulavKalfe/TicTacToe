# player1_moves = [2, 4, 6]
def check_win_for_player(pmoves, playername):
    winningmoves = list()
    moves_to_win = [[1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 5, 9], [3, 5, 7]]
    for i in moves_to_win:
        for j in pmoves:
            if j in i:
                winningmoves.append(j)
        sortedlist = sorted(winningmoves)
        # print(sortedlist)
        # print(i)
        if i == sortedlist:
            return f"Player {playername} won"

        else:
            winningmoves=list()


def game():

    chances = 9
    moves_done = int()
    # player 1 can register 5 moves
    player1_moves = list()
    # player 2 can register 4 moves
    player2_moves = list()
    valid_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    to_replace3 = [["1", "|", "2", "|", "3"], ["4", "|", "5", "|", "6"], ["7", "|", "8", "|", "9"]]

    # for i in to_replace3:
    #     print(" ".join(i))
    #     if to_replace3.index(i) != 2:
    #         print("-----------")

    # for i in to_replace3:
    #     # print(i)
    #     try:
    #         index = i.index("9")
    #         i[index] = "Fuck you"
    #     except ValueError:
    #         pass
    # print(to_replace3)

    while chances > moves_done:
        for i in to_replace3:
            print(" ".join(i))
            if to_replace3.index(i) != 2:
                print("-----------")
        move = int(input("Provide a number from 1 to 9: "))
        if move not in valid_move:
            print("Invalid move")
        elif move not in player1_moves and move not in player2_moves:
            if moves_done % 2 == 0:
                player1_moves.append(move)
                for i in to_replace3:
                    # print(i)
                    try:
                        index = i.index(str(move))
                        i[index] = "O"
                    except ValueError:
                        pass
                # print("Valid move from player 1")
                have_won = check_win_for_player(player1_moves, "1")
                if have_won is not None:
                    print(have_won)
                    break
            else:
                player2_moves.append(move)
                for i in to_replace3:
                    # print(i)
                    try:
                        index = i.index(str(move))
                        i[index] = "X"
                    except ValueError:
                        pass
                have_won = check_win_for_player(player2_moves, "2")
                if have_won is not None:
                    print(have_won)
                    break
            moves_done += 1
        else:
            print("Invalid move")



game()


# print(player1_moves)
# print(player2_moves)

