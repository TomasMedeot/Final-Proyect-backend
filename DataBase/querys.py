def querys(d_query):
    if d_query['function'] == 'R_U':
        return f"select * from STUDENT, PERSON where MAIL like '{d_query['mail']}';"
    elif d_query['function'] == 'W_U':
        return f"insert into PERSON(NAME, MAIL, TYPE) values ('{d_query['name']}','{d_query['mail']}', True);","insert into STUDENT(C_ABSCENSE, `YEAR`, GRADE,ID_T) values(0,'',''(SELECT ID_P FROM PERSON WHERE MAIL LIKE'{d_query['mail']}'));"
    elif d_query['function'] == 'R_S':
        return f"select * from STORAGE WHERE type like '(SELECT TYPE FROM PERSONA WHERE MAILE LIKE '{d_query['mail']}')'"
    elif d_query['fuction']  == 'W_S':
        return f"insert into STORAGE(DATE_ST, TEXT_ST,TYPE_ST) values ('{d_query['date']}','{d_query['text']}','{d_query['type']}');"
#Read user Query
