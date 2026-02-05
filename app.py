from flask import Flask, request,render_template
import pandas as pd
import numpy as np
import pickle


df =pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


#flask app
app = Flask(__name__)

#paths
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/recom',methods=['POST'])
def mysong():
    pass

if __name__ == "__main__":
    app.run(debug=True)