#!/usr/bin/python3
#Version 2.0 - updated to use Google Finance instead of Yahoo Finance, since support for YF is flakey and I was getting errors

import sys
import json
import urllib.request
import os

stocks = ['GOOG', 'RHT']

#set to 0 if you don't want to see trade time in the drop-down menu
times = 1
timeL = []

#set to 0 if you don't want to see a link to your Yahoo Finance portfolio
#NB: Google portfolio (if it exists) not supported yet - you'll have to use Yahoo portfolio for now
portfolio = 1

try:
    for i in stocks:
        urllib.request.urlretrieve("https://finance.google.com/finance/info?client=ig&q=" + str(i), "quote.json")

        #Google adds 1 extra line and 3 extra characters ('// ') to the first part of the file. the next two commands remove those so json can process it
        os.system("sed -ie '1d' quote.json")
        os.system("sed -ie '1s/^...//' quote.json")
        with open("quote.json") as data_file:
            data = json.load(data_file)
            price = data[0]["l"]
            change = data[0]["c"] 
            
            if times == 1:
                timeL.append(data[0]["lt"]) 

        name = i
        if len(i) > 4:
            name = i[:4]

        if len(price) > 6:
            price = price[:6]

        if change == None:
            change = "0.00"
        elif len(change) > 5:
            change = change[:5]

        print (name + ": " + price + " (", end="")

        if change[:1] == "+":
            print("\033[1;32m" + change + "\033[0m) | href='https://www.google.ca/finance?q=" + i + "' refresh=true")
        elif change[:1] == "-":
            print("\033[1;31m" + change + "\033[0m) | href='https://www.google.ca/finance?q=" + i + "' refresh=true")
        elif change[:1] == "0":
            print("0.00) | href='https://www.google.ca/finance?q=" + i + "' refresh=true")

    if times == 1:
        print("---")
        print("Trade Times")
        x = 0
        for i in stocks:
            name = i
            if len(i) > 4:
                name = i[:4]
            print(name + ": " + timeL[x])
            x = x + 1

    if portfolio == 1:
        print("---")
        print("Portfolio... | href='https://ca.finance.yahoo.com/portfolio/p_0/view/v1'")

    os.system("rm quote.json*")

except:
    print("[Error]")
    print("---")
    print("[Refresh] | refresh=true")
    exit()
    os.system("rm quote.json*")
