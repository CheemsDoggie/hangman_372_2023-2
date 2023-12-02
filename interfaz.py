# libreria para hacer interfaces con ventanas
import tkinter as tk

# ventana principal
root = tk.Tk()
root.title("Imagen de Fondo en Tkinter")

# Cargar la imagen
image_path = "./img/1.png"  # Reemplaza con la ruta de tu imagen
img = tk.PhotoImage(file=image_path)

# Crear un Canvas del tamaño de la ventana principal
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()

# Configurar la imagen de fondo
canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Resto de tu interfaz y código aquí

# hace que la ventana se mantenga activa
root.mainloop()