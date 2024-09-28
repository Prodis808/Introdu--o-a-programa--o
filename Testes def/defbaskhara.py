import math
def baskhara(a, b, c):
    Δ = (b**2) - (4 * a * c)
    if Δ == 0:
        x = (-b + math.sqrt(Δ)) / (2 * a)
        return(print(f'Existem 2 raízes, e elas são iguais\nAs duas raízes valem {x :.1f}'))
    elif Δ < 0:
        return(print('Não existem raízes reais para esses valores de a,b,c.'))
    else:
        x1 = (-b + math.sqrt(Δ)) / (2 * a)
        x2 = (-b - math.sqrt(Δ)) / (2 * a)
        return(print(f'Como o detla é maior que 0, as raizes são\nX1 = {x1}\nX2 = {x2}'))
               