#!/usr/bin/env python
#-*- coding=utf-8 -*-
__autor__ = 'nerowpt'

import logging
import getpass
import sys

class MyLog(object):
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logFile = './' + sys.argv[0][0:-3] + '.log'
        logFormat = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')
        #logFile = './testLog.txt'
        logHand = logging.FileHandler(logFile)
        logHand.setFormatter(logFormat)
        logHand.setLevel(logging.DEBUG)
        logHand.setLevel(logging.ERROR)
        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(logFormat)
        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandSt)
    def debug(self,msg):
        self.logger.debug(msg)
    def info(self,msg):
        self.logger.info(msg)
    def error(self,msg):
        self.logger.error(msg)
    def warn(self,msg):
        self.logger.warn(msg)
    def critical(self,msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug("I'm debug")
    mylog.info("I'm info")
    mylog.error("I'm error")
    mylog.warn("I'm warn")
    mylog.critical("I'm critical")
