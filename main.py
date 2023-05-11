
from flask import Flask
from flask import Flask, render_template
from flask import request
from flask import abort, redirect, url_for, make_response


app = Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html')

@app.route("/help")
def help():
 return "help me"

@app.route('/contact')
def contact():
 return app.send_static_file('contact.html')

@app.route('/about')
def about():
 return app.send_static_file('about.html')

@app.route('/gallery')
def gallery():
 return app.send_static_file('gallery.html')

 @app.route('/contact')
 def contact():
  return app.send_static_file('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
