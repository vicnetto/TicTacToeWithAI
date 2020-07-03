# TicTacToe with MINIMAX

TicTacToe is a classic game, very known by almost every novice programmer (and the rest of the word, of course). Different from the others, this game uses an algorithm called: "Minimax". In the hardest mode, the AI basically runs in between every possible moves, looking only for a win or a draw. 

**BUT, HOW MINIMAX WORK?** [Here](https://www.freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37/) you can find a little bit about minimax in TicTacToe.

## Clone and Run

To build it's very easy, you just need to take this steps:
1) Clone the repository and enter:
```
    $ git clone https://github.com/vicnetto/TicTacToeWithAI
    $ cd TicTacToeWithAI
```
2) Them just run the Python file:
```
    $ python main.py
```

3) Enjoy! :-)

## Game instructions

The first output line will be:
```
Input Command > 
```
The possible commands in the game are *start* and *exit*. Here is their explanation:
- **start <user/easy/medium/hard> <user/easy/medium/hard>**:  This command is to start the game. After the start it's possible to see two arguments, corresponding respectively to "X" and "O". You can insert 4 types of player, between them _user_, _easy_, _medium_ and _hard_.
    1) _user_ is the real player. You need to make the moves and try to win the game.
    2) _easy_ is the first computer difficult. Actually, is not that difficult, this mode is just the computer making random moves and trying to win the game.
    3) _medium_ is a little bit harder. Basically in this mode the computer makes 2 verifications, if no one of those are true, he will pick an random move, just like _easy_ mode. The two verifications are: if the AI needs just one move to win or if the other player needs just one too.
    4) _hard_ is actually impossible to win. This difficulty uses an algorithm called minimax. As explained above, this mode verifies all possibles moves in the board, for him and for the other player, picking only a position if it's guaranteed a win or a draw.
- **exit**: This commands exits que game.

Example: So to start an game user against hard AI, you should insert:
```c
Input Command > start user hard  # If you want to be the "O" player, insert: start hard user
---------  # -------------------
|       |  # | 1 3 | 2 3 | 3 3 |
|       |  # | 1 2 | 2 2 | 3 2 | < Numbers of the positions!
|       |  # | 1 1 | 2 1 | 3 1 |
---------  # -------------------
Enter the coordinates: > 1 1
---------
|       |
|       |
| X     |
---------
Making move level "hard"
---------
|       |
|   O   |
| X     |
---------
Enter the coordinates: >   
```

And so it goes until the end! Good luck trying to beat the beast haha :-)
