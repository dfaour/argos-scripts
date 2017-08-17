# argos-scripts
Scripts for the Argos Gnome Shell Extension
David Faour

## checkservers.py
Monitors a list of servers for connectivity. If all the servers are reachable, it will output a subtle green light (subtle to maximize top bar real estate). If one or more servers is not reachable, it outputs a red exclamation mark. Useful for keeping an eye on things.

## getnews.py
Will fetch news from an RSS feed to provide easy access to latest headlines.

Requires feedparser. To install:

`pip3 install feedparser`

## getquotes.py
Will fetch quotes and changes for stocks. Edit the 'stocks' list for your desired list.

Requires yahoo_finance. To install:

`pip3 install yahoo_finance`

To install the script in argos, copy it to ~/.config/argos and make it executable (chmod +x getquotes.py). Argos should pick it
up automatically.

April 25, 2017 (rev. Jun 8, 2017; August 17, 2017)
