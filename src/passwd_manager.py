import logging

from password_generator import PasswordGenerator
from threading import Thread
from time import sleep


class PasswdManager:

    def __init__(self):
        '''Class constructor.'''
        self.passwd_len = 10
        self.passwd_generator = PasswordGenerator()
        self.passwd_generator.minlen = self.passwd_len
        self.passwd_generator.maxlen = self.passwd_len
        self.updater_thread = Thread(name='updater_thread',
                                     target=self._updater_thread,
                                     daemon=True)
        self.updater_thread.start()
        logging.debug('PasswdManager.__init__() finishes')

    def get_curr_passwd(self):
        '''Password getter for password check.'''
        with open("passwd.txt", "r") as passwd_file:
            return passwd_file.read().rstrip()
        logging.debug('Got password from file.')

    def refresh_passwd(self):
        '''Refreshes password.'''
        with open("passwd.txt", "w") as passwd_file:
            passwd_file.write(self.passwd_generator.generate() + '\n')
        logging.debug('PasswdManager.RefreshPasswd() finishes.')

    def _updater_thread(self, period=3600):
        '''Thread function'''
        while True:
            self.refresh_passwd()
            sleep(preiod)
            logging.debug('Updated password.')
