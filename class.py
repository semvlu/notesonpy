class Coursereg:
    def newcourse(course):
        print("new course is here: " + course)

Coursereg.newcourse("control system")

class Students():
    def __init__(self, name, id): #construction formula
        self.stuname= name #self.entity=var
        self.stuid= id
    def showstudent(self): #attributes
        print("New student: " + self.stuname + " ID: " + self.stuid)
jamie= Students("jamie", "b10933333") #object
jamie.showstudent()

class Event():
    def __init__(self, id):
        self.urid= id
    def join(self):
        parid=["b10933001","b10933002","b10933003"]
        if self.urid in parid:
            print("重複報名")
        else:
            print(self.urid + "已報名成功")

lauren= Event("b10933028")
lauren.join()
