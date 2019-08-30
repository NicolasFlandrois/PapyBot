from papybot.controls import parser, randomchat, openjson
import json


# def test_openjson(monkeypath):
#     requests_mock.get('test.json', text={'data':['1', '2']})
#     assert type(openjson()) == dict
# Mock test create a controljson file to assert

def test_parser():
    assert parser("Aucun AUTRES que Londres?") == "londres"


def test_randomchat():
    test_list = ["chocolat", "Vanille", "oui", "non"]
    assert type(randomchat(test_list)) == str
