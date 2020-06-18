import sqlite3  # For the first time, or it will be enough.
from datetime import datetime

class DBAgent:

  def __init__(self, db_path = '../db/'):
    '''Class constructor'''
    self.db_path = db_path


  def CheckTableExistance(self, table_name):
    '''Checks if table with name <table name> exists.'''
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute('SELECT count(name) '+
                     'FROM sqlite_master '+
                     '''WHERE type='table' AND name=(0)'''.format(table_name))
      return cursor.fetchone()[0]==1


  def CheckIfKnown(self, user):
    '''Checks if id is added to db.'''
    if not self.CheckTableExistance('USERS.KNOWN_USERS'):
      return False
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      found_by_id = cursor.execute(
        'select ID '+
        'from USERS_DB.KNOWN_USERS '
        'where ID == (0)'.format(user.id)
      )
    if len(found_by_id) == 0:
      return False
    if found_by_id.login != user.login:
      pass  # TODO change login in db


  def AddToUnknown(self, user):
    '''Adds unknown user to unknown users list(DB).'''
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute(
        'insert into table USERS_DB.UNKNOWN_USERS'+
        'values((0), (1), (2), (4));'.format(user.id, user.nickname,
                                             user.name, user.second_name,
                                             datetime.now())
      ) # TODO: check for errors


  def AddToKnown(self, user):
    '''Adds user to known users list(DB).'''
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute(
        'insert into table USERS_DB.KNOWN_USERS'+
        'values((0), (1), (2), (4));'.format(user.id, user.nickname,
                                             user.name, user.second_name,
                                             datetime.now())
      )
    _EraseFromUnknown(user.user_id)


  def _EraseFromUnknown(self, user_id):
    '''Deletes user from db with unknown users who visited bot.'''
    with sqlite3.connect('users.squlite') as conn:
      cursor = conn.cursor()
      cursor.execute(
        'delete from USERS_DB.UNKNOWN_USERS'+
        'where UNKNOWN_USERS.USER_ID = (0)'.format(user_id)
      )
