from flask import Flask, request, render_template, url_for
from flask_restful import Resource, Api
from flask.views import MethodView
from sqlalchemy import create_engine
from json import dumps


e = create_engine('sqlite:///PaceUniversity.db')

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/students", methods= ["GET", "POST"] )
def Students():
    conn = e.connect()
    head = "All Student Info"
    query = conn.execute("select * from Student")
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return result
	

@app.route("/students/<UID>", methods= ["GET", "POST"])
def Student_UID(UID):
    conn = e.connect()
    head = "Student Info"
    query = conn.execute("select * from Student where UID='%s'"%UID)
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return result

@app.route("/students/<UID>/<Subject>", methods= ["GET", "POST"])
def SubjectGrade(UID, Subject):
    conn = e.connect()
    head = "Subject Grade"
    query = conn.execute("select * from Student where UID='{0}'and Subject1 = '{1}'".format(UID ,Subject))
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return result


if __name__ == '__main__':
    app.run(debug=True)
