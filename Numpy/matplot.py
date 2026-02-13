import matplotlib.pyplot as plt

# Years
years = [2000, 2005, 2010, 2015, 2020, 2023]

# Population data (in millions)
india = [1053, 1140, 1234, 1311, 1380, 1429]
china = [1267, 1304, 1338, 1371, 1412, 1411]
usa = [282, 295, 309, 321, 331, 339]
brazil = [176, 186, 195, 204, 213, 216]

# Create figure
plt.figure(figsize=(10,6))

# Plot lines
plt.plot(years, india, marker='o', label='India')
plt.plot(years, china, marker='s', label='China')
plt.plot(years, usa, marker='^', label='USA')
plt.plot(years, brazil, marker='d', label='Brazil')

# Chart styling
plt.title("Population Comparison of Major Countries (in Millions)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Population (Millions)")
plt.grid(True)
plt.legend()

# Show
plt.show()
