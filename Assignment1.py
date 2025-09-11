import math # for the math
import matplotlib.pyplot as plt # for the graphs
from prettytable import PrettyTable # for some print formatting

TOLERANCE = 1e-5
MAXITER = 20

def f(x) -> float: # given function
    return math.exp(x) + 2**-x + math.cos(x) - 6

def fprime(x) -> float: # derivative of given function
    return math.exp(x) - (2**-x) * math.log(2) - math.sin(x)

def Newton(p0: float) -> dict: # Newton's Method
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

def Secant(p0: float, p1: float) -> dict: # Secant Method
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

def Falsepos(p0: float, p1: float) -> dict: # False Position Method
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

if __name__ == '__main__':
    # given starting points
    p0 = 1.3
    p1 = 2

    # values for graphing f(x)
    x_vals = list(range(-5, 6))
    y_vals = [f(x) for x in x_vals]

    # initializing subplots and putting f(x) on them
    fig, axs = plt.subplots(1,3, figsize=(15,4))
    for ax in axs:
        ax.plot(x_vals, y_vals)
        ax.plot(x_vals, [0 for _ in x_vals])

    # run methods and create accepted value
    newtondict = Newton(p0)
    secantdict = Secant(p0, p1)
    falsedict = Falsepos(p0, p1)
    accepted_value = newtondict['last']['value']

    # plot estimated points on graphs
    axs[0].set_title("Newton Method")
    axs[0].plot(accepted_value, 0, 'ro')
    axs[0].annotate(f'({round(accepted_value, 6)}, 0)', xy=(accepted_value, 0), xytext=(accepted_value + 0.1, 0.5))

    axs[1].set_title("Secant Method")
    axs[1].plot(secantdict['last']['value'], 0, 'ro')
    axs[1].annotate(f'({round(secantdict['last']['value'], 6)}, 0)', xy=(secantdict['last']['value'], 0), xytext=(secantdict['last']['value'] + 0.1, 0.5))

    axs[2].set_title("False Position Method")
    axs[2].plot(falsedict['last']['value'], 0, 'ro')
    axs[2].annotate(f'({round(falsedict['last']['value'], 6)}, 0)', xy=(falsedict['last']['value'], 0), xytext=(falsedict['last']['value'] + 0.1, 0.5))

    # create tables from data
    field_names = ["Value", "Iteration", "Error"]

    newtontable = PrettyTable()
    newtontable.field_names = field_names
    newtontable.add_rows([
        [newtondict['secondlast']['value'], newtondict['secondlast']['iteration'], newtondict['secondlast']['error']],
        [newtondict['last']['value'], newtondict['last']['iteration'], newtondict['last']['error']]
    ])

    secanttable = PrettyTable()
    secanttable.field_names = field_names
    secanttable.add_rows([
        [secantdict['secondlast']['value'], secantdict['secondlast']['iteration'], secantdict['secondlast']['error']],
        [secantdict['last']['value'], secantdict['last']['iteration'], secantdict['last']['error']]
    ])

    falsetable = PrettyTable()
    falsetable.field_names = field_names
    falsetable.add_rows([
        [falsedict['secondlast']['value'], falsedict['secondlast']['iteration'], falsedict['secondlast']['error']],
        [falsedict['last']['value'], falsedict['last']['iteration'], falsedict['last']['error']]
    ])

    #display information
    print("Newton's Method:")
    print(newtontable)
    newtonrelerr = abs(accepted_value - newtondict['last']['value'])
    print(f'Relative Error: {newtonrelerr}\tAbsolute Error: {newtonrelerr/abs(accepted_value)}')

    print()

    print("Secant Method:")
    print(secanttable)
    secantrelerr = abs(accepted_value - secantdict['last']['value'])
    print(f'Relative Error: {secantrelerr}\tAbsolute Error: {secantrelerr/abs(accepted_value)}')

    print()

    print("False Position Method:")
    print(falsetable)
    falserelerr = abs(accepted_value - falsedict['last']['value'])
    print(f'Relative Error: {falserelerr}\tAbsolute Error: {falserelerr/abs(accepted_value)}')

    print()

    plt.show()

    # written response--------------------------------------------------------------------------------------------
    # Newton's and Secant took the same amount of iterations with 4 iterations, and False Position took 6.
    # Using Newton's to get the accepted value automatically gives the method a relative and absolue error of 0.
    # False Position has a higher relative and absolute error than Secant Method.
    # It's hard to say wheter Newton's or Secant are better than the other since they have the same number of iterations 
    # and we're using Newton's as the accepted value, but for this problem it seems False Position is definitely the worst method to use.
    # If we had a different accepted value this might would change, but it has the biggest errors and the most iterations.
    # It's also the most complex of the methods. Newton's is the simplest, but it requires an exact derivative where the Secant and False Positioning
    # approximates both.