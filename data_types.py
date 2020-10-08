import numpy as np

#integers

i = 10   # integer
print("The data type of i is ",type(i))   # integer


a_i = np.zeros(i,dtype=int)   # declare an array of zeros
print("The data type of a_i is ",type(a_i))   #np.ndarray
print("The data type of a_i[0] is", type(a_i[0]))   #int64


#floats

x = 119.0
print("The data type of x is ",type(x))

y = 1.19e2   # floating point number in sci notation
print("The data type of y is ",type(y))

z = np.zeros(i, dtype=float)
print("The data type of z is ",type(z))
print("The data type of z[0] is ",type(z[0]))