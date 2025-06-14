import yfinance as yf

def get_stock_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, group_by='ticker')
    return data
