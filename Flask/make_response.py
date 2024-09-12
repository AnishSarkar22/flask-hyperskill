from flask import Flask, make_response, Response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1> The Main Page, OK? </h1>')
    return response

@app.route('/data/get_error/')
def return_error():
    response = make_response('<p>Oops... Sounds like an error!</p>', 400)
    return response

@app.route('/custom', methods=['GET'])
def custom_response():
    content = "This is a custom response"
    response = Response(content, status=201, mimetype='text/plain')
    response.headers['X-Custom-Header'] = 'Some Value'
    return response

if __name__ == '__main__':
    app.run(debug=True)