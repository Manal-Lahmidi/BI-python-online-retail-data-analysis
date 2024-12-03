import pandas as pd

def extract_data(file_path):
    # Charger le fichier Excel
    data = pd.read_excel(file_path, engine='openpyxl')
    return data

if __name__ == "__main__":
    file_path = 'online_retail_II.xlsx'
    data = extract_data(file_path)
    print(data.head())
    print(data.info())
    

