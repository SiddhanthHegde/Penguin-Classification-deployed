import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from datetime import date

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    inp_features = []
    features = [x for x in request.form.values()]
    if features[0] == 'Biscoe':
        inp_features.append(0)
    if features[0] == 'Dream':
        inp_features.append(1)
    if features[0] == 'Torgersen':
        inp_features.append(2)
    
    for feature in features[1:7]:
        inp_features.append(float(feature))
    
    d = features[7]
    d = d.split('-')

    inp_features.append(d[2])

    inp_features = np.array(inp_features)
    inp_features = inp_features.reshape(1,8)
    pred = model.predict(inp_features)[0]

    if pred == 0:
        category = 'Adelie Penguin (Pygoscelis adeliae)'
    if pred == 1:
        category = 'Chinstrap penguin (Pygoscelis antarctica)'
    if pred == 2:
        category = 'Gentoo penguin (Pygoscelis papua)'

    return render_template('output.html', prediction_text='Penguin Species is {}'.format(category))


if __name__ == "__main__":
    app.run(debug=True)