
# base class for term in lambda calculus
class Term():
    pass

# variable
class Var(Term):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

# lambda abstraction
class Lam(Term):
    def __init__(self, var, body):
        super().__init__()
        self.var = var
        self.body = body

    def __str__(self):
        return "\lambda {self.var}."+str(self.body)

# application
class App(Term):
    def __init__(self, t1, t2):
        super().__init__()
        self.t1 = t1
        self.t2 = t2

    def __str__(self):
        return str(self.t1)+str(self.t2)