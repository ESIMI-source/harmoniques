import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Reconstruction de p(t) par série de Fourier (Exercice 3 - TD1)")
st.markdown("Signal périodique impair (onde carrée) reconstruit avec N harmoniques impairs.")

# Paramètres fixes
P0 = 1.0
T = 2 * np.pi
omega = 1.0  # car T = 2π → ω = 2π/T = 1
t = np.linspace(0, 2 * T, 2000)

# Signal original (onde carrée impaire)
def p_original(t):
    t_mod = np.mod(t, T)
    return np.where(t_mod < T/2, P0, -P0)

p_true = p_original(t)

# Slider pour choisir N
N = st.slider("Nombre maximal d'harmoniques N", min_value=1, max_value=51, value=5, step=2)

# Calcul de la série de Fourier tronquée (seulement n impairs ≤ N)
p_fourier = np.zeros_like(t)
n_impairs = [n for n in range(1, N + 1) if n % 2 == 1]

for n in n_impairs:
    bn = 4 * P0 / (np.pi * n)
    p_fourier += bn * np.sin(n * omega * t)

# Tracé
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, p_true, 'k', linewidth=2, label=r'$p(t)$ original (onde carrée)')
ax.plot(t, p_fourier, 'r--', linewidth=1.5, label=f'Approximation avec N = {N}')
ax.set_xlabel("Temps $t$")
ax.set_ylabel("$p(t)$")
ax.set_ylim(-1.6, 1.6)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
ax.set_title(f"Reconstruction de $p(t)$ avec {len(n_impairs)} harmoniques impairs")

# Affichage dans Streamlit
st.pyplot(fig)

# Optionnel : afficher les harmoniques utilisés
st.caption(f"Harmoniques utilisés : {n_impairs}")
