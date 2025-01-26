from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
from os.path import dirname, abspath, join
import sys
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(join(parent_dir, 'src'))
import database
import task
sys.path.append(current_dir)

@app.route("/")
def home():
    connection = database.open_database()
    tasks_dict = {}
    tasks_dict["incoming"] = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.INCOMING)]
    tasks_dict["incomplete"]  = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.INCOMPLETE)]
    tasks_dict["ongoing"]  = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.ONGOING)]
    tasks_dict["complete"]  = [ctask.name for ctask in database.get_all_tasks_of_status(connection,task.Status.COMPLETE)]

    return render_template("desk.html",tasks_dict = tasks_dict)


if __name__ == "__main__" :
 app.run(debug=True) #detect changes and update


