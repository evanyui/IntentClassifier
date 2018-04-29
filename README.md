# IntentClassifier
An easy-to-use intent classifier Python Interface using Naive Bayes Classifier from Textblob

#### Make training data in the data folder with the following format in json:<br>
```javascript
{
  "name": (name of intent),
  "utterances": [(list of training phrases)],
  "responses": [(list of responses)]
}
```
#### Make testing data in the test folder:<br>
```javascript
{
  "tests": [
    {
      "utterance": (phrase for test),
      "intent": (intent name)
    },
    {
      (other testing data)
    } ...]
}
```
<br>

___

#### Create a classifier
```python
r = IntentClassifier()
```
#### Train the classifier
```python
r.train()
```
- make sure your data folder contains the training data
#### Test for accuracy
```
r.test()
```
- make sure your text folder contains the testing data
#### Classify a target
```python
r.classify(text)
```
#### Get a response
```python
r.response(text)
```
