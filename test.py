#!/usr/bin/python3.7
# UTF8
# Date: Wed 02 Oct 2019 16:51:11 CEST
# Author: Nicolas Flandrois

from io import BytesIO
import json
from papybot.controls import *
from server import *
import urllib.request
import wikipedia

wikipedia.set_lang("fr")

# Unit Testing papybot.controls.py


def test_get_json():
    assert type(Papy.get_json('./papybot/data.json')) == dict


def test_mock_get_json(monkeypatch, tmpdir):
    results = {"mock_key": "mock_response"}

    def mockreturn(request):
        return BytesIO(json.dumps(results, sort_keys=True, indent=4,
                                  separators=(',', ': ')).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    p = tmpdir.mkdir('mocktest').join('test.json')

    with open(p, 'w') as out_f:
        out_f.write('{"mock_key":"mock_response"}')

    local_res = json.load(open(p))

    assert local_res == Papy.get_json(p)


def test_parser():
    assert Papy.parser("Aucun AUTRES que Londres?", './papybot/data.json'
                       ) == "Londres"


def test_randomchat(monkeypatch, tmpdir):
    def mockreturn(request):
        return BytesIO(json.dumps(results, sort_keys=True, indent=4,
                                  separators=(',', ': ')).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    p = tmpdir.mkdir('mocktest').join('test.json')

    with open(p, 'w') as out_f:
        out_f.write('{"fails":["chocolat", "non"], \
                    "msg":["Vanille", "oui"], \
                    "greetings":["Hello", "Bonjour"]}')

    assert type(Papy.randomchat(1, p)) == str
    assert type(Papy.randomchat(0, p)) == str
    assert type(Papy.randomchat(2, p)) == str


def test_wikipedia():
    assert type(Papy.wikipedia('London')) == dict
    assert Papy.wikipedia('Kennedy') == {'status': 1,
                                         'summary': "John Fitzgerald Kennedy /d͡ʒɑn fɪtsˈd͡ʒɛɹəld ˈkɛnədi/, dit \
Jack Kennedy, communément appelé John Kennedy et par ses initiales JFK, né le \
29 mai 1917 à Brookline (Massachusetts) et mort assassiné le 22 novembre 1963 \
à Dallas (Texas), est un homme d'État américain, 35e président des États-Unis. \
Entré en poste le 20 janvier 1961, il est, à 43 ans, le plus jeune président \
élu des États-Unis, et également le plus jeune président à mourir, moins de \
trois ans après son entrée à la Maison-Blanche, à l'âge de 46 ans.\nIl laisse \
son empreinte dans l'histoire des États-Unis par sa gestion de la crise des \
missiles de Cuba, son autorisation du débarquement de la baie des Cochons, \
son engagement pour le traité d'interdiction partielle des essais nucléaires, \
le programme Apollo dans le cadre de la course à l'espace, son opposition à \
la construction du mur de Berlin, sa politique d'égalité des genres et \
son assassinat.",
                                         'url': 'https://fr.wikipedia.org\
/wiki/John_Fitzgerald_Kennedy'}

    assert Papy.wikipedia('zsecfu') == {'status': 0,
                                        'error': 'Merci de redéfinir \
ta question, plus précisément. (e.g. Ajoute un pays)\nJe te propose : '}


# Mock Testing API
def test_mock_wikipedia(monkeypatch):
    res = {'status': 1,
           'summary': "James French Hill, né le 5 décembre 1956 à Little Rock, \
est un homme politique américain, membre du Parti républicain, représentant \
de l'Arkansas à la Chambre des représentants des États-Unis depuis 2015.\n\n\n\
== Biographie ==\nFrench Hill est un homme d'affaires millionnaire, exerçant \
dans le monde de la banque. Dans les années 1980, il travaille auprès de la \
commission sénatoriale sur la banque, le logement et les affaires urbaines, \
puis au département du Trésor.",
           'url': 'https://fr.wikipedia.org/wiki/French_Hill'}

    def mock_return(request):
        return res

    monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

    assert Papy.wikipedia('french_republican_date') == res


def test_mock_fails_wikipedia(monkeypatch):
    res = {'status': 0, 'error': 'Merci de redéfinir ta question, \
plus précisément. (e.g. Ajoute un pays)\nJe te propose : '}

    def mock_return(request):
        return res

    monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

    assert Papy.wikipedia('zsecfu') == res


def test_success_gmap(monkeypatch):

    def mock_success():
        # return
        pass

    parsed = 'Paris'
    success = {'source': 'https://maps.googleapis.com/maps/api/staticmap?\
center=Paris&zoom=10&size=150x150&scale=2&format=png32&markers=size:tiny%7C\
Paris&key=TESTKEY_6-ze^N@U&=v_!z)-$K%$_RANDOMSTR',
               'link': 'https://www.google.com/maps/place/Paris/'}

    monkeypatch.setattr(urllib.request, 'urlopen', mock_success)
    assert Papy.gmap(parsed, 'config.json', 'testkey') == success


def test_fails_gmap(monkeypatch):

    parsed = 'Hello (Chanson)'
    fails = {'source': 'Error', 'link': 'Error'}

    def mock_fails():
        # return {'X-Staticmap-API-Warning': 'Error geocoding: center, marker 1'}
        return fails

    monkeypatch.setattr(urllib.request, 'urlopen', mock_fails)
    assert Papy.gmap(parsed, 'config.json', 'testkey') == fails

# Flask Unit Testing > server.py
# How to do unit test on Flask > server.py?


def test_index():
    pass
    # return render_template('index.html', greetings=greetings)


def test_msg():
    pass
    # return jsonify(send)
    # Success: {'status': wiki['status'], 'papy': papyChat,
    #             'summary': wiki['summary'],
    #             'url': wiki['url'], 'gmapsource': gmap['source'],
    #             'gmaplink': gmap['link']}
    # Fails : send = {'status': wiki['status'], 'papy': papyChat,
    #             'error': wiki['error']}
