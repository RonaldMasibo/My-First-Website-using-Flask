from flask import  Flask, render_template, url_for, request
#This imports flask
#render-template enables the code to recognise there is a folder for template for reading the html file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
with app.app_context():
    db = SQLAlchemy(app)
#The above initialises our DB

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    #The function below will return a string anytime we create a new element
    def __repr__(self):
        return '<Task %r>' % self.id
    

app.debug = True
#This enables us not to keep restarting the server

@app.route('/', methods=['POST', 'GET'])
#The above creates a route for the server

def index():
    if request.method == 'POST':
        return 'HAAARROOO!!'

    else:
        return render_template('index1.html')
#The above is the main function of the application. The render_template('...') connects this file to the html file to return what is on that html file

if __name__== '__main__':
    app.run()

#The above code allows us to start/run the application