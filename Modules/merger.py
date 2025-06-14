import pandas as pd

def tag_event_window(stock_df, cyclone_df, window=5):
    stock_df['Event'] = 0
    for date in cyclone_df['landfall_date']:
        mask = (stock_df.index >= date - pd.Timedelta(days=window)) & (stock_df.index <= date + pd.Timedelta(days=window))
        stock_df.loc[mask, 'Event'] = 1
    return stock_df