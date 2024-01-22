import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the sinusoidal function
def sinusoidal_function(x, A, omega, phi):
    return A * np.cos(omega * x + phi)

# Load data from CSV file
file_path = 'data.csv'  # Replace with the actual file path
data = pd.read_csv(file_path, sep='\t')

# Extract columns from the DataFrame
angles_400_deg = data['angle']
angles_360 = np.radians(angles_400_deg*0.9)

a_z = data['a_z (g)']
err_a_z = data['err_a_z (g)']

# Perform the curve fit
initial_guess = [1.0, 2.0, 0.0]  # You may need to adjust the initial guess based on your data
params, covariance = curve_fit(sinusoidal_function, angles_360, a_z, sigma=err_a_z, p0=initial_guess)

# Get the fitted parameters
errors = np.sqrt(np.diag(covariance))
A_fit, omega_fit, phi_fit = params
err_Afit, err_omega_fit, err_phi_fit= errors
max_x = np.max(angles_360)
x_fit = np.linspace(0,max_x ,100)
print(params)
print(errors)
# Generate fitted y values using the fitted parameters
y_fit = sinusoidal_function(x_fit, A_fit, omega_fit, phi_fit)

# Plot the original data and the fitted sinusoidal curve
plt.errorbar(angles_360, a_z, yerr=err_a_z, fmt='o', label='Data with error bars')
plt.plot(x_fit, y_fit, label='Sinusoidal Fit', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

def inverse_function_and_error(y, delta_y, A, delta_A, omega, delta_omega, phi, delta_phi):
    # Calculate x as the inverse function of y
    print(y, A, y/A)
    x = (np.arccos(y / A) - phi) / omega
    
    # Error propagation formula
    term1 = (delta_y / y)**2 / (omega**2 * (1 - (y / A)**2))
    term2 = ((delta_A / A)**2 * (y / A)**2) / (omega**2 * (1 - (y / A)**2))
    term3 = ((delta_omega / omega)**2 * (np.arccos(y / A) - phi)**2) / (omega**2 * (1 - (y / A)**2))
    term4 = (delta_phi / phi)**2 / (omega**2 * (1 - (y / A)**2))
    print(x, term1, term2, term3, term4)
    # Calculate the uncertainty in x
    delta_x = np.sqrt(term1 + term2 + term3 + term4)*x
    
    return x, delta_x

angle, err_angle = inverse_function_and_error(a_z[2], err_a_z[2], A_fit, err_Afit, omega_fit, err_omega_fit, phi_fit, err_phi_fit)

print(np.degrees(angle), np.degrees(err_angle))