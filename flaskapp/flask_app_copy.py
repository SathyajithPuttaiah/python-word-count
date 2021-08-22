from flask import Flask
app = Flask(__name__) 

@app.route("/<word>")
def find_occurance_count(word):
    #word = request.args.get('word')
    print('received word is:',word)
    return "Hello World! to :"+ word

if __name__ == "__main__": 
    app.run(debug=True,host='0.0.0.0')
    #app.run(host='0.0.0.0')