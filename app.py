from flask import Flask, render_template, request, jsonify
import joblib
import re

#create a flask app
app = Flask(__name__)
#load pickle file

@app.route('/')
def Home():
    return render_template('index.html')

#standard_to = StandardScaler()

@app.route('/predict',methods=['POST'])
def predict():

    def text_preprocess(text): 
    
        # Emoticons
        text = text.replace(":/", " bad ")
        text = text.replace(":&gt;", " sad ")
        text = text.replace(":')", " sad ")
        text = text.replace(":-(", " frown ")
        text = text.replace(":(", " frown ")
        text = text.replace(":s", " frown ")
        text = text.replace(":-s", " frown ")
        text = text.replace("&lt;3", " heart ")
        text = text.replace(":d", " smile ")
        text = text.replace(":p", " smile ")
        text = text.replace(":dd", " smile ")
        text = text.replace("8)", " smile ")
        text = text.replace(":-)", " smile ")
        text = text.replace(":)", " smile ")
        text = text.replace(";)", " smile ")
        text = text.replace("(-:", " smile ")
        text = text.replace("(:", " smile ")
        text = text.replace(":/", " worry ")
        text = text.replace(":&gt;", " angry ")
        text = text.replace(":')", " sad ")
        text = text.replace(":-(", " sad ")
        text = text.replace(":(", " sad ")
        text = text.replace(":s", " sad ")
        text = text.replace(":-s", " sad ")
        text = text.replace("fu ck", "fuck")
        # Shortforms   
        text = re.sub(r'[\w]*don\'t[\w]*','do not',text)
        text = re.sub(r'[\w]*i\'ll[\w]*','i will',text)
        text = re.sub(r'[\w]*wasn\'t[\w]*','was not',text)
        text = re.sub(r'[\w]*there\'s[\w]*','there is',text)
        text = re.sub(r'[\w]*i\'m[\w]*','i am',text)
        text = re.sub(r'[\w]*won\'t[\w]*','will not',text)
        text = re.sub(r'[\w]*let\'s[\w]*','let us',text)
        text = re.sub(r'[\w]*i\'d[\w]*','i would',text)
        text = re.sub(r'[\w]*they\'re[\w]*','they are',text)
        text = re.sub(r'[\w]*haven\'t[\w]*','have not',text)
        text = re.sub(r'[\w]*that\'s[\w]*','that is',text)
        text = re.sub(r'[\w]*couldn\'t[\w]*','could not',text)
        text = re.sub(r'[\w]*aren\'t[\w]*','are not',text)
        text = re.sub(r'[\w]*wouldn\'t[\w]*','would not',text)
        text = re.sub(r'[\w]*you\'ve[\w]*','you have',text)
        text = re.sub(r'[\w]*you\'ll[\w]*','you will',text)
        text = re.sub(r'[\w]*what\'s[\w]*','what is',text)
        text = re.sub(r'[\w]*we\'re[\w]*','we are',text)
        text = re.sub(r'[\w]*doesn\'t[\w]*','does not',text)
        text = re.sub(r'[\w]*can\'t[\w]*','can not',text)
        text = re.sub(r'[\w]*shouldn\'t[\w]*','should not',text)
        text = re.sub(r'[\w]*didn\'t[\w]*','did not',text)
        text = re.sub(r'[\w]*here\'s[\w]*','here is',text)
        text = re.sub(r'[\w]*you\'d[\w]*','you would',text)
        text = re.sub(r'[\w]*he\'s[\w]*','he is',text)
        text = re.sub(r'[\w]*she\'s[\w]*','she is',text)
        text = re.sub(r'[\w]*weren\'t[\w]*','were not',text)
        
        
        # Remove punct except ! and ?
        text = re.sub(r"[,.:|(;@)-/^—#&%$<=>`~{}\[\]\'\"]+\ *", " ", text)
        # Separate out ! and ?
        text = re.sub("!", " ! ", text)
        text = re.sub("\?", " ? ", text)
    
        # Drop numbers
        text = re.sub("\\d+", " ", text)
            
        # Convert to lower
        text = text.lower()
        
        # Lots of words are not present in the fasttext embeddings. Replace them
        text = re.sub(r'[\w]*(fuc|fck|fvc|fuk|fucd)[\w]*','fuck',text)
        text = re.sub(r'[\w]*fag[\w]*','gay',text)
        text = re.sub(r'[\w]*gay[\w]*','gay',text)
        text = re.sub(r'[\w]*peni[\w]*','dick',text)
        text = re.sub(r'[\w]*(dic|dik)[\w]*','dick',text)
        text = re.sub(r'[\w]*bi[\w]*ch[\w]*','bitch',text)
        text = re.sub(r'[\w]*s[\w]*x[\w]*','sex',text)
        text = re.sub(r'[\w]*s[\w]*k[\w]*','suck',text)
        text = re.sub(r'[\w]*nigg[\w]*','suck',text)
        text = re.sub(r'[\w]*cock[\w]*','dick',text)
        text = re.sub(r'[\w]*cunt[\w]*','cunt',text)
        text = re.sub(r'[\w]*anal[\w]*','anal',text)
        text = re.sub(r'[\w]*ha{2,}[\w]*','haha',text)
        text = re.sub(r'[\w]*haha[\w]*','haha',text)
        text = re.sub(r'[\w]*wiki[\w]*','wikipedia',text)
        text = re.sub(r'[\w]*ency[\w]ia[\w]*','encyclopedia',text)   
            
        # Remove unwanted space
        text = " ".join(text.split())

        return text


    ## model
    model = joblib.load("oneverreastlog.sav")
    
    ## vectorizer
    tfidf = joblib.load("tfidfvectorizer.sav")


    text = request.form['sentiment']
    text = text_preprocess(text)
    print(text)
    vector = tfidf.transform([text])
    predicted = model.predict(vector.A)

    sentiments = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult',
       'identity_hate', 'clean']

    classified = ""

    for i, value in enumerate(predicted[0]):
        if value == 1:
            classified+=sentiments[i] + ", "

    



    return render_template('index.html', prediction_text =classified)
 
if __name__=="__main__":
    app.run(debug= True)
        