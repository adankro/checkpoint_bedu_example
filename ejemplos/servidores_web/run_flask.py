from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
#Decorator’s purpose is also served by the following representation −
#app.add_url_rule(‘/’, ‘hello’, hello_world)

@app.route('/user/<name>', methods=['POST', 'GET'])
def hello_user(name):
   return '<h1> Hello %s </h1>' % name

if __name__ == '__main__':
   app.run(port=8080, debug=True)
   #app.run(host, port, debug, options)
