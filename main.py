from scrap_engine import scrap_init
import pandas as pd 
from data_converter import flotify, replacer
from graph_handler import graph_generator
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
     
    print(roe, pe)
     
full_asset_data = {'ASSET_NAME':asset_name_list,'ROA':roe_list,'P_L':pe_list}
full_asset_dataframe = pd.DataFrame(full_asset_data)
print(full_asset_dataframe)
graph_generator(full_asset_dataframe)