data = {"191":"แจ้งเหตุด้วน","1668":"Hospital","1447":"ดับเพลิง"}

def searchNumber(message):
    for key , value in data.items():
        if value==message:
            print("Phone = ",key)

searchNumber("Hospital")