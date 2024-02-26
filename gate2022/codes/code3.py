import numpy as np
import matplotlib.pyplot as plt

# Define the band-limited function x(omega)
def x_omega(omega):
    if omega >= 100 and omega <= 200:
        return 1
    else:
        return 0

# Generate omega values
omega_values = np.linspace(0, 400, 1000)

# Calculate corresponding x(omega) values
x_omega_values = [x_omega(omega) for omega in omega_values]

# Plot x(omega)
plt.plot(omega_values, x_omega_values)
plt.xlabel('Omega (Hz)')
plt.ylabel('x(omega)')
plt.title('Band-limited Signal x(omega)')
plt.grid(True)
plt.xlim(0, 400)
plt.ylim(0, 1.2)  # Set y-axis limit slightly higher than 1 for better visualization
plt.savefig('x_omega_plot.png')  # Save the plot as an image file
plt.show()

