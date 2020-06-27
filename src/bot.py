import logging
import json
import urllib

from telebot import TeleBot
from telebot import apihelper

from src.db_agent import DBAgent
from src.passwd_manager import PasswdManager


def GetToken():
    '''Telebot token getter.'''
    with open("token.txt", "r") as token_file:
        return token_file.readline().rstrip()

# Objects used later.
logging.basicConfig(filename='./log/debug.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('main started')
# apihelper.proxy = {'https':'socks5://188.226.207.248:5555'}

passwd_manager = PasswdManager()
bot = TeleBot(GetToken())
db_agent = DBAgent()

@bot.message_handler(commands=['start'])
def StartingMessage(message):
    '''Starting message handler.'''
    if db_agent.CheckIfKnown(message.from_user):
        bot.send_message(
            chat_id=message.chat.id,
            text="Hello, {0}, ".format(message.from_user.first_name) +
            "you can get address writing /get."
        )
    else:
        bot.send_message(chat_id=message.chat.id,
                         text="What are you doing in my refregirator?")

@bot.message_handler(commands=['help'])
def HelpMessage(message):
    '''Prints help information.'''
    if (db_agent.CheckIfKnown(message.from_user)):
        bot.send_message(chat_id=message.chat.id,
                         text="Print /get to get ip address.")
    else:
        bot.send_message(chat_id=message.chat.id,
                         text="I won't let you in my refregirator, " +
                              "if you have no password.")

@bot.message_handler(commands=['get'])
def GetQuery(message):
    '''Answers to users query.'''
    if (db_agent.CheckIfKnown(message.from_user)):
        # TODO: Check if it is stable enough
        with urllib.request.urlopen("http://ip.jsontest.com/") as url:
            data = json.loads(url.read())
            bot.send_message(chat_id=message.chat.id, text=data["ip"])
    else:
        bot.send_message(chat_id=message.chat.id,
                         text="I don't unsedstand.")

def _CheckPasswd(message):
    '''Checks password from message.'''
    if (message.text == passwd_manager.GetCurrPasswd()):
        db_agent.AddToKnown(message.from_user)
        bot.send_message(chat_id=message.chat.id,
                         text="Welcome, {0}".format(message.from_user.first_name))
    else:
        bot.send_message(chat_id=message.chat.id,
                         text="Are you hungri?")

@bot.message_handler(commands=['register'])
def Login(message):
    '''Gives login to new user who got password.'''
    msg = bot.send_message(chat_id=message.chat.id,
                           text="Print password, if you know it.")
    bot.register_next_step_handler(msg, _CheckPasswd)


