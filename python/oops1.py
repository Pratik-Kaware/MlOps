class employee:
    def __init__(self):
        print("initialing")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("This shows the values assigned to the object")

    # This is method 
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

#create an object/instance of the class employee

sam = employee()

#printing the attribute
#print(sam.id)

#calling a method
sam.travel("kerala")
