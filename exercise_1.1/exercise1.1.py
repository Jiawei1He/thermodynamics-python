

# Import the CoolProp library
from CoolProp.CoolProp import PropsSI

# Define the temperature and the fluid
fluid = 'Water'

# Calculate the density in kg/m^3
density = PropsSI('D', 'T', 300, 'P', 101325, fluid)

# Print the result
print(f"The density of liquid water at 20 degrees Celsius is {density:.2f} kg/m³.")
