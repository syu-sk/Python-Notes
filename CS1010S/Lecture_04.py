'''Lecture 4'''

#change counter
def cc(amount, cointypes):
    #amount = total amount to be split into the change
    #cointype = list of change denominations
    cointypes.sort()
    if amount == 0:

        #---log---
        with open('testlog.txt', 'a') as file:
            file.write('\n')
            file.write(f'+1')
        #---log---

        return 1
    elif amount < 0:

        #---log---
        with open('testlog.txt', 'a') as file:
            file.write('\n')
            file.write(f'overflow!')
        #---log---

        return 0
    elif len(cointypes) == 0:
        return 0
    else:

        #---log---
        with open('testlog.txt', 'a') as file:
            file.write('\n')
            file.write(f'Taking {cointypes[-1]} out of {amount}...')
        #---log---

        return cc(amount - cointypes[-1], cointypes) + cc(amount, cointypes[:-1])

#print(cc(100, [50,20,10,5,1]))

#iterative process for this code is much harder.
#Iterative processes are as time-efficient and more space-efficient (reuse same line) than recursive processes, but recursive processes are easier and more elegant.
'''
Order of Growth:
Two considerations -- Time and Space.
To obtain,
1. Identify the basic computational step. For recursive processes, this will generally be the else block, the step which calls the local/other functions.
2. Try small values of n - that is, make a tree. Branch it out to obtain a general shape
3. Extrapolate this tree for very large n
4. Generalise

Time complexity:
- Count the leaves in the tree (for large computations)

Space complexity:
- Function Calls, i.e pending operations & recursive function calls
- Data Structures
- Simply put, the depth of the entire tree. Recall that order of growth it how much it grows in proportion to input growth.
'''

'''
Higher Order Functions:
Functions that input and output functions. Somewhat like a variable function.
They may be compared to parametric functions. (Where specific t values create different graph curves)
Simply put, they generalise common patterns by taking functions as input.
'''

#Example 1: Integration is a simple function, made up of a state of summation().

