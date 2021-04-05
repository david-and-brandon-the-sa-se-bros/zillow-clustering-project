import env

from acquire.acquire_zillow import acquire_zillow_df
from prepare.prepare_zillow import drop_unnecessary_columns, handle_missing_zillow_values

def wrangle_zillow_data():
    zillow_df = acquire_zillow_df()
    
    zillow_df = drop_unnecessary_columns(zillow_df)
    zillow_df = handle_missing_zillow_values(zillow_df)
    
    return zillow_df