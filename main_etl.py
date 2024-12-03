# Importer les fonctions depuis les autres fichiers Python
from extraction import extract_data
from transformation import transform_data
from loading import load_data
from analysis_visualisation import analyze_and_visualize

def main():
    # Étape 1 : Extraction
    file_path = 'online_retail_II.xlsx'
    print("Étape 1 : Extraction des données")
    data = extract_data(file_path)

    # Étape 2 : Transformation
    print("\nÉtape 2 : Transformation des données")
    transformed_data = transform_data(data)

    # Étape 3 : Chargement
    output_file = 'Cleaned_RetailData.xlsx'
    print("\nÉtape 3 : Chargement des données")
    load_data(transformed_data, output_file)

    # Étape 4 : Analyse et Visualisation
    print("\nÉtape 4 : Analyse et Visualisation")
    analyze_and_visualize(transformed_data)

if __name__ == "__main__":
    main()
