from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return ('html page')

@app.route('/page')
def page():
    return ("page 1.0 sample2 branch 2.0")

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)