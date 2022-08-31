from os.path import exists
import pandas as pd
import os
from pandas import testing as tm
import unittest
from ..billing_calc import calculate_billing

file_path ='.\client_files\Clients_total_bill.csv'

class TestBillingCalc(unittest.TestCase):
    
    def test_csv_creation(self):
        calculate_billing('.\client_files')
        
        self.assertTrue(exists(file_path))
        delete_file()
        


    def test_billing_calc(self):
        
        data = {'Client ID': [1.0, 1.0, 2.0, 3.0, 3.0], 'Client Name': ['C3P0 Ads', 'C3P0 Ads', 'Costa Atlantica', 'Only Programmatic Marketing', 'Only Programmatic Marketing'], 'Bill Currency': ['CHA', 'CHA', 'TAZ', 'TOK', 'TOK'], 'Total Cost': [550.0, 2200.0, 315.0, 6000.0, 12000.0]}
        expected = pd.DataFrame.from_dict(data).groupby(['Client ID', 'Client Name', 'Bill Currency'])['Total Cost'].sum()
        actual = calculate_billing('.\client_files')

        tm.assert_series_equal(expected, actual)
        delete_file()

    

def delete_file():
                
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("File has been deleted")
    else:
        print("File does not exist")


if __name__ == '__main__':
    unittest.main()
