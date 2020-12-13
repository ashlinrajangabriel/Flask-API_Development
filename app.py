import flask
from flask import request,render_template, jsonify
import sqlite3
import pandas as pd
from flask import Markup

app = flask.Flask(__name__ , template_folder='templates')
app.config["DEBUG"] = True

#UPLOAD

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        #df.set_index(['OrderDate'], inplace=True)
        df.index.name=None
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%Y-%M-%d') 

        summary = df.describe() 



        return render_template('index.html', shape=df.shape, columns = df.columns,correlation = df.corr().to_json() ,tables=[df.dtypes.to_frame().to_html(),summary.to_html(),df.to_html(),df.corr().to_html()],shape_of_data = 'shape of data',titles = ['','DataType of data','Description','DataPreview','Correlation Coefficient'])
    return render_template("index.html")



app.run()