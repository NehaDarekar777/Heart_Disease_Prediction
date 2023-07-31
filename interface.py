from flask import Flask, request, jsonify, render_template,redirect,url_for
from utils import HeartDisease
import config
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    # return jsonify({"Result":"Successful"})
    return render_template('index.html')

@app.route('/predict_heart_disease', methods = ['POST'])
def predict_heart_disease():
      try:
        data = request.form
        print("Data:", data)
    
        age      = eval(data['age'])
        sex      = eval(data['sex'])
        cp       = eval(data['cp'])
        trtbps   = eval(data['trtbps'])
        chol     = eval(data['chol'])
        fbs      = eval(data['fbs'])
        restecg  = eval(data['restecg'])
        thalachh = eval(data['thalachh'])
        exng     = eval(data['exng'])
        oldpeak  = eval(data['oldpeak'])
        slp      = eval(data['slp'])
        caa      = eval(data['caa'])
        thall    = eval(data['thall'])
            
        Obj = HeartDisease(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)
        heart_disease_pred = Obj.get_heart_disease_pred()

        # return jsonify({"Result":f"Heart Disease Prediction == {heart_disease_pred}"})

        return render_template('index.html', prediction = heart_disease_pred)
        
      except:
        print(traceback.print_exc())
        return redirect(url_for('/'))

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER)