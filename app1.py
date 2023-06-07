from flask import  Flask, render_template, url_for, request, redirect
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
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        #The above will create a new task

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Kulikuwa na issue bro'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        #Above will return all contents in order by which date they were created
        return render_template('index1.html', tasks=tasks)
#The above is the main function of the application. The render_template('...') connects this file to the html file to return what is on that html file

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting the task'
#The above is a route and function respectively created for deleting a task

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Kulikuwa na issue ku-update buda"
    else:
        return render_template('update.html',task=task)

if __name__== '__main__':
    app.run()

#The above code allows us to start/run the application