# Knights  
This is a program that solves logic puzzles.  

## Background
In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles.  
  
In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.  
  
The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.  
  
For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave.”  
  
Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave.  

## File explaination
**```logic.py```**  
This file is referenced from CS50AI's files and defines several classes for different types of logical connectives. These classes can be composed within each other, so an expression like And(Not(A), Or(B, C)) represents the logical sentence stating that symbol A is not true, and that symbol B or symbol C is true (where “or” here refers to inclusive, not exclusive, or).

A function named ```model_check``` is also included. ```model_check``` takes a knowledge base and a query. The knowledge base is a single logical sentence: if multiple logical sentences are known, they can be joined together in an And expression. ```model_check``` recursively considers all possible models, and returns True if the knowledge base entails the query, and returns False otherwise.

**```puzzle.py```**   
At the top, six propositional symbols are defined. ```AKnight```, for example, represents the sentence that “A is a knight,” while ```AKnave``` represents the sentence that “A is a knave.” Similarly, propositional symbols for characters B and C are defined as well.

What follows are four different knowledge bases, ```knowledge0```, ```knowledge1```, ```knowledge2```, and ```knowledge3```, which contains the knowledge needed to deduce the solutions to the upcoming Puzzles 0, 1, 2, and 3, respectively.

**```main```**  
The main function of this ```puzzle.py``` loops over all puzzles, and uses model checking to compute, given the knowledge for that puzzle, whether each character is a knight or a knave, printing out any conclusions that the model checking algorithm is able to make.
