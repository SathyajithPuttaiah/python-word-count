import mysql.connector
import re
from mysql.connector import errorcode

class WordCount:

    def __init__(self):
        pass

    def get_connection_details(self):
        try:

            #can set these as ENV variables
            MYSQL_USER = 'sathya'
            MYSQL_PASS = 'Sathyajith@123'
            MYSQL_HOST = 'mysql-db'
            #MYSQL_HOST = '65.0.127.175'
            MYSQL_PORT = 3306

            config = {
                'user': MYSQL_USER,
                'password': MYSQL_PASS,
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
    
    def get_word_count(self,word_to_search):
        try:
            result_dict = {}

            cnx,cur = self.get_connection_details()
            print('incoming word:',word_to_search)

            query = """SELECT page_searched,web_content
                    FROM wiki_database.wiki_table;"""
            cur.execute(query)
            records = cur.fetchall()

            for row in records:
                page_searched = str(row[0])
                web_content = str(row[1])
                print('inside records')
                word_count = len(re.findall(str(word_to_search).lower(), web_content.lower()))
                print('word_count:',word_count)

                result_dict[page_searched] = word_count

            return result_dict

        except Exception as e:
            cnx.close()
            cur.close()
            print('error in get_word_count():',e)
            raise

    