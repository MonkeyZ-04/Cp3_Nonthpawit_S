# หาจำนวนตัวอักษรพิมพ์เล็ก/พิมพ์ใหญ่

# ABcDEfg

def checkString(message):
    result ={"UPPER":0,"LOWER":0}
    for character in message:
        if character.isupper():
            result["UPPER"]+=1
        elif character.islower():
            result["LOWER"]+=1
        else:
            pass
    return result



x=checkString("ABcDEfg")
print(x)