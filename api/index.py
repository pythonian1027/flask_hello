from flask import Flask, request, abort

app = Flask(__name__)

messages = []

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_json()
    print ('received')
    # return 'Webhook received'
    if request.method=='POST':
        print (request.json)
        return 'success', 200
    else: 
        abort(400)
        
@app.route('/')
def home():
    global messages
    response = ''
    if messages:
        response = 'Updates: \n'
        response += '\n'.join(messages)
    return response
    # else:
    #     response = 'No updates'
    # return 'Hello, World 4!'

# @app.route('/about')
# def about():
#     return 'About'