from flask import Flask, flash, get_flashed_messages, render_template, redirect

app = Flask('__name__')
app.config['SECRET_KEY'] = 'So-Seckrekt'

@app.route('/')
def main_view():
    flash('You hang on our site for more than 5 hours in a row. Take a break, please.', 'info')
    return render_template('main.html')

@app.route('/not_ready')
def redirect_view():
    flash('This page is not ready yet! Return later!')
    return get_flashed_messages()[0]

# get_flashed_messages(category_filter=['info'])

if __name__ == '__main__':
    app.run(debug=True)