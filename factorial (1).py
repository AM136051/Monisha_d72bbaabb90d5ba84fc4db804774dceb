def recur_factorial(n):
  if n==1:
    return n
  else:
    return n*recur_factorial(n-1)
num=int(input("Enter a number:"))
print("The factorial of",num,"is",recur_factorial(num))
