# PapyBot
## [OC - Project 7 - Simple Grand Papy Robot (Chat Bot)]

**Date**: Wed 09 Oct 2019 16:25:41 CEST

**Author**: Nicolas Flandrois

**License**: MIT License Copyright (c) 2019 Nicolas Flandrois

**Version**: v1.2

-------------------------------------------------------------

**Description**:

[openclassrooms.com](openclassrooms.com) - DA Python - [Project 7 - Créez GrandPy Bot, le papy-robot](https://openclassrooms.com/fr/projects/158/assignment)

This project's objective is to create a chat bot, within it's own webpage.
The server runs on Python's Flask, UI designs are managed with Bootstrap, and interactions are geared through Jquery.

Like a messenger application, ***you*** (*the user*) type your message in the input box.
***PapyBot*** (the *chat bot program*) will answer you, to the best of his capacity, he might be a bit senile at times.

PapyBot will parse your query, filter relevent words, question Wikipedia API and Gmap API. If He can come up with informations, he will generate a random pharse along with the 2 first sentences of the *most* relevent wikipage. If a map is available, it will display it. However, if Papy doesn't understand your query, he will tell you to rephase (Becareful he might become nasty).

This program has a *'mid range'* memory, if you refresh the page, all previous interactions will be erased (told you Papy was a bit senile). Otherwise as long you keep interacting with him, the conversation remains available on screen.

**Enjoy!**

***How to run this script***:

On the server machine, launch the server.py file with Python 3.6 (and higher).

        python server.py

Depending on your server install, you may run this program locally and interact with it in your web browser on IP ***127.0.0.1:5000***.
For other server install refer to your server administrator, or DNS/IP registration, for further details.
This program is compatible with [Heroku](https://www.heroku.com/free). You may install it on Heroku, and run the page directly from there.
This version is available on [my Heroku space](https://papybotapp.herokuapp.com/)

-------------------------------------------------------------

***Setup recommendations***:

- Python 3.6 and up

    cf: requirements.txt for python dependencies required installs

    run in terminal:

        pip3 install -r [path-to-file]/requirements.txt
