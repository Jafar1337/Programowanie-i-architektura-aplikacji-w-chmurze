
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj na stronie głównej!"

if __name__ == '__main__':
    app.run()
