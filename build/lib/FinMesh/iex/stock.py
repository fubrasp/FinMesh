from ._common import *

#   Balance Sheet
IEX_BALANCE_SHEET_URL = prepend_iex_url('stock') + '{symbol}/balance-sheet'
def balance_sheet(symbol, vprint=False, **queries):
    ## Returns balance sheet data for the requested ticker.
    url = replace_url_var(IEX_BALANCE_SHEET_URL, symbol=symbol)
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)

#   Batch Requests
def batch_requests():
    raise ImplementationError("Function cannot be implemented.")

#   Book
IEX_BOOK_URL = prepend_iex_url('stock') + '{symbol}/book?'
def book(symbol, vprint=False):
    ## Returns book price data for the requested ticker.
    url = replace_url_var(IEX_BOOK_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Cash Flow

IEX_CASH_FLOW_URL = prepend_iex_url('stock') + '{symbol}/cash-flow'
def cash_flow(symbol, vprint=False, **queries):
    ## Returns the cash flow statement for the requested ticker.
    url = replace_url_var(IEX_CASH_FLOW_URL, symbol=symbol)
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)

#   Collections
IEX_COLLECTION_URL = prepend_iex_url('stock') + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName, vprint=False):
    ## Returns a list of tickers belonging to the requested collection.
    url = replace_url_var(IEX_COLLECTION_URL, collectionType=collectionType, collectionName=collectionName)
    return get_iex_json_request(url, vprint=vprint)

