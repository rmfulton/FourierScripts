import numpy as np
import matplotlib.pyplot as plt

# Function to compute the sum of the Fourier series up to N terms
def fourier_series(N, x):
    return np.sum([np.sin(k * x) / k for k in range(1, N+1)], axis=0)

# Bounding envelope function
def envelope(x):
    return np.sum([1/k for k in range(1, 21)])  # Estimate of upper bound for a reasonable N

# Values for x in the plot
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Number of terms to use in the series
max_terms = 50

# Plotting
plt.figure(figsize=(10, 6))

# Plot the first N terms and the bounding envelope
for N in range(1, max_terms+1, 5):  # Plot partial sums for increasing N
    y_values = fourier_series(N, x_values)
    plt.plot(x_values, y_values, label=f'N = {N}')

# Add the bounding envelope
upper_envelope = envelope(x_values)
lower_envelope = -upper_envelope
plt.fill_between(x_values, lower_envelope, upper_envelope, color='gray', alpha=0.2, label='Bounding Envelope')

# Add labels and title
plt.axhline(0, color='black',linewidth=0.5)  # x-axis
plt.axvline(0, color='black',linewidth=0.5)  # y-axis
plt.title("Partial Sums of Fourier Series: $\sum_{k=1}^\\infty \\frac{\\sin(kx)}{k}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
