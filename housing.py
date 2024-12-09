import pandas as pd
import data_processing

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
                id=row['prop_id'],
                property=row['building_name'],
                bed=row['num_beds'],
                bath=row['num_baths'],
                price=row['price'],
                sqft=row['sqft'],
                proximity=row['dis_to_campus_[mi]']
            )
            for _, row in df.iterrows()
        ]
    
class Bed(Housing):
   """ A class to filter housing by the number of bedrooms."""
   def __init__(self, id, property, bed, bath, price, sqft, proximity):
       super().__init__(id, property, bed, bath, price, sqft, proximity)

   def filter(housing_list, bed):
       """Filter housing by the number of bedrooms.
       
       Args:
            housing_list (list): List of Housing objects.
            bed (int): Desired number of bedrooms.

        Returns:
            list: A filtered list of Housing objects with the specified number of bedrooms.
       """
       return [house for house in housing_list if house.bed == bed]

class Bath(Housing):
   """ A class to filter housing by the number of bathrooms."""
   def __init__(self, id, property, bed, bath, price, sqft, proximity):
       super().__init__(id, property, bed, bath, price, sqft, proximity)


   def filter(housing_list, bath):
       """Filter housing by the number of bathrooms."""
       return [house for house in housing_list if house.bath == bath]


class Price(Housing):
   """ A class to filter housing by price."""
   def __init__(self, id, property, bed, bath, price, sqft, proximity):
       super().__init__(id, property, bed, bath, price, sqft, proximity)

   def filter(housing_list, min_price, max_price):
       """Filter housing by minimum and maximum price.
       Args:
            housing_list (list): List of Housing objects.
            bath (int): Desired number of bathrooms.

        Returns:
            list: A filtered list of Housing objects with the specified number of bathrooms.
       """
       return [house for house in housing_list if min_price <= house.price <= max_price]


class Distance(Housing):
   """ A class to filter housing by distance from campus."""
   def __init__(self, id, property, bed, bath, price, sqft, proximity):
       super().__init__(id, property, bed, bath, price, sqft, proximity)
   
   def convert_to_miles(kilometers):
       """Convert kilometers to miles."""
       return kilometers * 0.621371
   
   def filter(housing_list, max_distance, unit="miles"):
       """Filter housing by maximum distance, converting to miles if needed."""
       if unit == "kilometers":
           max_distance = Distance.convert_to_miles(max_distance)
       return [house for house in housing_list if house.proximity <= max_distance]

   print("\nSorry, no apartments match your preferences.")

if __name__ == "__main__":
   """Main function to load data, get user preferences, and find matching housing."""
   # Load housing data
   housing_list = Housing.load_housing_data('cleaned_housing_data.csv')


   # Welcome statement
   print("Welcome to University of Maryland Apartment Finder!\n")


   # User preferences
   bed = int(input("Number of bedrooms (1-5): "))
   bath = int(input("Number of bathrooms (1-5): "))
   min_price = float(input("Minimum price you are willing to pay: $"))
   max_price = float(input("Maximum price you are willing to pay: $"))
   max_distance = float(input("Maximum distance from campus: "))
   distance_unit = input("Is the distance in miles or kilometers? ").strip().lower()


   # Filter housing options
   filtered_by_bed = Bed.filter(housing_list, bed)
   filtered_by_bath = Bath.filter(filtered_by_bed, bath)
   filtered_by_price = Price.filter(filtered_by_bath, min_price, max_price)
   matching_houses = Distance.filter(filtered_by_price, max_distance, unit=distance_unit)


   # Display results
   if matching_houses:
       print("\nHere are the housing options that match your preferences:\n")
       for house in matching_houses:
           print(house)
   else:
       print("\nSorry, no housing options match your preferences.")
