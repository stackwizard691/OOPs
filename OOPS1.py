class employee:
    __user_id=0
    #dunder method or constructor
    def __init__(self,name,salary):
        self.__name=name
        self.id=employee.__user_id
        employee.__user_id+=1
        self.salary=salary
        self.designation="SDE"

    @staticmethod
    def get_id():
        return employee.__user_id 
    @staticmethod
    def set_id(val):
        employee.__user_id=val

    def getname(self):
        return self.__name

    def setname(self,value):
        self.__name=value
    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

#object or instance of employee class

# sam=employee()
# sam.travel("Kerela")
# print(sam.salary)