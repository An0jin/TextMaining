import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('world_population.csv')

# Display basic statistics
print("\n--- Basic Statistics ---")
print(f"Total countries in dataset: {len(df)}")
print("\nArea (km²) statistics:")
print(df['Area (km²)'].describe().to_string())
print("\nDensity (per km²) statistics:")
print(df['Density (per km²)'].describe().to_string())

# Find top and bottom countries by area and density
top_largest = df.nlargest(5, 'Area (km²)')[['Country/Territory', 'Area (km²)']]
top_smallest = df.nsmallest(5, 'Area (km²)')[['Country/Territory', 'Area (km²)']]
top_dense = df.nlargest(5, 'Density (per km²)')[['Country/Territory', 'Density (per km²)']]
least_dense = df.nsmallest(5, 'Density (per km²)')[['Country/Territory', 'Density (per km²)']]

# Display results
print("\n--- Largest Countries by Area ---")
print(top_largest.to_string(index=False))
print("\n--- Smallest Countries by Area ---")
print(top_smallest.to_string(index=False))
print("\n--- Most Densely Populated Countries ---")
print(top_dense.to_string(index=False))
print("\n--- Least Densely Populated Countries ---")
print(least_dense.to_string(index=False))

# Create visualizations
plt.figure(figsize=(15, 10))

# Plot 1: Area distribution
plt.subplot(2, 2, 1)
sns.histplot(df['Area (km²)'], bins=50, kde=True)
plt.xscale('log')
plt.title('Distribution of Country Areas (log scale)')

# Plot 2: Density distribution
plt.subplot(2, 2, 2)
sns.histplot(df['Density (per km²)'], bins=50, kde=True)
plt.xscale('log')
plt.title('Distribution of Population Density (log scale)')

# Plot 3: Area vs Density
plt.subplot(2, 1, 2)
sns.scatter(data=df, x='Area (km²)', y='Density (per km²)', alpha=0.6)
plt.xscale('log')
plt.yscale('log')
plt.title('Area vs Population Density (log-log scale)')
plt.tight_layout()

# Save the plots
plt.savefig('area_density_analysis.png')
print("\nAnalysis complete. Visualizations saved as 'area_density_analysis.png'")
