#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from bots.Bot import Bot


class TestBot(Bot):
    """
    Just for testing base bot functionalities.
    """

    def register_job(self):
        pass

    def message_handler(self, message):
        pass

    def bot_tick(self):
        pass
