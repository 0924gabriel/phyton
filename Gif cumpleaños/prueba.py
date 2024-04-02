import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cargar las imágenes de las diferentes expresiones emocionales
happy_img = plt.imread('gratis-png-p-ilustracion-sonrisas-emoji-sonrisa-iconos-de-computadora-whatsapp-emoji.png')  # Ruta a la imagen de la cara feliz
sad_img = plt.imread('gratis-png-iphone-emoji-tristeza-smiley-emoji.png')      # Ruta a la imagen de la cara triste
angry_img = plt.imread('cara-neutra.png')  # Ruta a la imagen de la cara enfadada

# Lista de emociones para alternar
emotions = [happy_img, sad_img, angry_img]

# Función para animar la cara cambiante
def animate(i):
    plt.cla()  # Limpiar el gráfico anterior
    plt.imshow(emotions[i % len(emotions)])  # Mostrar la imagen correspondiente a la emoción actual

# Configuración inicial del gráfico
fig = plt.figure()

# Crear la animación
ani = animation.FuncAnimation(fig, animate, frames=10, interval=500)

# Guardar la animación como un archivo GIF
ani.save('cara_cambiante_emociones.gif', writer='pillow', fps=1)