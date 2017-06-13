#!/usr/bin/python3

from yahoo_finance import Share
import sys

stocks = ['GOOG', 'RHT']

#set to 0 if you don't want to see trade time in the drop-down menu
times = 1

#set to 0 if you don't want to see a link to your Yahoo Finance portfolio
portfolio = 1

try:
    for i in stocks:
        price = Share(i)
        name = i
        if len(i) > 4:
            name = i[:4]
        price2 = price.get_price()
        if len(price2) > 6:
            price2 = price2[:6]
        change = price.get_change()
        if len(change) > 5:
            change = change[:5]
        print (name + ": " + price2 + " (", end="")
        if price.get_change()[:1] == "+":
            print("\033[1;32m" + change + "\033[0m) | href='https://ca.finance.yahoo.com/quote/" + i + "' refresh=true")
        elif price.get_change()[:1] == "-":
            print("\033[1;31m" + change + "\033[0m) | href='https://ca.finance.yahoo.com/quote/" + i + "' refresh=true")

    if times == 1:
        print("---")
        print("Trade Times")
        for i in stocks:
            price = Share(i)
            name = i
            if len(i) > 4:
                name = i[:4]
            print(name + ": " + price.get_trade_datetime())

    if portfolio == 1:
        print("---")
        print("Portfolio... | href='https://ca.finance.yahoo.com/portfolio/p_0/view/v1'")

except:
    print("[Error] | refresh=true")
