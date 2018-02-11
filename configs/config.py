__author__ = 'Ramesh'
import os
from simpleconfigparser import simpleconfigparser

def init():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    configs = simpleconfigparser()
    configs.read(APP_ROOT + '/config.ini')
    global config_dict
    config_dict = {s: dict(configs.items(s)) for s in configs.sections()}

if 'config_dict' not in globals():
    init()
