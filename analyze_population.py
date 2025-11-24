import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the clipboard (you can copy the data and run this script)
try:
    # Try reading from clipboard first
    df = pd.read_clipboard()
    
    # If the first column is unnamed, set it as index
    if df.columns[0].startswith('Unnamed'):
        df = df.set_index(df.columns[0])
    
    # Display basic information about the dataset
    print("\n=== Dataset Information ===")
    print(f"Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Display basic statistics
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    # Plot population trends for a few countries
    print("\n=== Plotting Population Trends ===")
    countries_to_plot = ['China', 'India', 'United States', 'Brazil', 'Nigeria']
    years = [col for col in df.columns if col.endswith('Population')]
    
    plt.figure(figsize=(12, 6))
    for country in countries_to_plot:
        if country in df.index:
            plt.plot(years, df.loc[country, years], marker='o', label=country)
    
    plt.title('Population Trends (1970-2022)')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
except Exception as e:
    print(f"Error: {e}")
    print("\nPlease copy the data to your clipboard and run this script again.")
