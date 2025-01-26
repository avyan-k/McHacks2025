from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)
import secrets
foo = secrets.token_urlsafe(16)
app.secret_key = foo
from os.path import dirname, abspath, join
import sys
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(join(parent_dir, 'src'))
import database
import task
sys.path.append(current_dir)




class TaskForm(FlaskForm):
    name = StringField('Task name', validators=[DataRequired(), Length(5, 40)])
    deadline = DateField('Deadline', format='%d-%m-%Y')
    estimated_time = StringField('Estimated Hours', validators=[DataRequired(), Length(1, 6 )])
    priority = StringField('Priority', validators=[DataRequired(), Length(1 , 2)])
    submit = SubmitField('Submit')
WEB_QUEUE = []
@app.route('/', methods=['GET', 'POST'])
def home():
    form = TaskForm()
    if form.validate_on_submit():
        form_task = task.Task(form.name.data,form.deadline.data,form.estimated_time.data,form.priority.data)
        WEB_QUEUE.append(form_task)
        form_task = TaskForm(formdata=None)
    connection = database.open_database()
    tasks_dict = {}
    tasks_dict["incoming"] = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.INCOMING)]
    tasks_dict["incomplete"]  = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.INCOMPLETE)]
    tasks_dict["ongoing"]  = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.ONGOING)]
    tasks_dict["complete"]  = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.COMPLETE)]

    return render_template("desk.html",tasks_dict = tasks_dict, form = form)

@app.route('/', methods =["GET", "POST"])
def get_new_task():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+first_name + last_name
    return render_template("form.html")

if __name__ == "__main__" :
 app.run(debug=True) #detect changes and update


