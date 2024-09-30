
import numpy as np
import matplotlib.pyplot as plt

mass = 5000
velocity = 150
altitude = 10000
g = 9.78



potential_energy = mass * g * altitude  # Constant potential energy

# Speed range
speeds = np.linspace(0, 200, num=101)  # Speed from 0 to 200 m/s


# Calculate kinetic energy for each speed
kinetic_energies = []
for velocity in speeds:
    kinetic_energy = 0.5 * mass * velocity**2
    kinetic_energies.append(kinetic_energy)  # Convert to kJ


# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(speeds, kinetic_energies, label='Kinetic Energy (J)', color='blue')
plt.plot(speeds,potential_energy+0*speeds, color='red', linestyle='--', label='Potential Energy (J)')

# Adding labels and title
plt.title('Kinetic Energy vs. Speed')
plt.xlabel('Speed (m/s)')
plt.ylabel('Energy (kJ)')
plt.legend()
plt.grid()

plt.show()



print(f"The kinetic energy is {kinetic_energy/1000} kJ")