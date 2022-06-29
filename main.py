from flask import Flask, request
from Users.users import usrlogin,verif,set_year
from MessagePdf.messagepdf import set_message,read_message,delete_message,set_pdf,read_arr_pdf,read_one_pdf
from DataBase.database import DataBase
from Settings.settings import xml

app = Flask('app')
app.secret_key = "Asusgo-proyect"
settings = xml()#Read setings on xml
database = DataBase(settings)#Create de database connection

#Test route
@app.route("/api")
def index():
    return {'msj':'conected'}

#login route
@app.route('/api/login', methods=['GET'])
def login():
    try:
        context = usrlogin()
        return context
    except:
        return {'msj':'error'}

#Verif route
@app.route('/callback')
def verification():
    try:
        context = verif(request.url,database)
        return context
    except:
        return {'msj':'error'}

#User route
@app.route('/api/user/set_year', methods=['POST'])
def setyear():
    try:
        context = set_year()
        return context
    except:
        return{'msj':'error'}

#Message read
@app.route('/api/message/read', methods=['GET'])
def readmessage():
    try:
        rq=request.get_json()
        context = read_message(rq,database)
        return context
    except:
        return {'msj':'error'}

#Message write
@app.route('/api/message/write', methods=['POST'])
def writemessage():
    try:
        rq=request.get_json()
        context = set_message(rq ,database)
        return context
    except:
        return{'msj':'error'}

#Message delete
@app.route('/api/message/delete', methods=['POST'])
def deletemessage():
    try:
        rq=request.get_json()
        context = delete_message(rq ,database)
        return context
    except:
        return{'msj':'error'}

#PDF insert
@app.route('/api/pdf/insert', methods=['POST'])
def insertpdf():
    try:
        context=set_pdf(request,database)
        return context
    except:
        return {'msj':'error'}

#PDF arr read
@app.route('/api/pdf/arrread', methods=['GET'])
def arrreadpdf():
    try:
        rq= request.get_json()
        context = read_arr_pdf(rq,database)
        return context
    except:
        pass

#PDF one read
@app.route('/api/message/pdf/oneread', methods=['GET'])
def onereadpdf():
    try:
        pass
    except:
        pass

if __name__ == "__main__":
    app.run(debug=True)