import mysql.connector
import wikipedia
import re

class helper:

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
                'raise_on_warnings': True,
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

    def search_wikipedia(self,word_to_search,cnx,cur):
        try:

            searches = wikipedia.search(word_to_search)
            print('searches:',searches)

            for search in searches:
                print('search:',search)
                web_content = wikipedia.page(search).content

                #count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('taxi'), web_content))
                #word_count = len(re.findall(word_to_search.lower(), web_content.lower()))
                #print('word_count:',word_count)

                """ #insert web content into table
                query = "INSERT INTO wiki_database.wiki_table (web_content) VALUES (%s, %s)"
                val = (web_content, word_count)
                cur.execute(query, val)
                cnx.commit() """

                #insert web content into table
                query = "INSERT INTO wiki_database.wiki_table (page_searched,web_content) VALUES (%s,%s)"
                val = (search,web_content)
                cur.execute(query,val)
                cnx.commit()
            
            #closing the connections
            cnx.close()
            cur.close()
        
        except Exception as e:
            #closing the connections
            cnx.close()
            cur.close()
            print('error in search_wikipedia():',e)