#   Company
IEX_COMPANY_URL = prepend_iex_url('stock') + '{symbol}/company?'
def company(symbol, vprint=False):
    ## Returns company data such as website, address, and description for the requested ticker.
    url = replace_url_var(IEX_COMPANY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Delayed Quote
IEX_DELAYED_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/delayed-quote?'
def delayed_quote(symbol, vprint=False):
    ## Returns a 15-minute delayed market quote for the requested ticker.
    url = replace_url_var(IEX_DELAYED_QUOTE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Dividends
IEX_DIVIDENDS_URL = prepend_iex_url('stock') + '{symbol}/dividends/{scope}?'
def dividends(symbol, scope, vprint=False):
    ## Returns dividend information for a requested ticker.
    url = replace_url_var(IEX_DIVIDENDS_URL, symbol=symbol, scope=scope)
    return get_iex_json_request(url, vprint=vprint)

#   Earnings
IEX_EARNINGS_URL = prepend_iex_url('stock') + '{symbol}/earnings'
def earnings(symbol, last=None, field=None, vprint=False):
    ## Returns earnings data such as actual EPS, beat/miss, and date for the requested ticker.
    url = replace_url_var(IEX_EARNINGS_URL, symbol=symbol)
    if last and field:
        url+= f"/{last}/{field}?"
    elif last:
        url+= f"/{last}?"
    else:
        url += '?'
    return get_iex_json_request(url, vprint=vprint)

#   Earnings Today
IEX_TODAY_EARNINGS_URL = prepend_iex_url('stock') + 'market/today-earnings?'
def today_earnings(vprint=False):
    ## Returns earnings data released today, grouped by timing and stock.
    url = IEX_TODAY_EARNINGS_URL
    return get_iex_json_request(url, vprint=vprint)

# DEPRECATED
"""#   Effective Spread
IEX_EFFECTIVE_SPREAD_URL = prepend_iex_url('stock') + '{symbol}/effective-spread?'
def effective_spread(symbol):
    url = replace_url_var(IEX_EFFECTIVE_SPREAD_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)"""

#   Estimates
IEX_ESTIMATES_URL = prepend_iex_url('stock') + '{symbol}/estimates?'
def estimates(symbol, vprint=False):
    ## Returns latest future earnings estimates for the requested ticker.
    url = replace_url_var(IEX_ESTIMATES_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Financials
IEX_FINANCIALS_URL = prepend_iex_url('stock') + '{symbol}/financials?'
def financials(symbol, period=None, vprint=False):
    ## Returns a brief overview of a company's financial statements.
    url = replace_url_var(IEX_FINANCIALS_URL, symbol=symbol)
    url += f'period={period}' if period else ''
    return get_iex_json_request(url, vprint=vprint)

#   Fund Ownership
IEX_FUND_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/fund-ownership?'
def fund_ownership(symbol, vprint=False):
    ## Returns the largest 10 fund owners of the requested ticker. This excludes explicit buy or sell-side firms.
    url = replace_url_var(IEX_FUND_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

IEX_HISTORICAL_URL = prepend_iex_url('stock')
def historical_price(symbol, period, date=None, vprint=False, **queries):
    ## Returns the historical price for the requested ticker.
    # Soon to be deprecated
    # Here the query string parameters are handled a bit differently because
    # there are so many.  This may be inconsistent but no other way is realistic
    url = IEX_HISTORICAL_URL + f"{symbol}/chart/{period}"
    if period == 'date':
        assert date not None, 'Please enter a valid date!'
        url += f'/{date}?'
    else:
        url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    url = append_iex_token(url)
    if vprint: print(f"Now fetching: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

#   Income Statement
IEX_INCOME_STATEMENT_URL = prepend_iex_url('stock') + '{symbol}/income'
def income_statement(symbol, vprint=False, **queries):
    ## Returns the income statement financial data for the requested ticker.
    url = replace_url_var(IEX_INCOME_STATEMENT_URL, symbol=symbol)
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)

#   Insider Roster
IEX_INSIDER_ROSTER_URL = prepend_iex_url('stock') + '{symbol}/insider-roster?'
def insider_roster(symbol, vprint=False):
    ## Returns the 10 largest insider owners for the requested ticker.
    url = replace_url_var(IEX_INSIDER_ROSTER_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Insider Summary
IEX_INSIDER_SUMMARY_URL = prepend_iex_url('stock') + '{symbol}/insider-summary?'
def insider_summary(symbol, vprint=False):
    ## Returns a summary of the insiders and their actions within the last 6 months for the requested ticker
    url = replace_url_var(IEX_INSIDER_SUMMARY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Insider Transactions
IEX_INSIDER_TRANSACTIONS_URL = prepend_iex_url('stock') + '{symbol}/insider-transactions?'
def insider_transactions(symbol, vprint=False):
    ## Returns a summary of insider transactions for the requested ticker.
    url = replace_url_var(IEX_INSIDER_TRANSACTIONS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Institutional Ownership
IEX_INSTITUTIONAL_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/institutional-ownership?'
def institutional_ownership(symbol, vprint=False):
    ## Returns the 10 largest instituional owners for the requested ticker. This is defined as explicitly buy or sell-side only.
    url = replace_url_var(IEX_INSTITUTIONAL_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   IPO Calendar
IEX_UPCOMING_IPOS_URL = prepend_iex_url('stock') + 'market/upcoming-ipos?'
def ipo_upcoming(vprint=False):
    ## Returns a list of upcoming IPOs for the current and next month.
    return get_iex_json_request(IEX_UPCOMING_IPOS_URL)

IEX_TODAY_IPOS_URL = prepend_iex_url('stock') + 'market/today-ipos?'
def ipo_today(vprint=False):
    ## Returns a list of IPOs happening today.
    return get_iex_json_request(IEX_TODAY_IPOS_URL)

#   Key Stats
IEX_STATS_URL = prepend_iex_url('stock') + '{symbol}/stats'
def key_stats(symbol, stat=False, vprint=False):
    ## Returns important and key statistics for the requested ticker.
    url = replace_url_var(IEX_STATS_URL, symbol=symbol)
    url += str(stat) if stat else '?'
    return get_iex_json_request(url, vprint=vprint)

#   Largest Trades
IEX_LARGEST_TRADES_URL = prepend_iex_url('stock') + '{symbol}/largest-trades?'
def largest_trades(symbol, vprint=False):
    ## Returns a delayed list of largest trades for the requested ticker.
    url = replace_url_var(IEX_LARGEST_TRADES_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   List
IEX_MARKET_LIST_URL = prepend_iex_url('stock') + '{symbol}/list/{list_type}?'
def market_list(symbol, list_type, displayPercent=None, vprint=False):
    ## Returns the 10 largest companies in the specified list.
    url = replace_url_var(IEX_MARKET_LIST_URL, symbol=symbol, list_type=list_type)
    url += f'displayPercent={displayPercent}' if displayPercent else ''
    return get_iex_json_request(url, vprint=vprint)

#   Logo
IEX_LOGO_URL = prepend_iex_url('stock') + '{symbol}/logo?'
def logo(symbol, vprint=False):
    ## Returns a Google APIs link to the logo for the requested ticker.
    url = replace_url_var(IEX_LOGO_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Market Volume (U.S.)
IEX_MARKET_VOLUME_URL = prepend_iex_url('stock') + 'market/volume?'
def market_volume(format=None, vprint=False):
    ## Returns market wide trading volume.
    url = IEX_MARKET_VOLUME_URL
    url += f'format={format}' if format else ''
    return get_iex_json_request(url, vprint=vprint)

#   News
IEX_NEWS_URL = prepend_iex_url('stock') + '{symbol}/news'
def news(symbol, last=None, vprint=False):
    ## Returns news item summaries for the requested ticker.
    url = replace_url_var(IEX_NEWS_URL, symbol=symbol)
    url += f'/last/{last}?' if last else '?'
    return get_iex_json_request(url, vprint=vprint)

#   OHLC
IEX_OHLC_URL = prepend_iex_url('stock') + '{symbol}/ohlc?'
def ohlc(symbol, vprint=False):
    ## Returns the most recent days open, high, low, and close data for the requested ticker.
    url = replace_url_var(IEX_OHLC_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Peers
IEX_PEERS_URL = prepend_iex_url('stock') + '{symbol}/peers?'
def peers(symbol, vprint=False):
    ## Returns a list of a requested ticker's peers.
    url = replace_url_var(IEX_PEERS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Previous Day Prices
IEX_PREVIOUS_URL = prepend_iex_url('stock') + '{symbol}/previous?'
def previous(symbol, vprint=False):
    ## Returns the previous day\'s price data for the requested ticker.
    url = replace_url_var(IEX_PREVIOUS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Price
IEX_PRICE_URL = prepend_iex_url('stock') + '{symbol}/price?'
def price(symbol, vprint=False):
    ## Returns a single float value of the requested ticker's price.
    url = replace_url_var(IEX_PRICE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Price Target
IEX_PRICE_TARGET_URL = prepend_iex_url('stock') + '{symbol}/price-target?'
def price_target(symbol, vprint=False):
    ## Returns analyst's price targets for the requested ticker.
    url = replace_url_var(IEX_PRICE_TARGET_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Quote
IEX_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/quote'
def quote(symbol, field=None, vprint=False):
    ## Returns price quote data for the requested ticker. Fields are able to be called individually.
    url = replace_url_var(IEX_QUOTE_URL, symbol=symbol)
    url += f'/{field}?' if field else '?'
    return get_iex_json_request(url, vprint=vprint)

#   Recommended Trends
IEX_RECOMMENDED_TRENDS_URL = prepend_iex_url('stock') + '{symbol}/recommendation-trends?'
def recommendation_trends(symbol, vprint=False):
    ## Returns analyst recommendations for the requested ticker.
    url = replace_url_var(IEX_RECOMMENDED_TRENDS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)

#   Sector Performance
IEX_SECTOR_PERFORMANCE_URL = prepend_iex_url('stock') + 'market/sector-performance?'
def sector_performance(vprint=False):
    ## Returns market performance for all sectors.
    return get_iex_json_request(IEX_SECTOR_PERFORMANCE_URL)

#   Splits
IEX_SPLITS_URL = prepend_iex_url('stock') + '{symbol}/splits'
def splits(symbol, scope=None, vprint=False):
    ## Returns a record of stock splits for the requested ticker.
    url = replace_url_var(IEX_SPLITS_URL, symbol=symbol)
    url += f'/{scope}?' if scope else '?'
    return get_iex_json_request(url, vprint=vprint)

#   Volume by Venue
IEX_VOLUME_BY_VENUE_URL = prepend_iex_url('stock') + '{symbol}/volume-by-venue'
def volume_by_venue(symbol, vprint=False):
    ## Returns trading volume for the requested ticker by venue.
    url = replace_url_var(IEX_VOLUME_BY_VENUE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
