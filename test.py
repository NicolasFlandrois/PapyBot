from controls import parser

def test_parser():
    assert parser("Aucun AUTRES que Londres?") == "londres"
