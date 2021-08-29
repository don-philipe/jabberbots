#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from src.jabberbots.bots.Bot import Bot


class TestBot(Bot):
    """
    Just for testing base bot functionalities.
    """

    def _init_help_text(self):
        pass

    def custom_config(self, config):
        pass

    def message_handler(self, message):
        pass

    def bot_tick(self):
        pass
