#!/usr/bin/python3

import json
import yfinance as yf
from flask import Flask, render_template, request
import locale

locale.setlocale(locale.LC_ALL, '')

# Set global "Current Stock" variable to keep up with what is being
# looked at between functions
global_current_stock = ""

# Set global variable to track status of "edit mode" as a boolean
global_edit_mode = False

# Refresh stocks in JSON file


def refresh_stocks():

    # Grab the stocks to check from the "stocks.json" file
    stocks_file = open("static/stocks.json", 'r')
    stock_data = json.load(stocks_file)
    stocks_file.close()

    # Grab stock info from each symbol
    for item in stock_data['ToCheck']:
        print("Gathering information on " + item + "...")
        stock_info = yf.Ticker(stock_data['ToCheck'][item])
        stock_data["Info"][item] = stock_info.info

    # Write info to json file
    stocks_file = open("static/stocks.json", "w")
    json.dump(stock_data, stocks_file, indent=4)
    stocks_file.close()

# Initialize Flask
app = Flask(__name__)

def first_stock():
    stocks_file = open("static/stocks.json", 'r')
    stock_data = json.load(stocks_file)
    stocks_file.close()

    keys = list(stock_data["ToCheck"].keys())
    stock_name = keys[0]
    return stock_name

# Load values from stocks JSON file
def load_values(stock_name = 'FirstRun'):

    # Set global tracked stock value to stock_name
    global global_current_stock
    global_current_stock = stock_name
    print("Current Stock: " + global_current_stock)

    # Open stocks.json file
    stocks_file= open("static/stocks.json", 'r')
    stock_data= json.load(stocks_file)
    stocks_file.close()

    # Create default value of first stock in list
    if stock_name == 'FirstRun':
        stock_name = first_stock()
        global_current_stock = stock_name
        print("Current Stock: " + global_current_stock)

    try: 
        stock_info = stock_data['Info'][global_current_stock]
    except:
        stock_name = first_stock()

    # Information to get from stock_info
    to_get_info = ['longName', 'logo_url', 'website', 'longBusinessSummary', 'shortName',
        'address1', 'city', 'state', 'zip', 'country',
        'phone', 'sector', 'industry', 'fullTimeEmployees', 'totalRevenue',
        'totalDebt', 'totalCash', 'profitMargins', 'grossMargins', 'operatingMargins', 
        'operatingCashflow', 'revenueGrowth', 'debtToEquity', 'lastFiscalYearEnd', '52WeekChange',
        'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'twoHundredDayAverage', 'averageVolume', 'averageDailyVolume10Day',
        'dividendRate', 'dividendYield', 'fiveYearAvgDividendYield', 'marketCap', 'regularMarketPrice']

    stocks_tracked = []
    stock_trailers = []
    stock_info_items = []

    # Load values from JSON file to list to pass to webpage
    for item in to_get_info:
        try:
            stock_info_items.append(stock_info[item])
        except:
            stock_info_items.append('N/A')

    # Add values for stocks being tracked
    for item in stock_data["ToCheck"]:
        if global_edit_mode == False:
            stocks_tracked.append(item)
        else:
            stocks_tracked.append("< " + item + " > --REMOVE")

    # Add trailing link for:
    #    If global_edit_mode is FALSE: link to start edit mode
    #    If global_edit_mode is TRUE: links to cancel editing, and to add a stock
    if global_edit_mode == False:
        stock_trailers.append("...Edit Stocks")
    else:
        stock_trailers.append("Add Stock")
        stock_trailers.append("...Cancel Editing")

    stock_info_items.append(stocks_tracked)
    print(stock_info_items)

    return stock_info_items

    # List of information for stock_info_items with index number
    # See "set_return()" for the setup
    #
    #  0 long_name = stock_info['longName']
    #  1 logo_url = stock_info['logo_url']
    #  2 website = stock_info['website']
    #  3 long_business_summary= stock_info['longBusinessSummary']
    #  4 short_name= stock_info['shortName']
    #  5 address = stock_info['address1']
    #  6 city = stock_info['city']
    #  7 state = stock_info['state']
    #  8 zipcode = stock_info['zip']
    #  9 country = stock_info['country']
    # 10 phone = stock_info['phone']
    # 11 ['sector']
    # 12 ['industry']
    # 13 ['fullTimeEmployees']
    # 14 ['totalRevenue']
    # 15 ['totalDebt']
    # 16 ['totalCash']
    # 17 ['profitMargins']
    # 18 ['grossMargins']
    # 19 ['operatingMargins']
    # 20 ['operatingCashflow']
    # 21 ['revenueGrowth']
    # 22 ['debtToEquity']
    # 23 ['lastFiscalYearEnd']
    # 24 ['52WeekChange']
    # 25 ['fiftyTwoWeekHigh']
    # 26 ['fiftyTowWeekLow']
    # 27 ['twoHundredDayAverage']
    # 28 ['averageVolume']
    # 29 ['averageDailyVolume10Day']
    # 30 ['dividendRate']
    # 31 ['dividendYield']
    # 32 ['fiveYearAvgDividendYield]
    # 33 ['marketCap']
    # 34 ['regularMarketPrice']
    # 35 [HTML for stocks being tracked on sidebar]
    # 36 [boolean for edit mode]

