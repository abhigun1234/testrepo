from flask import Flask,request,jsonify
from flask import render_template
from database.dbhelper import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/coursedetails',methods = ['POST', 'GET'])
def getCourseDetails():
   str={
  "courses": [
    {
      "duration": 3500,
      "id": 1, "name": "ANDROID"
    }
  ]
}
   courselist=[]
   courseDict={}
   #courselist=allCourses()
   courseDict={"courses":courselist}
   #return jsonify(courseDict)
   return jsonify(str)
@app.route('/fetchAllCourseDetails')
def fetchallCourse():
 data=allCourses()
 return jsonify(data)


if __name__ == "__main__":
  app.run()