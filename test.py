import json
from papybot.controls import *
from papybot.models import *
from papybot.views import *
from server import *
import urllib.request

# How to do unit test on Flask > server.py?


def test_openjson():
    assert type(Papy.openjson('./papybot/data.json')) == dict


def test_parser():
    assert Papy.parser("Aucun AUTRES que Londres?", './papybot/data.json') == "Londres"


def test_randomchat():
    test_list = ["chocolat", "Vanille", "oui", "non"]
    assert type(Papy.randomchat(test_list, 0)) == str


def test_wikipedia():
    assert type(Api.wikipedia('London')) == str
    assert Api.wikipedia('french_republican_date') == "The French Republican calendar (French: calendrier républicain français), also commonly called the French Revolutionary calendar (calendrier révolutionnaire français), was a calendar created and implemented during the French Revolution, and used by the French government for about 12 years from late 1793 to 1805, and for 18 days by the Paris Commune in 1871. The revolutionary system was designed in part to remove all religious and royalist influences from the calendar, and was part of a larger attempt at decimalisation in France (which also included decimal time of day, decimalisation of currency, and metrication). It was used in government records in France and other areas under French rule, including Belgium, Luxembourg, and parts of the Netherlands, Germany, Switzerland, Malta, and Italy.\n\nhttps://en.wikipedia.org/wiki/French_Republican_calendar"
    assert Api.wikipedia('zsecfu') == 'Merci de redéfinir ta question, plus précisément. (e.g. Ajoute un pays)\nJe te propose : '

# Mock Testing API
def test_mock_wikipedia(monkeypatch):
    res = "The French Republican calendar (French: calendrier républicain français), also commonly called the French Revolutionary calendar (calendrier révolutionnaire français), was a calendar created and implemented during the French Revolution, and used by the French government for about 12 years from late 1793 to 1805, and for 18 days by the Paris Commune in 1871. The revolutionary system was designed in part to remove all religious and royalist influences from the calendar, and was part of a larger attempt at decimalisation in France (which also included decimal time of day, decimalisation of currency, and metrication). It was used in government records in France and other areas under French rule, including Belgium, Luxembourg, and parts of the Netherlands, Germany, Switzerland, Malta, and Italy.\n\nhttps://en.wikipedia.org/wiki/French_Republican_calendar"

    def mock_return(request):
        return res

    monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

    assert Api.wikipedia('french_republican_date') == res

def test_mock_fails_wikipedia(monkeypatch):
    res = 'Merci de redéfinir ta question, plus précisément. (e.g. Ajoute un pays)\nJe te propose : '

    def mock_return(request):
        return res

    monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

    assert Api.wikipedia('zsecfu') == res

# NB: Google Map API is Managed by JavaScript.
# Therefor no unit test mock related to Gmap here.
