class Employee:
    __name = 0
    __Employee_no = 0
    __salary = 0

    def set_name(self, name):
        self.__name = name
        return self.__name

    def set_employee_no(self, Employee_no):
        self.__Employee_no = Employee_no
        return self.__Employee_no

    def set_Salary(self, salary):
        self.__salary = salary
        return self.__salary

    def get_name(self):
        return self.__name

    def get_Employee_no(self):
        return self.__Employee_no

    def get_salary(self):
        return self.__salary

#    def count(self):

    def showData(self):
        print("Employee Name: ", self.__name)
        print("Employee Number:" , self.__Employee_no)
        print("Employee's Salary: ", self.__salary)

    def NoOfEmployees(self, countEmployees):
        self.countEmployees = countEmployees + 1
        print("Total Number of Employees: ", self.countEmployees)

print ("Hello World")
