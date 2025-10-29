import term
import utils

# the only values are lambda-abstractions
def isval(t:term.Term)->bool:
    return isinstance(t, term.Lam)

# single step computation
def eval1(t:term.Term)->tuple[term.Term, bool]:
    if isinstance(t, term.App):
        v1 = isval(t.t1)
        v2 = isval(t.t2)

        if v2 and isinstance(t.t1, term.App):
            return tuple[utils.beta(v2, t.t1), True]
        
        if v1:
            t2p, proceed = eval1(t.t2)
            return tuple[term.App(v1, t2p), proceed]
        
        t1p, proceed = eval1(t.t1)
        return tuple[term.App(t1p, t.t2), proceed]

    # no rule applies
    return tuple[t, False]

# multi-step computation
def eval(t:term.Term)->term.Term:
    proceed = True

    while proceed:
        t, proceed = eval1(t)

    return t