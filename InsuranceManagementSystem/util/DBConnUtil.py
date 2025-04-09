# File: util/DBConnUtil.py

import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:

    @staticmethod
    def getConnection():
        props = DBPropertyUtil.getDBProperties("db.properties")
        connection = mysql.connector.connect(
            host=props["host"],
            user=props["user"],
            password=props["password"],
            database=props["database"]
        )
        return connection
