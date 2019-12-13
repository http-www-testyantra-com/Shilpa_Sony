class College:
    College_name = "BLDE"
    CID = 14
    CL = "Bangalore"
    def __init__(self,Name,age,phno,email,sid):
        self.Name = Name
        self.age = age
        self.phno = phno
        self.email = email
        self.sid = sid
    def get_Ia(self,iamarks,Total):
        self.Total += iamarks
        self.success()

    def get_Grade(self,percent):
        if percent < 35:
            print("Fail")
        elif percent < 70 and percent > 35:
            print("Second class")
        else:
            print("FCD")

    @staticmethod
    def get_Sid():
        roll_no = int(input("enter the roll nor "))
        return roll_no

    @staticmethod
    def failure():
        print("transaction failure")

    @classmethod
    def change_CName(cls, new = " "):
        if new == " ":
            cls.College_name = new
        cls.success()
    @classmethod
    def modify_CollegeId(cls, new = 0):
        if new == 0:
            new = cls.get_College()
        cls.College_Id = new
        cls.success()
    @staticmethod
    def get_College():
        new = float(input("enter new Cid "))
        return new


    def display(self):
        self.Name,self.age,self.phno,self.email,self.sid

    def modifyStudentDetails(self,Name = " ",age = 0,email = ""):
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

Reeta = College("reeta",25,934234923782142,"reeta@gmail.com",1)
Seetha = College("reeta",26,934234923782142,"SEETHA@gmail.com",2)

College.get_College()
College.success()
College.change_CName()
Reeta.display()
Reeta.get_Grade(40)
Reeta.get_Ia(25,100)
Reeta.get_Sid()
Reeta.modifyStudentDetails()







