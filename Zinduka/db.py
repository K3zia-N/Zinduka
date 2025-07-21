# import sqlite3
import pymysql

def get_db_connection():
 conn: None
 try:
  conn = pymysql.connect(
   host="localhost",
   user="root",
   password="",
   database="Zinduka"
  )
  return conn
except pymysql.Error as e:
 # error handling
 return None
except Exception as e:
 print(f"An unexpected error occurred: {e}")
 return None
