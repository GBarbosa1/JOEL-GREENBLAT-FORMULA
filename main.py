import yfinance as yf
import pandas as pd

assets_dataframe = pd.read_json('assets_name.json')
print(assets_dataframe)


for index, row in assets_dataframe.iterrows():
    asset = row['YFINANCE_CODE']
    asset_data = yf.Ticker(asset).info
    try:
        asset_roa = 100*asset_data['returnOnAssets']

    except:
        print(asset+'error')
    print(asset_roa)


