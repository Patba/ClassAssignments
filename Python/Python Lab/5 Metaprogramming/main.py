class MojaMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print(f"Nazwa klasy: {clsname}")
        print(f"Nazwa klasy: {superclasses}")
        print(f"Nazwa klasy: {attributedict}")
        return type.__new__(cls, clsname, superclasses, attributedict)



class S:
    pass

class A(S,metaclass=MojaMeta):

    def mm(self):
        pass
    pass

class B(A):
    pass

a = A()
b = B()
print(a.mm.__qualname__)

