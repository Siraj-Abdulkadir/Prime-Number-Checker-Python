myInput = int(input("Enter any number:"))
primeNumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

if(myInput < 1):
 print("The number have to be greater than 1!")
else:
 squaredRoot = round(myInput**0.5)
 print(squaredRoot)
