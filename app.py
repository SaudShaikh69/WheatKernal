import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import sklearn
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = pickle.load(open('./Save_Model/SVCModel.pkl', 'rb'))
print(model)

db = psycopg2.connect(host="ec2-44-194-232-228.compute-1.amazonaws.com",user="iiicvzcgbwvtdm",password="3c6fb0b05066a7b9bb5bfa90772e0d53087442dc43506d6160237e11dfc5ed95",database="d4c5toomeitbr4")
cur = db.cursor()
cur.execute("create table if not exists wheatkernel1(area NUMERIC(6,3),perimeter NUMERIC(6,3), "
            "compactness NUMERIC(6,3),kernellength NUMERIC(6,3),kernelwidth NUMERIC(6,3),asymmetriccoeff NUMERIC(6,3), "
            "kernelcoefflen NUMERIC(6,3), wheattype VARCHAR(20))")
db.commit()

@cross_origin()
@app.route('/', methods=['GET'])
def home():
    print("Inside home page")
    return render_template('./index.html')

@cross_origin()
@app.route('/home/info', methods=['GET'])
def info():
    return render_template('./infopage.html')

@cross_origin()
@app.route('/home/developer', methods=['GET'])
def Developer():
    return render_template('./Developerpage.html')

@cross_origin()
@app.route('/home/contact', methods=['GET'])
def Contact():
    return render_template('./Contactpage.html')

@cross_origin()
@app.route('/index',methods=['GET'])
def index_page():
    print("Inside Index Page")
    return render_template('./index1.html')


@cross_origin()
@app.route('/home/how-to-use',methods=['GET'])
def how_to():
    return render_template('./how_to.html')


@cross_origin()
@app.route('/index/predict',methods=['POST','GET'])
def predict():
    print("Inside model")
    if request.method == 'POST':
        print("inside model")
        area = float(request.form['Area'])
        perimeter = float(request.form['Perimeter'])
        compactness = float(request.form['Compactness'])
        length_kernel = float(request.form['Length Of Kernel'])
        kernel_width = float(request.form['Width Of Kernel'])
        asym_co = float(request.form['Asymmetry Coefficient'])
        kernel_coeff_len = float(request.form['Len.Kernel Groove'])
        print(area)

        cols = ([[area, perimeter, compactness, length_kernel, kernel_width, asym_co, kernel_coeff_len]])
        cols = np.array(cols)
        print(area)
        feat = cols
        print(feat)
        predictions = model.predict(feat)

        output = predictions

        print(output)

        col1 = float(request.form['Area'])
        col2 = float(request.form['Perimeter'])
        col3 = float(request.form['Compactness'])
        col4 = float(request.form['Length Of Kernel'])
        col5 = float(request.form['Width Of Kernel'])
        col6 = float(request.form['Asymmetry Coefficient'])
        col7 = float(request.form['Len.Kernel Groove'])
        type1 = "Kama"
        type2 = "Rosa"
        type3 = "Canadian"

        if output == 1:
            cur.execute(f"insert into wheatkernel1 values{(col1, col2, col3, col4, col5, col6, col7, type1)}")
            db.commit()
            return render_template('./index2.html', Prediction_text="The Wheat Kernel is of type Kama")
        elif output == 2:
            cur.execute(f"insert into wheatkernel1 values{(col1, col2, col3, col4, col5, col6, col7, type2)}")
            db.commit()
            return render_template('./index2.html', Prediction_text="The Wheat Kernel is of type Rosa")
        else:
            cur.execute(f"insert into wheatkernel1 values{(col1, col2, col3, col4, col5, col6, col7, type3)}")
            db.commit()
            return render_template('./index2.html', Prediction_text="The Wheat Kernel is of type Canadian")

    else:
        return render_template('./index.html')


if __name__ == "__main__":
    app.run(debug=True)
