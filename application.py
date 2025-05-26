import pickle
from flask import Flask , render_template , request , jsonify

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# for standardization
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

#####  import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb' )) 
# folder then file name  then read binary mode
standard_scaler=pickle.load(open('models/scaler.pkl','rb' ))




@app.route('/') # home page redirect

def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET' , 'POST']) # prediction page redirect
def predict_data():

    if request.method == 'POST':
            # Retrieve and convert form data
            temperature = float(request.form.get('temperature', 0))
            rh = float(request.form.get('rh', 0))
            ws = float(request.form.get('ws', 0))
            rain = float(request.form.get('rain', 0))
            ffmc = float(request.form.get('ffmc', 0))
            dmc = float(request.form.get('dmc', 0))
            isi = float(request.form.get('isi', 0))
            classes = request.form.get('classes', '').strip()
            region = request.form.get('region', '').strip()

            new_data_scaled =  standard_scaler.transform([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
            # Make prediction using the loaded model
            result = ridge_model.predict(new_data_scaled)
            
            return render_template('home.html', results=result[0])
    else:
        return render_template('home.html')




if __name__ == '__main__':
    app.run( host='0.0.0.0',debug=True)