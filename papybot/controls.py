#!/usr/bin/python3.7
# UTF8
# Date: Fri 30 Aug 2019 21:46:04 CEST
# Author:  Nicolas Flandrois

import json
import random
import requests
import wikipedia


class Papy:
    """Papy, grouping get_json, Parser, randomChat, and StatusParser"""

    @staticmethod
    def get_json(path):
        """Json file reader, returning it's content in pure form."""
        with open(path, 'r') as f:
            text = json.load(f)
        return text


    @staticmethod
    def parser(msg:str, path):
        """
        Given a string, this function will split the string into a set of words,
        and then
        """

        ignore_set = set(Papy.get_json(path)["parser"])
        msg_set =  set(msg.lower().replace(".", "").replace(",", "").replace("?", "")
                    .replace(";", "").replace(":", "").replace("!", "").split())

        return " ".join(msg_set.difference(ignore_set)).capitalize()


    @staticmethod
    def randomchat(status, path):
        """
        Randomly return a string item from a list of strings.
        Get a status from the status tracker, returns a list accordingly.
        Fails = 0; msg = 1; Greating = 2
        """
        if status is 0:
            # Status == fails
            lstmsg = Papy.get_json(path)["fails"]
        elif status is 1:
            # Status == Success
            lstmsg = Papy.get_json(path)["msg"]
        else :
            # Status == Greetings
            lstmsg = Papy.get_json(path)["greetings"]

        return random.choice(lstmsg)



    @staticmethod
    def wikipedia(request: str):
        """
        Given a String request, this function will fetch a wikipedia summary,
        and URL string.
        If not found, or exception raised, an error message will be displaid.
        In the end, this function returns a Dictionary with Status & Message
        """
        try:
            return {'status':1, 'msg':f'{wikipedia.summary(request)}\n\n\
{wikipedia.page(request).url}'}
        except:
            return {'status':0, 'msg':f"Merci de redéfinir ta question, plus \
précisément. (e.g. Ajoute un pays)\nJe te propose : {', '.join(set([i for i in wikipedia.search(request)]))}"}
