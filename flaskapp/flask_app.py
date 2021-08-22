from flask import Flask
from helper_flask import helper_flask
from flask import jsonify

app = Flask(__name__) 

#helper object
helper_obj = helper_flask()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<word>")
def find_occurance_count(word):
    #word = request.args.get('word')
    print('received word is:',word)
    #return "Hello World! to :"+ word
    result_dict = helper_obj.get_word_count(word)
    return jsonify(result_dict)

if __name__ == "__main__": 
    #app.run()
    app.run(debug=True,host='0.0.0.0')