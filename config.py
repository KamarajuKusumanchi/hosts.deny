import configparser
import os

Config = configparser.ConfigParser()
Config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
