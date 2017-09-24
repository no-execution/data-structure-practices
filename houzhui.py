val = {'+':1,'-':1,'*':2,'/':2,'(':0,'**':3}
def post(pre):
    equ = pre.split()
    a = []   #储存符号的stack
    res = [] #储存结果（数字也放进去）
    for i in range(0,len(equ)):
        if equ[i] in '+-**/':
            if len(a) == 0:
                a.append(equ[i])
            elif val[equ[i]]>val[a[-1]]:
                a.append(equ[i])
            elif val[equ[i]]<=val[a[-1]]:
                while len(a) != 0 and val[equ[i]]<=val[a[-1]]:
                    res.append(a.pop())
                a.append(equ[i])
        elif equ[i] == '(':
            a.append(equ[i])

        elif equ[i] == ')':
            while a[-1] != '(':
                res.append(a.pop())
            a.pop()
        else:
            res.append(equ[i])
    while len(a) != 0:
        res.append(a.pop())
    print(' '.join(res))

def main():
    post('5 * 3 ** ( 4 - 2 )')

main()
                
            
        
            
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
