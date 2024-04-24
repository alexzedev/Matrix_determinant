# Program to calculate Matrix determinant
# importing Numpy package 
import numpy as np 

n = int(2)
# Lines below reads inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter the 2 numbers of first row of Matrix separated by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter the 2 numbers of second row of Matrix separated by space : ").strip().split()))[:n]

# creating a 2X2 Numpy matrix 
n_array = np.array([(list1), (list2)])
  
# Displaying the Matrix 
print("Numpy Matrix is:") 
print(n_array) 
  
# calculating the determinant of matrix 
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 2X2 matrix:") 
print(int(det)) 