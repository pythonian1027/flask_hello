from flask import Flask, request, abort

app = Flask(__name__)

messages = []

@app.route('/webhook', methods=['POST'])
def webhook():
    global messages
    payload = request.get_json()    
    # return 'Webhook received'
    if request.method=='POST':
        message = payload['message']
        messages.append(message)
        return 'Webhook received successfully', 200
    else: 
        abort(400)
        
@app.route('/')
def home():
    global messages
    response = ''
    if messages:
        response = 'Updates: \n'
        response += '\n'.join(messages)
    else:
        response = 'No updates'
    return response        
    # return 'Hello, World 4!'

# @app.route('/about')
# def about():
#     return 'About'