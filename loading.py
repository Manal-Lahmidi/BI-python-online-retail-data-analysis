import pandas as pd

def load_data(data, output_file):
    # Export des données transformées vers un fichier Excel
    data.to_excel(output_file, index=False)
    print(f"Données exportées vers : {output_file}")

if __name__ == "__main__":
    from transformation import transform_data
    from extraction import extract_data

    file_path = 'online_retail_II.xlsx'
    output_file = 'Cleaned_RetailData.xlsx'

    data = extract_data(file_path)
    transformed_data = transform_data(data)
    load_data(transformed_data, output_file)
