# Meida Monk Billing Calcuation

This project creates a single CSV file that calculatates the final cost of all the client's projects charged in their Billing Currency.
in this project Pandas Libary is used to work and manage the Data from the CSV files provided. The objective of this project is to know which Currency each project is charged in and make the convertion from that currency to the equal value of the Client's Billing Currency. 


# Requirements

  * Python 3.7
    * Pandas Lib
    * os Lib
    * unittest
  
# Execution & Output

Run from command line. From the Root Media_Monk_Test do the following to run the main script:

```
python main.py
```

output:
```
Client ID  Client Name                  Bill Currency
1.0        C3P0 Ads                     CHA               2750.0
2.0        Costa Atlantica              TAZ                315.0
3.0        Only Programmatic Marketing  TOK              18000.0
Name: Total Cost, dtype: float64
```
# Unittest

Run from command line. From the Root Media_Monk_Test do the following to run the Unittest:

```
python -m core.test.test_billing_calc
```
output:
```
File has been deleted
.File has been deleted
.
----------------------------------------------------------------------
Ran 2 tests in 0.066s

OK
```


