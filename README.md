# IntentClassifier
An easy-to-use intent classifier Python Interface using Naive Bayes Classifier from Textblob

#### Make training data in the data folder with the following format in json:<br>
{<br>
  "name": (name of intent),<br>
  "utterances": [(list of training phrases)],<br>
  "responses": [(list of responses)]<br>
}<br>
#### Make testing data in the test folder:<br>
{<br>
  "tests": [{<br>
      "utterance": (phrase for test),<br>
      "intent": (intent name)<br>
    },<br>
    {<br>
      (other testing data)<br>
    } ...]<br>
}<br>
<br>
#### Create a classifier
r = IntentClassifier()
#### Train the classifier
r.train()
- make sure your data folder contains the training data
#### Test for accuracy
r.test()
- make sure your text folder contains the testing data
#### Classify a target
r.classify(text)
#### Get a response
r.response(text)
