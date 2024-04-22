# Nim
This is an AI that teaches itself to play Nim through _reinforcement learning_.  
```
$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
```
## Background - The Nim game  
In a Nim game, the gameboard begin with some number of piles, each with some number of objects. Players take turns: on a player’s turn, the player removes any non-negative number of objects from any one non-empty pile. Whoever removes the last object loses.  

## File explanation    
**```nim.py```**  
Two classes are defined in this file: ```Nim``` and ```NimAI```.  

- **the ```Nim``` class:**  
  This class defines how a Nim game is played. In the ```__init__``` function, notice that every Nim game needs to keep track of a list of piles, a current player (0 or 1), and the winner of the game (if one exists). The ```available_actions``` function returns a set of all the available actions in a state. For example, ```Nim.available_actions([2, 1, 0, 0])``` returns the set ```{(0, 1), (1, 1), (0, 2)}```, since the three possible actions are to take either 1 or 2 objects from pile 0, or to take 1 object from pile 1.  
  The remaining functions are used to define the gameplay: the ```other_player``` function determines who the opponent of a given player is, ```switch_player``` changes the current player to the opposing player, and move performs an action on the current state and switches the current player to the opposing player.
    
- **the ```NimAI``` class:**  
  This class defines the AI that will learn to play Nim. In the ```__init__``` function, we start with an empty ```self.q``` dictionary. The ```self.q``` dictionary will keep track of all of the current Q-values learned by our AI by mapping ```(state, action)``` pairs to a numerical value. As an implementation detail, though we usually represent state as a list, since lists can’t be used as Python dictionary keys, we’ll instead use a tuple version of the state when getting or setting values in ```self.q```.

- **the ```train``` and ```play```function:**  
  These two functions use the ```Nim``` and ```NimAI``` classes. The ```train``` function trains an AI by running n simulated games against itself, returning the fully trained AI. The ```play``` function accepts a trained AI as input, and lets a human player play a game of Nim against the AI.
