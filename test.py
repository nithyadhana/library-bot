# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:17:06 2018

@author: Surya
"""
import csv
csv_file = csv.reader(open('books1.csv'), delimiter=",")
zone = "1"        
for row in csv_file:
    if zone == row[0]:
        speech = ("\n\nBook Id: " + row[0] + "\n Book Title: " + row[1] + "\n Authors: " + row[2] + "\n Publication: " + row[3] + "\n Rack Number:" + row[4])
        
        print(speech)
        
