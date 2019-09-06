#!/usr/bin/python3.7
# UTF8
# Date: Fri 30 Aug 2019 21:46:04 CEST
# Author: Nicolas Flandrois

import json
import random
import wikipedia


class Papy(object):
    """Papy, grouping OpenJson, Parser, randomChat, and StatusParser"""

    def openjson(path):
        """Json file reader, returning it's content in pure form."""
        with open(path, 'r') as f:
            text = json.load(f)
        return text


    def parser(msg:str, path):
        """
        Given a string, this function will split the string into a set of words,
        and then
        """

        ignore_set = set(Papy.openjson(path)["parser"])
        msg_set =  set(msg.lower().replace(".", "").replace(",", "").replace("?", "")
                    .replace(";", "").replace(":", "").replace("!", "").split())

        return " ".join(msg_set.difference(ignore_set)).capitalize()


    def randomchat(lstmsg:list, status):
        """Randomly return a string item from a list of strings."""
            # def statusParser():
            # """Get a status from the status tracker, returns a list accordingly"""
            # Fails = 0; msg = 1; Greating = 2
                # if status is 0:
                #   use fails message
                # elif status is 1:
                #   Use msg
                # else :
                #   use Greetings
        # if status is 0:
        #   use fails message
        # elif status is 1:
        #   Use msg
        # else :
        #   use Greetings
        return random.choice(lstmsg)


        # def StatusTracker():

    # Create class 'Search engine' or 'API'
        # def wikisearch(searchObject):
        '''Given a string remotely search in wiki what's needed'''
        # Try:
            # from wikipedia import summary, page, set_lang
            # First set langue to french with: wikipedia.set_lang("fr")
            # stock search variable in a var 'city' or called 'seachObject'
            # summary(city, sentences=2)
            # page(city).url
                ## NB: No Way around it.
                # The function wikipedia.page().content cannot split a summary of n sentences
                # And Summary cannot give the url
        # Except:
            # Change status to Fails
            # If "wikipedia.exceptions.DisambiguationError" Possibly invit user to precise his query? e.g. (test lang:en)"roma"
                # return '\nMerci de redéfinir la question, plus précisément. (e.g. Ajoute un pays)\nJe te propose : ' wikipedia.search(searchObjet)


class Api(object):
    """Managing in Api all API related requests"""


    def wikipedia(request: str):
        """
        Given a String request, this function will fetch a wikipedia summary,
        and URL string.
        If not found, or exception raised, an error message will be displaid.
        """
        try:
            return f'{wikipedia.summary(request)}\n\n{wikipedia.page(request).url}'
        except:
            return f"Merci de redéfinir ta question, plus précisément. (e.g. Ajoute un pays)\nJe te propose : {', '.join(set([i for i in wikipedia.search(request)]))}"


    def gmap_key(request, key_id, path='config.json'):
        """Provides the API link with APIKey, as a String"""
        return f"https://www.google.com/maps/embed/v1/search?key={Papy.openjson(path)[key_id]}&q={'+'.join(request.split())}"
