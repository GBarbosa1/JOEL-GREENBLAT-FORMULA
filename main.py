import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

assets_dataframe = pd.read_json('assets_name.json')
roa_list = []
pe_list = []
asset_name_list = []


for index, row in assets_dataframe.iterrows():
    asset = row['YFINANCE_CODE']
    asset_name_list.append(asset)
    
    try:
        asset_data = yf.Ticker(asset).info
        asset_roa = 100*asset_data['returnOnAssets']
        asset_roa = round(asset_roa,2)
        roa_list.append(asset_roa)

    except:
         asset_roa = 0
         roa_list.append(asset_roa)
         print(asset+'error on roa, roa is'+str(asset_roa))
         pass
    
    try:
        asset_trailing_pe = asset_data['trailingPE']
        asset_trailing_pe = round(asset_trailing_pe,2)
        pe_list.append(asset_trailing_pe)
        
    except:
        asset_trailing_pe = 0
        pe_list.append(asset_trailing_pe)
        print(asset+'error on pe, pe is'+str(asset_trailing_pe))
        pass
    

 

full_asset_data = {'ASSET_NAME':asset_name_list,'ROA':roa_list,'P_L':pe_list}

dataframe_full_asset_data = pd.DataFrame(data=full_asset_data)



dataframe_full_asset_data.fillna(value = 0, inplace=True)
dataframe_full_asset_data.sort_values(by='ROA', ascending=False, inplace= True)

x = dataframe_full_asset_data.ROA.tolist()
y = dataframe_full_asset_data.P_L.tolist()

dataframe_full_asset_data.to_excel('magic_list_list.xlsx')

plt.scatter(x, y)
plt.show()
