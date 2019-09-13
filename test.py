from io import BytesIO
import json
from papybot.controls import *
from pathlib import Path
import pytest
from server import *
import urllib.request

# How to do unit test on Flask > server.py?


def test_get_json():
    assert type(Papy.get_json('./papybot/data.json')) == dict


def test_mock_get_json(monkeypatch, tmpdir):
    results = {"mock_key":"mock_response"}

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
    assert Papy.wikipedia('french_republican_date') == {'status':1,
    'msg':'The French Republican \
calendar (French: calendrier républicain français), also commonly called \
the French Revolutionary calendar (calendrier révolutionnaire français), \
was a calendar created and implemented during the French Revolution, and \
used by the French government for about 12 years from late 1793 to 1805, \
and for 18 days by the Paris Commune in 1871. The revolutionary system \
was designed in part to remove all religious and royalist influences from \
the calendar, and was part of a larger attempt at decimalisation in France \
(which also included decimal time of day, decimalisation of currency, and \
metrication). It was used in government records in France and other areas \
under French rule, including Belgium, Luxembourg, and parts of the \
Netherlands, Germany, Switzerland, Malta, and Italy.\n\n\
https://en.wikipedia.org/wiki/French_Republican_calendar'}
    assert Papy.wikipedia('zsecfu') == {'status':0,
    'msg':'Merci de redéfinir ta question, plus \
précisément. (e.g. Ajoute un pays)\nJe te propose : '}


# Mock Testing API
def test_mock_wikipedia(monkeypatch):
    res = {'status':1,
    'msg':'The French Republican \
calendar (French: calendrier républicain français), also commonly called \
the French Revolutionary calendar (calendrier révolutionnaire français), \
was a calendar created and implemented during the French Revolution, and \
used by the French government for about 12 years from late 1793 to 1805, \
and for 18 days by the Paris Commune in 1871. The revolutionary system \
was designed in part to remove all religious and royalist influences from \
the calendar, and was part of a larger attempt at decimalisation in France \
(which also included decimal time of day, decimalisation of currency, and \
metrication). It was used in government records in France and other areas \
under French rule, including Belgium, Luxembourg, and parts of the \
Netherlands, Germany, Switzerland, Malta, and Italy.\n\n\
https://en.wikipedia.org/wiki/French_Republican_calendar'}

    def mock_return(request):
        return res

    monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

    assert Papy.wikipedia('french_republican_date') == res


def test_mock_fails_wikipedia(monkeypatch):
    res = {'status':0, 'msg':'Merci de redéfinir ta question, \
plus précisément. (e.g. Ajoute un pays)\nJe te propose : '}

    def mock_return(request):
        return res

    monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

    assert Papy.wikipedia('zsecfu') == res

# NB: Google Map API is Managed by JavaScript.
# Therefor no unit test mock related to Gmap here.
