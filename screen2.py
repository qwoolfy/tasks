def to_float(num):
    if str(num)== num:
        return("невозможно преобразовать")
    else:
        float_num=float(num)
        return(float_num)
    
def avg(a,b,c,d):
    srzn=(a+b+c+d) / 4
    return round (srzn,5)

def mul_to_int(a,b):
    result = a*b
    if int(result)==result:
        return(int(result))
    else:
        return(float(result))
    
a = int(input())
import math
R= (3*a/math.pi*4)**(1./3.)
print (R)