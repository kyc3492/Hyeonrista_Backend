from warnings import catch_warnings
import pymysql

def get_cafe_list(sql):
    try:
        db = pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='',
                              db='usr',
                              charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        '''print(result[0]["name"])'''
        return result
    finally:
        db.close()

'''get_cafe_list("SELECT * FROM usr.cafes;")'''