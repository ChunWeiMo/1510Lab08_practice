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
    board = dict()
    for row in range(rows):
        for column in range(columns):
            position = (row, column)
            room = make_room()
            if row == 0 and column == 0:
                room = "Entrance"
            if row == rows - 1 and column == columns - 1:
                room = "Goal"
            board[position] = room
    return board


def board_size(board):
    east_wall = 1
    south_wall = 1
    for grid in board:
        if grid[0] > south_wall:
            south_wall = grid[0]
        if grid[1] > east_wall:
            east_wall = grid[1]
    return south_wall, east_wall


def make_character():
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}


def describe_current_location(character):
def describe_current_location(character):
    location = (character['X-coordinate'], character['Y-coordinate'])
    if location == (0, 0):
        print("You stand at the entrance, start your advance to SE corner.")
        print()
    print(
        f"You are at X: {character['X-coordinate']}, Y: {character['Y-coordinate']}.")


def describe_current_hp(character):
    print(f"Your current HP: {character['Current HP']}")
    print()


def get_user_choice():
    direction_list = (0, 1, 2, 3)
    while True:
        print('The direction you can choose 0: North, 1: East, 2: South, 3: West')
        direction = int(input("Enter a number to choose direction: "))
        print()
        print()
        if direction in direction_list:
            break
        print("Incorrect input, try again.")
        print()
    # print(direction)
    return direction


def validate_move(board, character, direction):
    north_wall, west_all = 0, 0
    south_wall, east_wall = board_size(board)
    can_move = True
    if character["Y-coordinate"] <= north_wall and direction == 0:
        can_move = False
        print("You are stopped by North wall\n")
    if character["X-coordinate"] >= east_wall and direction == 1:
        can_move = False
        print("You are stopped by East wall\n")
    if character["Y-coordinate"] >= south_wall and direction == 2:
        can_move = False
        print("You are stopped by South wall\n")
    if character["X-coordinate"] <= west_all and direction == 3:
        can_move = False
        print("You are stopped by West wall\n")
    return can_move


def move_character(character, direction):
    if direction == 0:
        character["Y-coordinate"] -= 1
        print("moving toward North...")
    if direction == 1:
        character["X-coordinate"] += 1
        print("moving toward East...")
    if direction == 2:
        character["Y-coordinate"] += 1
        print("moving toward South...")
    if direction == 3:
        character["X-coordinate"] -= 1
        print("moving toward West...")


def check_for_foes():
    encounter = False
    foe = random.randint(0, 3)
    if foe == 0:
        encounter = True
        print("A foe appear! Start a battle!")
    return encounter


def guessing_game(character):
    attack = int(input("Enter an integer [1, 5] to attack the foe: "))
    foe_randint = random.randint(1, 5)
    if attack == foe_randint:
        print("Nice attack! The foe is killed!")
    else:
        print("Miss. The foe makes a counterattack. You lose 1 HP.")
        print("Miss. The foe makes a counterattack. You lose 1 HP.")
        character["Current HP"] -= 1


def is_alive(character):
    if character["Current HP"] <= 0:
        print("You dead...")
        print("Close the game.")
        print("You dead...")
        print("Close the game.")
        return False
    else:
        return True


def check_if_goal_attained(board, character):
    south_wall, east_wall = board_size(board)
    if character["X-coordinate"] == east_wall and character["Y-coordinate"] == south_wall:
        achieved_goal = True
        print("Congratulation! You achieve the goal!")
        return achieved_goal


def game():
    rows = 4
    columns = 4
    board = make_board(rows, columns)
    print(board)
    south_wall, east_wall = board_size(board)
    print(f"This is a {south_wall} X {east_wall} board.")
    character = make_character()
    achieved_goal = False

    while not achieved_goal:
        describe_current_location(character)
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
    game()


if __name__ == "__main__":
    main()
