# lambda function

"""

lambda argument(input) : expression(=return)

"""

x=lambda name:name+(" it's function")
sum=lambda x,y : x+y
multiply = lambda a,b:a*b

def myPower(z):
    return lambda i:z**i
r = myPower(5) #r = lambda, r = lambda i:z**i
result = r(2)

print(x("Non"))
print(sum(1,2))
print(multiply(5,10))
print(result)