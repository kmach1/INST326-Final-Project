import pandas as pd

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

    def clean_data(self):
        """
        Clean the data and return the cleaned data
        """
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