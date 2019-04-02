import os

from flask import Flask, render_template, jsonify, json, request, session, redirect, url_for
import pandas as pd
import pickle
import json

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

stop_list = nltk.corpus.stopwords.words('english')
stemmer = nltk.stem.porter.PorterStemmer()

classifier_saved = open("../models/classification/randomforestmodel.pickle", "rb") #binary read
classifier_load = pickle.load(classifier_saved)

from flask import request
# Creating App

def create_app(config_name):
    app = Flask(__name__, static_folder='../../static/dist',
                template_folder='../../static')

    @app.route("/")
    def index():
        return render_template('home.html')
        
    @app.route("/buyer")
    def home2():
        return render_template('buyer.html')

    @app.route('/create_task', methods=['POST'])
    def create_task():
        itemname = request.form.get('itemname')
        print(itemname)
        if itemname is None:
            task = {
                'status': False
            }
        else:
            #itemname = "natural 01 bioaqua make up profesional compact powder bedak padat"
            # text processing
            name = nltk.word_tokenize(itemname)
            name = [w.lower() for w in name]
            name = [w for w in name if re.search('^[a-z]+$',w)]
            name = [w for w in name if w not in stop_list]
            name = [stemmer.stem(w) for w in name]

            # just point towards any trained model will do, this is to get the feature identified by the best model
            colname_list = pd.read_pickle("app/colname_list")

            # creating df to put data in
            corpus = colname_list[0:0].columns.values.tolist()
            fulllist = {}
            for words in corpus:
                if words[0] in name:
                    fulllist[words[0]] = [1]
                else:
                    fulllist[words[0]] = [0]
            df = pd.DataFrame(data=fulllist)

            # running the classifier on the df
            # currently the best classifier saved as randomforestmodel.pickle, rmb to change name later if the classifier name change also
            
            category = classifier_load.predict(df)[0]     

            category_list = '{ "0": "Face Palette", "1": "Foundation", "2": "Blush On", "3": "Powder", "4": "Other Face Cosmetics", "5": "BB & CC Cream", "6": "Contour", "7": "Concealer", "8": "Highlighter", "9": "Primer", "10": "Setting Spray", "11": "Bronzer", "12": "Lipstick", "13": "Lip Tint", "14": "Lip Gloss", "15": "Lip Liner", "16": "Other Lip Cosmetics", "17": "Others", "18": "Casual Dress", "19": "Party Dress", "20": "Maxi Dress", "21": "A Line Dress", "22": "Bodycon Dress", "23": "Wedding Dress", "24": "Big Size Dress", "25": "Tshirt", "26": "Blouse", "27": "Shirt", "28": "Tanktop", "29": "Crop Top ", "30": "Big Size Top", "31": "Iphone", "32": "Samsung", "33": "Sony", "34": "Xiaomi", "35": "Others Mobile & Tablet", "36": "Blackberry", "37": "Lenovo", "38": "Nokia", "39": "Brandcode", "40": "Infinix", "41": "Oppo", "42": "Vivo", "43": "Asus", "44": "Evercoss", "45": "Advan", "46": "Huawei", "47": "Mito", "48": "Sharp", "49": "Motorola", "50": "Strawberry", "51": "Realme", "52": "Smartfren", "54": "Honor", "55": "Alcatel", "56": "Maxtron", "57": "SPC" }'
            category_list_load = json.loads(category_list)
            task = {
                'status': True,
				'itemname': itemname,
                'category': int(category),
                'category_name': category_list_load[str(category)]
            }
        
        return jsonify({'task': task})
    return app