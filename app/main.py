
from helper import helper

#word to be searched
word_to_search = 'taxi'

#helper object
helper_obj = helper()


try:

    #get the DB connection
    cnx,cur = helper_obj.get_connection_details()

    #create database 'wiki_database' if its not present
    helper_obj.create_database(cnx,cur)

    #create table 'wiki_table' if its not present
    helper_obj.create_table(cnx,cur)

    helper_obj.search_wikipedia(word_to_search,cnx,cur)

    print('process completed')

except Exception as e:
    print('Error in process:',e)
