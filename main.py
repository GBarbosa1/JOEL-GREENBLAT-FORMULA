from scrap_engine import scrap_init, get_url, get_element_xpath, strip
import pandas as pd 
from data_converter import flotify, replacer
from graph_handler import graph_generator
from dataframe_handler import data_sort
import time
roe_list = []
pe_list = []
asset_name_list = []    
assets_dataframe = pd.read_json('assets_name.json')
base_url = 'https://statusinvest.com.br/acoes/'
browser = scrap_init(base_url)


for index, row in assets_dataframe.iterrows():
    asset = row['B3_CODE']
    asset_name_list.append(asset)
    asset_url = base_url + asset
    get_url(browser,asset_url)
    try:
        roe=get_element_xpath(browser,'//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[1]/div/div/strong')
        roe=strip(roe)
        roe_list.append(roe)


    except:
         roe = 0
         roe_list.append(roe)
         print("Error acquiring "+ asset)
         pass
    
    try:
        pe=get_element_xpath(browser,'//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong')
        pe=strip(pe)
        pe_list.append(roe)
        
        
    except:
         pe = 0
         pe_list.append(roe)
         print("Error acquiring "+ asset)
         pass
     
    print(roe, pe, time.time())
     
full_asset_data = {'ASSET_NAME':asset_name_list,'ROE':roe_list,'P_L':pe_list}
full_asset_dataframe = pd.DataFrame(data = full_asset_data, columns=['ASSET_NAME','ROE','P_L'])
full_asset_dataframe = full_asset_dataframe.apply(lambda x: x.str.replace(',','.'))
full_asset_dataframe = full_asset_dataframe.apply(lambda x: x.str.replace('-',''))
full_asset_dataframe = full_asset_dataframe.apply(lambda x: x.str.replace('%',''))
full_asset_dataframe = full_asset_dataframe.apply(lambda x: x.str.replace('null','0'))
full_asset_dataframe=data_sort(full_asset_dataframe,'P_L',False, True)
full_asset_dataframe = full_asset_dataframe.astype({'ASSET_NAME': 'str', 'ROE':'float', 'P_L':'float'}, errors= 'raise')
full_asset_dataframe=full_asset_dataframe[full_asset_dataframe.ROE >= 25]
full_asset_dataframe.to_csv('JOEL.csv')
graph_generator(full_asset_dataframe)
