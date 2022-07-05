from flask import Flask, redirect, request
from flask_cors import CORS
from Users.users import usrlogin,verif,set_year
from MessagePdf.messagepdf import set_message,read_message,delete_message,set_pdf,read_arr_pdf,read_one_pdf
from DataBase.database import DataBase
from Settings.settings import xml

app = Flask('app')
cors = CORS(app)
app.secret_key = "Asusgo-proyect"
settings = xml()#Read setings on xml
database = DataBase(settings)#Create de database connection
users=[]#save the loged users

#Test route
@app.route("/api", methods=['GET'])
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
@app.route('/api/callback', methods=['GET'])
def verification():
    try:
        context = verif(request.url,database)
        user = context['element']
        users.append(user)
        code = users.index(user)
        return redirect('http://localhost:3000/alumnos?'+str(code))
    except:
        return {'msj':'error'}

@app.route('/api/getuser', methods=['GET'])
def get_user():
    user = users[int(request['id'])]
    return {'user':user[0]}

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
    #try:
    file = request.files
    rq = request.get_json()
    context=set_pdf(rq,file,database)
    return context
    '''except:
        return {'msj':'error'}'''

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