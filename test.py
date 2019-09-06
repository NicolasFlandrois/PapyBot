from papybot.controls import *
import json


# def test_openjson(monkeypath):
#     requests_mock.get('test.json', text={'data':['1', '2']})
#     assert type(openjson()) == dict
# Mock test create a controljson file to assert

def test_parser():
    assert parser("Aucun AUTRES que Londres?") == "londres"


def test_randomchat():
    test_list = ["chocolat", "Vanille", "oui", "non"]
    assert type(randomchat(test_list, 0)) == str

def test_wikipedia():
    assert type(wikipedia('London')) == tuple
    assert wikipedia('french_republican_date')[0] == \
        "The French Republican calendar (French: calendrier républicain \
français), also commonly called the French Revolutionary calendar \
(calendrier révolutionnaire français), was a calendar created and implemented \
during the French Revolution, and used by the French government for about 12 \
years from late 1793 to 1805, and for 18 days by the Paris Commune in 1871. \
The revolutionary system was designed in part to remove all religious and \
royalist influences from the calendar, and was part of a larger attempt at \
decimalisation in France (which also included decimal time of day, \
decimalisation of currency, and metrication). It was used in government \
records in France and other areas under French rule, including Belgium, \
Luxembourg, and parts of the Netherlands, Germany, Switzerland, Malta, and \
Italy.\
\
https://en.wikipedia.org/wiki/French_Republican_calendar"
    assert wikipedia('zsecfu')[0] == 'Information not found.'
    assert wikipedia('zsecfu')[1] == 'Information not found.'
