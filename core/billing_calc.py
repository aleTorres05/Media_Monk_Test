import csv
from csv_reader import read_csv_files

def calculate_billing():

    clients, rates, platform_cost = read_csv_files('..\client_files')
    client_billing_info=[]
        
    for _, client in clients.iterrows():
        
        client_currency = client['Bill Currency']
        client_project = platform_cost[['Advertising Cost', 'Currency']].where(platform_cost['Client ID'] == client['Client ID']).dropna()
        
        for _, project in client_project.iterrows():
            #aqui se busca la divisa basada en la del cliente
            rate_value = rates.loc[rates['Origin Currency'] == project['Currency']][client_currency]
            #se multiplica costo de projecto por valor de la divisa
            cost_project = project['Advertising Cost'] * rate_value
            #se saca el costo por el servicio del proyecto 
            service_rate_cost = cost_project * client['Service Rate']
            #Costo total del proyecto
            total_cost = cost_project + service_rate_cost

            for _, value in total_cost.items():
                client_billing_info.append([client['Client ID'], client['Client Name'], client['Bill Currency'], value])

                
    return client_billing_info

def create_csv():

    client_billing_info = calculate_billing()
    header = ['Client ID', 'Client Name', 'Bill Currency', 'Total']
    with open('Clients_total_bill.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) 
        writer.writerows(client_billing_info)             


print(create_csv())