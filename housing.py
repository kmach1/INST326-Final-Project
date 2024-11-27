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


class PriceFilter: 
    def __init__():
        pass
    pass  
       
