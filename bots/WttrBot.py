#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from bots.Bot import Bot  # added in favor of 'import Bot' for unit testing
import urllib.request
import urllib.parse
import re


class WttrBot(Bot):
    """
    This bot uses the wttr.in API to fetch current weather for desired
    location.
    TODO: use JSON format for forecast https://wttr.in/Nuremberg?format=j1
    """

    HELP = "Send location name to get weather information about it."

    def message_handler(self, message):
        """
        Check message body for being a word and use that word for request
        at https://wttr.in. The word is interpreted as a city/place name.
        The answer string from wttr is then returned to the requesting user.
        @param message: the message should be only characters and whitespaces
        """
        print(message.body.any())
        city = re.search("^[A-ZÄÖÜa-zäöüß ]*$", message.body.any())
        if city is not None and len(city.group()) > 1:
            quoted_city = urllib.parse.quote(city.group())
            wttr = urllib.request.urlopen("https://wttr.in/" + quoted_city
                                          + "?format=4").read()
            answer = wttr.decode('utf_8')
        else:
            answer = "Location name should consist of characters and spaces " \
                     "only."
        Bot.send_message(self, answer, message.from_)

    def register_job(self):
        """
        """
        pass

    def bot_tick(self):
        """
        """
        pass
