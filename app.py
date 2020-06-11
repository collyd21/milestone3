import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Milestone 3 Project"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
