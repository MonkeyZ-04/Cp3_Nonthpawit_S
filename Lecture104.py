class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastname,"'s cart")
        #ใช้ข้อมูลภายในClass

customer1 = Customer()
customer1.name = "Nonthpawit"
customer1.lastname = "MonkeyZ"
customer1.addCart()

custom2 = Customer()
custom2.name = "Ming"
custom2.lastname = "Chanakan"
custom2.addCart()

custom3 = Customer()
custom3.name = "First"
custom3.lastname = "One"
custom3.addCart()

custom4 = Customer()
custom4.name = "Nawin"
custom4.lastname = "Blue"
custom4.addCart()