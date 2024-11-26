"""
Resposnsible for cleaning and approving the .txt input data
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
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None

    def read_input(self):
        """
        Read the input file and return the data as a pandas dataframe
        """
        pass

    def clean_data(self, data):
        """
        Clean the data and return the cleaned data
        """
        if self.data is None:
            print("No data to clean.")
            return None

    def process_input(self):
        """
        Process the input data
        """
        self.clean_data()
        return self.data
    
    def filter_data(self, budget=None, room_count=None, square_footage=None, proximity=None):
        """
        Filter the housing data based on user preferences for budget, room count, square footage, and proximity.
        
        Args:
        budget (int or None): Maximum budget the user is willing to spend
        room_count (int or None): Minimum number of rooms required
        square_footage (int or None): Minimum square footage required
        proximity (float or None): Maximum distance to campus in miles
        
        Returns:
        pd.DataFrame: Filtered housing data based on the user's preferences
        """
        filtered_data = self.data
        
        # Filter based on budget
        if budget is not None:
            filtered_data = filtered_data[filtered_data['Budget'] <= budget]
        
        # Filter based on room count
        if room_count is not None:
            filtered_data = filtered_data[filtered_data['Room Count'] >= room_count]
        
        # Filter based on square footage
        if square_footage is not None:
            filtered_data = filtered_data[filtered_data['Square Footage'] >= square_footage]
        
        # Filter based on proximity
        if proximity is not None:
            filtered_data = filtered_data[filtered_data['Proximity'] <= proximity]
        
        return filtered_data

# Sample usage of the class:
input_file = 'housing.py'

# Initialize the InputProcessing class
housing_processor = InputProcessing(input_file)

# Read and clean the data
housing_processor.read_input()

# Process the input data
cleaned_data = housing_processor.process_input()

# Filter the data based on user preferences (example)
filtered_housing = housing_processor.filter_data(budget=1200, room_count=2, proximity=2.0)

# Display the filtered results
print(filtered_housing)
