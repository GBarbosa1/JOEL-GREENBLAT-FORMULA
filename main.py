from scrap_engine import scrap_init
import pandas as pd 
from data_converter import flotify, replacer
from graph_handler import graph_generator
import time
roe_list = []
pe_list = []
asset_name_list = []    
assets_dataframe = pd.read_json('assets_name.json')
base_url = 'https://statusinvest.com.br/acoes/'


for index, row in assets_dataframe.iterrows():
    asset = row['B3_CODE']
    asset_name_list.append(asset)
    asset_url = base_url + asset
    soup = scrap_init(True, asset_url)
    
    try:
        
        roe = soup.find('div', title='Mede a capacidade de agregar valor de uma empresa a partir de seus próprios recursos e do dinheiro de investidores.')
        roe = roe.find('strong',class_ ='value d-block lh-4 fs-4 fw-700').text.strip()
        roe = replacer(roe, '%', '')
        roe = replacer(roe, ',','.')
        roe = flotify(roe)
        roe_list.append(roe)

    except:
         roe = 0
         roe_list.append(roe)
         print("Error acquiring "+ asset)
         pass
    
    try:
        pe = soup.find('div', title='Dá uma ideia do quanto o mercado está disposto a pagar pelos lucros da empresa.')
        pe = pe.find('strong',class_ ='value d-block lh-4 fs-4 fw-700').text.strip()
        pe = replacer(pe, '%', '')
        pe = replacer(pe, ',','.')
        pe = flotify(pe)
        pe_list.append(pe)
        
        
    except:
         print("Error acquiring "+ asset)
         pass
     
    print(roe, pe, time.time())
     
full_asset_data = {'ASSET_NAME':asset_name_list,'ROE':roe_list,'P_L':pe_list}
full_asset_dataframe = pd.DataFrame(data = full_asset_data, columns=['ASSET_NAME','ROE','P_L'])

full_asset_dataframe.sort_values(by = 'ROE', ascending = False, inplace = True)
full_asset_dataframe.sort_values(by = 'P_L', ascending = True, inplace = True)
full_asset_dataframe = full_asset_dataframe[full_asset_dataframe.ROE >= 25]
full_asset_dataframe.to_csv('JOEL.csv')
graph_generator(full_asset_dataframe)
full_asset_dataframe.reset_index(inplace = True)
