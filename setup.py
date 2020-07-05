from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='ip-teller',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
    'pyTelegramBotAPI==3.7.1',
    'random-password-generator==2.1.0'
    ]
)
