# stockcheck

Stockcheck is a basic Python Flask application.

Use is simple: 

1: Clone the repo into a directory
2: cd to the subdirectory
3: Run 'server.py'
4: Direct your web browser to localhost:5000

The stock information will show up on the right hand side of the screen.
The list of stocks that you are tracking will show up on the left hand side of the screen.
At the bottom of the list of tracked stocks, there is an Edit link.
Clicking the edit link allows you to add or remove stocks from the list
(Note: you WILL need both the name of the stock, as well as the stock symbol)

This application makes use of the YFinance (Yahoo Finance) module for Python, and you will need to install it if it is not already installed.