
from tkinter import *
import re
from tkinter import messagebox

i = 0

estado_resultado = False

def salir():
    if messagebox.askokcancel("Salir", "¿Deseas salir de la calculadora?"):
        root.destroy()

def acerca_de():
    messagebox.showinfo("Acerca de", "Esta es una calculadora básica creada con Python y Tkinter. Permite realizar operaciones aritméticas simples como suma, resta, multiplicación y división. También incluye funciones para borrar la entrada y manejar errores de cálculo.")

def click(valor):
    global i
    global estado_resultado
    entrada.insert(i, valor)
    estado_resultado = False
    i = len(entrada.get())

def clickNumero(valor):
    global i
    global estado_resultado
    if estado_resultado:
        entrada.delete(0, END)
        estado_resultado = False
    entrada.insert(i, valor)
    i = len(entrada.get())

def borrar():
    global i
    entrada.delete(0, END)
    i = 0

def borrar_ultimo():
    global i
    global estado_resultado
    entrada.delete(len(entrada.get())-1, END)
    estado_resultado = False
    i = len(entrada.get())


def operaciones():
    global estado_resultado
    try:
        operacion = entrada.get()
        operacion = re.sub(r'(\d+)²', r'(\1)**2', operacion)
        operacion = re.sub(r'(\d+)³', r'(\1)**3', operacion)
        operacion = re.sub(r'√(\d+)', r'(\1)**0.5', operacion)
        #TODO: Agregar soporte para numeros dentro de parentesis, por ejemplo: (2 + 3)²
        operacion_limpia = re.sub(r'\b0+(?=\d)', '', operacion)
        resultado = eval(operacion_limpia)
        entrada.delete(0, END)
        entrada.insert(0, resultado)
        estado_resultado = True
    except:
        entrada.delete(0, END)
        entrada.insert(0, "Error")

       
root = Tk() #creamos la ventana

root.protocol("WM_DELETE_WINDOW", salir)

root.title("Calculadora") 

menu = Menu(root)
root.config(menu = menu)

menu_archivo = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Archivo", menu = menu_archivo)
menu_archivo.add_command(label = "Salir", command = salir)

menu_ayuda = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Ayuda", menu = menu_ayuda)
menu_ayuda.add_command(label = "Acerca de", command = acerca_de)

entrada = Entry(root, font = ('Curier 20')) #creamos un cuadro de texto
entrada.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5) #ubicamos el cuadro de texto

boton1 = Button(root, text = '1', width = 5, height = 2, command = lambda: clickNumero('1'))
boton2 = Button(root, text = '2', width = 5, height = 2, command = lambda: clickNumero('2'))
boton3 = Button(root, text = '3', width = 5, height = 2, command = lambda: clickNumero('3'))
boton4 = Button(root, text = '4', width = 5, height = 2, command = lambda: clickNumero('4'))
boton5 = Button(root, text = '5', width = 5, height = 2, command = lambda: clickNumero('5'))
boton6 = Button(root, text = '6', width = 5, height = 2, command = lambda: clickNumero('6'))
boton7 = Button(root, text = '7', width = 5, height = 2, command = lambda: clickNumero('7'))
boton8 = Button(root, text = '8', width = 5, height = 2, command = lambda: clickNumero('8'))
boton9 = Button(root, text = '9', width = 5, height = 2, command = lambda: clickNumero('9'))
boton0 = Button(root, text = '0', width = 5, height = 2, command = lambda: clickNumero('0'))

boton_borrar_todo = Button(root, text = 'AC', width = 13, height = 2, command = lambda: borrar())
boton_borrar = Button(root, text = 'C', width = 5, height = 2, command = lambda: borrar_ultimo())
boton_parentesis_abrir = Button(root, text = '(', width = 5, height = 2, command = lambda: clickNumero('('))
boton_parentesis_cerrar = Button(root, text = ')', width = 5, height = 2, command = lambda: clickNumero(')'))
boton_punto = Button(root, text = '.', width = 5, height = 2, command = lambda: clickNumero('.'))

boton_suma = Button(root, text = '+', width = 5, height = 2, command = lambda: click('+'))
boton_resta = Button(root, text = '-', width = 5, height =2, command = lambda: click('-'))
boton_multiplicacion = Button(root, text = '*', width = 5, height = 2, command = lambda: click('*'))
boton_division = Button(root, text = '/', width = 5, height = 2, command = lambda: click('/'))
boton_raiz = Button(root, text = '√', width = 5, height = 2, command = lambda: click('√'))
boton_cuadrado = Button(root, text = 'x²', width = 5, height = 2, command = lambda: click('²'))
boton_cubo = Button(root, text = 'x³', width = 5, height = 2, command = lambda: click('³'))
boton_igual = Button(root, text = '=', width = 5, height = 2, command = lambda: operaciones())

#ubicamos los botones

boton_borrar_todo.grid(row = 1, column = 0, columnspan=2, padx = 5, pady = 5)
boton_cuadrado.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_cubo.grid(row = 1, column = 3, padx = 5, pady = 5)
boton_raiz.grid(row = 2, column = 0, padx = 5, pady = 5)
boton_parentesis_abrir.grid(row = 2, column = 1, padx = 5, pady = 5)
boton_parentesis_cerrar.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_division.grid(row = 2, column = 3, padx = 5, pady = 5)

boton7.grid(row = 3, column = 0, padx = 5, pady = 5)
boton8.grid(row = 3, column = 1, padx = 5, pady = 5)
boton9.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_multiplicacion.grid(row = 3, column = 3, padx = 5, pady = 5)

boton4.grid(row = 4, column = 0, padx = 5, pady = 5)
boton5.grid(row = 4, column = 1, padx = 5, pady = 5)
boton6.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column = 3, padx = 5, pady = 5)

boton1.grid(row = 5, column = 0, padx = 5, pady = 5)
boton2.grid(row = 5, column = 1, padx = 5, pady = 5)
boton3.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 5, column = 3, padx = 5, pady = 5)

boton_punto.grid(row = 6, column = 0, padx = 5, pady = 5)
boton0.grid(row = 6, column = 1, padx = 5, pady = 5)
boton_borrar.grid(row = 6, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 6, column = 3, padx = 5, pady = 5)

root.mainloop() #ejecutamos la ventana