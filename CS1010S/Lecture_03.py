'''Lecture 3'''

#recursive
def recursive(n):
    if n<3:
        return n 
    else:
        return recursive(n-1) + 2*recursive(n-2) +3*recursive(n-3)

#print(recursive(5))

#iterative
def iterative(n):
    while n>=3:
        return recursive(n-1) + 2*recursive(n-2) +3*recursive(n-3)
    return n

#print(iterative(5))

def is_fib(n):
    fib=[1,1]
    if n == 1:
        return True
    while n > fib[-1]:
        fib.append(fib[-1] + fib[-2])    
        if n == fib[-1]:
            return True
    return False

#print(is_fib(4181))


def make_fare(stage1, stage2, base_fare, increment, block1, block2):
    def inner_func(n):
        if n < stage1:
            return base_fare
        elif n > stage1 and n < stage2:
            return base_fare + ((n - stage1) * increment / block1)
        elif n > stage2:
            return base_fare + ((stage2 - stage1) * increment / block1) + ((n - stage2) * increment / block2)
    return inner_func

comfort_fare = make_fare(1000,10000,3.0,0.22,400,350)    #this assigned function returns inner_func, which accepts a singular argument n.
#print(comfort_fare(3500))


def add_order(a,b):
    total = ''.join([str(a),str(b)])
    return int(total)

#print(add_order(123,234))