import numpy as np
import matplotlib.pyplot as plt

print("Setup successful! Quantum Tunneling project shuru karte hain.")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Test Plot - Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()