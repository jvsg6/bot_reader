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
    p = W.get_sheet_by_name(name='Sheet1')

    a = []

    for row in p.iter_rows():
        b = []
        for k in row:
            if k.internal_value != None:
                val = k.internal_value
                if type(val) == unicode:
                    #val = val.encode('cp1251')
                    print val.encode('utf-8')
                b.append(val)
        if b != []:
            a.append(b)
    print "\n".join([str(i) for i in a])

    return


def main():
    print "Done!"
    myPath = os.getcwd()
    readPrice(myPath + "/try_1.xlsx")
    return

if __name__ == "__main__":
    sys.exit(main())