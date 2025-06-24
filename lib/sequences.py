#!/usr/bin/env python3

def print_fibonacci(length):
      if (length == 0) :
        print ([])
      elif (length == 1) :
        print ([0])
      elif (length == 2) :
         print( [0, 1] )
      else:
           result = [0, 1]
           while len(result) < length:
            result.append(result[-1] + result[-2])
           print(result) 
print(print_fibonacci(10))

