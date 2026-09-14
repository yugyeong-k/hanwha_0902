import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

#0차원
arr0 = np.array(100)

#1차원
arr1 = np.array([1, 2, 3])

#2차원[행, 열]
arr2 = np.array([[1, 2, 3],[4, 5, 6]])

#3차원[면, 행, 열]
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

#배열 차원 수 확인: ndim
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#배열 차원 수 정의
arr5 = np.array([1,2,3,4], ndmin=5)
print(arr5, arr5.ndim)
