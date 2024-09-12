from flask import Flask, redirect

app = Flask('main')

@app.route('/')
def main_view():
    return "Hello, it's the Main Page!"

@app.route('/redirector')
def redirect_view():
    return redirect('/')

app.run()