# Tic-Tac-Toe
Using *Minimax*, this project implements an AI to play Tic-Tac-Toe optimally.
![image](https://github.com/KingJJ676/Projects_for_CS50AI/assets/130853046/40b620c4-aaa3-4ad1-a1dc-9194d00c535b)  

## File explaination  
There are two main files in this project: ```runner.py``` and ```tictactoe.py```. ```tictactoe.py``` contains all of the logic for playing the game, and for making optimal moves. ```runner.py``` has been implemented by CS50, and contains all of the code to run the graphical interface for the game.  

## ```tictactoe.py```
The function initial_state returns the starting state of the board. The board is represented as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY.  
  
- ```The player``` function should take a board state as input, and return which player’s turn it is (either X or O).
- ```The actions``` function should return a set of all of the possible actions that can be taken on a given board.
- ```The result``` function takes a board and an action as input, and should return a new board state, without modifying the original board.
- ```The winner``` function should accept a board as input, and return the winner of the board if there is one.
- ```The terminal``` function should accept a board as input, and return a boolean value indicating whether the game is over.
- ```The utility``` function should accept a terminal board as input and output the utility of the board.
- ```The minimax``` function should take a board as input, and return the optimal move for the player to move on that board.


