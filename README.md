## Dropout or not
I've tried running the model with and without **a dropout layer of 0.5**, and the result and other details are as below.  
  

| With Dropdown | No Dropdown |
|:----------------------:|:--------------------:|
| ![alt text](image.png) | ![alt text](image-1.png)|
|![alt text](image-2.png) | ![alt text](image-3.png) |

First, look at the 10 epochs in the top left image. The accuracy increased stably as more epochs are done, starting from 0.48 to 0.97. Similarly, the model got an accuracy of 0.97 on the testing data set, which is reasonable. 
  
Next, look at the epochs in the top right image. The accuracy seems to be gradually increasing for the first 8 epochs, leveraging from 0.47 to 0.98. However, it endured a sudden decrease in the 9th epoch, lowering to 0.95. The accuracy went back to about 0.98 in the next epoch, but was surprisingly low on the testing data set with an accuracy of 0.94. I surmise that this is due to the happening of overfitting in the 9th epoch. Which is why the model performed really well in the 10th epoch, but rather badly on the testing data set. 
