# Zillow Clustering Project
- This project uses a clustering model to predict logerror from the Zillow data set.
- In this README we will :
    * Explain what the project is. 
    * Explain how to reproduce our work. 
    * Contain notes from project planning.

## Setup this project
* Dependencies
    1. [utilities.py](https://github.com/david-ryan-alviola/utilities/releases)
        * Use release 2.3.2 or greater
    2. python
    3. pandas
    4. scipy
    5. sklearn
    6. numpy
    7. matplotlib.pyplot
    8. seaborn
* Steps to recreate
    1. Clone this repository
    2. Install `utilities.py` according to the instructions
    3. Setup env.py
        * Remove the .dist extension (should result in `env.py`)
        * Fill in your user_name, password, and host
        * If you did not install `utilities.py` in your cloned repository, replace the "/path/to/utilities" string with the path to where `utilities.py` is installed
    4. Open `zillow_clustering_project_final.ipynb` and run the cells



## Data Dictionary
This is the structure of the data after preparation:
Name | Description | Type
:---: | :---: | :---:
tax_value | The assesed value of the property for tax purposes | float
bathrooms | The number of bathrooms a property has  | float
bedrooms  | The number of bedrooms in home |   float
fractional_bathrooms | The number of fractional bathrooms in home| float
sqft | Calculated total finished living area of the home | float
lot_size | Area of the lot in square feet | float
rooms |  Number of bedrooms in home  | float
units |  Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...) | int
age |  The age on years since the residence was built | int
structure_tax_value | The assessed value of the built structure  | float
tax_value | The total property tax assessed for that assessment year | float
land_tax_value | The assessed value of the land area of the parcel | float
tax_amount | The total tax assessed value of the property | float
error | Difference of the Zestimate and the actual transaction price | float
