import sqlite3
import logging
import os

from datetime import datetime
import logging


class DBAgent:

    def __init__(self):
        '''Class constructor'''
        self.db_path = './db/'

    def CheckExistance(self):
        '''Checks if table exists.'''
        logging.debug("DBAgent.CheckExistance()")
        try:
            conn = sqlite3.connect(self.db_path + 'users.sqlite')
            cursor = conn.cursor()
            cursor.execute('SELECT * ' +
                           'FROM sqlite_master ' +
                           "WHERE type='table' AND name='users';")
            row = cursor.fetchone()
            return row is not None
        except sqlite3.OperationalError:
            logging.debug("Create ./db path.")
            os.mkdir("db")
            conn = sqlite3.connect(self.db_path + 'users.sqlite')
            return False

    def CheckIfKnown(self, user):
        '''Checks if id is added to USERS.KNOWN.'''
        if not self.CheckExistance():
            self._CreateAllDb()
            self.AddToUnknown(user)
            logging.debug('Table does not exisit.')
            return False
        # Check if known
        with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
            cursor = conn.cursor()
            # Update name & login
            cursor.execute(
              'UPDATE users ' +
              "SET first_nm = '{0}', ".format(user.first_name) +
              "    last_nm  = '{0}', ".format(user.last_name) +
              "    user_nm  = '{0}'  ".format(user.username) +
              "WHERE user_id=={0};".format(user.id)
            )
            cursor.fetchone()
            # Check if user exists
            cursor.execute(
              'SELECT user_id ' +
              'FROM users ' +
              'WHERE user_id=={0} AND known;'.format(user.id)
            )
            row = cursor.fetchone()

        if row is None:
            logging.debug('row == None in DBAgent.CheckIfKnown()')
            self.AddToUnknown(user)
            return False
        return True

    def AddToUnknown(self, user):
        '''Adds unknown user to unknown users list(DB).'''
        with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(
              'INSERT OR IGNORE INTO users ' +
              '(user_id, first_nm, last_nm, user_nm, known) ' +
              "VALUES ('{0}', '{1}', '{2}', '{3}', FALSE);".format(
                user.id,
                user.first_name,
                user.last_name,
                user.username
              )
            )

    def AddToKnown(self, user):
        '''Adds user to known users list(DB).'''
        if not self.CheckExistance():
            self._CreateAllDb()
            self.AddToUnknown(user)
        with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(
              'UPDATE users ' +
              "SET known = TRUE " +
              "WHERE user_id='{0}';".format(user.id)
            )

    def _CreateAllDb(self):
        '''Creates schema and tables'''
        with open('src/create.sql') as script_file:
            query_string = script_file.read()
            with sqlite3.connect(self.db_path + 'users.sqlite') as conn:
                cursor = conn.cursor()
                cursor.execute(query_string)
