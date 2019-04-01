#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import telebot
import sys
import logging
import time
import os
import openpyxl as px
import numpy as np
import pprint

def readPrice(pathToDB):
    W = px.load_workbook(pathToDB)
    p = W['Sheet1']

    a = []

    for row in p.iter_rows():
        b = []
        for k in row:
            if k.internal_value != None:
                val = k.internal_value
                if type(val) == unicode:
                    val = val.encode('utf-8')
                    val = val.lower()
                b.append(val)
        if b != []:
            a.append(b)

    return a

def checkAvailability(listPosition, reqCom):
    for xlStr in listPosition:
        if reqCom.decode("utf-8").lower() == xlStr[0].decode("utf-8").lower():
            print xlStr[0], xlStr[1], "рублей"
            return
    print "Comics \'{0}\' not found".format(reqCom)
    return


def readAndCheckAvailability(listPosition):
    while True:
        print "Write comics name"
        reqCom = raw_input()
        if reqCom == "":
            break
        checkAvailability(listPosition, reqCom)
    return

def main():
    myPath = os.getcwd()
    listPosition = readPrice(myPath + "/try_1.xlsx")
    readAndCheckAvailability(listPosition)
    print "Done"
    return

if __name__ == "__main__":
    sys.exit(main())