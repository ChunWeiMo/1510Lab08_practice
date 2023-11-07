def make_board(rows, columns):
    board = dict()
    for row in range(rows):
        for column in range(columns):
            tuple_template = (row, column)
            board[tuple_template] = 'Empty room'
    return board


def board_size(board: dict):
    east_wall = 1
    south_wall = 1
    for grid in board:
        if grid[0] > south_wall:
            south_wall = grid[0]
        if grid[1] > east_wall:
            east_wall = grid[1]
    return (south_wall, east_wall)


def make_character():
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}


def describe_current_location(board: dict, character: dict):
    south_wall, east_wall = board_size(board)
    print(f"This is a {south_wall} X {east_wall} board.")
    print(
        f"You are at row: {character['X-coordinate']}, column: {character['Y-coordinate']}.")
    # if character['X-coordinate'] > east_wall or character['X-coordinate'] < 0 or character['Y-coordinate'] > south_wall or character['Y-coordinate'] < 0:
    #     print("WARNING: Out of the board")


def get_user_choice():
    # North-East-South-West
    direction_list = (0, 1, 2, 3)
    direction = ''
    while True:
        print('the direction you can choose 0: North, 1: East, 2: South, 3: West')
        direction = int(input("Enter a number to choose direction: "))
        if direction in direction_list:
            break
        print("Incorrect input, try again.")
        print()
    # print(direction)
    return direction


def validate_move(board: dict, character: dict, direction: int):
    north_wall = 0
    west_wall = 0
    south_wall, east_wall = board_size(board)
    print(f'south_wall: {south_wall}')
    print(f'east_wall: {east_wall}')

    can_move = True
    if character["Y-coordinate"] <= north_wall and direction == 0:
        can_move = False
    if character["X-coordinate"] >= east_wall and direction == 1:
        can_move = False
    if character["Y-coordinate"] >= south_wall and direction == 2:
        can_move = False
    if character["X-coordinate"] <= west_wall and direction == 3:
        can_move = False

    # print(f'charactor now:{character["X-coordinate"]}, {character["Y-coordinate"]}')
    return can_move


# move_character(character)
def move_character(character, direction):
    if direction == 0:
        character["Y-coordinate"] -= 1
    if direction == 1:
        character["X-coordinate"] += 1
    if direction == 2:
        character["Y-coordinate"] += 1
    if direction == 3:
        character["X-coordinate"] -= 1
        

def check_if_goal_attained(board, character, achieved_goal):
    south_wall, east_wall = board_size(board)
    print(f"south_wall: {south_wall}")
    print(f"east_wall: {east_wall}")
    if character["X-coordinate"] == east_wall and character["Y-coordinate"] == south_wall:
        achieved_goal = True
        print("Congratulation! You arrive the goal!")
    return achieved_goal


def game():  # called from main
    rows = 3
    columns = 3
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while not achieved_goal:
        # // Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
        describe_current_location(board, character)
    # there_is_a_challenger = check_for_foes()
    # if there_is_a_challenger:
    # guessing_game(character)
        achieved_goal = check_if_goal_attained(board, character)
    # else:
    # // Tell the user they can’t go in that direction
    # // Print end of game stuff like congratulations or sorry you died


def main():
    board = make_board(4, 9)
    print(board)

    character = make_character()
    print(character)

    # get_user_choice()
    # print(1 in [0, 1, 2, 3])
    # direction = 3
    character = {'X-coordinate': 3, 'Y-coordinate': 8, 'Current HP': 5}
    # print(f"direction: {direction}")
    # print(validate_move(board, player, direction))

    describe_current_location(board, character)
    
    achieved_goal = False
    print(check_if_goal_attained(board, character, achieved_goal))
    


if __name__ == "__main__":
    main()