def set_return(page_name, stock_info_items):
    return_template = render_template(page_name,
                    long_name=stock_info_items[0],
                    logo_url=stock_info_items[1],
                    website=stock_info_items[2],
                    long_business_summary=stock_info_items[3],
                    short_name=stock_info_items[4],
                    address=stock_info_items[5],
                    city=stock_info_items[6],
                    state=stock_info_items[7],
                    zipcode=stock_info_items[8],
                    country=stock_info_items[9],
                    phone=stock_info_items[10],
                    sector=stock_info_items[11],
                    industry=stock_info_items[12],
                    full_time_employees=locale.format_string('%10.0f', stock_info_items[13], grouping=True),
                    total_revenue=locale.currency(stock_info_items[14], symbol=True, grouping=True),
                    total_debt=locale.currency(stock_info_items[15], symbol=True, grouping=True),
                    total_cash=locale.currency(stock_info_items[16], symbol=True, grouping=True),
                    profit_margins='{:.4%}'.format(stock_info_items[17]),
                    gross_margins='{:.4%}'.format(stock_info_items[18]),
                    operating_margins='{:.4%}'.format(stock_info_items[19]),
                    operating_cashflow=locale.currency(stock_info_items[20], symbol=True, grouping=True),
                    revenue_growth='{:.4%}'.format(stock_info_items[21]),
                    debt_to_equity=stock_info_items[22],
                    last_fiscal_year_end=locale.currency(stock_info_items[23], symbol=True, grouping=True),
                    fifty_two_week_change='$' + locale.str(stock_info_items[24]),
                    fifty_two_week_high=locale.currency(stock_info_items[25], symbol = True, grouping = True),
                    fifty_two_week_low=locale.currency(stock_info_items[26], symbol=True, grouping=True),
                    two_hundred_day_average=locale.currency(stock_info_items[27]),
                    average_volume=locale.format_string('%10.0f', stock_info_items[28], grouping=True),
                    average_daily_volume_10_day=locale.format_string('%10.0f', stock_info_items[29], grouping=True),
                    dividend_rate='{:.4%}'.format(stock_info_items[30]),
                    dividend_yield='{:.4%}'.format(stock_info_items[31]),
                    five_year_avg_dividend_yield='{:.4%}'.format(stock_info_items[32]),
                    market_cap=locale.currency(stock_info_items[33], symbol=True, grouping=True),
                    regular_market_price=locale.currency(stock_info_items[34], symbol=True, grouping=True),
                    tracked_stocks=stock_info_items[35],
                    edit_flag=global_edit_mode)
    return return_template


