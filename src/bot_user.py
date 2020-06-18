class BotUser:
  def __init__(self, telegram_user):
    '''Fills fields with info of telegram_user.'''
    self.first_name = telegram_user.first_name
    self.second_name = telegram_user.last_name
    self.username = telegram_user.username
    self.id = telegram_user.id

  def NameToCall(self):
    '''Returns full name.'''
    return first_name + ' ' + second_name
