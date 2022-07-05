import datetime
from Users.Verificate.verificate import *
from DataBase.querys import querys

#Login
def usrlogin():
    try:
        context =url_login()
        return context
    except:
        return {'msj':'error'}

#Verificate
def verif(url,database):
    try:
        print(url)
        #get information of user
        context =callback(url)

        #Verificate the mail direction
        if ('@liceopaz.edu.ar' in context['email']) == True:#Personal

            context['function']='R_U'
            db_r = database.datasearch(querys(context)[0])

            if db_r != ():
                return {'element':db_r}
            else:
                context['function']='W_U'
                db_r =database.datainsert(querys(context)[0])
                context['function']='R_U'
                db_r = database.datasearch(querys(context)[0])
                return {'element':db_r}

        elif ('@alumnos.liceopaz.edu.ar' in context['email'])== True:#Students
            context['function']='R_U'
            db_r = database.datasearch(querys(context)[1])

            if db_r != ():
                return {'element':db_r}
            else:
                context['function']='W_U'
                database.datainsert(querys(context)[1])
                context['function']='R_U'
                db_r = database.datasearch(querys(context)[1])
                return {'element':db_r}
        else:    
            return {'msj':'mail not valid'}
    except:
        return {'msj':'error'}

def set_year():
    pass

def Update_abscence():
    pass