# Basic route
@app.route('/')
def index():
    stock_info_items = load_values("FirstRun")
    return_template = set_return('index.html', stock_info_items)
    return return_template

# Route to set up editing
@app.route('/edit')
def set_edit():
    # Set edit mode flag
    global global_edit_mode
    global_edit_mode = True

    print("Current Stock: " + global_current_stock)

    # Load the values to display
    stock_info_items = load_values(global_current_stock)
    return_template = set_return('index.html', stock_info_items)
    return return_template

# Cancel edit mode
@app.route('/canceledit')
def cancel_edit():
    # Set edit mode flag to cancel editing
    global global_edit_mode
    global_edit_mode = False

    # Load the values to display
    stock_info_items = load_values(global_current_stock)
    return_template = set_return('index.html', stock_info_items)
    return return_template

# Route to go to the Add a stock page
@app.route('/add')
def go_add():
    global global_edit_mode
    return render_template('add.html')

# Route to actually add the stock
@app.route('/addstock', methods=['GET', 'POST'])
def add_stock():
    stock_name = request.form.get("stockname", "")
    stock_symbol = request.form.get("stocksymbol", "")
    print('Stock Name: ' + stock_name)
    print('Stock Symbol: ' + stock_symbol)

    # Open file and load JSON stocks file
    stocks_file = open("static/stocks.json", "r")
    stocks_data = json.load(stocks_file)
    stocks_file.close()

    stocks_data['ToCheck'][stock_name] = stock_symbol

    # Write info to json file
    stocks_file = open("static/stocks.json", "w")
    json.dump(stocks_data, stocks_file, indent=4)
    stocks_file.close()

    refresh_stocks()
    global global_current_stock
    global_current_stock = stock_name

    # Load the values to display
    stock_info_items = load_values(global_current_stock)
    return_template = set_return('index.html', stock_info_items)
    return return_template

# Route to handle removing a stock in the Tracked Stocks list
@app.route('/remove/<stock_name>')
def remove_stock(stock_name):
    global global_current_stock

    # The remove link for a stock is messy. Clean it up
    # Iterate through the words in the passed stock_name
    # variable, separated by a space. Skip the "added bits"
    # that are not the name in the remove link, specifically:
    #   <
    #   >
    #   --REMOVE
    # And add the remaining words to the stock_name_parts list
    # Join the list into a space-separated string real_stock_name
    # to pass to load_values. This handles multi-word stock names
    stock_name_parts = []
    for word in stock_name.split():
        if word == "<":
            pass
        elif word == ">":
            pass
        elif word == "--REMOVE":
            pass
        else:
            stock_name_parts.append(word)

    real_stock_name = ' '.join(stock_name_parts)
    stock_info_items = load_values()

    stocks_file = open("static/stocks.json", "r")
    stock_data = json.load(stocks_file)
    stocks_file.close()
    del stock_data["ToCheck"][real_stock_name]
    del stock_data["Info"][real_stock_name]
    stocks_file = open("static/stocks.json", "w")
    json.dump(stock_data, stocks_file, indent=4)
    stocks_file.close()

    global global_current_stock
    global global_edit_mode
    global_current_stock = "FirstRun"
    global_edit_mode = False

    stock_info_items = load_values(global_current_stock)

    return_template = set_return('index.html', stock_info_items)
    return return_template

# Route to handle removing a stock in the Tracked Stocks list
@app.route('/check/<stock_name>')
def check_stock(stock_name):
    global global_current_stock
    global_current_stock = stock_name
    stock_info_items = load_values(global_current_stock)
    return_template = set_return('index.html', stock_info_items)
    return return_template

# Route to refresh stocks.json using stocks in Tracked Stocks list
@app.route('/refresh')
def go_refresh():
    refresh_stocks()
    stock_info_items = load_values()
    return_template = set_return('index.html', stock_info_items)
    return return_template

# Start Flask server
if __name__ == '__main__':
    app.run(debug=True, host='localhost')
