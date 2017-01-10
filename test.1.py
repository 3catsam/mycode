from flask import Flask, jsonify, abort
from flask import make_response,render_template
from flask import url_for





app = Flask(__name__)
@app.route('/')
def root():
    return '<h1>hello</h1>'


if __name__ == '__main__':
    app.run(host='', port=8000, debug=True)
