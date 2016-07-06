__author__ = 'Sergei Wallace'

import sys
import random

"""
Code improvements:
1. get surround_head to be an argument that works so it doesnt have to be initialized twice
2. put functions in different files
    a. if after this is done, the shadow variable warning is still there, fix that
3. consider adding an optional inputs for the game
    a. for the size of the board
    b. initial size of the snake
    c. whether to leave board history or to clear after every move
    note, have default set to a value, say snake_game(rows == 20, cols == 20, snake == 3, history == 'no')
"""


def main():
    """
    This function initiates the game Snake. The game prints a board with the player and snake on opposite corners and
    requests an input move to direct the player. This continues until the snake catches the player or the snake can't
    move. The game ends and prints whether the player won or lost and the number of turns the player survived.

    :return: no return statement
    """

    def create_array(size):
        """#This function creates the rows of the board.

        :param size: numbs of rows of the matrix
        :return: a list of dash elements for rows of the board
        """

        return ["_"] * size

    def create_matrix(rows, cols):
        """

        :param rows: numbs of rows of the matrix
        :param cols: number of columns of the matrix
        :return: the board matrix
        """

        matrix = create_array(rows)
        for i in range(rows):
            matrix[i] = create_array(cols)
        return matrix


    rows = 10
    cols = 11

    #Initializing the board
    board = create_matrix(rows,  cols)

    def display_matrix(matrix):
        """
        prints the matrix
        :param matrix: the matrix to be printed
        :return: no return statement
        """

        for r in range(0, rows,  1):
            for c in range(0, cols,  1):
                print(matrix[r][c], end=" ")
            print()
        return

    #initializing the turn counter
    count = 0

    #initializing the player list
    player = [[1,  0]]

    #initializing the snake list
    last_row = len(board) - 1
    last_col = len(board[0]) - 1
    snake = [[last_row,  last_col - 2],  [last_row,  last_col - 1],  [last_row,  last_col]]

    def display_snake(snake):
        """
        prints the snake onto the board
        :param snake: the snake list
        :return: board matrix
        """

        board[player[0][0]][player[0][1]] = 'i'
        for i in range(0, len(snake), 1):
            board[snake[i][0]][snake[i][1]] = 'X'
        return board
    display_snake(snake)

#########################

    def grow(snake, board):
        """
        adds an element to the snake's tail every five turns. The element is added at any one of the elements
         surrounding the tail of the snake except except any prohibited elements.
        :param snake: snake list
        :param board: board matrix
        :return: new snake list with the appended element to its tail
        """

        tail = len(snake)-1
        surround_tail1 = [[snake[tail][0]-1, snake[tail][1]], [snake[tail][0]+1, snake[tail][1]]]
        surround_tail2 = [[snake[tail][0], snake[tail][1]-1], [snake[tail][0], snake[tail][1]+1]]
        surround_tail = surround_tail1 + surround_tail2
        valid = []
        for i in range(0, len(surround_tail), 1):
            if 0 <= surround_tail[i][0] < len(board) and 0 <= surround_tail[i][1] < len(board[0]):
                if board[surround_tail[i][0]][surround_tail[i][1]] != 'X':
                    valid.append(surround_tail[i])
        if not valid:
            return print("Snake can't grow anymore. Game Over. You win in ", count, " turns")
    
        return snake.append(random.choice(valid))
    display_matrix(display_snake(snake))

    def distance(a, b):
        """
        Measures the distance between elements in an list
        :param a: first list
        :param b: second list
        :return: the distance between the two elements
        """

        d = ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
        return d

    #initializing the surround_head list
    surround_head1 = [[snake[0][0]-1, snake[0][1]], [snake[0][0]+1, snake[0][1]]]
    surround_head2 = [[snake[0][0], snake[0][1]-1], [snake[0][0], snake[0][1]+1]]
    surround_head = surround_head1 + surround_head2

    def closest(player, snake, surround_head):
        """
        Finds the element [surround the snake's head] between the snake's head and the player. Used to decide where the
        head of the snake should go next.
        :param player: the player list
        :param snake: the snake list
        :param surround_head: a list of elements surrounding the head of the snake
        :return: the closest element to the player in surround_head
        """

        close = surround_head[0]
        for i in range(0, len(surround_head), 1):
            if distance(player[0], surround_head[i]) <= distance(player[0], close):
                if surround_head[i] not in snake:
                    if 0 <= surround_head[i][0] < len(board) and 0 <= surround_head[i][1] < len(board[0]):
                        close = surround_head[i]
        if close == 'X':
            #end game statement if the player wins
            return print("Snake can't move. Game Over. You win in ", count, " turns")
        return close

    def end_game(player, snake, count):
        """
        The end game statement if the player loses
        :return: sys.exit() to quit the program
        """

        if player[0] in snake:
            print("Game Over")
            print("You lose. You survived ", count,  "turns")
            return sys.exit()

    def move(board, snake, count):
        """
        This function takes an input key for where you want the player to move and then, if the move is allowed, will
        move the player there and also move the snake towards the player. The function will check every move if the
        snake has gotten the player and if he has, will print a statement and end the game.
        :param board: board matrix
        :return: move function to continue the game
        """

        tail = len(snake)-1

        #initializing the surround_head list in move
        surround_head1 = [[snake[0][0]-1, snake[0][1]], [snake[0][0]+1, snake[0][1]]]
        surround_head2 = [[snake[0][0], snake[0][1]-1], [snake[0][0], snake[0][1]+1]]
        surround_head = surround_head1 + surround_head2

        surround_player1 = [[player[0][0]-1, player[0][1]], [player[0][0]+1, player[0][1]]]
        surround_player2 = [[player[0][0], player[0][1]-1], [player[0][0], player[0][1]+1]]
        surround_player = surround_player1 + surround_player2

        arrow = input("Enter j to move left,  k to move right,  i to move up,  and m to move down.")

        def position(key):
            if key is 'k':
                x = 3
                return x
            elif key is 'j':
                x = 2
                return x
            elif key is 'm':
                x = 1
                return x
            elif key is 'i':
                x = 0
                return x
            else:
                print("Invalid key")
                return move(board, snake, count)

        direction = position(arrow)

        if 0 <= surround_player[direction][0] < len(board) and 0 <= surround_player[direction][1] < len(board[0]):
            count += 1
            if count % 5 == 0:
                board[player[0][0]][player[0][1]] = '_'
                player[0] = surround_player[direction]
                board[snake[tail][0]][snake[tail][1]] = '_'
                snake.insert(0, closest(player, snake, surround_head))
                snake = snake[:-1]
                grow(snake, board)
                display_matrix(display_snake(snake))
                end_game(player, snake, count)
            else:
                board[player[0][0]][player[0][1]] = '_'
                player[0] = surround_player[direction]
                board[snake[tail][0]][snake[tail][1]] = '_'
                snake.insert(0, closest(player, snake, surround_head))
                snake = snake[:-1]
                display_matrix(display_snake(snake))
                end_game(player, snake, count)
        else:
            print("Invalid Move,  try again")
        return move(board, snake, count)

    move(board, snake, count)

if __name__ == "__main__":
    main()


