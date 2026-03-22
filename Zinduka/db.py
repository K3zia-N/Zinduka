import sqlite3
import pymysql

def get_db_connection():
 conn = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="Zinduka"
 )
 return conn
