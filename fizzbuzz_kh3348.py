# -*- coding: utf-8 -*-
"""fizzbuzz_kh3348.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18ZEq7kx0SD5vqFHW8YX8uS3UrndCUkr8
"""

def FizzBuzz(start,finish):
    outlist=[]
    for i in range(start,finish+1):
        if i%3==0 and i%5==0:
            outlist.append('FizzBuzz')
        elif i%3==0:
            outlist.append('Fizz')
        elif i%5==0:
            outlist.append('Buzz')
        else:
            outlist.append(i)
    return outlist

#test case
FizzBuzz(1,15)