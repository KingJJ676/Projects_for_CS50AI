# Parser
This is an AI that parse sentences and extract noun phrases.
```
$ python parser.py
Sentence: Holmes sat.
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat

Noun Phrase Chunks
holmes
```
  
## File Explanation
**The ```sentences``` directory**  
There are ten files in this directory, each containing an English sentence. The AI can be tested on these data sets.  

**```parser.py```**   
The _context free grammar_ are predefinied by the CS50 staff team. Yet, I am the one who definied the _NONTERMINALS_ grammar rules.   

**```main.py```**  
This function first accepts a sentence as input, either from a file or via user input. The sentence is preprocessed and then parsed according to the context-free grammar defined by the file. The resulting trees are printed out, and all of the “noun phrase chunks” are printed as well. Note that a "noun phrase chunk" is a noun phrase that doesn’t contain other noun phrases within it.  

**```np_chunk```**  
This function accept a ```tree``` representing the syntax of a sentence, and return a list of all of the noun phrase chunks in that sentence.
