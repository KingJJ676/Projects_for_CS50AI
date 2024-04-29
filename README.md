# Traffic  
This is an AI that identifies which traffic sign appears in a photograph.  

```
$ python traffic.py gtsrb
Epoch 1/10
500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
Epoch 2/10
500/500 [==============================] - 6s 11ms/step - loss: 2.0086 - accuracy: 0.4082
Epoch 3/10
500/500 [==============================] - 6s 12ms/step - loss: 1.3055 - accuracy: 0.5917
Epoch 4/10
500/500 [==============================] - 5s 11ms/step - loss: 0.9181 - accuracy: 0.7171
Epoch 5/10
500/500 [==============================] - 7s 13ms/step - loss: 0.6560 - accuracy: 0.7974
Epoch 6/10
500/500 [==============================] - 9s 18ms/step - loss: 0.5078 - accuracy: 0.8470
Epoch 7/10
500/500 [==============================] - 9s 18ms/step - loss: 0.4216 - accuracy: 0.8754
Epoch 8/10
500/500 [==============================] - 10s 20ms/step - loss: 0.3526 - accuracy: 0.8946
Epoch 9/10
500/500 [==============================] - 10s 21ms/step - loss: 0.3016 - accuracy: 0.9086
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535
```
## Background  



## Dropout or not
I've tried running the model with and without **a dropout layer of 0.5**, and the result and other details are as below.  
  

| With Dropdown | No Dropdown |
|:----------------------:|:--------------------:|
| ![alt text](images/image.png) | ![alt text](images/image-1.png)|
|![alt text](images/image-2.png) | ![alt text](images/image-3.png) |

First, look at the 10 epochs in the top left image. The accuracy increased stably as more epochs are done, starting from 0.48 to 0.97. Similarly, the model got an accuracy of 0.97 on the testing data set, which is reasonable. 
  
Next, look at the epochs in the top right image. The accuracy seems to be gradually increasing for the first 8 epochs, leveraging from 0.47 to 0.98. However, it endured a sudden decrease in the 9th epoch, lowering to 0.95. The accuracy went back to about 0.98 in the next epoch, but was surprisingly low on the testing data set with an accuracy of 0.94. I surmise that this is due to the happening of overfitting in the 9th epoch. Which is why the model performed really well in the 10th epoch, but rather badly on the testing data set. 
