class Primes:
     def first(k):
         
         
         def is_prime(n):
             
             import math
             for i in range(2,math.floor(math.sqrt(n))+1):
                 if n%i == 0:
                     
                     
                     return False
                 return True
             lst = []
            
             count = 0
             for num in range(1,15000000) :
                 if is_prime(num) == True:
                     lst.append(num)
                     count += 1
                     if count >= k:
                         return lst
             return lst
print(Primes.first(4))
         
