# INST326-Final-Project - UMD Off-Campus Housing Finder
**About the Poject**
A Python-based housing finder application designed specifically for University of Maryland students to search and analyze off-campus apartment options.
**Project Description**
This project helps UMD students find off-campus housing by processing apartment data and allowing users to filter based on their preferences. The application reads housing data from CSV files and provides detailed insights about available apartments near campus. 

**Features**
Data Processing: Reads and processes housing data from a CSV file.
- Apartment Details: Displays key information, including:
- Property name
- Number of bedrooms
- Number of bathrooms
- Monthly rent per person
- Square footage
- Distance from campus (calculated from the STAMP Student Union)

**Accessing the Repository**
You can view the project files and code directly on GitHub:
https://github.com/kmach1/INST326-Final-Project
No need to clone the repository unless you want to run the project locally.

**Usage**
- Command-Line
The program is run from the command line. It processes an input file containing apartment data, applies filters specified by the user, and saves the cleaned data to a CSV file.

(Example Command)
"""python housing.py --input_file apartments.csv --budget 1200 --room_count 2 --square_footage 1000 --proximity 2.0"""

Arguments
--budget: Maximum monthly rent per person (e.g., --budget 1200).
--room_count:  Number of bedrooms (e.g., --room_count 2).
--square_footage:  Minimum square footage (e.g., --square_footage 1000).
--proximity: Maximum distance from campus in miles (e.g., --proximity 2.0).


Contributions 
Karalyn Mach, Genevieve Koduol, Theodore Rose, Sarah Bamba

Distributed under the MIT License. See LICENSE.txt for more information.
MIT License




