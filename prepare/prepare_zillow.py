import env
import utilities as utils

def drop_unnecessary_columns(zillow_df):
    df = zillow_df.copy()
    
    df = utils.handle_missing_values(df, .6, .4)
    drop_cols = ['id', 'parcelid', 'finishedsquarefeet12', 'fullbathcnt', 'propertylandusetypeid', 'heatingorsystemtypeid', 'censustractandblock']
    
    return df.drop(columns=drop_cols)

def handle_missing_zillow_values(zillow_df):
    df = zillow_df.copy()
    
    df['buildingqualitytypeid'].fillna(value=8.0, inplace=True)    
    df['calculatedbathnbr'].fillna(value=2.0, inplace=True)
    df['calculatedfinishedsquarefeet'].fillna(value=1542, inplace=True)
    df['lotsizesquarefeet'].fillna(value=7205, inplace=True)
    df['propertyzoningdesc'].fillna(value="LAR1", inplace=True)
    df['regionidcity'].fillna(value=12447, inplace=True)
    df['regionidzip'].fillna(value=97319, inplace=True)
    df['unitcnt'].fillna(value=1, inplace=True)
    df['yearbuilt'].fillna(value=1970, inplace=True)
    df['structuretaxvaluedollarcnt'].fillna(value=136399.0, inplace=True)
    df['heatingorsystemdesc'].fillna(value='Central', inplace=True)
    df['taxamount'].fillna(value=4447.63, inplace=True)
    
    return df