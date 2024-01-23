import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the sinusoidal function
def sinusoidal_function(x, omega, phi, offset):
    return a_z[0] * np.cos(omega * x + phi) + offset

# Load data from CSV file
file_path = 'data.csv'  # Replace with the actual file path
data = pd.read_csv(file_path, sep='\t')

# Extract columns from the DataFrame
angles_400_deg = data['angle']
angles_360 = np.radians(angles_400_deg*0.9)

a_z = data['a_z (g)']
err_a_z = data['err_a_z (g)']

# Perform the curve fit
initial_guess = [1.0, 0.0, 0.0]  
params, covariance = curve_fit(sinusoidal_function, angles_360, a_z, sigma=err_a_z, p0=initial_guess)

# Get the fitted parameters
errors = np.sqrt(np.diag(covariance))
omega_fit, phi_fit, offset_fit = params
err_omega_fit, err_phi_fit, err_offset= errors
max_x = np.max(angles_360)
x_fit = np.linspace(0,max_x ,100)
print(params)
print(errors)
# Generate fitted y values using the fitted parameters
y_fit = sinusoidal_function(x_fit, omega_fit, phi_fit, offset_fit)

# Plot the original data and the fitted sinusoidal curve
plt.errorbar(angles_360, a_z, yerr=err_a_z, fmt='o', label='Data with error bars')
plt.plot(x_fit, y_fit, label='Sinusoidal Fit', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

def inverse_function_and_error(y, delta_y, A, delta_A, omega, delta_omega, phi, delta_phi):
    # Calculate x as the inverse function of y
    x = (np.arccos(y / A) - phi)/ omega

    dx_dy = -1/(A*omega*np.sqrt(1 - y**2/A**2))
    dx_dA = y/(A**2*omega*np.sqrt(1 - y**2/A**2))
    dx_domega = -(-phi + np.arccos(y/A))/omega**2
    dx_dphi = -1/omega

    # Error propagation formula
    term1 = (dx_dy*delta_y)**2
    term2 = (dx_dA*delta_A)**2
    term3 = (dx_domega*delta_omega)**2
    term4 = (dx_dphi*delta_phi)**2
    # Calculate the uncertainty in x
    delta_x = np.sqrt(term1 + term2 + term3 + term4)
    
    return x, delta_x

angle = [np.nan]*len(a_z)
err_angle = [np.nan]*len(a_z)

for i in range(len(a_z)):
    angle[i], err_angle[i] = inverse_function_and_error(a_z[i], err_a_z[i], a_z[0], err_a_z[0], omega_fit, err_omega_fit, phi_fit, err_phi_fit)

print(np.degrees(angle))
print(np.degrees(err_angle))