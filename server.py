from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(input):
    return 'Sorry! No response. Try again.'

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<input>')
def say(input):
    return f'Hi {input}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return word * num

if __name__ == '__main__':
    app.run(debug=True)