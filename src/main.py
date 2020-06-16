from telebot import TeleBot
from password_generator import PasswordGenerator
from db_agent import DBAgent


def GetToken():
  '''Telebot token getter.'''
  with token_file = open("token.txt", "r"):
    return token_file.read()


def main():
  '''Func with main actions.'''
  # Objects used later.
  passwd_manager = PasswdManager()
  bot = TeleBot(GetToken())
  db_agent = DBAgent();

  bot.polling(none_stop=False, interval=0, timeout=20)

  @bot.message_handler(commands=['start'])
  def StartingMessage(message):
    '''Starting message handler.'''
    chat_id = message.chat.id
    name = message.from_user.first_name
    second_name = message.from_user.second_name

    if db_agent.CheckIfKnown(chat_id):  # Think over situations, when we found more than 2 (guess it means that user changed login)
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

if __name__ == "__main__":
  main()
