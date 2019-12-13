class Bank:
    Bank_name = "ICICI"
    L_ROI = 14
    MBL = "Mumbai"
    def __init__(self,Name,age,phno,email,Bal = 0):
        self.Name = Name
        self.age = age
        self.phno = phno
        self.email = email
        self.Bal = Bal
    def deposit(self,amt):
        self.Bal += amt
        self.success()

    def withdraw(self,amt = 0):
        if amt == 0:
            amt = self.get_amount()
        if amt > self.Bal:
            self.failure()
            print("insufficient balance")
            return self.Bal == amt

    @staticmethod
    def get_amount():
        amount = int(input("enter the amount "))
        return amount

    @staticmethod
    def failure():
        print("transaction failure")

    @classmethod
    def change_BName(cls, new = " "):
        if new == " ":
            cls.Bank_name = new
        cls.success()
    @classmethod
    def modify_ROI(cls, new = 0):
        if new == 0:
            new = cls.get_ROI()
        cls.ROI = new
        cls.success()
    @staticmethod
    def get_ROI():
        new = float(input("enter new ROI "))
        return new
    @staticmethod
    def sub(a,b):
        return a-b

    def display(self):
        self.Name,self.age,self.phno,self.email,self.Bal

    def modify(self,Name = " ",age = 0,email = ""):
        if Name != " ":
            self.Name = Name
        if age != 0:
            self.age = age

        if email != email:
            self.email = email
        self.success()


    @staticmethod
    def success():
        print("transaction successfull")
class Bank2(Bank):
    def __init__(self,Name,age,phno,email,pan,aadhar,Bal = 0):
        super(Bank2,self).__init__(Name,age,phno,email,Bal = 0)
        self.pan = pan
        self.aadhar = aadhar
    def add_aadhar_pan(self,pan,aadhar):
        self.pan = pan
        self.aadhar = aadhar
    def display(self):
        print("aadhar number is ", self.aadhar)
        print("pan is ", self.pan)

Reeta = Bank("reeta",25,934234923782142,"reeta@gmail.com",10000)
Seetha = Bank("reeta",26,934234923782142,"SEETHA@gmail.com",10000)
Bank.modify_ROI()
Reeta.display()
Reeta.withdraw()
Bank.get_amount()
Bank.display(Reeta)
# Bank.withdraw(Reeta,1000)
Bank.change_BName()
o2 = Bank2("reeta",25,934234923782142,"reeta@gmail.com","pan123","aad6789",10000)
Bank2.add_aadhar_pan(1231566151,"dhgdshfsdhfhsdf")
o2.display()





