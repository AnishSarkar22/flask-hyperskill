from flask import Flask, request


MAIN_PAGE_GET = '''
<h1>Welcome!</h1>
<form method='post'>
<input type='submit' value='Push me!'>
</form>
'''

MAIN_PAGE_POST = '''
<h1>Perfect!</h1>
<p>You succesfully sent POST request via your browser!</p>
'''

app = Flask('main')

@app.route('/', methods=['POST', 'GET'])
def main_view():
    if request.method == 'POST':
        return MAIN_PAGE_POST
    elif request.method == 'GET':
        return MAIN_PAGE_GET

app.run()