

# Import the CoolProp library
from CoolProp.CoolProp import PropsSI

# Define the temperature and the fluid
fluid = 'air'
temperature = 20+273.15
pressure = 101325
# Calculate the density in kg/m^3
speed_sound = PropsSI('SPEED_OF_SOUND', 'P', pressure, 'T', temperature, fluid)
enthalpy = PropsSI('H', 'T', temperature, 'P', pressure, fluid)
energy = PropsSI('U', 'T', temperature, 'P', pressure, fluid)
specific_volume = 1/PropsSI('D', 'T', temperature, 'P', pressure, fluid)
enthalpy_new = energy + pressure*specific_volume
temperature = PropsSI('T', 'H', enthalpy, 'P', pressure, fluid)

# Print the result
print(f"The speed of sound of air at 20 degrees and 1 atm is {speed_sound:.2f} m/s.")

print(f"The energy of air at 20 degrees and 1 atm is {energy:.2f} J/kg.")
print(f"The enthalpy of air at 20 degrees and 1 atm is {enthalpy:.2f} J/kg.")
print(f"The enthalpy of air at 20 degrees and 1 atm is {enthalpy_new:.2f} J/kg.")
# http://www.coolprop.org/coolprop/HighLevelAPI.html