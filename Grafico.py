import pandas as pd
import matplotlib.pyplot as plt

# Datos de Manuelita
manuelita = [
    4.6,4.6,4.8,4.6,5.0,5.0,5.0,5.0,
    4.8,4.8,4.8,5.2,4.8,4.8,5.0,4.8,
]

# Datos de Incauca
incauca = [
    4.8,4.8,4.6,5.0,5.2,4.6,5.0,5.0,
    4.6,5.0,5.2,5.2,5.0,4.6,5.2,5.0,
]

# Crear DataFrame
data = pd.DataFrame(
    {
        "Empresa": ["Manuelita"] * len(manuelita) + ["Incauca"] * len(incauca),
        "Peso Azúcar": manuelita + incauca,
    }
)

plt.figure(figsize=(8, 6))
plt.boxplot([manuelita, incauca], labels=["Manuelita", "Incauca"])
plt.title("Comparación del Peso de Azúcar por Empresa", fontweight="bold")
plt.xlabel("Empresa")
plt.ylabel("Peso de Azúcar (g)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Línea horizontal en 5g (valor objetivo)
plt.axhline(y=5, color="red", linestyle="--", label="Objetivo: 5g")
plt.legend()
plt.show()

# Datos opcionales: Añadir puntos de datos individuales
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.boxplot(x="Empresa", y="PesoAzucar", data=data, color="lightgray")
sns.swarmplot(x="Empresa", y="PesoAzucar", data=data, color="black", alpha=0.7)
plt.axhline(y=5, color="red", linestyle="--")
plt.title("Distribución de PesoAzucar con Datos Individuales")
plt.show()
