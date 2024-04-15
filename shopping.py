import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - + 0 Administrative, an integer
        - 1 Administrative_Duration, a floating point number
        - + 2 Informational, an integer
        - 3 Informational_Duration, a floating point number
        - + 4 ProductRelated, an integer
        - 5 ProductRelated_Duration, a floating point number
        - 6 BounceRates, a floating point number
        - 7 ExitRates, a floating point number
        - 8 PageValues, a floating point number
        - 9 SpecialDay, a floating point number
        - *10 Month, an index from 0 (January) to 11 (December)
        - + 11 OperatingSystems, an integer
        - + 12 Browser, an integer
        - + 13 Region, an integer
        - + 14 TrafficType, an integer
        - *15 VisitorType, an integer 0 (not returning) or 1 (returning)
        - *16 Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # open file
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        
        # define two lists to store return values
        all_evidences = []
        all_labels = []

        # define target datatypes
        months = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}
        ints = [0, 2, 4, 11, 12, 13, 14]
        floats = [1, 3, 5, 6, 7, 8, 9]
        VisitorType = {'Returning_Visitor': 1, 'New_Visitor': 0}
        Weekend = {'TRUE': 1, 'FALSE': 0}

        # skip header row
        next(rows)

        # read each row and record evidence into respective_evidences        
        for row in rows:
            respective_evidences = []
            for i in range(len(row) - 1):

                # modify month, Visitortype, weekend to int 
                if i == 10:
                    respective_evidences.append(months.get(row[i], row[i]))
                elif i == 15:
                    respective_evidences.append(VisitorType.get(row[i], row[i]))
                elif i == 16:
                    respective_evidences.append(Weekend.get(row[i], row[i]))

                # modify elements to int or float
                elif i in ints:
                    respective_evidences.append(int(row[i]))
                elif i in floats:
                    respective_evidences.append(float(row[i]))
                else:
                    raise ValueError('unexpected value in load_data')
                    
            # append respective_evidences into all_evidences
            all_evidences.append(respective_evidences)

            # append label into all_labels
            all_labels.append(1 if row[-1] == 'TRUE' else 0)

    # return result
    return (all_evidences, all_labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors = 1)
    return neigh.fit(evidence, labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    positive_correct, positives, negative_correct, negatives = 0, 0, 0, 0

    # calculate positive & negative correct rate
    for i in range(len(labels)):
        if labels[i] == 1:
            positives += 1
            if predictions[i] == 1:
                positive_correct += 1
        else:
            negatives += 1
            if predictions[i] == 0:
                negative_correct += 1

    # calculate sensitivity and specificity
    sensitivity = float(positive_correct / positives)
    specificity = float(negative_correct / negatives)

    # return result
    return (sensitivity, specificity)

if __name__ == "__main__":
    main()
