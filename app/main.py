import time

from database_helper import DatabaseHelper
from retrieve_wiki import RetrieveWiki

#word to be searched
word_to_search = 'taxi'

#object creation
db = DatabaseHelper()
wiki = RetrieveWiki()


try:

    #time.sleep(5)

    #get the DB connection
    cnx,cur = db.get_connection_details()

    #create database 'wiki_database' if its not present
    db.create_database(cnx,cur)

    #create table 'wiki_table' if its not present
    db.create_table(cnx,cur)

    wiki.retrieve(word_to_search,cnx,cur)

    print('process completed')

except Exception as e:
    print('Error in process:',e)
