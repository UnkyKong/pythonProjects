# Starter Code
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " + \
                    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You bumped into a wall."
GAME_OVER = "Thanks for playing."
EXIT_ROOM_SENTINEL = "exit"


# IMPORTANT: When submitting to Sense, do not modify any code above this line or the function signature below.

def navigate(current_room: str, user_input: str):
    """
    Given a current_room in rooms and a user_input, return a tuple (next_room, err_msg) with
    next_room -- where you are after or EXIT_ROOM_SENTINEL
    err_msg -- message to print, if any, empty, GAME_OVER, INVALID_DIRECTION, or CANNOT_GO_THAT_WAY
    """

    # First check for invalid input
    if user_input not in VALID_INPUTS:
        next_room = current_room
        err_msg = INVALID_DIRECTION
    # Check for valid directions and whether you can move in that direction
    elif user_input in DIRECTIONS:
        if user_input in rooms[current_room]:
            next_room = rooms[current_room][user_input]
            err_msg = ''
        else:
            next_room = current_room
            err_msg = CANNOT_GO_THAT_WAY
    # Handle the exit command
    else:
        next_room = EXIT_ROOM_SENTINEL
        err_msg = GAME_OVER

    # Do not modify anything below this line.

    return next_room, err_msg


command = input('input command here').capitalize()

starting_room = 'Great Hall'
navigate(starting_room, command)