import csv
import itertools
import sys
import math

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def person_info(people, one_gene, two_genes, have_trait):
        """
        returns a dict including: a person's "gene number", "trait or not", "parent or not"
        """
        members = {}
        for person in people:
            info = {
                  "gene_number": 1 if person in one_gene else 2 if person in two_genes else 0,
                  "trait": True if person in have_trait else False,
                  "parents": True if people[person]["father"] != None and people[person]["mother"] != None else False
            }

            members[person] = info
        return members
    

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # knowing a person's "gene number" and "trait or not"
    info = person_info(people, one_gene, two_genes, have_trait)

    # calculate probability of having that number of genes
    probabilities = {}
    for person in info:

        # no parent
        if info[person]["parents"] == False:
            # formula: PROBS["gene"][gene_number] * PROBS["trait"][gene_number][trait]
            p = PROBS["gene"][info[person]["gene_number"]] * PROBS["trait"][info[person]["gene_number"]][info[person]["trait"]]
        
        # have parent
        elif info[person]["parents"] == True:
            father = info[people[person]["father"]]["gene_number"] # father's gene_number
            mother = info[people[person]["mother"]]["gene_number"] # mother's gene_number
            
            # gene=2
            if info[person]["gene_number"] == 2:
                
                # father
                if father == 0:
                    a = PROBS["mutation"]
                elif father == 1:
                    a = 0.5
                else:
                    a = 1 - PROBS["mutation"]

                # mother
                if mother == 0:
                    b = PROBS["mutation"]
                elif mother == 1:
                    b = 0.5
                else:
                    b = 1 - PROBS["mutation"]
                
                # calculate probability for have trait & no trait
                if info[person]["trait"] == True:
                    p = a * b * PROBS["trait"][2][True]
                else:
                    p = a * b * PROBS["trait"][2][False]
            
            # gene = 1
            elif info[person]["gene_number"] == 1:

                # A: father provides gene, mother does not
                # father provides gene
                if father == 0:
                    Aa = PROBS["mutation"]
                elif father == 1:
                    Aa = 0.5
                else:
                    Aa = 1 - PROBS["mutation"]
                # mother does not provide gene
                if mother == 0:
                    Ab = 1 - PROBS["mutation"]
                elif mother == 1:
                    Ab = 0.5
                else:
                    Ab = PROBS["mutation"]
                
                A = Aa * Ab

                # B: that 1 gene from mother
                # father does not provide gene
                if father == 0:
                    Ba = 1 - PROBS["mutation"]
                elif father == 1:
                    Ba = 0.5
                else:
                    Ba = PROBS["mutation"]
                # mother provides gene
                if mother == 0:
                    Bb = PROBS["mutation"]
                elif mother == 1:
                    Bb = 0.5
                else:
                    Bb = 1 - PROBS["mutation"]
                
                B = Ba * Bb
                
                # calculate probability for have trait & no trait
                if info[person]["trait"] == True:
                    p = (A + B) * PROBS["trait"][1][True]
                else:
                    p = (A + B) * PROBS["trait"][1][False]
                
            # gene = 0
            elif info[person]["gene_number"] == 0:
                
                # father 
                if father == 0:
                    a = 1 - PROBS["mutation"]
                elif father == 1:
                    a = 0.5
                else:
                    a = PROBS["mutation"]

                # mother
                if mother == 0:
                    b = 1 - PROBS["mutation"]
                elif mother == 1:
                    b = 0.5
                else:
                    b = PROBS["mutation"]
                
                # calculate probability for have trait & no trait
                if info[person]["trait"] == True:
                    p = a * b * PROBS["trait"][0][True]
                else:
                    p = a * b * PROBS["trait"][0][False]
            
            else:
                raise ValueError("Error when calculating gene probability")
        else:
            raise ValueError("Error when calculating gene probability")
        
        probabilities[person] = p

    # given all persons' joint probability, calculate joint P of all these happening together
    joint_probability = math.prod(probabilities.values())
    return joint_probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:

        # update gene distribution
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p

        # update trait distribution
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    for person in probabilities:

        # normalize gene distribution
        Sum_g = sum(probabilities[person]["gene"].values())
        a = 1 / Sum_g
        for d in probabilities[person]["gene"]:
            probabilities[person]["gene"][d] *= a
            
        # normalize trait distribution
        Sum_t = sum(probabilities[person]["trait"].values())
        b = 1 / Sum_t
        probabilities[person]["trait"][True] *= b
        probabilities[person]["trait"][False] *= b


if __name__ == "__main__":
    main()
