import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_and_visualize(data):
    # Revenus mensuels
    revenue = data.groupby(['Year', 'Month'])['TotalAmount'].sum().reset_index()
    sns.lineplot(data=revenue, x='Month', y='TotalAmount', hue='Year', palette={2009: 'blue', 2010: 'orange'})
    plt.title('Revenus mensuels (2009 vs 2010)')
    plt.xlabel('Mois')
    plt.ylabel('Revenus (€)')
    plt.show()

    # Produits les plus populaires
    top_products = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    print(top_products)
    top_products.plot(kind='bar', title='Top 10 des produits les plus vendus')
    plt.ylabel('Quantité vendue')
    plt.show()

    # Répartition géographique
    country_revenue = data.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)
    print(country_revenue)
    country_revenue.plot(kind='bar', title='Top 10 des pays par revenus')
    plt.ylabel('Revenus (€)')
    plt.show()

    # Panier moyen
    avg_basket = data.groupby('Invoice')['TotalAmount'].sum().mean()
    print(f"Panier moyen : {avg_basket:.2f} €")
    plt.hist(data.groupby('Invoice')['TotalAmount'].sum(), bins=30, color='skyblue', edgecolor='black')
    plt.axvline(avg_basket, color='red', linestyle='dashed', linewidth=1.5, label=f'Panier moyen: {avg_basket:.2f} €')
    plt.title('Répartition des montants des commandes')
    plt.xlabel('Montant des commandes (€)')
    plt.ylabel('Nombre de commandes')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from transformation import transform_data
    from extraction import extract_data

    file_path = 'online_retail_II.xlsx'
    data = extract_data(file_path)
    transformed_data = transform_data(data)
    analyze_and_visualize(transformed_data)
    
