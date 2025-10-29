import term

# variable index shifting
def shift(d, c:int, t:term.Term):
    if isinstance(t, term.Var):
        if t.num < c:
            return t
        else:
            return term.Var(t.num+d)
    if isinstance(t, term.Lam):
        return shift(d, c+1, t.body)
    if isinstance(t, term.App):
        return term.App(shift(d, c, t.t1), shift(d, c, t.t2))

# substitute ind to s in t
def substitute(ind:int, s, t:term.Term) -> term.Term:
    if isinstance(t, term.Var):
        if t.num == ind:
            return s
        else:
            return t
    if isinstance(t, term.Lam):
        return term.Lam(substitute(ind+1, shift(1, 0, s), t))
    if isinstance(t, term.App):
        return term.App(substitute(ind, s, t.t1), substitute(ind, s, t.t2))
    
# specific substitution for beta-reduction
def beta(s, t:term.Term)->term.Term:
    return shift(-1, 0, substitute(0, shift(1, 0, s), t))