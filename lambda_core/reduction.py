import term

# single-step term reduction function
# implements call-by-value strategy
def step_reduce(t:term.Term) -> term.Term:

    # application
    if isinstance(t, term.App):

        # reduce LHS
        if not isvalue(t.t1):
            return term.App(step_reduce(t.t1), t.t2)
        
        # reduce RHS
        if not isvalue(t.t2):
            return term.App(t.t1, step_reduce(t.t2))
        
        # apply function
        return substitute(t.t1, t.t2)
    return t

# the only values are lambda-abstraction
def isvalue(t:term.Term) -> bool:
    return isinstance(t, term.Lam)

    
    
