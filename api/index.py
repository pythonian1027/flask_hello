from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method=='POST':
        print (request.json)
        return 'success', 200
    else: 
        abort(400)
        

#def home():
#    return 'Hello, World 3!'

#@app.route('/about')
#def about():
#    return 'About'