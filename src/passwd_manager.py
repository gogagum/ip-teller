from password_generator import PasswordGenerator


class PasswdManager:

  def __init__(self):
    '''Class constructor.'''
    self.passwd_len = 10
    passwd_generator = PasswordGenerator()


  def GetCurrPasswd(self):
    '''Password getter for password check.'''
    with open("passwd.txt", "r") as passwd_file:
      return curr_passwd.read()


  def RefreshPasswd(self):
    '''Refreshes password.'''
    with open("passwd.txt", "w") as passwd_file:
      passwd_file.write(passwd_generator.generate(minlen=self.passwd_len,
                                                  maxlen=self.passwd_len))
