import pandas as pd
from data_processing import InputProcessing

""" Final Project: Student Housing Finder
UMD Student Housing Finder Framework

A Python framework designed to help University of Maryland students find suitable housing 
by filtering and comparing rental properties based on customizable criteria.
"""

class Housing:
    """A class representing a housing option for University of Maryland students.

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
        self.id = id
        self.property = property
        self.bed = bed
        self.bath = bath
        self.price = price
        self.sqft = sqft
        self.proximity = proximity

    def __str__(self):
        return (f"{self.property}: {self.bed} beds, {self.bath} baths, "
                f"${self.price}, {self.sqft} sqft, {self.proximity} miles")

    def load_housing_data(filepath):
        """Load housing data from a CSV file and convert it into a list of Housing objects."""
        housing_processor = InputProcessing(filepath)
        cleaned_data = housing_processor.process_input()
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
            for _, row in cleaned_data.iterrows()
        ]

class Bed(Housing):
    """A class to filter housing by the number of bedrooms."""
    def __init__(self, id, property, bed, bath, price, sqft, proximity):
        super().__init__(id, property, bed, bath, price, sqft, proximity)

    def filter(housing_list, min_bed, max_bed):
        filtered_list = [house for house in housing_list if min_bed <= house.bed <= max_bed]
        if not filtered_list:
            return filtered_list, f"No houses with bedrooms between {min_bed} and {max_bed}."
        return filtered_list, None

class Bath(Housing):
    """A class to filter housing by the number of bathrooms."""
    def __init__(self, id, property, bed, bath, price, sqft, proximity):
        super().__init__(id, property, bed, bath, price, sqft, proximity)

    def filter(housing_list, min_bath, max_bath):
        filtered_list = [house for house in housing_list if min_bath <= house.bath <= max_bath]
        if not filtered_list:
            return filtered_list, f"No houses with bathrooms between {min_bath} and {max_bath}."
        return filtered_list, None

class Price(Housing):
    """A class to filter housing by price."""
    def __init__(self, id, property, bed, bath, price, sqft, proximity):
        super().__init__(id, property, bed, bath, price, sqft, proximity)

    def filter(housing_list, min_price, max_price):
        filtered_list = [house for house in housing_list if min_price <= house.price <= max_price]
        if not filtered_list:
            return filtered_list, f"No houses within the price range ${min_price} - ${max_price}."
        return filtered_list, None

class Distance(Housing):
    """A class to filter housing by distance from campus."""
    def __init__(self, id, property, bed, bath, price, sqft, proximity):
        super().__init__(id, property, bed, bath, price, sqft, proximity)

    def filter(housing_list, min_distance, max_distance):
        filtered_list = [house for house in housing_list if min_distance <= house.proximity <= max_distance]
        if not filtered_list:
            return filtered_list, f"No houses within the distance range {min_distance} - {max_distance} miles."
        return filtered_list, None
    
class FilterPreference:
    def __init__(self, housing_list):
        self.housing_list = housing_list

    def filter(self, priorities):
        results = []
        priority_message = "No results found."

        # Print original ranges with correct priority status
        print("\nOriginal Ranges:")
        for key, (min_val, max_val, is_priority) in priorities.items():
            print(f"{key}: {min_val} - {max_val} {'(Priority)' if is_priority else '(Non-Priority)'}")

        # Get all ranges including adjusted ones for non-priorities
        min_beds, max_beds, min_baths, max_baths, min_price, max_price, min_distance, max_distance = self.adjust_filters(
            min_beds=priorities.get('beds', (0, float('inf'), False))[0],
            max_beds=priorities.get('beds', (0, float('inf'), False))[1],
            min_baths=priorities.get('baths', (0, float('inf'), False))[0],
            max_baths=priorities.get('baths', (0, float('inf'), False))[1],
            min_price=priorities.get('price', (0, float('inf'), False))[0],
            max_price=priorities.get('price', (0, float('inf'), False))[1],
            min_distance=priorities.get('distance', (0, float('inf'), False))[0],
            max_distance=priorities.get('distance', (0, float('inf'), False))[1],
            priorities={k: (v[0], v[1]) for k, v in priorities.items() if v[2]}  # Only pass actual priorities
        )

        # Print adjusted ranges
        print("\nAdjusted Ranges:")
        print(f"Beds: {min_beds} - {max_beds} {'(Priority)' if 'beds' in priorities and priorities['beds'][2] else '(Non-Priority)'}")
        print(f"Baths: {min_baths} - {max_baths} {'(Priority)' if 'baths' in priorities and priorities['baths'][2] else '(Non-Priority)'}")
        print(f"Price: {min_price} - {max_price} {'(Priority)' if 'price' in priorities and priorities['price'][2] else '(Non-Priority)'}")
        print(f"Distance: {min_distance} - {max_distance} {'(Priority)' if 'distance' in priorities and priorities['distance'][2] else '(Non-Priority)'}")

        for house in self.housing_list:
            # Check priority filters first
            priority_match = True
            for key, (min_val, max_val, is_priority) in priorities.items():
                if not is_priority:
                    continue
                if key == 'beds' and not (min_val <= house.bed <= max_val):
                    priority_match = False
                    break
                elif key == 'baths' and not (min_val <= house.bath <= max_val):
                    priority_match = False
                    break
                elif key == 'price' and not (min_val <= house.price <= max_val):
                    priority_match = False
                    break
                elif key == 'distance' and not (min_val <= house.proximity <= max_val):
                    priority_match = False
                    break

            if not priority_match:
                continue

            # Check all ranges (including adjusted non-priority ranges)
            if (min_beds <= house.bed <= max_beds and
                min_baths <= house.bath <= max_baths and
                min_price <= house.price <= max_price and
                min_distance <= house.proximity <= max_distance):
                results.append(house)

        if results:
            priority_message = None

        return results, priority_message
    
    def adjust_filters(self, min_beds, max_beds,
                min_baths, max_baths, min_price, max_price,
                min_distance, max_distance, priorities):
            
            if 'beds' not in priorities:
                min_beds = max(0, min_beds - 1)
                max_beds += 1
            if 'baths' not in priorities:
                min_baths = max(0, min_baths - 1)
                max_baths += 1
            if 'price' not in priorities:
                min_price = max(0, min_price - 250)
                max_price += 250
            if 'distance' not in priorities:
                min_distance = max(0, min_distance - 0.2)
                max_distance += 0.2

            return min_beds, max_beds, min_baths, max_baths, min_price, max_price, min_distance, max_distance