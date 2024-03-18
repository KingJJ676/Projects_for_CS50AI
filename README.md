# Minesweeper
This is an AI that plays minesweeper.  
![image](https://github.com/KingJJ676/Projects_for_CS50AI/assets/130853046/f6bbffb7-9f75-47a1-93be-5bc6cbd8daed)  

## Knowledge representation
The AI’s knowledge base is represented like the below.  
```{A, B, C, D, E, F, G, H} = 1```  
Every logical sentence in this representation has two parts: a set of cells on the board that are involved in the sentence, and a number count, representing the count of how many of those cells are mines. The above logical sentence says that out of cells A, B, C, D, E, F, G, and H, exactly 1 of them is a mine.  
![image](https://github.com/KingJJ676/Projects_for_CS50AI/assets/130853046/35bfa785-2ccd-41cf-afa0-cd12defdff8a)  

## Files explanations
There are two main files in this project: ```runner.py``` and ```minesweeper.py```.   

### ```runner.py``` 
This file has been implemented by the CS50 team, and contains all of the code to run the graphical interface for the game.   

### ```minesweeper.py```
This file contains all of the logic the game itself and for the AI to play the game. There are three classes defined in this file, ```Minesweeper```, which handles the gameplay; ```Sentence```, which represents a logical sentence that contains both a set of cells and a count; and ```MinesweeperAI```, which handles inferring which moves to make based on knowledge.  

- **```The Minesweeper class```**  
  This class has been implemented by the CS50 team. Notice that each cell is a pair (i, j) where i is the row number (ranging from 0 to height - 1) and j is the column number (ranging from 0 to width - 1).  

- **```The Sentence class```**  
  This class is used to represent logical sentences of the form described in the Background. Each sentence has a set of cells within it and a count of how many of those cells are mines. The class also contains functions ```known_mines``` and ```known_safes``` for determining if any of the cells in the sentence are known to be mines or known to be safe. It also contains functions ```mark_mine``` and ```mark_safe``` to update a sentence in response to new information about a cell.  

- **```The MinesweeperAI class```**
  This class implements an AI that can play Minesweeper. The AI class keeps track of a number of values. ```self.moves_made``` contains a set of all cells already clicked on, so the AI knows not to pick those again. ```self.mines``` contains a set of all cells known to be mines. ```self.safes``` contains a set of all cells known to be safe. And ```self.knowledge``` contains a list of all of the Sentences that the AI knows to be true.  







