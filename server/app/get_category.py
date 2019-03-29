import pandas as pd
import pickle

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

stop_list = nltk.corpus.stopwords.words('english')
stemmer = nltk.stem.porter.PorterStemmer()


from flask import request

@app.route('/create_task', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        task = {
            'status': 'False'
        }
    else:
        itemname = "natural 01 bioaqua make up profesional compact powder bedak padat"
        # text processing
        name = nltk.word_tokenize(itemname)
        name = [w.lower() for w in name]
        name = [w for w in name if re.search('^[a-z]+$',w)]
        name = [w for w in name if w not in stop_list]
        name = [stemmer.stem(w) for w in name]

        # just point towards any trained model will do, this is to get the feature identified by the best model
        X_train = pd.read_pickle("../models/classification/X_train_best_choice_7")

        # creating df to put data in
        corpus = X_train[0:0].columns.values.tolist()
        fulllist = {}
        for words in corpus:
            if words[0] in name:
                fulllist[words[0]] = [1]
            else:
                fulllist[words[0]] = [0]
        df = pd.DataFrame(data=fulllist)

        # running the classifier on the df
        # currently the best classifier saved as logregmodel.pickle, rmb to change name later if the classifier name change also
        classifier_saved = open("../models/classification/logregmodel.pickle", "rb") #binary read
        classifier_load = pickle.load(classifier_saved)
        category = classifier_load.predict(df)[0]        
        task = {
            'status': 'True',
            'category': category
        }
        
    tasks.append(task)
    return jsonify({'task': task}), 201
    
    
# itemname = "natural 01 bioaqua make up profesional compact powder bedak padat"
# # text processing
# name = nltk.word_tokenize(itemname)
# name = [w.lower() for w in name]
# name = [w for w in name if re.search('^[a-z]+$',w)]
# name = [w for w in name if w not in stop_list]
# name = [stemmer.stem(w) for w in name]
# 
# X_train = pd.read_pickle("../models/classification/X_train_best_choice_7")
# 
# # creating df to put data in
# corpus = X_train[0:0].columns.values.tolist()
# fulllist = {}
# for words in corpus:
#     if words[0] in name:
#         fulllist[words[0]] = [1]
#     else:
#         fulllist[words[0]] = [0]
# df = pd.DataFrame(data=fulllist)
# 
# # running the classifier on the df
# classifier_saved = open("../models/classification/logregmodel.pickle", "rb") #binary read
# classifier_load = pickle.load(classifier_saved)
# category = classifier_load.predict(df)[0]
# print(category)