class A:
    # def b(self):
    #     return "Function inside A"
    pass

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    # def b(self):
    #     return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b())