# A list of all global variables used in the project, to make the variables
# more usable again.

END = 2
DRAW = 1
KEEP = 0

ROW = 2
# ROW -> type: int
#    The purpose of this global variable is to define where is
#    exactly the first number of the input. In another words, it is
#    basically the place in the input string that is possible to
#    find the row number.

COLUMN = 0
# COLUMN -> type: int
#    This global variable makes almost the same thing of the ROW
#    variable, but in another place in the string. In the same way,
#    this number have the position of the second input number on
#    the string.

USER = 0
# USER -> type: int
#    Now we have some variables which define the player type. The first
#    one is "USER". User type is a real player, which can insert positions
#    with the catch function.

EASY = 1
# EASY -> type: int
#    This is the basic "IA" player. Of course this is not even
#    considered an IA. This mode is just the computer making random
#    moves to the board.

MEDIUM = 2
# MEDIUM -> type: int
#    The second "AI" searches for real good moves. First of all, it looks
#    for a movement that will bring the victory. Second, if there wasn't
#    movements to win the game, it searches for blocks on the opponent.
#    Third, if there is no of those options, it just insert an random
#    position.
