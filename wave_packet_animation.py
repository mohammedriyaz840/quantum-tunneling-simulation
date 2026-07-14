import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- Grid Setup ----
N = 1000
x_min, x_max = -20, 20
x = np.linspace(x_min, x_max, N)
dx = x[1] - x[0]

# ---- Barrier Setup ----
V0 = 15
barrier_width = 1.0
V = np.zeros(N)
V[(x > 0) & (x < barrier_width)] = V0

# ---- Initial Gaussian Wave Packet ----
x0 = -10
sigma = 1.0
k0 = 5.0

psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
psi = psi / np.sqrt(np.sum(np.abs(psi)**2) * dx)

# ---- Momentum space setup ----
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)

# ---- Time evolution operators ----
dt = 0.01
hbar = 1.0
m = 1.0

exp_V = np.exp(-1j * V * dt / (2 * hbar))
exp_K = np.exp(-1j * (hbar * k**2) / (2 * m) * dt)

# ---- Simulation loop (Split-Step Fourier Method) ----
n_steps = 400
psi_frames = []

psi_current = psi.copy()

for step in range(n_steps):
    psi_current = exp_V * psi_current
    psi_k = np.fft.fft(psi_current)
    psi_k = exp_K * psi_k
    psi_current = np.fft.ifft(psi_k)
    psi_current = exp_V * psi_current
    psi_frames.append(np.abs(psi_current)**2)

# ---- Animation ----
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, psi_frames[0], color='blue', linewidth=2)
barrier_plot = ax.fill_between(x, 0, V/V0 * 0.3, color='gray', alpha=0.4, label='Barrier')

ax.set_xlim(x_min, x_max)
ax.set_ylim(0, 0.5)
ax.set_xlabel('Position (x)')
ax.set_ylabel('Probability Density |ψ(x,t)|²')
ax.set_title('Quantum Tunneling: Wave Packet vs Barrier')
ax.legend()
ax.grid(True, alpha=0.3)

def update(frame):
    line.set_ydata(psi_frames[frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=n_steps, interval=20, blit=True)

print("Animation ban rahi hai aur save ho rahi hai... thoda time lagega, please wait.")
ani.save('quantum_tunneling_animation.gif', writer='pillow', fps=30)
print("Animation successfully saved as quantum_tunneling_animation.gif")

plt.show()