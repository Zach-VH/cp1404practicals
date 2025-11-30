"""
Flask API test
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<head>'
            '   <title> Hello World </title>'
            '</head>'
            '<body>'
            '   <h1> Hello World :> </h1>'
            '</body>')

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/temperature')
@app.route('/temperature/<celsius>')
def convert_celsius_to_fahrenheit(celsius=0.0):
    """Function to convert Celsius into Fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"<h1>{fahrenheit}</h1>"

if __name__ == '__main__':
    app.run()