def vatCalculate(totalPrince = float(input("Total Prince :  "))):
    result = totalPrince+(totalPrince*7/100)
    return result
print(vatCalculate())