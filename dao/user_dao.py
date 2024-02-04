from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify
from configs import config
from dao.base_dao import BaseDao

# baseDao class for making connection as it needs to be done only one not for every model , return a conn object and cursor object - done


class UserModelDao():
    def __init__(self , basedao):
        self.conn = basedao.connection  # conn object
        self.cur = basedao.cursor   # cursor object


    def get_all_user_model(self):
        select_query = '''
        SELECT * FROM info
    '''
        self.cur.execute(select_query)
        result = self.cur.fetchall()
        if len(result)>0:
            # return {"payload": result}
            return make_response({"payload":result},200)
        else:
            return "No Data Found"
    
    def add_user_model(self,data):
        insert_query = '''
    INSERT INTO info (id, name, email) VALUES (%s, %s, %s)
'''
        self.cur.execute(insert_query, data)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    def add_multiple_users_model(self, data):
        # Generating query for multiple inserts
        insert_query = '''
    INSERT INTO info (id, name, email) VALUES (%s, %s, %s)
'''
        for userdata in data:
            self.cur.execute(insert_query, userdata)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)

    def delete_user_by_id_model(self,id):
        delete_query = '''
        DELETE FROM info WHERE id = %s
    '''
        self.cur.execute(delete_query, (id,))
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)
        
    
    def update_user_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    def patch_user_model(self, data):
        qry = "UPDATE users SET "
        for key in data:
            if key!='id':
                qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {data['id']}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)
        



__name__ == "__main__"

dao_instance = BaseDao()
user_model_instance = UserModelDao(dao_instance)

if dao_instance.connect():
    print("Connection established")
    print(user_model_instance.get_all_user_model())
    print(user_model_instance.add_user_model({"id" : 1  , "name":"test","email":"test@gmail.com"}))