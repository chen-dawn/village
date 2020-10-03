from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello_world')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
