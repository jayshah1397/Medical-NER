from flask import Flask
from flask import request
from flask import jsonify
import json
import pickle
import spacy

# Define a flask app
app = Flask(__name__)

#model = load_model("C:/Users/jaysh/OneDrive/Desktop/Technical/ColumbiaMedicalNER")
with open("Pickle_Ner_Model.pkl", 'rb') as file:  
    model_ner = pickle.load(file)



@app.route('/result', methods=['POST'])
def model_pred():
    # Main page
    result=request.form.get("mysentence")

    a=[]
    doc = model_ner(result)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        a.append(ent.text+ " "+ str(ent.start_char)+ " "+str(ent.end_char)+" "+ent.label_)
    print(a)
    response = app.response_class(
        response=json.dumps(a),
        status=200,
        mimetype='application/json'
    )
    print(result)
    #return render_template("index2.html")
    return response


@app.route('/',methods=['GET'])
def index():
	print("hello")
	return app.send_static_file("index.html")