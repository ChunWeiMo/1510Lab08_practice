"""
Chun-Wei, Mo
A01375071
"""
import random


def make_room():
    """
    Return a random room from 5 kinds fo room.

    :postcondtion: return a random room from 5 kinds of room
    :return: a string
    """
    room = {0: 'Empty room', 1: 'Spike trap',
            2: 'Poison gas', 3: 'Camp fire', 4: 'Spirit fountain'}
    room_seed = random.randint(0, 4)
    return room[room_seed]


def room_effect(board, character):
    """
    Calculate character current hp after room effect.

    :param board: a dictionary
    :param character: a dictionary
    :precondition:
    """
    location = (character['X-coordinate'], character['Y-coordinate'])
    if board[location] == 'Empty room':
        print('You enter a empty room. Keep going.')
    elif board[location] == 'Spike trap':
        print('You get injured by a spike trap, causing 1 damage.')
        character['Current HP'] -= 1
    elif board[location] == 'Poison gas':
        print('You enter a poison chamber. Poison gas has caused 1 damage.')
        character['Current HP'] -= 1
    elif board[location] == 'Spirit fountain':
        print("You discover a spirit fountain and get spirit blessing, healing 1 HP.")
        character['Current HP'] += 1
    elif board[location] == 'Camp fire':
        print("You have found a camp fire left by previous adventurers and rested for a while, healing 1 HP.")
        character['Current HP'] += 1


def make_board(rows, columns):
    """
    Create a rows * columns map with 5 kinds of rooms as a dictionary.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be integer equal to or greater than 2
    :postcondition: create a a rows * columns map as a dictionary
    :postcondition: key is a tuple that contains a set of coordinates and each value is string representing the room name
    :postcondition: (0, 0) is Entrance and (rows - 1, columns - 1) is Goal
    :postcondition: (0, 0) is Entrance and (rows - 1, columns - 1) is Goal
    :postcondition: 5 kinds of rooms include 'Empty room', 'Spike trap', 'Poison gas', 'Camp fire', and 'Spirit fountain'
    :return: a dictionary
    """
    room = {0: 'Empty room', 1: 'Spike trap',
            2: 'Poison gas', 3: 'Camp fire', 4: 'Spirit fountain'}
    board = dict()
    room_list = list()
    for row in range(rows):
        for column in range(columns):
            position = (row, column)
            if row == 0 and column == 0:
                board[position] = "Entrance"
            elif row == rows - 1 and column == columns - 1:
                board[position] = "Goal"
            else:
                room_seed = random.randint(0, 4)
                room_list.append(room_seed)
                board[position] = room[room_seed]
    return board


def board_size(board):
    """
    Return the boundaries of the board.

    :param board: a dictionary
    :precondition: key is a tuple that contains a set of coordinates
    :postcondition: return the boundaries of the board
    :return: a tuple
    >>> board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (1, 0): 'Spike trap', (1, 1): 'Goal'}
    >>> board_size(board)
    (1, 1)

    >>> board = board = {(0, 0): 'Entrance', (0, 1): 'Spike trap', (0, 2): 'Empty room', (1, 0): 'Spirit fountain', (
            1, 1): 'Spirit fountain', (1, 2): 'Poison gas', (2, 0): 'Camp fire', (2, 1): 'Empty room', (2, 2): 'Goal'}
    >>> board_size(board)
    (2, 2)
    """
    east_wall = 1
    south_wall = 1
    for grid in board:
        if grid[0] > south_wall:
            south_wall = grid[0]
        if grid[1] > east_wall:
            east_wall = grid[1]
    return south_wall, east_wall


