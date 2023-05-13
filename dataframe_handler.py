import pandas as pd

def data_sort(dataframe, by, ascending = True, inplace = True):
    try:
        dataframe.sort_values()(by=by, ascending=ascending, inplace=inplace)
    except:
        raise Exception("Data sort failed")
    return data_sort
    
    
def data_filter(dataframe, column, filter_min=False, filter_max=False):
    if filter_min != False:
        dataframe = dataframe[dataframe.column >= filter_min]
    
    elif filter_max != False:
        dataframe = dataframe[dataframe.column <= filter_min]
    
    else:
        dataframe = dataframe[dataframe.column >= filter_min]
        dataframe = dataframe[dataframe.column <= filter_max]
    return dataframe

def df_converter(dataframe, name_path):
    if name_path == 'csv':
        dataframe.to_csv(name_path)
    
    elif name_path == 'xlsx':
        dataframe.to_xlsx(name_path)
        
def reader(file):
    if file.endswith('.csv'):
        dataframe = pd.read_csv(file)
    
    elif file.endwith('.xlsx'):
        dataframe = pd.read_excel(file)
    return dataframe
    
def reset_index(dataframe, inplace=True):
    if inplace == True:
        dataframe.reset_index(dataframe,inplace=inplace)
    