def summation(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + summation(term, next(a), next, b)
#above is the summation formula, which is a higher order function in itself, summing up terms from a to b, with custom function for a, and custom increments.
#this summation formula is required for the integration formula

def integral(function, dx, a, b):
    def add_dx(x):
        return x + dx 
    return dx * summation(function, a+(dx/2), add_dx, b)
#requires base understanding of integration approximation (recall rectangles under the line). dx is the width of the rectangles. The smaller the closer the approximation.

#print(integral(lambda x: x**3, 0.01, 0, 1))
#this approximates the area under the graph x^3, from 0 to 1, with each rectangle having a 0.01 unit width.
#Maximum recursion limit under default python is ~1000, so dx can only be small to a certain extent.

'''
Closures:
Learnt before...
Recursive functions return itself, and has a self-terminating statement to ensure it runs till the specified limit is reached.
What is instead of returning itself, a function returns a separate function? This is known as a closure.

Closely related to higher order functions.
Closures are inner functions which are 'captured' i.e returned by a state of the higher order function.
They are normally assigned to a variable, and then able to be executed later when desired.
'''

#Example 1: Differentiation transforms a function into another function (i.e the gradient)

def derivative(function, dx):
    def diff_formula(x):
        return (function(x+dx)-function(x)) / dx
    return diff_formula
    #closure - a particular state of derivative() is captured in diff_formula which is then returned in a 'frozen' state.
    #also do note diff_formula is the differentiation formula hard coded.

diff_quad1 = derivative(lambda x: x**2 + 3*x + 5, 0.00001)
#this code essentially returns the diff_formula i.e a state of derivative() with a set formula and rectangle width.
#this closure can be executed when need be (the next line). assigning to variable makes it more readable though unnecessary.

#print(diff_quad1(2))
#finds approximated derivative of the curve x^2 + 5, returns value when x = 2.
#unlike integral(), derivative () is a non-recursive function, so dx can realistically be as small as default python's float limit.

#Example 2: Newton's Method -- A way to find the root of an equation
'''
1. Start with initial guess x0.
2. Sub x0 into equation
3. If equation is 0, solution is x0.
4. Otherwise, sub x with x - ( g(x)/g'(x) ). Continue doing this until equation falls within tolerance. (i.e close enough to 0)
'''

#this example uses differentiation. note differentiation formula requires a dx input
def newton(function, first_guess, dx):
    df = derivative(function, dx)       #returns f'(x)

    def improve(x):                 #this function refines the x value to bring the equation gradually to =0
        return x - (function(x) / df(x))

    def query(v):
        tolerance = 0.00001         #can be set to a customisable argument
        return abs(v) < tolerance   #returns True/False, verification for solution validity

    def attempt(xvalue):            #where steps 1-2 (first recursion) occur, and subsequently steps 3,4... until query() returns True. lowk, iterative sounds way simpler
        if query(function(xvalue)):
            return xvalue           #when this inevitably computes to be True, the returned xvalue will be the solution!
        else:
            return attempt(improve(xvalue))

    return attempt(first_guess)

#print(newton(lambda x: x**2 - 4, 0, 0.0001))

def inewton(function, x, dx):
    df = derivative(function, dx)

    def query(equation):
        tolerance = 0.00001
        return abs(equation) < tolerance

    if query(function(x)):
        return (x)
    else:
        while not query(function(x)):   #pretty similar to the one above. However this is iterative -- cycles back if solution returns False on query
            x = x - function(x) / df(x) #improve function hard coded here, can be changed to a function
        return(x)

#print(inewton(lambda x: x**2 - 4, 0, 0.0001))

#sqrt function. By using newton's method as a higher order function.
#let a = sqrt(x). Then a^2 = x  ==>  x - a^2 = 0
def sqrt(x):
    return newton(lambda a: x-a**2, x/2, 0.0001)    #here the 'a' is the variable that is repeatedly guessed, not x. x is a constant given in the sqrt().
#print(sqrt(9))

#as a higher order function, more complex equations like logarithms can be solved.
#let lg(x) = k. Then x = 10^k  ==>  x - 10^k = 0
def lg(x):
    return newton(lambda k: x - 10**k, x/2, 0.0001)
#print(lg(7))


'''
Fold functions:
- A recursive higher order function. It returns a higher order function itself.
- Just like other recursive functions, it has an inbuilt mechanic to terminate itself upon reaching a specified limit.
'''

#Example 1: fold()

#To compute a binary operation on a function f. i.e f(0) x f(1) x f(2) ... f(n) where n can be specified
#This goes one step beyond summation() whereby even the binary operator can be specified. A function with very high flexibility.

def fold(operator, function, n):
    if n==1:
        return function(1)     #f(n), but has to be hard coded as it is the terminator. can also be a variable argument
    else:
        return operator(fold(operator, function, n-1), function(n))     
        #'folds' the terms together, i.e stacking them using an operator.
        #stacks an additional f(n) everytime this else block is reached. 

#print(fold(lambda x,y: x*y, lambda x: 3, 5))
#realise that this only works if the operation is the same, and has no impact regardless of the order of operations.

def ifold(operator, function, n):
    x = 1
    for i in range(1, n+1):
        x = operator(x, function(i))
    return x
    #iterative version more readable and easier as with above.

#print(ifold(lambda x,y: x*y, lambda x: 3, 5))

#useful for exponents...

def expt(a, n): #a**n
    return fold(lambda x,y: x*y, lambda x:a, n-1)
    #returns ((((a)*a)*a)...) however many times until it is terminated (until n=0)


'''Tutorial 4'''
#1 (corr)
def simpson(f, a, b, n):
    sol = 0
    h = (b - a) / n
    for i in range(0, n+1):
        if i == 0 or i == n:
            sol += (h/3) * f(a + i*h)
        elif i%2 == 1:
            sol += (h*4/3) * f(a + i*h)
        else:
            sol += (h*2/3) * f(a + i*h)
    return sol

#print(simpson(lambda x: x**3, 0, 1, 100))

#2 (corr)
def fold(operator, function, n):
    if n == 0:
        return function(0)
    else:
        return operator(function(n), fold(operator, function, n-1))

def g(k):
    return fold(lambda x,y : x*y, lambda x: (x - (x + 1)**2), k)

#print(g(8))

#3a (corr)
def accumulate(combiner, base, term, a, next, b):
    if a > b:
        return base
    else:
        return combiner(term(a), accumulate(combiner, base, term, next(a), next, b))
#show sum defined. (corr)
def summation(term, a, next, b):
    return accumulate(lambda x, y: x + y, 0, lambda x: x, a, lambda x: x + 1, b) #next function to be left in summation, does not strictly have to be x + 1

#3b (iterative)
def iaccumulate(combiner, base, term, a, next, b):
    sol = base
    while a <= b:
        sol = combiner(sol, term(a))    #more efficient solution... idk. check answers
        a = next(a)
    return sol

#print(accumulate(lambda x, y: x*y, 1, lambda x: x, 1, lambda x: x + 1, 10))
#print(iaccumulate(lambda x, y: x*y, 1, lambda x: x, 1, lambda x: x + 1, 10))

#4
#(a)(i) (corr)
def make_point(x,y):
    return [x, y]

def x_point(point):
    return point[0]
def y_point(point):
    return point[1]
def print_point(point):
    return f'Coordinates: ({x_point(point)}, {y_point(point)})'

#(a)(ii) (corr)
def make_segment(p1, p2):
    return [p1, p2]
def start_segment(seg):
    return tuple(seg[0])
def end_segment(seg):
    return tuple(seg[1])

#(a)(iii) (corr)
def midpoint_segment(seg):
    p1 = start_segment(seg)
    p2 = end_segment(seg)
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

#(b) (corr)
def length(seg):
    x = abs(x_point(start_segment(seg)) - x_point(end_segment(seg)))
    y = abs(y_point(start_segment(seg)) - y_point(end_segment(seg)))
    return (x**2 + y**2)**0.5
    #or def sqrt(x):
    #   return newton(lambda a: x-a**2, x/2, 0.0001) for more organic albeit estimated solution
def make_rectangle(s1, s2):
    return [s1, s2]
def side_x(rect):
    return rect[0]
def side_y(rect):
    return rect[1]
def perimeter(rect):
    return f'Perimeter of rectangle: {2*(length(side_x(rect)) + length(side_y(rect)))}'
def area(rect):
    return f'Area of rectangle: {length(side_x(rect))*length(side_y(rect))}'

#testing
c1 = make_point(2, 3)
#print(x_point(c1))
#print(print_point(c1))

c2 = make_point(8, 3)
d1 = make_segment(c1, c2)
#print(start_segment(d1))
#print(end_segment(d1))

#print(midpoint_segment(d1))

c3 = make_point(2, 6)   #simple horizontal rectangle, 6 x 3. note 4th corner is technically not needed
d2 = make_segment(c1, c3)
#print(length(d2))
e1 = make_rectangle(d1, d2)

#print(perimeter(e1))
#print(area(e1))