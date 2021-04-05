import env
import utilities as utils
import pandas as pd

def drop_unnecessary_columns(zillow_df):
    df = zillow_df.copy()
    
    df = utils.handle_missing_values(df, .6, .4)
    drop_cols = ['id', 'parcelid', 'finishedsquarefeet12', 'fullbathcnt', 'propertylandusetypeid', 'heatingorsystemtypeid', 'censustractandblock', 'rawcensustractandblock', 'regionidzip', 'assessmentyear', 'regionidcounty', 'yearbuilt']
    
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
    df['taxvaluedollarcnt'].fillna(value=358879, inplace=True)
    df['landtaxvaluedollarcnt'].fillna(value=203174, inplace=True)
    
    return df

def rename_zillow_columns(zillow_df):
    df = zillow_df.copy()
    
    rename_dict = {'bathroomcnt' : 'bathrooms', 'bedroomcnt' : 'bedrooms', 'buildingqualitytypeid' : 'build_quality', 'calculatedbathnbr' : 'fractional_bathrooms', 'calculatedfinishedsquarefeet' : 'sqft', 'lotsizesquarefeet' : 'lot_size', 'propertycountylandusecode' : 'land_use_code', 'propertyzoningdesc' : 'zoning_desc', 'regionidcity' : 'city_id', 'roomcnt' : 'rooms', 'unitcnt' : 'units', 'structuretaxvaluedollarcnt' : 'structure_tax_value', 'taxvaluedollarcnt' : 'tax_value', 'landtaxvaluedollarcnt' : 'land_tax_value', 'taxamount' : 'tax_amount', 'logerror' : 'error', 'transactiondate' : 'transaction_date', 'heatingorsystemdesc' : 'heat_system_desc', 'propertylandusedesc' : 'property_land_use_desc'}
    
    return df.rename(columns=rename_dict)

def encode_zillow_categoricals(zillow_df):
    df = zillow_df.copy()

    fips_dummies = pd.get_dummies(df.fips, dummy_na=False, drop_first=True)
    heat_dummies = pd.get_dummies(df.heat_system_desc, dummy_na=False, drop_first=True)
    prop_use_dummies = pd.get_dummies(df.property_land_use_desc, dummy_na=False, drop_first=True)
    
    return pd.concat([df, fips_dummies, heat_dummies, prop_use_dummies], axis=1)

def add_features(zillow_df):
    df = zillow_df.copy()
    
    df['age'] = 2017 - df['yearbuilt']
    
    return df
    
    