nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

print("Hola,", nombre)
print("Tienes", edad, "años")

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))

suma = numero1 + numero2import matplotlib.pyplot as plt

# Top 10 empresas del Ecuador por ingresos 2025 (millones de USD)
# Fuente: Ranking Empresarial 2025, Superintendencia de Compañías
empresas = {
    "Corporación Favorita": 2690,
    "Aurelian Ecuador": 1745,
    "Ecuacorriente": 1664,
    "Corporación El Rosado": 1658,
    "Santa Priscila": 1648,
    "Primax": 1401,
    "Pronaca": 1140,
    "Dinadec": 1138,
    "Conecel": 1030,
    "Tuti": 1008,
}

nombres = list(empresas.keys())
ingresos = list(empresas.values())

# Gráfico 1: barras horizontales
plt.figure(figsize=(10, 6))
plt.barh(nombres, ingresos, color="steelblue")
plt.gca().invert_yaxis()
plt.title("Top 10 empresas del Ecuador por ingresos 2025")
plt.xlabel("Ingresos (millones de USD)")
plt.tight_layout()
plt.savefig("grafico_barras.png")

# Gráfico 2: pastel
plt.figure(figsize=(9, 9))
plt.pie(ingresos, labels=nombres, autopct="%1.1f%%")
plt.title("Participación de ingresos entre las 10 empresas")
plt.savefig("grafico_pastel.png")

# Estadísticas básicas
print("Total:", sum(ingresos), "millones")
print("Promedio:", round(sum(ingresos) / len(ingresos), 2), "millones")
print("Mayor:", nombres[ingresos.index(max(ingresos))], "-", max(ingresos))
print("Menor:", nombres[ingresos.index(min(ingresos))], "-", min(ingresos))

plt.show()
print("La suma es:", suma)
