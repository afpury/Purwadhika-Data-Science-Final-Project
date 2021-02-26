# Dashboard for predict target
from flask import Flask, render_template, request, url_for, redirect
import pickle
import pandas as pd

app= Flask(__name__)

# halaman index
@app.route('/')
def index():
    return render_template('index.html')

# halaman businessinsight
@app.route('/businessinsight', methods=['POST', 'GET'])
def businessinsight():
    return render_template('businessinsight.html')

# halaman result
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form
        df_to_predict = pd.DataFrame({
            'age':[input['age']],
            'job':[input['job']],
            'marital':[input['marital']],
            'education':[input['education']],
            'default':[input['default']],
            'balance':[input['balance']],
            'housing':[input['housing']],
            'loan':[input['loan']],
            'contact':[input['contact']],
            'day':[input['day']],
            'month':[input['month']],
            'campaign':[input['campaign']],
            'pdays':[input['pdays']],
            'previous':[input['previous']]
        }, index = [0])
        
        prediksi = model.predict(df_to_predict)
            
        if prediksi == 0:
            hasil = "not subscribe."
        else:
            hasil = "subscribe."
        return render_template('result.html', data = input, pred = hasil)

if __name__ == '__main__' :

    filename = 'model.sav'
    model = pickle.load(open(filename,'rb'))
    app.run(debug=True)