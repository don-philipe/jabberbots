#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys
import json
import asyncio
import signal
import logging
from src.jabberbots.bots.TestBot import TestBot
from src.jabberbots.bots.WttrBot import WttrBot


def main(argv):
    config = read_config()
    bots = create_bots(config, log_level=logging.DEBUG)
    mainloop = asyncio.get_event_loop()
    mainloop.add_signal_handler(signal.SIGINT, stop_bots, bots)
    mainloop.call_soon(run_bots, bots, mainloop)
    try:
        mainloop.run_forever()
    finally:
        mainloop.close()


def read_config():
    """
    Reads the config file.
    @return: a dictionary containing the configuration for all bots.
    """
    config = None
    with open('config.json', 'r') as fh:
        config = json.load(fh)
    return config


def create_bots(config, log_level):
    """
    @return: the list of all bots created by this method
    """
    bots = []
    for bot in config:
        for key in config[bot]:
            if key == "type":
                bot_added = False
                if config[bot][key] == "TestBot":
                    bots.append(TestBot(config[bot]["jid"], config[bot]["password"], bot, None, log_level))
                    bot_added = True
                elif config[bot][key] == "WttrBot":
                    bots.append(WttrBot(config[bot]["jid"], config[bot]["password"], bot, None, log_level))
                    bot_added = True

                if bot_added:
                    print("### added " + bot + " ###")
    return bots


def run_bots(bots, loop):
    """
    @param bots: the bots to connect
    @param loop: the asyncio loop which should run the bots
    """
    for bot in bots:
        loop.create_task(bot.connect())


def stop_bots(bots):
    """
    Call stop method of all listed bots
    @param bots: the bots to stop
    """
    print("### stopping all bots... ###")
    for bot in bots:
        if bot.is_running():
            bot.stop_bot()


if __name__ == "__main__":
    main(sys.argv)
