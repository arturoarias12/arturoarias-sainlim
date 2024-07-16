import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import LogLocator

#Load data from Excel file.
data = pd.read_excel('sainlimdata.xlsx')

#Extract LIM and SAIN values.
x_values = data['LIM']
y_values = data['SAIN']

#Set the default font to Arial for all text in the plot.
plt.rcParams['font.family'] = 'Arial'

#Convert LIM and SAIN columns to numeric, setting errors='coerce' to convert non-numeric values to NaN.
data['LIM'] = pd.to_numeric(data['LIM'], errors='coerce')
data['SAIN'] = pd.to_numeric(data['SAIN'], errors='coerce')

#Drop rows where either LIM or SAIN is NaN after conversion.
data = data.dropna(subset=['LIM', 'SAIN'])

#Initialize the plot.
plt.figure(figsize=(10, 6))

#Plot the points corresponding to products.
plt.scatter(x_values, y_values, c='gray', label='Productos', s=10)

#SAIN and LIM lines at y=5 and x=7.5 respectively.
plt.axhline(y=5, color='green', linestyle='-', label='SAIN=5')
plt.axvline(x=7.5, color='red', linestyle='-', label='LIM=7.5')

#Set logarithmic scale.
plt.xscale('log')
plt.yscale('log')

#Quadrant names.
plt.text(0.7, 10, 'RECOMENDADOS', fontsize=14, weight='bold', color='green')
plt.text(10, 10, 'CONSUMO OCASIONAL', fontsize=14, weight='bold', color='gold')
plt.text(1, 1, 'NEUTROS', fontsize=14, weight='bold', color='darkorange')
plt.text(10, 1, 'A LIMITAR', fontsize=14, weight='bold', color='red')

#Set the axis labels.
plt.xlabel('LIM', fontsize=14, weight='bold', color='red')
plt.ylabel('SAIN', fontsize=14, weight='bold', color='green')

#Set up ScalarFormatter for both axes.
formatter = ScalarFormatter()

#Disable the scientific notation for numbers.
formatter.set_scientific(False)

#Apply the formatter to the x and y axes.
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_formatter(formatter)

#Define the ticks for the x-axis using LogLocator.
#x_ticks_locator = LogLocator(base=10.0, numticks=12)
#plt.gca().xaxis.set_major_locator(x_ticks_locator)

#Title of the plot.
plt.title('SAIN-LIM PRODUCTOS', fontsize=14, weight='bold')

#Show grid.
#plt.grid(True, which="both", ls="--")

#Show legend.
#plt.legend()

#Display the plot.
plt.show()

