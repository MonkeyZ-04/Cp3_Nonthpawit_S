def sumnation(number):
    total = 0
    for i in number:
        total+=i
        print(i)
    avg = total/len(number)
    return total,avg


x=[1,2,3,4,5,6,7,8]


print(sumnation(x))