//pattern1
def pyramid(p):
   for m in range(0, p):
      for n in range(0, m+1):
         print("* ",end="")
      print("\r")
p = 5
pyramid(p)


//pattern2
def pyramid(p):
   X = 2*p - 2
   for m in range(0, p):
      for n in range(0, X):
         print(end=" ")
      X = X - 2
      for n in range(0, m+1):
         print("* ", end="")
      print("\r")
p = 10
pyramid(p)


//pattern3
n = 0
r = 5
for m in range(1, r+1):
   for gap in range(1, (r-m)+1):
      print(end=" ")
   while n != (2*m-1):
      print("* ", end="")
      n = n + 1
   n = 0
   print()
   
   
//pattern5
length = 6
k = (2 * length) - 2
for p in range(0, length):
   for n in range(0, k):
      print(end=" ")
   k = k - 1
   for n in range(0, p + 1):
      print("@", end=' ')
   print(" ")
Output
