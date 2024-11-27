import pandas as pd
from housing import Housing
import argparse

"""
Responsible for cleaning and approving the .csv input data
"""


class InputProcessing:
    """
    This class is responsible for reading the input data, cleaning it and processing it

    Attributes:
    input_file (str): The path to the input file
    
    Methods:
    read_input: Read the input file and return the data as a pandas dataframe
    clean_data: Clean the data and return the cleaned data
    process_input: Process the input data
    filter_data: Filter the data based on user preferences
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None

    def read_input(self):
        """
        Read the input file and return the data as a pandas dataframe
        """
        try:
            self.data = pd.read_csv(self.input_file)
        except Exception as e:
            print(f"Error reading the input file: {e}")
            self.data = None

    def clean_data(self):
        """
        Clean the data and return the cleaned data
        """
        if self.data is None:
            print("No data to clean.")
            return None
        
        # Append "(Studio)" to prop_id if num_beds is "Studio"
        self.data['prop_id'] = self.data.apply(
            lambda row: f"{row['prop_id']} (Studio)" if row['num_beds'] == 'Studio' else row['prop_id'], axis=1
        )

        # Standardize the num_beds column to be just integers
        # Since some values are in the format "Studio"
        self.data['num_beds'] = self.data['num_beds'].apply(lambda x: 1 if x == 'Studio' else int(x))
        
        # Remove any commas in the sqft column and convert to integers
        self.data['sqft'] = self.data['sqft'].str.replace(',', '')

        return self.data
    
    def process_input(self):
        """
        Process the input data
        """
        self.read_input()
        cleaned_data = self.clean_data()
        return cleaned_data



''' {Sample usage of the class}
Setting the input file
input_file = 'housing.csv'

Initialize the InputProcessing class
housing_processor = InputProcessing(input_file)

Read and clean the data
housing_processor.read_input()

Process the input data
cleaned_data = housing_processor.process_input()

Filter the data based on user preferences (example)
filtered_housing = housing_processor.filter_data(budget=1200, room_count=2, proximity=2.0)

Display the filtered results
print(filtered_housing)
'''

def parse_args():
    parser = argparse.ArgumentParser(description="Process housing data.")
    parser.add_argument('input_file', type=str, help='The path to the input CSV file')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    input_file = args.input_file

    housing_processor = InputProcessing(input_file)
    housing_processor.read_input()
    cleaned_data = housing_processor.process_input()

    print("No Errors in processing housing data!")
    print("----------------")
    print("You can now enter your prefrences.")
    print("Appliciple filters are: budget, room_count, square_footage, proximity")
    print("Example: housing.py --budget 1200 --room_count 2 --square_footage 1000 --proximity 2.0")
    
    output_file = 'cleaned_housing_data.csv'
    cleaned_data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
