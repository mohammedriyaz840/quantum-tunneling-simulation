import numpy as np
import matplotlib.pyplot as plt

# ---- Physical Constants (Natural Units) ----
hbar = 1.0
m = 1.0
V0 = 2.0   # Barrier height
L = 1.0    # Barrier width

# ---- Energy range ----
E = np.linspace(0.01, 4.0, 500)

# ---- Wave number inside barrier (complex-safe formula) ----
k2 = np.sqrt(2 * m * np.abs(V0 - E) + 0j) / hbar

# ---- Transmission coefficient calculation ----
numerator = 4 * E * (V0 - E)
denominator = numerator + V0**2 * np.sinh(k2 * L)**2
T = numerator / denominator
T = np.real(T)

# ---- Plotting ----
plt.figure(figsize=(8,5))
plt.plot(E, T, color='blue', linewidth=2, label='Transmission Coefficient T(E)')
plt.axvline(x=V0, color='red', linestyle='--', label=f'Barrier Height V0 = {V0}')
plt.xlabel('Particle Energy (E)')
plt.ylabel('Transmission Coefficient (T)')
plt.title('Quantum Tunneling: Transmission Coefficient vs Energy')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('transmission_coefficient.png', dpi=300)
plt.show()