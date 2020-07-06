import ip_teller_src

from ip_teller_src.directory_manager import DirectoryManager
from setuptools import setup, find_packages
from os.path import join, dirname

directory_manager = DirectoryManager()

setup(
    version=ip_teller_src.__version__,
    name='ip-teller',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
    'pyTelegramBotAPI==3.7.1',
    'random-password-generator==2.1.0'
    ],
    entry_points={
   'console_scripts': [
       'ip-teller = ip_teller_src.core:main'
       ]
   }
)
