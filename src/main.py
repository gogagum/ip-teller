from telebot import TeleBot
from telebot import apihelper
from password_generator import PasswordGenerator
from db_agent import DBAgent
from passwd_manager import PasswdManager


def GetToken():
  '''Telebot token getter.'''
  with open("token.txt", "r") as token_file:
    return token_file.readline()[:-1]


def main():
  '''Func with main actions.'''
  # Objects used later.
  apihelper.proxy = {'https':'socks5://188.226.207.248:5555'}
  # passwd_manager = PasswdManager()
  bot = TeleBot(GetToken())
  # db_agent = DBAgent();

  @bot.message_handler(commands=['start'])
  def StartingMessage(message):
    '''Starting message handler.'''
    print('start worked somwhere\n')
    chat_id = message.chat.id
    name = message.from_user.first_name
    second_name = message.from_user.second_name

    if db_agent.CheckIfKnown(chat_id):
      bot.send_message("Hello, (0), ".format(name + ' ' + second_name) +
                       "you can get address writing /get.")
    else:
      bot.send_message("What are you doing in my refregirator?")

  @bot.message_handler(commands=['help'])
  def HelpMessage(message):
    '''Prints help information.'''
    pass

  @bot.message_handler(commands=['get'])
  def GetQuery(message):
    '''Answers to users query.'''
    pass

  @bot.message_handler(commands=['login'])
  def Login(message):
    '''Gives login to new user who got password.'''
    pass

  bot.polling()

if __name__ == "__main__":
  main()
