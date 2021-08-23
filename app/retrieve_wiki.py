import wikipedia
import re

class RetrieveWiki:

    def __init__(self):
        pass
    
    def retrieve(self,word_to_search,cnx,cur):
        try:

            searches = wikipedia.search(word_to_search)
            print('searches:',searches)

            for search in searches:
                print('search:',search)
                web_content = wikipedia.page(search).content

                #count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('taxi'), web_content))
                #word_count = len(re.findall(word_to_search.lower(), web_content.lower()))
                #print('word_count:',word_count)

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
            raise