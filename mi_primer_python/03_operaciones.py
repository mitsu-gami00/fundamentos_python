
# UNIDAD 05 Operaciones matemáticas básicas
# Ahora crearás un archivo independiente para practicar operaciones. En la terminal CMD, dentro de la carpeta del
# proyecto, escribe:
# CMD
# type nul > 03_operaciones.py
# dir
# Abre 03_operaciones.py en VS Code. Guarda los ejemplos y ejecútalos después de cada ejercicio con python
# 03_operaciones.py o py 03_operaciones.py.
# 5.1. Suma (+)

numero1 = 12
numero2 = 8
print(numero1 + numero2)

# Resultado esperado: 20. El operador + suma dos números.
# AHORA TE TOCA · EJERCICIO 8 — Suma tus valores
# Crea lapices = 7 y cuadernos = 4. Muestra con print() el total de artículos.
# Comprueba: El resultado debe ser 11.

lapices = int(input("Ingrese la cantidad de lápices: "))
cuadernos = int(input("Ingrese la cantidad de cuadernos: "))
total_articulos = lapices + cuadernos
print(total_articulos)

# 5.2. Resta (-)

dinero = 5000
gasto = 1800
print(dinero - gasto)

# Resultado esperado: 3200. El operador - calcula una diferencia.
# AHORA TE TOCA · EJERCICIO 9 — Dinero que queda
# Declara variables para presupuesto = 10000 y compra = 3750. Muestra cuánto dinero queda.
# Comprueba: El resultado debe ser 6250.

presupuesto = int(input("Ingrese el presupuesto: "))
compra = int(input("Ingrese el gasto de la compra: "))
dinero_que_queda = presupuesto - compra
print(dinero_que_queda)

# 5.3. Multiplicación (*)

precio = 2500
cantidad = 3
print(precio * cantidad)
# Resultado esperado: 7500. En Python se utiliza el asterisco *.
# AHORA TE TOCA · EJERCICIO 10 — Costo total
# Si cada entrada cuesta 4000 y compras 5, calcula el precio total con variables y print().
# Comprueba: El resultado debe ser 20000.

costo_entrada = int(input("Ingrese el costo de cada entrada: "))
cantidad_entradas_compradas = int(input("Ingrese la cantidad de entradas compradas: "))
costo_total = costo_entrada * cantidad_entradas_compradas
print(costo_total)

# 5.4. División (/)

total = 20
personas = 4
print(total / personas)

# Resultado esperado: 5.0. La división / produce un resultado de tipo float, incluso cuando es exacta.
# AHORA TE TOCA · EJERCICIO 11 — Reparto exacto
# Reparte 48 objetos entre 6 personas usando /.
# Comprueba: El resultado debe ser 8.0.

cantidad_objetos = int(input("Ingrese la cantidad de objetos: "))
cantidad_personas = int(input("Ingrese la cantidad de personas: "))
print(cantidad_objetos / cantidad_personas)

# 5.5. División entera (//)

lapices = 17
paquetes = 5
print(lapices // paquetes)
# Resultado esperado: 3. El operador // devuelve el cociente entero para estos números positivos.
# AHORA TE TOCA · EJERCICIO 12 — Grupos completos
# Si tienes 23 estudiantes y cada equipo debe tener 4, calcula cuántos equipos completos puedes formar con //.
# Comprueba: El resultado debe ser 5.

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
tamaño_equipo = int(input("Ingrese el tamaño de cada equipo: "))
equipos_completos = cantidad_estudiantes // tamaño_equipo
print(equipos_completos)

# 5.6. Módulo (%)

lapices = 17
paquetes = 5
print(lapices % paquetes)

# Resultado esperado: 2. El operador % indica el resto de una división.
# AHORA TE TOCA · EJERCICIO 13 — Elementos sobrantes
# Con 23 estudiantes en equipos de 4, utiliza % para saber cuántos estudiantes quedan fuera de equipos completos.
# Comprueba: El resultado debe ser 3.

print(cantidad_estudiantes % tamaño_equipo)

# 5.7. Potencia (**)

base = 3
exponente = 2
print(base ** exponente)

# Resultado esperado: 9. El operador ** eleva un número a una potencia.
# AHORA TE TOCA · EJERCICIO 14 — Cálculo de potencia
# Crea dos variables para calcular 2 elevado a 5 utilizando **.
# Comprueba: El resultado debe ser 32.

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(base ** exponente)

# 5.8. Guardar resultados en variables
# También puedes almacenar el resultado de una operación y mostrarlo después:

precio = 2500
cantidad = 3
total = precio * cantidad
print("Total de la compra:")
print(total)

# RESULTADO ESPERADO
# Total de la compra:
# 7500

# AHORA TE TOCA · EJERCICIO 15 — Promedio de notas
# Crea las variables nota1 = 6.0, nota2 = 5.0 y nota3 = 7.0. Calcula el promedio guardándolo en una variable y
# muéstralo con print().
# Comprueba: Debe mostrarse 6.0. Recuerda utilizar paréntesis para sumar antes de dividir.
# COMPROBACIÓN DE OPERADORES
# En tu archivo deben aparecer los siete operadores: +, -, *, /, //, %, **, además de un resultado almacenado en una
# variable.

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(promedio)