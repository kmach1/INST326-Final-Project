import pandas as pd

""" Final Project: Student Housing FInder
UMD Student Housing Finder Framework

A Python framework designed to help University of Maryland students find suitable housing 
by filtering and comparing rental properties based on customizable criteria.

"""
class Housing:
    """  A class representing a housing option for University of Maryland students.

    Attributes:
        id (int): Unique identifier for the property.
        property (str): Name or title of the property.
        bed (int): Number of bedrooms in the property.
        bath (int): Number of bathrooms in the property.
        price (float): Monthly rental price of the property.
        sqft (int): Square footage of the property.
        proximity (float): Distance from campus in miles or kilometers.
    """
    def __init__(self, id, property, bed, bath, price, sqft, proximity):
        self.name = id
        self.property = property
        self.bath = bath 
        self.price = price 
        self.sqft = sqft
        self.proximity = proximity

    def __str__(self):
        return (f"{self.property}: {self.bed} Beds, {self.bath} Baths, ${self.price}/month, "
                f"{self.sqft} sqft, {self.proximity} miles from campus")
    

    def load_housing_data(filepath):
        """"Load housing data from a CSV file and convert it into a list of Housing objects."""
       
        """USE the cleaned_housing_data.csv file for the data in the housing.py file!!!!!!!!!!!!!
        """
        df = pd.read_csv(filepath)
        return [
            Housing(
                id=row['property_id'],
                property=row['building_name'],
                bed=row['number_of_beds'],
                bath=row['number_of_bathrooms'],
                price=row['price'],
                sqft=row['square_feet'],
                proximity=row['distance_to_campus']
            )
            for _, row in df.iterrows()
        ]
    
    def filter_housing(housing_list, bed, bath,max_price, min_sqft, max_distance):
        """filter the housing based on user preference"""
        """Filter housing options based on user preferences."""
        filtered_houses = []  # Create an empty list to store matching houses
        
        for house in housing_list:
            if (house.bed == bed and
                house.bath == bath and
                house.price <= max_price and
                house.sqft >= min_sqft and
                house.proximity <= max_distance):
                filtered_houses.append(house)  # Add the matching house to the list

        return filtered_houses  # Return the list of matching houses
            

if __name__ == "__main__": 
    """Main function to load data, get user preferences, and find matching housing."""
    # Load housing data
    housing_list = Housing.load_housing_data('cleaned_housing_data.csv')
    #Welcome Statement
    print("Welcome to University of Maryland Apartment Finder!\n")
    #User preferences
    bed = int(input("Number of bedrooms (1-5): "))
    bath = int(input("Number of bathrooms(1-5): "))
    max_price = float(input("Maximim price you are willing to pay: $"))
    min_sqft = int(input("Minimum square footage desired: "))
    max_distance = float(input("Maximum distance from campus in miles: "))

    # Filter housing options
    matching_houses = Housing.filter_housing(housing_list, bed, bath, max_price, min_sqft, max_distance)
    # Display results
    if matching_houses:
        print("\nHere are the apartments that match your preferences:\n")
        for house in matching_houses:
            print(house)
    else:
        print("\nSorry, no apartments match your preferences.")



