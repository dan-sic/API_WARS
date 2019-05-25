from flask import Flask, request, json, render_template, url_for
import requests
app = Flask(__name__)


@app.route('/')
def home():
    # planets = requests.get('https://swapi.co/api/planets/').json()
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)