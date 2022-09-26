#B0822012q1.py 第一題
import math as m
A=input().split()
for i in range(len(A)):
    A[i] = float(A[i])

B=input().split()
for i in range(len(B)):
    B[i] = float(B[i])

print(m.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2+(A[2]-B[2])**2))
