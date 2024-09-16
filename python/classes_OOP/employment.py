class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
        
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " +str(days) + " days."
        
plato = Supervisors('plato', 'phil','Phil050phy')

emily = Chefs('Emily', 'A')
Tzu = Chefs('Tzu', 'S')


print(emily.leave_request(4))
print(plato.password)