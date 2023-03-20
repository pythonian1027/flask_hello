from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_json()
    return 'Webhook received'
    # if request.method=='POST':
    #     print (request.json)
    #     return 'success', 200
    # else: 
    #     abort(400)
        
@app.route('/')
def home():
    return 'Hello, World 4!'

@app.route('/about')
def about():
    return 'About'