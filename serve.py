from flask import Flask, request, render_template

from define import *

app = Flask(__name__)

@app.route('/')
def root():
    return 'Root'

@app.route('/netbar')
def netbar():
    return render_template('netbar.html', age=18)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
