import sqlite3
import logging

from datetime import datetime

class DBAgent:

  def __init__(self):
    '''Class constructor'''
    self.db_path = '../db/'


  def CheckExistance(self):
    '''Checks if table exists.'''
    logging.debug("DBAgent.CheckExistance()")
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute('SELECT * '+
                     'FROM sqlite_master '+
                     "WHERE type='table' AND name='USERS';")
      row = cursor.fetchone()
      return row != None


  def CheckIfKnown(self, user):
    '''Checks if id is added to USERS.KNOWN.'''
    if not self.CheckExistance():
      self._CreateAllDb()
      self.AddToUnknown(user)
      return False
    # Check if known
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      found_by_id = cursor.execute(
        'SELECT id ' +
        'FROM users ' +
        'WHERE users.user_id={0} AND users.known=TRUE;'.format(user.id)
      )
      # Update name & login
      cursor.execute(
        'UPDATE USERS ' +
        "SET users.first_name  = '{0}', ".format(user.first_name) +
        "    users.second_name = '{0}', ".format(user.second_name) +
        "    users.login       = '{0}', ".format(user.login) +
        "WHERE users.user_id=(0);".format(user.id)
      )
    if len(found_by_id) == 0:
      AddToUnknown(user)
      return False
    return True

  def AddToUnknown(self, user):
    '''Adds unknown user to unknown users list(DB).'''
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute(
        'INSERT INTO users (id, first_nm, last_nm, user_nm, known) '+
        "VALUES ('{0}', '{1}', '{2}', '{3}', FALSE);".format(user.id,
                                                             user.first_name,
                                                             user.second_name,
                                                             user.username)
      )


  def AddToKnown(self, user):
    '''Adds user to known users list(DB).'''
    with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute(
        'UPDATE users '+
        "SET known = TRUE "+
        "WHERE id='{0}';".format(user.id)
      )


  def _CreateAllDb(self):
    '''Creates schema and tables'''
    with open('create.sql') as script_file:
      query_string = script_file.read()
      with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
        cursor = conn.cursor()
        cursor.execute(query_string)