def make_character():
    """
    Create and return a dictionary representing character.

    :postcondition: Create and return a dictionary that contains the following 
                    key:value pairs: 'X-coordinate': 0, 'Y-coordinate'": 0, 'Current HP': 5
    :return: a dictionary
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}


def describe_current_location(character):
    """
    Print character's current location.

    :param character: a dictionary
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :precondition: 'Current HP' must greater than 0
    :postcondition: print character's current location

    >>> {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    'You stand at the entrance, start your advance to SE corner.'

    'You are at X: 0, Y: 0.'

    >>> {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 5}
    'You are at X: 2, Y: 3.'
    """
    location = (character['X-coordinate'], character['Y-coordinate'])
    if location == (0, 0):
        print('You stand at the entrance, start your advance to SE corner.')
        print()
    print(
        f"You are at X: {character['X-coordinate']}, Y: {character['Y-coordinate']}.")


def describe_current_hp(character):
    """
    Print character's current hp.

    :param character: a dictionary
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :precondition: the value of "Current HP" must equal to or greater than 0
    :postcondition: print character's current hp

    >>> {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    'Your current HP: 5'


    >>> {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 0}
    'Your current HP: 0'

    """
    print(f"Your current HP: {character['Current HP']}")
    print()


def get_user_choice():
    """
    Ask the user to enter the direction they wish to travel.

    :postcondition: ask the user to enter an integer between 0 and 3 inclusive.
    :return: a integer
    """
    direction_list = (0, 1, 2, 3)
    while True:
        print('The direction you can choose 0: North, 1: East, 2: South, 3: West')
        direction = int(input("Enter a number to choose direction: "))
        print()
        print()
        if direction in direction_list:
            break
        # raise StopIteration('Incorrect input, try again.')
        print('Incorrect input, try again.')
        print()
    return direction


def validate_move(board, character, direction):
    """
    Determine where the player is on the board and whether they can travel in their desired direction.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: an integer
    :precondition: the keys of board must be tuples that contains a set of coordinates
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :precondition: 'Current HP' must greater than 0
    :precondition: direction must be integer between 0 and 3 inclusive
    :postcondition: determine whether they can travel in their desired direction
    :return: True if they can travel in their desired direction
    :return: False if they cannot travel in their desired direction

    >>> board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
    >>> character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> direction = 0
    >>> validate_move(board, character, direction)
    True

    >>> board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
    >>> character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    >>> direction = 0
    >>> validate_move(board, character, direction)
    False
    """
    north_wall, west_all = 0, 0
    south_wall, east_wall = board_size(board)
    can_move = True
    if character['Y-coordinate'] <= north_wall and direction == 0:
        can_move = False
        print('You are stopped by North wall\n')
    if character['X-coordinate'] >= east_wall and direction == 1:
        can_move = False
        print('You are stopped by East wall\n')
    if character['Y-coordinate'] >= south_wall and direction == 2:
        can_move = False
        print('You are stopped by South wall\n')
    if character['X-coordinate'] <= west_all and direction == 3:
        can_move = False
        print('You are stopped by West wall\n')
    return can_move


def move_character(character, direction):
    """
    Updates the character's X- and Y-coordinates.

    :param character: an dictionary
    :param direction: an integer
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :precondition: 'Current HP' must greater than 0
    :precondition: direction must be integer between 0 and 3 inclusive
    :postcondition: updates the character's X- and Y-coordinates

    >>> character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
    >>> direction = 0
    >>> move_character(character, direction)
    >>> character
    {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5}

    >>> character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
    >>> direction = 3
    >>> move_character(character, direction)
    >>> character
    {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    """
    if direction == 0:
        character['Y-coordinate'] -= 1
        print('moving toward North...')
    if direction == 1:
        character['X-coordinate'] += 1
        print('moving toward East...')
    if direction == 2:
        character['Y-coordinate'] += 1
        print('moving toward South...')
    if direction == 3:
        character['X-coordinate'] -= 1
        print('moving toward West...')


def check_for_foes():
    """
    Generate a random number to check whether encounter a foe.

    :postcondition: generate a random number between 0 and 3 inclusive to check whether encounter a foe
    :return: True if the random number is equal to 0
    :return: False if the random number is not equal to 0
    """
    encounter = False
    foe = random.randint(0, 3)
    if foe == 0:
        encounter = True
        print('A foe appear! Start a battle!')
    return encounter


def guessing_game(character):
    """
    Guess a number between 1 and 5 inclusive to check if it is equal to the random number.

    :param character: an dictionary
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :precondition: 'Current HP' must greater than 0
    :postcondition: prompt player to input a number between 1 and 5 and generate a random integer
    :postcondition: if player's input is not equal to the random integer, 'Current HP' reduce 1
    """
    attack = int(input('Enter an integer [1, 5] to attack the foe: '))
    foe_randint = random.randint(1, 5)
    if attack == foe_randint:
        print('Nice attack! The foe is killed!')
    else:
        print('Miss. The foe makes a counterattack. You lose 1 HP.')
        character["Current HP"] -= 1


def is_alive(character):
    """
    Determine the character's Current HP is greater than or equal to 0.

    :param character: an dictionary
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :postcondition: determine the character's Current HP is greater than or equal to 0
    :return: True if Current HP is greater than 0
    :return: False if Current HP is equal to or less than 0

    >>> character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
    >>> is_alive(character)
    True

    >>> character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 0}
    >>> is_alive(character)
    False
    """
    if character['Current HP'] <= 0:
        print('You dead...')
        print('Close the game.')
        return False
    else:
        return True


def check_if_goal_attained(board, character):
    """
    Determine the character whether reach the south east corner.

    :param character: an dictionary
    :precondition: character must have keys 'X-coordinate', 'Y-coordinate', and 'Current HP' with value of integer
    :precondition: 'Current HP' must greater than 0
    :postcondition: determine the character whether reach the South East corner
    :return: True if the character reach the south east corner

    >>> board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Goal'}
    >>> character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> check_if_goal_attained(board, character)
    True

    >>> board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Goal'}
    >>> character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> check_if_goal_attained(board, character)
    None
    """
    south_wall, east_wall = board_size(board)
    if character['X-coordinate'] == east_wall and character['Y-coordinate'] == south_wall:
        achieved_goal = True
        print('Congratulation! You achieve the goal!')
        return achieved_goal


def game():
    """
    Run the game.
    """
    rows = 2
    columns = 2
    board = make_board(rows, columns)
    print(board)
    south_wall, east_wall = board_size(board)
    print(f"This is a {south_wall} X {east_wall} board.")
    character = make_character()
    achieved_goal = False

    while not achieved_goal:
        describe_current_location(character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            room_effect(board, character)
            if not is_alive(character):
                break
            describe_current_hp(character)

        there_is_a_challenger = check_for_foes()
        if there_is_a_challenger:
            guessing_game(character)
            describe_current_hp(character)
            if not is_alive(character):
                break

        achieved_goal = check_if_goal_attained(board, character)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
