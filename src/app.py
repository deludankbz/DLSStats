from flask import Flask, render_template
import json
from lib import PlayerFinder
# from fuzzywuzzy import fuzz

# TODO FIX: Fix paths

app = Flask("DLSStats", static_url_path='/static')
with open('PythonScripts/json/PlayerInfo.json', 'r') as f: playerDict = json.load(f)

@app.route('/q=<search_query>')
def search(search_query):
    newSearch = PlayerFinder(search_query=search_query, playerDict=playerDict)
    return render_template('playerInfo.html', plData=newSearch.findPlayersByName())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)

