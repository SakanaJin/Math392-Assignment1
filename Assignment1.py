import math
import matplotlib.pyplot as plt

TOLERANCE = 1e-5
MAXITER = 20

def f(x) -> float:
    return math.exp(x) + 2**-x + math.cos(x) - 6

def fprime(x) -> float:
    return math.exp(x) - (2**-x) * math.log(2) - math.sin(x)

def Newton(p0: float) -> dict:
    toreturn = {"last": {"value": None, "iteration": None, "error": None}}
    for i in range(MAXITER + 1):
        temp = p0 - f(p0)/fprime(p0)
        err = abs(temp - p0)
        p0 = temp
        toreturn['secondlast'] = toreturn['last']
        toreturn['last'] = {'value': p0, 'iteration': i, 'error': err}
        if err < TOLERANCE:
            return toreturn
    else:
        return None

def Secant(p0: float, p1: float) -> dict:
    toreturn = {'last': {'value': None, 'iteration': None, 'error': None}}
    fp0 = f(p0)
    fp1 = f(p1)
    for i in range(MAXITER + 1):
        temp = p1 - (fp1*(p1 - p0))/(fp1 - fp0)
        err = abs(temp - p1)
        toreturn['secondlast'] = toreturn['last']
        toreturn['last'] = {'value': temp, 'iteration': i, 'error': err}
        if err < TOLERANCE:
            return toreturn
        p0 = p1
        p1 = temp
        fp0 = fp1
        fp1 = f(temp)
    else:
        return None

def Falsepos(p0: float, p1: float) -> dict:
    toreturn = {'last': {'value': None, 'iteration': None, 'error': None}}
    fp0 = f(p0)
    fp1 = f(p1)
    for i in range(MAXITER + 1):
        temp = p1 - (fp1*(p1 - p0))/(fp1 - fp0)
        err = abs(temp - p1)
        toreturn['secondlast'] = toreturn['last']
        toreturn['last'] = {'value': temp, 'iteration': i, 'error': err}
        if err < TOLERANCE:
            return toreturn
        ftemp = f(temp)
        if ftemp * fp1 < 0:
            p0 = p1
            fp0 = fp1
        p1 = temp
        fp1 = ftemp
    else:
        return None

def main() -> None:
    p0 = 1.3
    p1 = 2

    x_vals = list(range(-5, 6))
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals)
    plt.plot(x_vals, [0 for _ in x_vals])

    newtondict = Newton(p0)
    secantdict = Secant(p0, p1)
    falsedict = Falsepos(p0, p1)

    plt.plot(newtondict['last']['value'], 0, 'ro')
    plt.annotate(f'({newtondict['last']['value']}, 0)', xy=(newtondict['last']['value'], 0), xytext=(newtondict['last']['value'] + 0.1, 0.5))
    plt.show()

    #print(f'newton: {newtondict}\nsecant: {secantdict}\nfalse: {falsedict}')


    

if __name__ == "__main__":
    main()