# Program do wyliczenia determinanty macierzy
# importuje bibliotekę Numpy
import numpy as np 

n = int(2)
# Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map()
list1 = list(map(int, 
	input("\nEnter the 2 numbers of first row of Matrix separated by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter the 2 numbers of second row of Matrix separated by space : ").strip().split()))[:n]

# tworzy macierz 2x2
n_array = np.array([(list1), (list2)])
  
# Wyświetla macierz 2x2 
print("Numpy Matrix is:") 
print(n_array) 
  
# Kalkuluje determinante macierzy 
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 2X2 matrix:") 
print(int(det)) 