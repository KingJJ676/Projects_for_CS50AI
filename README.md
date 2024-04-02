# Crossword
This is an AI that generate crossword puzzles.  
```
$ python generate.py data/structure1.txt data/words1.txt output.png
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```  
![image](https://github.com/KingJJ676/Projects_for_CS50AI/assets/130853046/5820b98c-e3a2-4582-ae57-26acb5e874f1)
  
## File explaination  
There are two Python files in this project: ```crossword.py``` and ```generate.py```. The first was implemented by CS50, and I contributed on the second one.  
  
**```crossword.py```**  
This file defines two classes, ```Variable``` (to represent a variable in a crossword puzzle) and ```Crossword``` (to represent the puzzle itself).  
  
 **```generate.py```**
- **```enforce_node_consistency```**  
   This function updates ```self.domains``` such that each variable is node consistent.  
- **```revise```**  
  This function make variable x arc consistent with variable y.  
- **```ac3```**  
  Using the AC3 algorithm, this function enforce arc consistency on the problem. Arc consistency is achieved when all the values in each variable’s domain satisfy that variable’s binary constraints.  
- **```assignment_complete```**  
  This function checks to see if the given ```assignment``` is complete.  
- **```consistent```**  
  This fucntion checks to see if the given ```assignment``` is consistent.  
- **```order_domain_values```**  
  This function returns a list of the values in the domain of ```var```, ordered according to the *least-constraining values heuristic*.
- **```select_unassigned_variable```**  
  This function return a single variable in the crossword puzzle that is not yet assigned by assignment, according to the *minimum remaining value heuristic* and then the *degree heuristic*.
- **```backtrack```**  
  This function accepts a partial assignment ```assignment``` as input and, using *backtracking search*, return a complete satisfactory assignment of variables to values if it is possible to do so.
  
