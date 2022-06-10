from Users.Verificate.verificate import *

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
        context =callback(url)

        #obtains the direction of the mail
        m_direction = '@gmail' in context['email']

        #verificate the email
        if (m_direction == True) and (context['verif']==True):
            print(True)
            return context
        else:
            return {'msj':'mail not valid'}
    except:
        return {'msj':'error'}