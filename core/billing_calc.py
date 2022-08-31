import pandas as pd
from .csv_reader import read_csv_files

#This funtion returs a CSV File with the proper calculations for each customer's project 
def calculate_billing(folder_path):

    clients, rates, platform_cost = read_csv_files(folder_path)
    client_total_cost_dict={'Client ID':[], 'Client Name':[], 'Bill Currency':[],'Total Cost':[]}

    #Iterates all clients and their Index from the Clients DataFrame   
    for _, client in clients.iterrows():
        
        client_project = platform_cost[['Client ID', 'Advertising Cost', 'Currency']].where(platform_cost['Client ID'] == client['Client ID']).dropna()

        #Iterates all projects and their Index from the Client Projects DataFrame 
        for _, project in client_project.iterrows():
            #Creates a DataFrame with the convertion of currency from Project Currency and client Bill Currency 
            client_currency = rates.loc[rates['Origin Currency'] == project['Currency']][client['Bill Currency']]
            #Multiply the cost of the project by the convertion rate to get the Currency conversion 
            cost_project = project['Advertising Cost'] * client_currency
            #Calculate the cost of the Service Rate for each project  
            service_rate_cost = cost_project * client['Service Rate']
            #Total project cost
            total_cost = cost_project + service_rate_cost
            
            client_total_cost_dict['Client ID'].append(project['Client ID'])
            client_total_cost_dict['Client Name'].append(client['Client Name'])
            client_total_cost_dict['Bill Currency'].append(client['Bill Currency'])
            client_total_cost_dict['Total Cost'].append(total_cost.iloc[0])

    #Creates a DataFrame and provide the total cost for all the project per client 
    client_total_cost = pd.DataFrame.from_dict(client_total_cost_dict).groupby(['Client ID', 'Client Name', 'Bill Currency'])['Total Cost'].sum()

    client_total_cost.to_csv('.\client_files\Clients_total_bill.csv') 

    return client_total_cost

