from flask import Flask, render_template
import json
from lib import PlayerFinder
from fuzzywuzzy import fuzz

app = Flask(__name__, static_url_path='/static')
with open('PythonScripts\json\PlayerInfo.json', 'r') as f: playerDict = json.load(f)

@app.route('/q=<search_query>')
def search(search_query):
    newSearch = PlayerFinder(search_query=search_query, playerDict=playerDict)
    return render_template('playerInfo.html', plData=newSearch.findPlayersByName())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.0.70')