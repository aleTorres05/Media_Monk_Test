import pandas as pd
import os

def read_csv_files(folder_path):
    
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            if file == 'clients.csv':
                clients = pd.read_csv(f'..\client_files\{file}')
            elif file == 'fx_rates.csv':
                rates = pd.read_csv(f'..\client_files\{file}')
            else:
                platform_cost = pd.read_csv(f'..\client_files\{file}')
        
    return clients, rates, platform_cost
