from configs import config
from flask import make_response, jsonify
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseDao:
    def __init__(self):
        self.connection = mysql.connector.connect(host=config['host'],user=config['username'],password=config['password'],database=config['database'])
        self.cursor = self.connection.cursor()
        self.connection.commit()
        # self.connection.autocommit=True
        # self.engine = create_engine('mysql+mysqlconnector://{}:{}@localhost/{}' , format(config['username'] , config['password'] , config['database']))
        # self.Session = sessionmaker(bind=self.engine)


    # def connect(self):
    #     try:
    #         self.session = self.Session()
    #         return True
    #     except Exception as e:
    #         print(f"Error connecting to database: {str(e)}")
    #         return False

    # def disconnect(self):
    #     try:
    #         self.session.close()
    #         return True
    #     except Exception as e:
    #         print(f"Error disconnecting from database: {str(e)}")
    #         return False

    #     print("Connection established")
