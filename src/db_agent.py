import sqlite3  # For the first time, or it will be enough.

class DBAgent:

  def init(self):
    '''Class constructor'''
    pass

  def CheckIfKnown(self, user_id):
    '''Checks if id is added to db.'''
    with sqlite3.connect('known_users.sqlite') as conn:
      cursor = conn.cursor()
      found_by_id = cursor.execute(
        'select ID' +
        'from USERS_DB.KNOWN_USERS' +
        'where ID = (0)'.format(chat_id)
      )
    return len(found_by_id) == 1   # Think over situations, when we found more than 2 (guess it means that user changed login)

  def AddToUnknown(self, user):
    '''Adds stranger to unknown.'''
    with sqlite3.connect('strangers.sqlite') as conn:
      cursor = conn.cursor()
      cursor.execute('') # TODO: write query

  def _EraseFromUnknown(self, user_id):
    '''In case user becomes from stranger to known user, when logged in.'''
    with sqlite3.connect('strangers.squlite') as conn:
      cursor = conn.cursor()
      cursor.execute('') # TODO: write query
