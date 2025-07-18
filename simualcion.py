import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Parámetros físicos
n = 2
m1 = 1
m2 = 100 ** n
v1 = 0.0
v2 = -1.0
x1 = 1.0
x2 = 3.0

dt = 0.001
count = 0

# Datos para animar
posiciones_x1 = []
posiciones_x2 = []
conteo_colisiones = []

# Simulación sin animación todavía
while True:
    # Colisión entre bloques
    if x2 - x1 <= 1.0:
        new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
        v1, v2 = new_v1, new_v2
        count += 1

    # Colisión con el muro
    if x1 <= 0 and v1 < 0:
        v1 = -v1
        count += 1

    x1 += v1 * dt
    x2 += v2 * dt

    posiciones_x1.append(x1)
    posiciones_x2.append(x2)
    conteo_colisiones.append(count)

    if v1 > v2 and v2 > 0:
        break

# -------- Interfaz con muro --------

fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(-1, 6)
ax.set_ylim(-0.2, 1.2)
ax.set_facecolor("white")
ax.axis("off")

# Muro (estático a la izquierda)
muro = patches.Rectangle((-0.1, 0), 0.1, 1.0, color='gray')

# Bloques móviles
bloque1 = patches.Rectangle((0, 0), 1.0, 1.0, color='blue')
bloque2 = patches.Rectangle((0, 0), 1.0, 1.0, color='red')

# Añadir al gráfico
ax.add_patch(muro)
ax.add_patch(bloque1)
ax.add_patch(bloque2)

# Conteo de colisiones
texto = ax.text(0.2, 1.05, '', fontsize=14, color="black", weight="bold")

def init():
    bloque1.set_xy((posiciones_x1[0], 0))
    bloque2.set_xy((posiciones_x2[0], 0))
    texto.set_text('')
    return bloque1, bloque2, texto

def update(frame):
    bloque1.set_xy((posiciones_x1[frame], 0))
    bloque2.set_xy((posiciones_x2[frame], 0))
    texto.set_text(f"Colisiones: {conteo_colisiones[frame]}")
    return bloque1, bloque2, texto

ani = animation.FuncAnimation(
    fig, update, frames=len(posiciones_x1),
    init_func=init, blit=True, interval=1, repeat=False
)

plt.show()
