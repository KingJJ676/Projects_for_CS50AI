# Shopping
This is an AI that predicts whether online shopping customers will complete a purchase.    
```
$ python shopping.py shopping.csv
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```

## File Explanation  
**```shopping.csv```**  
This is the data set for the project and contains about 12,000 user sessions. The first seventeen columns are the _evidences_ and the last column is the _label_.  

**```shopping.py```**  
The ```main``` function loads data from a CSV spreadsheet by calling the ```load_data``` function and splits the data into a training and testing set. The ```train_model``` function is then called to train a machine learning model on the training data. Then, the model is used to make predictions on the testing data set. Finally, the ```evaluate``` function determines the sensitivity and specificity of the model, before the results are ultimately printed to the terminal.  

- **```load_data```**:  
  Accepts a CSV filename as its argument, open that file, and return a tuple (```evidence```, ```labels```). ```evidence``` is a list of all of the evidence for each of the data points, and ```labels``` is a list of all of the labels for each data point.
- **```train_model```**:  
  Accepts a list of evidence and a list of labels, and return a ```scikit-learn``` _nearest-neighbor classifier__ (a k-nearest-neighbor classifier where k = 1) fitted on that training data.
- **```evaluate```**:  
  Accepts a list of labels (the true labels for the users in the testing set) and a list of predictions (the labels predicted by your classifier), and return two floating-point values (```sensitivity```, ```specificity```).
