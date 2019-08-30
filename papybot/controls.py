#!/usr/bin/python3.7
# UTF8
# Date: Fri 30 Aug 2019 21:46:04 CEST
# Author: Nicolas Flandrois

import json
import random


def openjson(path):
    """Json file reader, returning it's content in pure form."""
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


def randomchat(lstmsg:list):
    """Randomly return a string item from a list of strings."""
    return random.choice(lstmsg)

