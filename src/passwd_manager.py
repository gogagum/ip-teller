class PasswdManager:
  def init(self):
    '''Class constructor.'''
    passwd_generator = PasswordGenerator()

  def GetCurrPasswd(self):
    '''Password getter for password check.'''
    with open("passwd.txt", "r") as passwd_file:
      return curr_passwd.read()

  def RefreshPasswd(self):
    '''Refreshes password.'''
    with open("passwd.txt", "w") as passwd_file:
      passwd_file.write(passwd_generator.generate())  # TODO: choose format
