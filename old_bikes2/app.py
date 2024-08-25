from flask import Flask,render_template,url_for,request,redirect
import joblib


model = joblib.load('./models/linearRegression.lb')
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/output.html')
def output():
    return render_template('output.html')



@app.route('/userdata',methods=['GET','POST'])
def userdata():
    if request.method =='POST':
        username=request.form['username']
        useremail=request.form['useremail']
        usermsg=request.form['usermsg']
        user_received_data= [username,useremail,usermsg]
          # Store the user data in a text file
        with open('userdata.txt', 'a') as file:
            file.write(f"Username: {username}\n")
            file.write(f"Email: {useremail}\n")
            file.write(f"Message: {usermsg}\n")
            file.write("-----------------\n")
        return user_received_data
@app.route('/thankyou.html')
def thanks():
   return render_template('thankyou.html')
@app.route('/survey.html')
def survey():
    return render_template('survey.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# @app.route('/thankyou.html')
# def thankyou():
#     return render_template('thankyou.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method =='POST':
      brand_name = int(request.form ["brand_name"])
      Kms_Driven = int(request.form ["Kms_Driven"]  )
      owner = int(request.form ["owner"]  )
      age = int(request.form ["age"]  )  
      power = int(request.form ["power"] )

    brand_dict = {'Bajaj': 1,'Royal Enfield': 2,'Hero': 3,'Honda': 4,'Yamaha': 5,'TVS': 6,
                        'KTM': 7,'Suzuki': 8,'Harley-Davidson': 9,'Kawasaki': 10,'Hyosung': 11,
                        'Mahindra': 12,'Benelli': 13,'Triumph': 14,'Ducati': 15,'BMW': 16}
                
    brand_dict2 = {value:key  for key, value in brand_dict.items()}
    print(brand_dict2) 

    unseen_data=[[Kms_Driven,owner,age,power,brand_name]]
    PREDICTION = model.predict(unseen_data)[0][0]   # array([25421.25421])
    
    return render_template('output.html', 
                           bike_type=brand_dict2[brand_name], 
                           owner=owner, 
                           kilometers_driven=Kms_Driven, 
                           years_used=age, 
                           power=power, 
                           prediction_text=int(PREDICTION))


if __name__ =="__main__":
    app.run(debug=True)