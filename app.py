from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Pooja M'

if __name__=='__main__':
    app.run()