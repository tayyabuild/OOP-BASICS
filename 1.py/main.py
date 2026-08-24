''' Create a class “Programmer” for storing information of few programmers working at
Microsoft'''

class Programmer:
    company = 'Microsoft'                      #this is a class attribute i.e. every programmer in this class works at Microsoft
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


m = Programmer("Mudassar", 10000000, 23425)
print(m.name, m.salary, m.pin)

a = Programmer("Ali", 3600000, 23996)
print(a.name, a.salary, a.pin)
