#Librerias
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

#leer csv
laterales = pd.read_csv("Laterales.csv")

laterales['DuelosGanados'] = laterales['DuelosGanados'].str.rstrip('%').astype('float') #Transformamos los percentages
laterales['DuelosAereosGanados'] = laterales['DuelosAereosGanados'].str.rstrip('%').astype('float')
laterales['BarridasGanadas'] = laterales['BarridasGanadas'].str.rstrip('%').astype('float')
laterales['PasesAcertados'] = laterales['PasesAcertados'].str.rstrip('%').astype('float')
laterales['CambiosDeJuegoExitosos'] = laterales['CambiosDeJuegoExitosos'].str.rstrip('%').astype('float')
laterales['Tiros a puerta'] = laterales['Tiros a puerta'].str.rstrip('%').astype('float')

#Eliminamos algunas columnas
laterales = laterales.drop(['Goles dentro del area'], axis=1)
laterales = laterales.drop(['Goles fuera del area'], axis=1)

# ------- PART 1: Create background
# number of variable
categories=list(laterales)[4:]
print(categories)
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
print(angles)

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)

# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable

# Chaka 
values=laterales.loc[0].values.flatten().tolist()
values = values[3:]
print(len(values))
ax.plot(angles, values, linewidth=1, linestyle='solid', label="EL CHAKA")
ax.fill(angles, values, 'b', alpha=0.1)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()