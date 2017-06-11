#!/usr/bin/python3

from yahoo_finance import Share
import sys

stocks = ['GOOG', 'RHT']

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
            print("\033[1;32m" + change + "\033[0;37m ) | href='https://ca.finance.yahoo.com/quote/" + i + "' refresh=true")
        elif price.get_change()[:1] == "-":
            print("\033[1;31m" + change + "\033[0;37m ) | href='https://ca.finance.yahoo.com/quote/" + i + "' refresh=true")

    #If you use yahoo finance watchlist...
    #print("---")
    #print("Portfolio... | href='https://ca.finance.yahoo.com/portfolio/p_0/view/v1'")

except:
    print("[Connection error...]")
