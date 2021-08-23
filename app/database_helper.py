import mysql.connector
import wikipedia
import re
from mysql.connector import errorcode

class DatabaseHelper:

    def __init__(self):
        pass
    
    def get_connection_details(self):
        try:

            #can set these as ENV variables
            MYSQL_USER = 'sathya'
            MYSQL_PASS = 'Sathyajith@123'
            MYSQL_HOST = 'mysql-db'
            #MYSQL_HOST = '65.0.11.162'
            MYSQL_PORT = 3306

            config = {
                'user': MYSQL_USER,
                'password': MYSQL_PASS,
                #'host': '13.235.71.113',
                'host': MYSQL_HOST,
                'port': MYSQL_PORT
            }

            cnx = mysql.connector.connect(**config)
            cur = cnx.cursor()

            return cnx,cur
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print('Error in get_connection_details():',err)
                raise

    def create_database(self,cnx,cur):
        try:
            #check whether the database present or not.
            #if not present, create a new one
            query = """SELECT count(1)
                    FROM information_schema.schemata
                    WHERE lower(schema_name) LIKE 'wiki_database';"""
            #print('query:',query)

            cur.execute(query)
            db_count = cur.fetchone()[0]

            print('db_count:',db_count)

            if db_count > 0:
                print('database present. Dont create')
            else:
                print('create the database')
                cur.execute("CREATE DATABASE wiki_database")
        except Exception as e:
            #closing the connections
            cnx.close()
            cur.close()
            print('error in create_database():',e)
            raise

    def create_table(self,cnx,cur):
        try:
            #check whether the table present or not.
            #if not present, create a new one
            query = """SELECT count(1) from information_schema.tables 
                    where lower(table_name) = 'wiki_table'
                    and lower(table_schema) = 'wiki_database' ;"""
            #print('query:',query)

            cur.execute(query)
            table_count = cur.fetchone()[0]

            print('table_count:',table_count)

            if table_count > 0:
                print('table present. dont create')
            else:
                print('create the table')
                cur.execute("CREATE TABLE wiki_database.wiki_table (page_searched varchar(100) ,web_content LONGBLOB, word_count int)")

        except Exception as e:
            #closing the connections
            cnx.close()
            cur.close()
            print('error in create_table():',e)
            raise