# Zillow Clustering Project
- This project uses a clustering model to predict logerror from the Zillow data set.
- In this README we will :
    * Explain what the project is and goals the team attemted to reach. 
    * Explain how to reproduce our work. 
    * Contain notes from project planning.

## Goals
* Identify the drivers for errors in Zestimates by incorporating clustering methodologies.
* Document the process and analysis throughout the data science pipeline.
* Demonstrate our process and articulate the information that was discovered.

**Deliverables:**
1. README.md file containing overall project information, how to reproduce work, and notes from project planning.
2. Jupyter Notebook Report detailing the pipeline process.
3. Python modules that automate the data acquistion, preparation, and exploration process.

## Key Findings

## Project Planning
* The The Kanban board used for planning is<a href="https://github.com/orgs/david-and-brandon-the-sa-se-bros/projects/1"> here</a>
   * `Data Acquisition`: Data is collected from the codeup cloud database with an appropriate SQL query
   * `Data Prep`: Column data types are appropriate for the data they contain
   * `Data Prep`: Missing values are investigated and handled
   * `Data Prep`: Outliers are investigated and handled
   * `Exploration`: the interaction between independent variables and the target variable is explored using visualization and statistical testing
   * `Exploration`: Clustering is used to explore the data. A conclusion, supported by statistical testing and visualization, is drawn on whether or not the clusters are helpful/useful. At least 3 combinations of features for clustering should be tried.
   * `Modeling`: At least 4 different models are created and their performance is compared. One model is the distinct combination of algorithm, hyperparameters, and features.

Project Requirements:
   - Best practices on data splitting are followed
   - The final notebook has a good title and the documentation within is sufficiently explanatory and of high quality
   - Decisions and judment calls are made and explained/documented
   - All python code is of high quality

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
