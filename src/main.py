from telebot import TeleBot
from telebot import apihelper

from db_agent import DBAgent
from passwd_manager import PasswdManager
from bot_user import BotUser


def GetToken():
  '''Telebot token getter.'''
  with open("token.txt", "r") as token_file:
    return token_file.readline().rstrip()


def main():
  '''Func with main actions.'''
  # Objects used later.
  apihelper.proxy = {'https':'socks5://188.226.207.248:5555'}
  passwd_manager = PasswdManager()
  bot = TeleBot(GetToken())
  db_agent = DBAgent();


  @bot.message_handler(commands=['start'])
  def StartingMessage(message):
    '''Starting message handler.'''
    user = BotUser(message.from_user)

    if db_agent.CheckIfKnown(user):
      bot.send_message(chat_id=message.chat_id,
                       text="Hello, (0), ".format(user.NameToCall()) +
                            "you can get address writing /get.")
    else:
      bot.send_message(chat_id=message.chat.id,
                       text="What are you doing in my refregirator?")


  @bot.message_handler(commands=['help'])
  def HelpMessage(message):
    '''Prints help information.'''
    user = BotUser(message.from_user)
    if (db_agent.CheckIfKnown(user)):
      pass
    else:
      bot.send_message(chat_id=message.chat_id,
                       text="I won't let you in my refregirator, "+
                            "if you have no password.")


  @bot.message_handler(commands=['get'])
  def GetQuery(message):
    '''Answers to users query.'''
    user = BotUser(message.from_user)
    if (db_agent.CheckIfKnown(user)):
      pass
    else:
      bot.send_message(chat_id=message.chat_id,
                       text="I don't unsedstand.")


  @bot.message_handler(func=lambda message: True, content_types=['text'])
  def Login(message):
    '''Gives login to new user who got password.'''
    if (message.text == PasswdManager.GetCurrPasswd()):
      db_agent.AddToKnown(0)
    else:
      bot.send_message(chat_id=message.chat_id,
                       text="Are you hungri?")


  bot.polling()

if __name__ == "__main__":
  main()
