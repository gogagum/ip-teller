import logging
import json
import urllib

from telebot import TeleBot
from telebot import apihelper

from src.db_agent import DBAgent
from src.passwd_manager import PasswdManager

class Bot:

    def __init__(self):
        '''Default constructor.'''
        logging.basicConfig(filename='./log/debug.log',
                            level=logging.DEBUG,
			    format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
    
        logging.debug("Bot constructor.")
    
        self.passwd_manager = PasswdManager()
        self.telebot = TeleBot(self._getToken())
        self.db_agent = DBAgent()

        self.telebot.register_message_handler(
	    lambda message: self.starting_message(message), commands=['start'])
	
        self.telebot.register_message_handler(
	    lambda message: self.help_message(message), commands=['help'])
					  
        self.telebot.register_message_handler(
	    lambda message: self.get_query(message), commands=['get'])

        self.telebot.register_message_handler(
	    lambda message: self.get_login(message), commands=['register'])				  

    def starting_message(self, message):
        '''Starting message handler.'''
        logging.debug("Starting message.")
        if self.db_agent.check_if_known(message.from_user):
            self.telebot.send_message(
                chat_id=message.chat.id,
                text="Hello, {0}. ".format(message.from_user.first_name) +
                "You can get address writing /get."
            )
        else:
            self.telebot.send_message(chat_id=message.chat.id,
                                      text="What are you doing in my refregirator?")


    def _getToken(self):
        '''Telebot token getter.'''
        try:
            token_file = open("token.txt", "r")
        except FileNotFoundError:
            print("Couldn`t open token file.")
            logging.debug("Couldn`t open token file.")
            quit()
        else:
            return token_file.readline().rstrip()

    def help_message(self, message):
        '''Prints help information.'''
        logging.debug("Help message.")
        if (self.db_agent.check_if_known(message.from_user)):
            self.telebot.send_message(chat_id=message.chat.id,
                                      text="Print /get to get ip address.")
        else:
            self.telebot.send_message(chat_id=message.chat.id,
                                      text="I won't let you in my refregirator, " +
                                           "if you have no password.")

    def get_query(self, message):
        '''Answers to users query.'''
        logging.debug("Get query.")
        if self.db_agent.check_if_known(message.from_user):
            logging.debug("Known user {}".format(message.from_user))
            with urllib.request.urlopen("https://ifconfig.me/all.json") as url:
                data = json.loads(url.read().decode('utf-8'))
                self.telebot.send_message(chat_id=message.chat.id, text=data["ip_addr"])
        else:
            logging.debug("Unknown user {}".format(message.from_user))
            self.telebot.send_message(chat_id=message.chat.id,
                                      text="I don't understand.")

    def _check_passwd(message):
        '''Checks password from message.'''
        if (message.text == passwd_manager.GetCurrPasswd()):
            self.db_agent.add_to_known(message.from_user)
            bot.send_message(chat_id=message.chat.id,
                             text="Welcome, {0}".format(message.from_user.first_name))
        else:
            bot.send_message(chat_id=message.chat.id,
                             text="Are you hungri?")

    def login(self, message):
        '''Gives login to new user who got password.'''
        msg = self.telebot.send_message(chat_id=message.chat.id,
                                        text="Print password, if you know it.")
        self.telebot.register_next_step_handler(msg, _CheckPasswd)
