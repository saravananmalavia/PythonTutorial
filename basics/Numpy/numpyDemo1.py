import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr5 = np.array([1, 2, 3, 4], ndmin=5)

print(arr5)
print('number of dimensions :', arr5.ndim)