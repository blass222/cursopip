import numpy as np
# array numpy
arr = np.array([1,2,3,4,5,6,7,8,9,10], dtype='float64')
arr = arr.astype(np.float64)

print(arr)

# Dimenciones numpy arrays
scalar = np.array([1,2,23])

print(scalar)
print(scalar.ndim)

#Creando array con numpy }

lista = list(range(0,10)) #lista normal de python
print(lista)

print(np.arange(0,10,2))

print(np.zeros((5,5)))

print(np.eye((5)))

print(np.random.rand(5,5))

print(np.random.randint(5,50,(10,10)))


#shape y reshape

arr = np.random.randint(1,10,(15,15))
print(arr)


print(np.reshape(arr,(15,15), 'A')) #los rangos tirnen que ser el mismo que el array


#Funciones principales de numpy

arr = np.random.randint(1,10,(5,5))
matriz = arr.reshape(5,5)
print(arr) 
print(matriz.argmax(0))
print(matriz.ptp())
print(np.percentile(arr, 50))
print(np.median(matriz,1))
print(np.std(matriz))
print(np.var(matriz))
print(np.mean(arr))
array = ([1,2,3],[4,5,6])
array2 = ([7,8,9],[10,11,12])



#conditional

arry = np.linspace(1,10,10, dtype='int8')
print(arry > 6)
print((arry < 6) & (arry > 8))


#Operaciones

arr8 = np.arange(0,10)
arr28 = arr.copy()

print(arr8 *2)
print(arr28 /2)
print(arr8 + arr28)

matriz8 = np.reshape(0,10)
matriz28 = matriz8.copy()

print(matriz8 + matriz28)







