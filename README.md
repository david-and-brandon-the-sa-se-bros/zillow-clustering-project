# _Inzestigating What’s Driving the Errors in Zillow’s Zestimates_

![](http://zillow.mediaroom.com/image/Zillow_Wordmark_Blue_RGB.jpg)


## Zillow Clustering Project 
   - __by David Alviola & Brandon Bryant__
- This project uses a clustering model to predict logerror from the Zillow data set.
- In this README we will :
    * Explain what the project is and goals the team attemted to reach. 
    * Explain how to reproduce our work. 
    * Contain notes from project planning.

## Goals
* Identify the drivers for errors in Zestimates, incorporating clustering methodologies on this project.
* Document our process/ workflow used to accomplish the project goals.
* Demonstrate our process and summarize/ communicate our findings.

**Deliverables:**
1. README.md file containing overall project information, how to reproduce work, and notes from project planning.
2. Jupyter Notebook Report detailing the pipeline process.
3. Python modules that automate the data acquistion, preparation, and exploration process.

## Key Findings

## Project Planning
* The The Kanban board used for planning is <a href="https://github.com/orgs/david-and-brandon-the-sa-se-bros/projects/1">here</a>
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
        * Use release 2.5.1 or greater
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
    3. Open `zillow_clustering_project_final.ipynb` and run the cells

## Data Dictionary
This is the structure of the data after preparation:
#### Target
Name | Description | Type
:---: | :---: | :---:
error | Difference of the Zestimate and the actual transaction price | float

#### Features (from best model)
Name | Description | Type
:---: | :---: | :---:
large_homes | Indicates if the property is in the large home cluster  | int
newer_properties  | Indicates if the property is in the newer properties cluster |   int
sqft | The total square feet of the property | float
longitude | The decimal longitude of the property | float
age | Age of the property calculated by subtracting the year built from 2017 | int
ventura_county | Indicates if the property is in the Ventura County cluster  | int
older_high_quality_properties | Indicates if the property is in the older, high quality cluster | int
north_la_county | Indicates if the property is in the North LA county cluster | int
orange_county | Indicates if the property is in the Orange County cluster | int

#### Other Data
Name | Description | Type
:---: | :---: | :---:
build_quality | Measure of quality from best (lowest) to worst (highest) | int
6059 | Indicates if a property is in FIPS county 6059 (Orange) | int
small_homes | Indicates if a property is in the small homes cluster | int
west_la_county | Indicates if a property is in the West LA County cluster | int
fractional_bathrooms | The number of bathrooms in a property including half baths | float
latitude | The decimal latitude of the property | float
6111 | Indicates if a property is in FIPS county 6111 (Ventura) | int
medium_homes | Indicates if a property is in the medium homes cluster | int
older_low_quality_properties | Indicates if a property is in the older, low quality property cluster | int