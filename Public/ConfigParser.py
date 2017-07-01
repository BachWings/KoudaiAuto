__author__ = 'Bach'
__time__ = '2017/5/19'

import configparser


def getConfig(section, key):
    config = configparser.ConfigParser()
    config.read("E:\\Github\\KoudaiAuto\\PocketWallet\\PageObject\\PwProperties.ini", encoding="utf-8")
    return config.get(section, key)

