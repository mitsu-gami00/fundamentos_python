
# nombre = "Camila"
# ciudad = "Santiago"
# print(nombre)
# print(ciudad)
# print(type(nombre))

# """ 
# RESULTADO ESPERADO
# Camila
# Santiago
# <class 'str'>
# """

# """
# AHORA TE TOCA · EJERCICIO 3 — Practica el tipo str
# Debajo del ejemplo, crea tres variables con el nombre de una película, un videojuego y una asignatura. Muéstralas
# con print() y aplica type() a una de ellas.
# Comprueba: El tipo debe aparecer como str; observa que los textos están entre comillas.
# """

# pelicula = input("Ingrese el nombre de una película: ")
# videojuego = input("Ingrese el nombre de un videojuego: ")
# asignatura = input("Ingrese el nombre de una asignatura: ")

# print(f'Película: {pelicula} \n Tipo de dato: {type(pelicula)}')
# print(f'Videojuego: {videojuego} \n Tipo de dato: {type(videojuego)}')
# print(f'Asignatura: {asignatura} \n Tipo de dato: {type(asignatura)}')


# """
# 4.2. Enteros: int
# Un int es un número entero, sin parte decimal. No se escribe entre comillas si deseas utilizarlo como número.
# """
# edad = 16
# cantidad = 25
# print(edad)
# print(cantidad)
# print(type(edad))
# """
# RESULTADO ESPERADO
# 16
# 25
# <class 'int'>"""


# """
# AHORA TE TOCA · EJERCICIO 4 — Practica el tipo int
# Crea variables numéricas para tu edad, cantidad de hermanos y año actual. Muestra las tres con print() y verifica el
# tipo de una con type().
# Comprueba: Si escribes "16" entre comillas, Python lo reconoce como texto, no como número entero.
# """
# mi_edad = int(input("Ingrese su edad: "))
# cantidad_hermanos = int(input("Ingrese la cantidad de hermanos: "))
# año_actual = int(input("Ingrese el año actual: "))

# print(f'Mi edad: {mi_edad} \n Tipo de dato: {type(mi_edad)}')
# print(f'Cantidad de hermanos: {cantidad_hermanos} \n Tipo de dato: {type(cantidad_hermanos)}')
# print(f'Año actual: {año_actual} \n Tipo de dato: {type(año_actual)}')

# """
# 4.3. Decimales: float
# Un float guarda números con parte decimal. En Python se utiliza punto (.), no coma (,), como separador decimal.
# """

# precio = 1599.90
# altura = 1.65
# print(precio)
# print(altura)
# print(type(altura))

# """
# RESULTADO ESPERADO
# 1599.9
# 1.65
# <class 'float'>
# """

# """
# AHORA TE TOCA · EJERCICIO 5 — Practica el tipo float
# Declara variables para el precio de un producto, la temperatura y un promedio de notas. Imprime los tres valores y
# utiliza type() en dos de ellos.
# Comprueba: Todos deben contener valores numéricos escritos con punto decimal.
# """
# precio_producto = float(input("Ingrese el precio de un producto: "))
# temperatura = float(input("Ingrese la temperatura: "))
# promedio_notas = float(input("Ingrese el promedio de notas: "))

# print(f'Precio del producto: {precio_producto} \n Tipo de dato: {type(precio_producto)}')
# print(f'Temperatura: {temperatura} \n Tipo de dato: {type(temperatura)}')
# print(f'Promedio de notas: {promedio_notas} \n Tipo de dato: {type(promedio_notas)}')

# """
# 4.4. Booleanos: bool
# Un bool expresa uno de dos valores lógicos: True (verdadero) o False (falso). Deben escribirse con mayúscula inicial y
# sin comillas.
# PYTHON
# """
# tiene_computador = True
# esta_lloviendo = False
# print(tiene_computador)
# print(esta_lloviendo)
# print(type(tiene_computador))


# """
# RESULTADO ESPERADO
# True
# False
# <class 'bool'>
# """

# """AHORA TE TOCA · EJERCICIO 6 — Practica el tipo bool
# Crea tres variables booleanas para indicar si tienes Internet, si terminaste la tarea y si tienes clases mañana.
# Imprime sus valores y verifica el tipo de una.
# Comprueba: True y False no llevan comillas."""

# hay_internet = True
# tarea_terminada = True
# clases_manaña = False

# print(f'Tengo Internet: {hay_internet} \n Tipo de dato: {type(hay_internet)}')
# print(f'Tarea terminada: {tarea_terminada} \n Tipo de dato: {type(tarea_terminada)}')
# print(f'Clases mañana: {clases_manaña} \n Tipo de dato: {type(clases_manaña)}')

# # 4.5. Integración: ficha de producto
# # En el mismo archivo, agrega una ficha de producto que contenga nombre (str), cantidad (int), precio (float) y
# # disponibilidad (bool). Debes imprimir cada valor y comprobar su tipo.

nombre_producto = input("Ingrese el nombre del producto: ")
cantidad_producto = int(input("Ingrese la cantidad del producto: "))
precio_producto = float(input("Ingrese el precio del producto: "))
disponibilidad_producto = True if input("¿El producto está disponible? (si/no): ").lower() == 'si' else False

print(f'Nombre: {nombre_producto} \n Tipo: {type(nombre_producto)}')
print(f'Cantidad: {cantidad_producto} \n Tipo: {type(cantidad_producto)}')
print(f'Precio: {precio_producto} \n Tipo: {type(precio_producto)}')
print(f'Disponibilidad: {disponibilidad_producto} \n Tipo: {type(disponibilidad_producto)}')

# AHORA TE TOCA · EJERCICIO 7 — Cuatro tipos en una ficha
# Inventa un producto de una tienda, crea cuatro variables con los tipos correspondientes e imprime los valores y el
# tipo de cada variable.
# Comprueba: Antes de continuar, asegúrate de haber utilizado str, int, float y bool dentro del mismo archivo.
