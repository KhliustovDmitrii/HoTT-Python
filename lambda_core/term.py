# definition of terms in lambda-calculus
# de Bruijn indices are user for inner representation

# base class for term
class Term():
    pass

# variable
class Var(Term):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def __str__(self):
        return " " + self.num + " "

# lambda abstraction
class Lam(Term):
    def __init__(self, body):
        super().__init__()
        self.body = body

    def __str__(self):
        return "\lambda "+str(self.body)

# application
class App(Term):
    def __init__(self, t1, t2):
        super().__init__()
        self.t1 = t1
        self.t2 = t2

    def __str__(self):
        return str(self.t1)+str(self.t2)