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
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        ip.read_input()
        self.assertIsNotNone(ip.data)
    
    def test_clean_data(self):
        '''
        Testing the clean_data method
        '''
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        ip.read_input()
        ip.clean_data()
        self.assertIsNotNone(ip.data)
    
    def test_process_input(self):
        '''
        Testing the process_input method
        '''
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        ip.read_input()
        ip.clean_data()
        data = ip.process_input()
        self.assertIsNotNone(data)
    
    def test_filter_data(self):
        '''
        Testing the filter_data method
        '''
        ip = InputProcessing("INST326 Final Project Housing Info - Main_Sheet.csv")
        ip.read_input()
        ip.clean_data()
        data = ip.process_input()
        filtered_data = ip.filter_data(budget=100000, room_count=3, square_footage=1000, proximity=5)
        self.assertIsNotNone(filtered_data)

if __name__ == '__main__':
    unittest.main()