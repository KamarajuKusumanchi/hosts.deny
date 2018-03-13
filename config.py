from configparser import ConfigParser, ExtendedInterpolation
import os

Config = ConfigParser(interpolation=ExtendedInterpolation())
Config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
