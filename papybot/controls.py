#!/usr/bin/python3.7
# UTF8
# Date:
# Author: Nicolas Flandrois

import json


def openjson(path):
    with open(path, 'r') as f:
        text = json.load(f)
    return text


def parser(msg:str):
    """
    Given a string, this function will split the string into a set of words,
    and then
    """

    ignore_set = set(openjson('data.json')["parser"])
    msg_set =  set(msg.lower().replace(".", "").replace(",", "").replace("?", "")
                .replace(";", "").replace(":", "").replace("!", "").split())

    return " ".join(msg_set.difference(ignore_set))
