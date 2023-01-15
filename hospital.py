

from flask import Flask, render_template,redirect,request

from database2 import fetchdata,adddata,specificdata,updatedata,deletedata
app=Flask(__name__,template_folder='template')#create object of flask class
@app.route("/")
def home1():
    return render_template("home1.html")



@app.route("/aboutuslink")
def aboutus():
    return render_template("aboutus.html")

@app.route("/maplink")
def map():
    return render_template("map.html")


@app.route("/appointmentbookinglink")
def appointmentbooking():
    return render_template("appointmentbooking.html")


@app.route("/activitylink")
def activity():
    return render_template("activity.html")

@app.route("/showlink")
def showfun():
    datalist=fetchdata()
    return render_template("show.html",data=datalist)





@app.route("/savelink1",methods=["POST"])
def save1():
    name=request.form["uname"]
    email=request.form["email"]
    dname=request.form["dname"]
    date1=request.form["date1"]
    time1=request.form["time1"]
    branch=request.form["branch"]
    
    t=(name,email,dname,date1,time1,branch)
    adddata(t)
    return render_template("appointmentbooking.html")
    


@app.route("/editlink1/<int:id>")
def displayforupdate1(id):
    datalist=specificdata(id)
    return render_template("edit1.html",data=datalist)

@app.route("/updatelink/<int:id>",methods=["POST"])
def updatefun1(id):
    
    name=request.form["uname"]
    email=request.form["email"]
    dname=request.form["dname"]
    date1=request.form["date"]
  
    
    t=(name,email,dname,date1,id)
    
    updatedata(t)
    return redirect("/showlink")

@app.route("/deletelink1/<int:id>")
def deletefun1(id):
    deletedata(id)
    return redirect("/showlink")



if __name__=="__main__":#main is a syntax
    app.run(debug=True)