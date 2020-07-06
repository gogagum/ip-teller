import logging

from os import path
from os import mkdir
from os.path import expanduser

class DirectoryManager:

  def __init__(self):
      '''Class constructor'''
      self.GetDirToSave()

  def CreateAllDir(self):
      if not path.exists(self.dir_to_save):
          mkdir(self.dir_to_save)
          mkdir(self.dir_to_save + "/log")
          mkdir(self.dir_to_save + "/db")

  def GetDirToSave(self):
      '''Gets standart directory location to save files.'''
      self.dir_to_save = self.GetHomeDir() + "/ip-teller/"
      if not path.exists(self.dir_to_save):
          self.CreateAllDir()
      if not path.exists(self.dir_to_save + "/log"):
          mkdir(self.dir_to_save + "/log")
      if not path.exists(self.dir_to_save + "/db"):
          mkdir(self.dir_to_save + "/db")
      return(self.dir_to_save)

  def GetHomeDir(self):
      return expanduser("~")

  def GetToken(self):
      '''Telebot token getter.'''
      try:
          token_file = open(self.dir_to_save + "token.txt", "r")
      except FileNotFoundError:
          print("Couldn`t open token file. " +
                "Please add token file according to readme and restart app.")
          logging.debug("Couldn`t open token file. Stopping.")
          quit()
      else:
          return token_file.readline().rstrip()
