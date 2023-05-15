import pandas as pd
class CustomError(Exception):
    pass

def data_sort(dataframe, by, ascending = True, inplace = True):
    try:
        dataframe.sort_values(by=by, ascending=ascending, inplace=inplace)
        return dataframe
    except CustomError as error :
        print(error)
        pass
        
def reader(file):
    if file.endswith('.csv'):
        dataframe = pd.read_csv(file)
    
    elif file.endwith('.xlsx'):
        dataframe = pd.read_excel(file)
    return dataframe
    
def reset_index(dataframe, inplace=True):
    if inplace == True:
        dataframe.reset_index(dataframe,inplace=inplace)
    
