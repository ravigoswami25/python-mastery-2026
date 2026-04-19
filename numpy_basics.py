import numpy as np

print("NumPy imported successfully")


#Create Arrays
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

print(arr + 5)
print(arr * 2)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)

arr = np.zeros((3,3))

print(arr)


arr = np.ones((2,2))
print(arr)


arr = np.arange(0,10)
print(arr)

arr = np.random.rand(5)

print(arr)
arr = np.random.randint(1, 100, 5)

print(arr)
print(arr.mean())
