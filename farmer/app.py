from flask import Flask , render_template,url_for,request
import pandas as pd 
import joblib 
import sqlite3
from pymongo import MongoClient
std_scaler = joblib.load('./models/std_scaler.lb')
kmeans_model = joblib.load('./models/kmeans_model.lb')
df = pd.read_csv("./models/filter_crops.csv")
app = Flask(__name__) 

connection_string= "mongodb+srv://nishamdb05:UyL2JNa3NR9X2uA0@cluster0.qfyfq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
# database , collection 
database = client["Farmer2"]    # database 
collection = database['FarmerData1']  # table create or collection 

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/home.html')
def home():
    return render_template('home.html') 

@app.route('/output.html')
def output():
    return render_template('output.html') 

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/about_crops.html')
def about_crops():
    return render_template('about_crops.html')

@app.route('/predict',methods=['GET','POST'])
def predict(): 
    if request.method == 'POST': 
        N = int(request.form['N'])
        PH = float(request.form['PH'])
        P = int(request.form['P'])
        K = int(request.form['K'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])   # type == number >> text 
        UNSEEN_DATA = [[N,P,K,temperature,humidity,PH,rainfall]] 
        transformed_data = std_scaler.transform(UNSEEN_DATA)
        cluster = kmeans_model.predict(transformed_data)[0]
        suggestion_crops = list(df[df['cluster_no'] == cluster]['label'].unique())
        data = {"N":N,"P":P,"K":K,"temperature":temperature,"humidity":humidity,"PH":PH,"rainfall":rainfall}
        data_id = collection.insert_one(data).inserted_id
        print("Your data is inserted into the mongodb your record id is : ",data_id)
        return render_template('output.html', crops=suggestion_crops)
    
   








@app.route('/thankyou.html')
def thanks():
   return render_template('thankyou.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ =="__main__":
    app.run(debug=True) 


  