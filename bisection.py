def equ(x):
    return x*x+2*x-4
def bis(a,b):
    if equ(a)*equ(b)>0:
        return 'no solution'
    if equ(a)>0:
        right = a
        left = b
    elif equ(a)<0:
        left = a
        right = b    
    mid = (left+right)/2
    while (right-left)>=0.0000000001:
        if equ(mid)>0:
            right = mid
        elif equ(mid)==0:
            return mid
        elif equ(mid)<0:
            left=mid
        mid = (right+left)/2
    return mid
    

def main():
    a=bis(0,2)
    print(a,equ(a))
main()
