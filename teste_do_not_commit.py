import yfinance as yf
asset_data = yf.Ticker('AMAR3.SA').info
print(asset_data)
asset_roa = 100*asset_data['returnOnAssets']
asset_trailing_pe = asset_data['trailingPE']
print(asset_roa, asset_trailing_pe)