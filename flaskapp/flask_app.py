from flask import Flask
from helper_flask import WordCount
from flask import jsonify

app = Flask(__name__) 

#helper object
wc = WordCount()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<word>")
def find_occurance_count(word):
    #word = request.args.get('word')
    print('received word is:',word)
    #return "Hello World! to :"+ word
    result_dict = wc.get_word_count(word)
    return jsonify(result_dict)

if __name__ == "__main__": 
    #app.run()
    app.run(debug=True,host='0.0.0.0')