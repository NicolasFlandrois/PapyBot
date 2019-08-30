from control import parser

def test_parser():
    assert parser("Acun AUTRES que Londre") == "londre"
