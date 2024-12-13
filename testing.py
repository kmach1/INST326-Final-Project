import unittest
#importing the InputProcessing class from the module data_processing.py
from data_processing import InputProcessing

class TestInputProcessing(unittest.TestCase):
    '''
    Testing the InputProcessing class
    '''
    def test_read_input(self):
        '''
        Testing the read_input method
        '''
        # Create an instance of the InputProcessing class with the CSV file
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        # Call the read_input method to load the data
        ip.read_input()
        # Assert that the 'data' attribute is not None after reading the input
        self.assertIsNotNone(ip.data)
    
    def test_clean_data(self):
        '''
        Testing the clean_data method
        '''
        # Create an instance of the InputProcessing class with the CSV file
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        # First, read the input data
        ip.read_input()
        # Call the clean_data method to clean the loaded data        
        ip.clean_data()
        # Assert that the 'data' attribute is not None after cleaning
        self.assertIsNotNone(ip.data)
    
    def test_process_input(self):
        '''
        Testing the process_input method
        '''
        # Create an instance of the InputProcessing class with the CSV file
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        # Read the input data
        ip.read_input()
        # Clean the data
        ip.clean_data()
        # Call the process_input method to process the cleaned data
        data = ip.process_input()
        # Assert that the processed data is not None
        self.assertIsNotNone(data)

# Entry point for the unittest framework
if __name__ == '__main__':
    unittest.main()
