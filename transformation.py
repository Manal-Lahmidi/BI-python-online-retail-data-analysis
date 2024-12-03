import pandas as pd

def transform_data(data):
    # Nettoyage des données

    #Supprimez les lignes vides :
    data.dropna(inplace=True)

    #Supprimez les doublons :
    data.drop_duplicates(inplace=True)

    # Convertir la colonne 'InvoiceDate' en datetime :
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    #Filtrez les transactions avec des quantités ou des prix négatifs :
    data = data.loc[(data['Quantity'] > 0) & (data['Price'] > 0)].copy()

    # Ajout de colonnes calculées
    data.loc[:, 'TotalAmount'] = data['Quantity'] * data['Price']
    data.loc[:, 'Year'] = data['InvoiceDate'].dt.year
    data.loc[:, 'Month'] = data['InvoiceDate'].dt.month

    return data

if __name__ == "__main__":
    from extraction import extract_data
    file_path = 'online_retail_II.xlsx'
    data = extract_data(file_path)
    transformed_data = transform_data(data)
    print(transformed_data.head())
    print( transformed_data['Year'].unique())
    print( transformed_data['Month'].unique())

