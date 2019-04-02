# Copyright (C) <2019>  <John Díaz / HapticLemon / jdl.profesional@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


# Aplica algunos conceptos interesantes :
#	- Conversión de diccionarios a conjuntos
#	- Intersección de conjuntos
#	- deepcopy
#	- Funciones "lambda"
#	- Función "reduce"
#	- Función con número de parámetros arbitrario.

import copy
from functools import reduce

# Calcula la intersección de claves de un número arbitrario de 
# diccionarios.
def intersect(*dicts):
	# Al convertir un diccionario a set nos quedamos con sus claves (!)
	# de modo que puedo guardarlas en una lista.
	# setlist = [{1, 2, 3, 4, 6}, {1, 3, 4, 5, 6}, {2, 3, 4, 6, 7}]
	setlist = []
	for dic in dicts:
		setlist.append(set(dic))

	# Obtengo la intersección (x & y ) de las claves de los diccionarios
	# Reduce me permite ir "consumiendo" la lista de claves.
	# {1, 2, 3, 4, 6} & {1, 3, 4, 5, 6} -> {1, 3, 4, 6}
	# {1, 3, 4, 6} & {2, 3, 4, 6, 7} -> {3, 4, 6}
	# interseccion = {3, 4, 6}
	interseccion = reduce(lambda x,y: x & y, setlist)

	return interseccion

# Elimina las claves del diccionario que no estén en intersección
def normaliza(diccionario, interseccion):
	copia_diccionario = copy.deepcopy(diccionario)

	for key in diccionario:
		if key not in interseccion:
			# Tengo que trabajar con una copia ya que
			# NO PUEDE MODIFICARSE AL VUELO UN DICCIONARIO 
			# QUE SE ESTÁ ITERANDO
			del copia_diccionario[key]

	return copia_diccionario

# Defino 3 diccionarios con algunas claves comunes (3 y 4)
d1 = {1:0.11, 2:0.21, 3:0.31, 4:0.41, 6:0.61}
d2 = {1:0.12, 3:0.32, 4:0.42, 5:0.52, 6:0.62}
d3 = {2:0.23, 3:0.33, 4:0.43, 6:0.63, 7:0.73}

print ("\nDiccionarios originales :")
print (d1)
print (d2)
print (d3)

# Calculo la intersección de las claves de los diccionarios
interseccion = intersect(d1,d2,d3)

# Elimino de los diccionarios las claves que no sean comunes.
d11 = normaliza(d1, interseccion)
d21 = normaliza(d2, interseccion)
d31 = normaliza(d3, interseccion)

# Los nuevos diccionarios una vez "podados" de claves no comunes.
print ("\nDiccionarios con las claves comunes :")
print (d11)
print (d21)
print (d31)
