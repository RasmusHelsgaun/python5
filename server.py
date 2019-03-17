from flask import Flask, request, Response
app = Flask(__name__)

SERVER_PASSWORD = 'rh'

@app.route('/', methods=['POST'])
def validate_password():
    client_password = request.get_json()['password']
    
    if client_password == SERVER_PASSWORD:
        return Response(status=200)
    else:
        return Response(status=404)