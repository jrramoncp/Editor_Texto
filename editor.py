from tkinter import *
from tkinter import filedialog as FileDialog # Para el manejo de archivos

# Variable global de ruta

ruta = "" # Para almacenar info

# Funciones

def nuevo():
    ''' Borra el contenido del texto dejandolo vacio y reinicia cualquier posible config'''
    global ruta
    lower_text.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, END )
    root.title("Editor de texto")

def abrir(): 
    global ruta

    lower_text.set("Abrir fichero")

    ruta = FileDialog.askopenfilename(
        initialdir= ".",
        filetypes=(
                ("Ficheros de texto", "*.txt"),
                    ),
        title="Abrir Fichero."
        )

    if ruta != "":  # Si es una ruta valida
        fichero = open(ruta, "r")
        contenido = fichero.read() 
        texto.delete(1.0, END) # Nos aseguramos de que el contenido que tenemos actualmente este en blanco
        texto.insert("insert", contenido) # Inserta el contenido del fichero
        fichero.close() # Cierra el fichero
        root.title(ruta + "- Editor de texto") # Cambia el titlo de la ventana

def guardar(): 
    lower_text.set("Guardar fichero")

    global ruta

    if ruta != "": 
        contenido = texto.get(1.0, "end") # Capturamos el texto
        fichero = open(ruta, "w+") # Creamos o abrimos el fichero
        fichero.write(contenido) # Escribir texto en el fichero
        fichero.close() # Cerrar el fichero
        lower_text.set("Guardado correctamente") # Modificamos el mensaje del pie

def guardar_como():
    lower_text.set("Guardar como)")

def open_readme(): 
    ''' Funcion para abrir el fichero readme en  una ventana nueva'''
    global ruta

    emergente = Tk()
    readme = Text(emergente)
    readme.pack(fill="both", expand=1)
    readme.config(padx=6, pady=4, bd=0, font=("Consolas", 12))
    file = open("README.md", "r")
    readme.insert("insert", file.read())
    file.close()
    
    emergente.mainloop()


# Interfaz de usuario
## Ventana principal

root = Tk()
root.title("Editor de texto")

## Barra de menú

menubar = Menu(root)
root.config(menu=menubar)
archive = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archive)
archive.add_command(label="Nuevo", command=nuevo)
archive.add_command(label="Abrir", command=abrir)
archive.add_command(label="Guardar", command= guardar)
archive.add_command(label="Guardar Como")
archive.add_command(label="Cerrar")


help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=help)
help.add_command(label = "Acerca de...", command=open_readme)

## Ventana de texto

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))

## Mensaje inferior
lower_text = StringVar()
lower_text.set("Bienvenido al editor de texto")
lower_info = Label(root, textvariable=lower_text, justify="right")
lower_info.pack(side="left")


# Enlazar funciones con los botones del menu



# Bucle Principal
root.mainloop()
