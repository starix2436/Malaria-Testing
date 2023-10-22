import numpy as np
from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/answer")
def answer():
    return render_template('answer.html')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    sex = int(request.form.get("sex"))
    fever = int(request.form.get("fever"))
    cold = int(request.form.get("cold"))
    rigor = int(request.form.get("rigor"))
    fatigue = int(request.form.get("fatigue"))
    headace = int(request.form.get("headace"))
    bitter_tongue = int(request.form.get("bitter_tongue"))
    vomitting = int(request.form.get("vomitting"))
    diarrhea = int(request.form.get("diarrhea"))
    Convulsion = int(request.form.get("Convulsion"))
    Anemia = int(request.form.get("Anemia"))
    jundice = int(request.form.get("jundice"))
    cocacola_urine = int(request.form.get("cocacola_urine"))
    hypoglycemia = int(request.form.get("hypoglycemia"))
    prostraction = int(request.form.get("prostraction"))
    hyperpyrexia = int(request.form.get("hyperpyrexia"))

    # prediction=np.array([[sex,fever,cold,rigor,fatigue,headace,bitter_tongue,vomitting,diarrhea,Convulsion,Anemia,jundice,cocacola_urine,hypoglycemia,prostraction,hyperpyrexia]])
    model = pickle.load(open('model.pkl', 'rb'))
    # preds=model.predict(prediction)
   # if(preds>0.50):
    # pd="You have got Maleria"
   # else:
    # pd="You dont have Maleria"

    # return render_template('answer.html', prediction_text=pd)
    if (sex == 1):
        prediction = np.array([[fever, cold, rigor, fatigue, headace, bitter_tongue, vomitting, diarrhea,
                              Convulsion, Anemia, jundice, cocacola_urine, hypoglycemia, prostraction, hyperpyrexia, 0, 1]])
        preds = model.predict(prediction)
        if preds == 1:
            pd = "Your test has detected the presence of Malaria.\n Kindly Consult the nearest Doctor"
        else:
            pd = "Your test has not detected any presence of Malaria.\nBut still confirm the nearest Doctor"
    else:
        prediction = np.array([[fever, cold, rigor, fatigue, headace, bitter_tongue, vomitting, diarrhea,
                              Convulsion, Anemia, jundice, cocacola_urine, hypoglycemia, prostraction, hyperpyrexia, 1, 0]])
        preds = model.predict(prediction)
        if preds == 1:
            pd = "Your test has detected the presence of Malaria.\n Kindly Consult the nearest Doctor"
        else:
            pd = "Your test has not detected any presence of Malaria.\nBut still confirm the nearest Doctor"

    return render_template('result.html', prediction_text=pd)


if __name__ == "__main__":
    app.run(debug=True)
