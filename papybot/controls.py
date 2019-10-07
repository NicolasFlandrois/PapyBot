#!/usr/bin/python3.7
# UTF8
# Date: Wed 02 Oct 2019 16:51:11 CEST
# Author: Nicolas Flandrois

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
    def parser(msg: str, path):
        """
        Given a string, this function will split the string into a set of words,
        and then
        """

        ignore_set = set(Papy.get_json(path)["parser"])
        msg_set = set(msg.lower().replace(".", "").replace(",", "")
                      .replace("?", "").replace(";", "").replace(":", "")
                      .replace("!", "").split())

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
        else:
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
            return {'status': 1, 'summary': wikipedia.summary(request,
                                                              sentences=3),
                    'url': wikipedia.page(request).url}
        except:
            return {'status': 0, 'error': f"Merci de redéfinir ta question, \
plus précisément. (e.g. Ajoute un pays)\nJe te propose : \
{', '.join(set([i for i in wikipedia.search(request)]))}"}

    @staticmethod
    def gmap(request: str, key_path, key_name):
        """
        Given a String request, this function will return a dictionnary
        combined with the Gmap Static API Key, and the search extention,
        All formated to Gmap Static API specifications. The Link argument
        refers to a clickable Link to include in the HTML links' <a></a> anchor.
        """
        search = '+'.join(request.split())
        source = f"https://maps.googleapis.com/maps/api/staticmap?center={search}&zoom=10&size=150x150&scale=2&format=png32&markers=size:tiny%7C{search}&key={Papy.get_json(key_path)[key_name]}"
        link = f"https://www.google.com/maps/place/{search}/"
        try:
            res = requests.get(source)
            if res.headers['X-Staticmap-API-Warning'] == 'Error geocoding: center, marker 1':
                return {'source': 'Error', 'link': 'Error'}
            else:
                return {'source': source, 'link': link}
        except:
            return {'source': source, 'link': link}
