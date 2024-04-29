
class Employee:
    num_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mail.com'

        Employee.num_emps +=1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey','Schafer',5000)
emp_2 = Employee('Test','Smith',6000)

#print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

#print (emp_1.pay)
#Employee.apply_raise(emp_1)
#print (emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_emps)

