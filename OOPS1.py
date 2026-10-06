class employee:
    #dunder method or constructor
    def __init__(self):
        
        self.id=12
        self.salary=60000
        self.designation="SDE"

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

#object or instance of employee class

sam=employee()
sam.travel("Kerela")
print(sam.salary)