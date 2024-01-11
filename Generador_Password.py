import tkinter as tk
from tkinter import ttk
import random
import pyperclip

def generar_contrasena(longitud):
    letras = "QWERTYUIOPÑLKJHGFDSAZXCVBNM.qwertyuiopñlkjhgfdsazxcvbnm"
    numeros = "1234567890"
    signos = "!.,-$%&.#,%&"

    caracteres = letras + numeros + signos
    contrasena = "".join(random.sample(caracteres, longitud))
    return contrasena

def mostrar_contrasena():
    longitud = int(entry_longitud.get())
    contrasena_generada = generar_contrasena(longitud)
    label_resultado.config(text=f"New Password: {contrasena_generada}")
    btn_copiar.config(state=tk.NORMAL)  # Habilitar el botón de copiar
    contrasena_generada_global.set(contrasena_generada)  # Almacenar la contraseña globalmente

def copiar_contrasena():
    contrasena = contrasena_generada_global.get()
    pyperclip.copy(contrasena)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Configurar el estilo
estilo = ttk.Style()
estilo.configure("TButton", padding=6, font=("Arial", 12, "bold"), background="red", foreground="black")
estilo.configure("TLabel", font=("Arial", 14), background="light green", foreground="black")
estilo.configure("TEntry", font=("Arial", 12), background="white")

# Crear variables
contrasena_generada_global = tk.StringVar()

# Crear widgets
label_longitud = ttk.Label(ventana, text="Longitud de la contraseña:", style="TLabel")
entry_longitud = ttk.Entry(ventana, font=("Arial", 12), style="TEntry")
btn_generar = ttk.Button(ventana, text="Generar Contraseña", command=mostrar_contrasena, style="TButton")
label_resultado = ttk.Label(ventana, text="", style="TLabel")
btn_copiar = ttk.Button(ventana, text="Copiar Contraseña", command=copiar_contrasena, state=tk.DISABLED, style="TButton")

# Colocar widgets en la ventana
label_longitud.pack(pady=10)
entry_longitud.pack(pady=10)
btn_generar.pack(pady=10)
label_resultado.pack(pady=10)
btn_copiar.pack(pady=10)

# Ajustar el tamaño de la ventana
ventana.geometry("400x300")

# Iniciar el bucle de eventos
ventana.mainloop()
