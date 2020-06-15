import sqlite  # For the first time, or it will be enough.

from telebot import TeleBot
from password_generator import PasswordGenerator

def main():
  # Classes used later.
  passwd_generator = PasswordGenerator()
  bot = TeleBot(GetToken())


  def GetToken():
    '''Telebot key getter.'''
    with token_file = open("token.txt", "r"):
      return token_file.read()

  def GetCurrPasswd():
    '''Password getter for password check.'''
    with passwd_file = open("passwd.txt", "r"):
      return curr_passwd.read()

  def RefreshPasswd():
    '''Refreshes password.'''
    with passwd_file = open("passwd.txt", "w"):
      passwd_file.write(passw_generator.generate())  # TODO: choose format

if __name__ == "__main__":
  main()
