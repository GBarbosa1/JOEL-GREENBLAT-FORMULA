import yfinance as yf
import pandas as pd

assets_dataframe = pd.read_json('assets_name.json')
roa_list = []
pe_list = []


for index, row in assets_dataframe.iterrows():
    asset = row['YFINANCE_CODE']
    
    
    try:
        asset_data = yf.Ticker(asset).info
        asset_roa = 100*asset_data['returnOnAssets']
        asset_trailing_pe = asset_data['trailingPE']
        asset_roa = round(asset_roa,2)
        asset_trailing_pe = round(asset_trailing_pe,2)
        roa_list.append(asset_roa)
        pe_list.append(asset_trailing_pe)

    

    except:
        print(asset+'error')

print(roa_list)

