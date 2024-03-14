from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either knight or knave
    Or(AKnight, AKnave), 
    # if A is knight, then A's sentence is true. 
    Or(Not(AKnight), And(AKnight, AKnave)),
    # if A is knave, then A's sentence is false.
    Or(Not(AKnave), Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And( 
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    # if A is knight, then A's sentence is true.
    Or(Not(AKnight), And(AKnave, BKnave)),
    # if A is knave, then A's sentence is false.
    Or(Not(AKnave), Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    # if A is knight, then true.
    Or(Not(AKnight), Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # if A is knave, then false.
    Or(Not(AKnave), Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # if B is kinght, then true.
    Or(Not(BKnight), Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    # if B is knave, then false.
    Or(Not(BKnave), Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    # if A is knight, then one of two sentences is true.
    Or(Not(AKnight), Or(AKnight, AKnave)),
    # if A is knave, then one of two sentences is false.
    Or(Not(AKnave), Not(Or(AKnight, AKnave))),
    # if B is knight, then B1 true.
    Or(Not(BKnight), AKnave),
    # if B is knave, then B1 false.
    Or(Not(BKnave), Not(AKnave)),
    # if B is knight, then B2 true.
    Or(Not(BKnight), CKnave),
    # if B is knave, then B2 false.
    Or(Not(BKnave), Not(CKnave)),
    # if C is knight, then true.
    Or(Not(CKnight), AKnight),
    # if C is knave, then false.
    Or(Not(CKnave), Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
