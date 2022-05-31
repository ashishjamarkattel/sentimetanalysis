## Toxic Comment Classification


Description

The threat of abuse and harassment online means that many people stop expressing themselves and give up on seeking different opinions. Platforms struggle to effectively facilitate conversations, leading many communities to limit or completely shut down user comments.

Dataset : jigsaw kaggle 

Labels to predict

- comment_text 	
- toxic 
- severe_toxic 	
- obscene 	
- threat 	
- insult 	
- identity_hate 	
- clean

Dealing with the Highly unbalanced data accuracy could be not the best measure but using it insted better to use 
f1 score or micro/macro average.

Since it is classification problem 

###### Model 
- logistic regression
- tree based.
- svm could be useful

For the multilabel model above should be modified to predict which can be done by OnevsRestClassifier



### Requirement.txt

```
Numpy
Sklearn
joblib
seaborn
nltk
pandas
re
flask
```

## To test 

```
git pull [repo]
cd [sentiment] (open the directory in visual studio or any text editor.)

Run app.py for visual studio or flask run in terminal

and connect to local host.

```

### Improvement 
There are various place for improvement.
    1. Vectorizer such as word2vec could have result more.
    2. Performance matrix used is accuary which could be changed to macro/micro average 
    3. Deep learning model could be much used.
    4. Classes could be much balanced.
    5. other model could be used to classifiy for the better result
### 
## Insight

```
Ram is the good boy and he is good
```
![alt text](https://github.com/ashishjamarkattel/sentimetanalysis/blob/master/moodme.PNG)

```
ram is dangerous and he might kill you and me
```
![alt text](https://github.com/ashishjamarkattel/sentimetanalysis/blob/master/toxic.png)

```
Fuck and ran away
```

![alt text](https://github.com/ashishjamarkattel/sentimetanalysis/blob/master/multiple.png)

