from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from konlpy.tag import Okt
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, KFold

chatbot = pd.read_csv('chatbotA.csv',index_col = 0, encoding = 'EUC-KR')
okt = Okt()

def tw_tokenizer(text):
    tokens_ko = okt.morphs(text)
    return tokens_ko

Tfidf_vect = TfidfVectorizer(tokenizer = tw_tokenizer ,
                             max_df = 0.9,
                             min_df = 0,
                             stop_words= None,
                             max_features = 10000,
                            )

Tfidf_vect_morphs = Tfidf_vect.fit_transform(metrix['comment'])



xgb_clf = XGBClassifier(booster = 'gbtree', max_depth = 1, gamma = 100,
                    n_estimators = 300, random_state = 42, learning_rate = 0.5)

xgb_clf.fit(train, label)


from flask import Flask, request

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    x = request.form['left']
    qus = xgb_clf.predict(Tfidf_vect.transform([x]))
    
    
    if int(qus) == 1:
        if x.find('동아리') >= 0:
            return chatbot['intent'][0]
        elif x.find('졸업조건')>= 0 or x.find('졸업요건') >= 0:
            return chatbot['intent'][1]
        elif x.find('증명서') >=0:
            return chatbot['intent'][2]
        elif x.find('학교일정') >= 0 or x.find('학사일정') >=0:
            return chatbot['intent'][3]
        elif x.find('성적장학금') >= 0 or x.find('장학금') >=0:
            return chatbot['intent'][4]
        elif x.find('주차장') >=0:
            return chatbot['intent'][6]
        elif x.find('행정반') >=0:
            return chatbot['intent'][14]
        elif x.find('달구지') >=0:
            return chatbot['intent'][5]
        elif x.find('휴학신청') >=0 or x.find('휴학')>=0:
            return chatbot['intent'][11]
        elif x.find('미용실') >= 0:
            return chatbot['intent'][12]
        elif x.find('학생증') >=0:
            return chatbot['intent'][13]
        elif x.find('카페') >=0:
            return chatbot['intent'][15]
        elif x.find('힐링존') >=0:
            return chatbot['intent'][16]
        elif x.find('열람실')>=0:
            return chatbot['intent'][17]
        elif x.find('와이파이')>=0 or x.find('wifi') >=0 or x.find('WIFI') >=0:
            return chatbot['intent'][18]
        elif x.find('pc방') >= 0 or x.find('피방') >=0 or x.find('피시방')>=0:
            return chatbot['intent'][9]
        else :
            return '예상 질문에 없어요 ㅠㅠ.'
            
    elif int(qus) == 2:
        return '교양 관련 질문인가요?'
    elif int(qus) == 3:
        return '필수교양 관련 질문인가요?'
    elif int(qus) == 4:
        return '학과 관련 질문인가요?'
    elif int(qus) == 5:
        return '학과 관련 질문인가요?'
    elif int(qus) == 6:
        return '학과 관련 질문인가요?'
    elif int(qus) == 7:
        return '학과 관련 질문인가요?'
    elif int(qus) == 8:
        return '학과 관련 질문인가요?'
    
    else:
        return '0번입니다.'


@app.route('/multiply', methods=['POST'])
def multiply():
    left = request.form['left']
    rite = request.form['rite']

    return str(int(left) * int(rite))


if __name__ == '__main__':
    app.run()
