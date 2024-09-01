from flask import Flask, render_template, url_for, request
import joblib
import sqlite3

model_file_path = ".\\models\\bernolinaivebayes.lb"
model = joblib.load(model_file_path)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/thank.html')
def thank():
    return render_template('thank.html')

if __name__ == "__main__":
    app.run(debug=True)