from flask import Flask, render_template
import json
from fuzzywuzzy import fuzz

app = Flask(__name__)
with open('PythonScripts\json\PlayerInfo.json', 'r') as f: playerDict = json.load(f)

@app.route('/q=<search_query>')
def search(search_query):
    print(search_query)
    fuzzResults = []
    for players in playerDict:
        fuzzPartRatio = fuzz.partial_ratio(search_query, players)
        fuzzUQRatio = fuzz.UWRatio(search_query, players)
        debugDict = {'name': players.title(), 'fuzzPartRatio': fuzzPartRatio, 'fuzzUQRatio': fuzzUQRatio}
        if fuzzPartRatio >= 75: fuzzResults.append(debugDict)
        elif fuzzPartRatio >= 80 and fuzzUQRatio >= 80: return players
        elif fuzzPartRatio >= 95 or fuzzUQRatio >= 95: return players
    return fuzzResults

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.0.11')