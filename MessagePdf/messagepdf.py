from DataBase.querys import *
import datetime
import os

def set_message(request,database):
    try:
        context={}
        context['text']=request['text']
        context['type']=request['type']
        context['date']=datetime.datetime.now().strftime('%d/%m/%Y')
        context['function']='W_S'
        dr_r = database.datainsert(querys(context))
        return {'msj':dr_r}
    except:
        return {'msj':'error'}

def read_message(request,database):
    try:
        context={}
        context['type']=request['type']
        context['function']='R_S'
        dr_r = database.datasearch(querys(context))
        return {'element':dr_r}
    except:
        return {'msj':'error'}

def delete_message(request,database):
    try:
        context={}
        context['id']=request['id']
        context['function']='D_S'
        dr_r = database.datainsert(querys(context))
        return {'element':dr_r}
    except:
        return {'msj':'error'}

def set_pdf(request,file,database):
    context = {}
    context=request
    print(context)
    '''context['function']='R_PDF_S'
    db_r = database.datasearch(querys(context)[0])
    if db_r != ():
        context['function']='W_PDF_S'
        database.datainsert(querys(request))
        folderdirectory = './MessagePdf/pdf_storage'
        rq = file
        file = rq['file']
        file.save(os.path.join(folderdirectory,request['name']+'.pdf'))'''
    return {'msj':'saved pdf'}

def read_arr_pdf(request,database):
    request['function']='R_PDF_S'
    db_r = database.datasearch(querys(request)[1])
    return {'element':db_r}

def read_one_pdf(request,database):
    folderdirectory = './MessagePdf/pdf_storage'
    request['function']='R_PDF_S'
    db_r = database.datasearch(querys(request)[2])
    db_r = db_r[0]
    name = db_r[1]
    f = os.path.join(folderdirectory,name)
    return {'file':f,'name':name}