#lecture 5 no notes :p


'''Tutorial 5'''
#3
def even_rank(t):
    return t[1::2]

print(even_rank((1,2,3,4,5,6,7,8)))

#4
def odd_even_sum(t):
    return (sum(t[::2]), sum(t[1::2]))

print(odd_even_sum((1,2,3,4,5)))

#5
def hanoi(ndisc, src, dest, aux):

    if ndisc == 1:
        return (src, dest)      #base case -- move one disc from src to dest directly
    else:
        return (hanoi(ndisc - 1, src, aux, dest), hanoi(1, src, dest, aux), hanoi(ndisc - 1, aux, dest, src))
        '''
        recursive function: 
        assuming i know how to move n - 1 discs from point A to B.
        then n - 1 discs on top are moved to aux, 
        after that move largest disc from src to dest,
        and finally n - 1 discs are moved from aux to dest, successfully relocating the tower.
        this function repeats until ndisc = 1, where it is simply moved from its src to its dest.
        '''

print(hanoi(3, 1, 2, 3))


def addition(x, y):
    return x + y

print(addition(3, 6))