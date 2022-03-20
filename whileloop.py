import time
time.time()

timestamp = time.time()

#Python Program to find Sum of N Natural Numbers #

num = 100

if num < 0:
  print("Enter a positive number")
else:
  sum = 0
  #use while loop to iterative until zero
  while(num > 0):
    sum += num
    num -= 1
    print("The sum is ", sum)

#Program completed #

timestamp2 = time.time()
print(timestamp2 - timestamp)