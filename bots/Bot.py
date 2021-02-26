#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging
import asyncio
import signal
import time
import aioxmpp
import aioxmpp.dispatcher


class Bot(metaclass=ABCMeta):
    """
    This is the template class for all bots. It cares about low level stuff
    like initializing connection and running the main loop.
    """

    def __init__(self, jid, passwd, name, white_list, log_level, tick_interval=5, custom_config=None):
        """
        Initializes with parameters, sets logging level. Adds the receive_message
        method as callback for a message dispatcher.
        @param jid: jabber-ID of the account as string
        @param passwd: password of the account as string
        @param name: a name for the bot
        @param white_list: a list of JIDs from which messages are accepted
        @param log_level: the log level to set
        @param tick_interval: the interval between two bot ticks in seconds (default: 5)
        @param custom_config: custom config from config.json (default: None)
        """
        self.jid = jid
        self.passwd = passwd
        self.HELP = "Help text"
        self.name = name
        logging.basicConfig(level=log_level)
        self.log = logging.getLogger(name)
        self.white_list = white_list
        self.tick_interval = tick_interval
        self.client = None
        if custom_config is not None:
            self.custom_config(custom_config)
        #self.avatar = self._init_avatar()

    @abstractmethod
    def custom_config(self, config):
        """
        Custom configuration for the various bots.
        @param config: the "custom_config" object of the bot from config.json
        """
        pass

    def _init_avatar(self, image_location):
        """

        @param image_location:
        @return:
        """
        data = "TODO read image"
        avatar_set = aioxmpp.avatar.AvatarSet("image/png",
                                              None, None, data, None)
        return avatar_set

    async def connect(self):
        """
        Do the connecting stuff. Purges password variable after successful
        connecting.
        """
        self.log_msg("### Bot " + self.name + " connecting... ###", logging.DEBUG)
        self.client = aioxmpp.PresenceManagedClient(
            aioxmpp.JID.fromstr(self.jid), aioxmpp.make_security_layer(self.passwd))
        #avatar_service = self.client.summon(aioxmpp.avatar.AvatarService)
        #avatar_service.publish_avatar_set(self.avatar)
        dispatcher = self.client.summon(aioxmpp.dispatcher.SimpleMessageDispatcher)
        dispatcher.register_callback(aioxmpp.MessageType.CHAT, None, self._receive_message)
        async with self.client.connected() as stream:
            self.log_msg("### Bot " + self.name + " is connected ###", logging.DEBUG)
            self.passwd = None
            while True:
                await asyncio.sleep(self.tick_interval)
                self.bot_tick()

    @abstractmethod
    def bot_tick(self):
        """
        Things that should be done every tick.
        """
        pass

    def _receive_message(self, message):
        """
        The method that is registered at the message dispatcher. Checks for
        text "help" or "hilfe" and sends help message in that cases. Otherwise
        forwards received message to messageHandler() which has to be
        implemented by the extending class.
        @param message: the received message
        """
        if message.body:
            text = message.body.any()
            if text.lower() == "help" or text.lower() == "hilfe":
                self._get_help(message.from_)
            else:
                self.message_handler(message)

    @abstractmethod
    def message_handler(self, message):
        """
        Things that should be done when receiving a message. Has to be
        implemented by the extending class.
        @param message: the received message
        """
        pass

    def send_message(self, text, jid):
        """
        Send the given message text to the given jid with type 'chat'.
        @param text: the message text
        @param jid: the recipient of the message
        """
        msg = aioxmpp.Message(to=jid, type_=aioxmpp.MessageType.CHAT)
        msg.body[None] = text
        if self.client.running:
            asyncio.create_task(self.client.send(msg))

    async def send_message_all(self, message, jids):
        """
        Send a given message to a list of jids.
        @param message: the message text to send
        @param jids: a list of jids to send the message to
        """
        for jid in jids:
            await self.send_message(message, jid)

    def get_bot_name(self):
        """
        Get the bots name.
        @return: this bots name
        """
        return self.name

    def stop_bot(self):
        """
        Stops the bot.
        """
        self.log_msg("### stopping Bot " + self.name + "... ###", logging.DEBUG)
        self.client.stop()
        while self.client.running:
            time.sleep(1)

    @abstractmethod
    def register_job(self):
        """
        Register a job that runs on the server and notifies
        the (jabber)client on specified events or after a
        specified period of time.
        """
        pass

    def _get_help(self, jid):
        """
        @param jid: the jid of the user who wants help
        Send help information to user.
        """
        self.send_message(self.HELP, jid)

    def is_running(self):
        """
        Returns whether this bot is running or not.
        @return: the running state
        """
        return self.client.running

    def log_msg(self, msg, level):
        """
        Log message with root logger.
        @param msg: the message to log
        @param level: the log level
        """
        self.log.log(level, msg)
