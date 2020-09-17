import pickle

from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__, template_folder='templates')
pipe = pickle.load(open('model/pipe.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    args = request.form
    print(args)
    new = pd.DataFrame({
        'age': [args.get('age')],
        'education': [args.get('education')],
        'gender': [args.get('gender')]
    })
    prediction = round(float(pipe.predict(new)[0]), -4)
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
