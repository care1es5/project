#!/usr/bin/env python

import sys
import codecs



if __name__ == "__main__":
	data = ""
        with open("payload","r") as f:
             data = f.read().split()
        morse_lookup = {
        "A":"di-dah",
        "B":"dah-di-di-dit",
        "C":"dah-di-dah-dit",
        "D":"dah-di-dit",
        "E":"dit",
        "F":"di-di-dah-dit",
        "G":"dah-dah-dit",
        "H":"di-di-di-dit",
        "I":"di-dit",
        "J":"di-dah-dah-dah",
        "K":"dah-di-dah",
        "L":"di-dah-di-dit",
        "M":"dah-dah",
        "N":"dah-dit",
        "O":"dah-dah-dah",
        "P":"di-dah-dah-dit",
        "Q":"dah-dah-di-dah",
        "R":"di-dah-dit",
        "S":"di-di-dit",
        "T":"dah",
        "U":"di-di-dah",
        "V":"di-di-di-dah",
        "W":"di-dah-dah",
        "X":"dah-di-di-dah",
        "Y":"dah-di-dah-dah",
        "Z":"dah-dah-di-dit",
        "0":"dah-dah-dah-dah-dah",
        "1":"di-dah-dah-dah-dah",
        "2":"di-di-dah-dah-dah",
        "3":"di-di-di-dah-dah",
        "4":"di-di-di-di-dah",
        "5":"di-di-di-di-dit",
        "6":"dah-di-di-di-dit",
        "7":"dah-dah-di-di-dit",
        "8":"dah-dah-dah-di-dit",
        "9":"dah-dah-dah-dah-dit"
                
        }
        morse_lookup = {v: k for k, v in morse_lookup.iteritems()}
	print "".join(morse_lookup[m] for m in data)
