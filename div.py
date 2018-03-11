'''
In this program i will make division without using / sign
this program work on python 2.7
'''
#this function for calculate remainder of Div
def remaindeOfDiv(a, b):
    a = a * 10
    count=0
    while a - b >= 0 :
        a=a-b
        count += 1
    return count,a
# this function used for calculate division
# c is the numbers after ","
def divi_sion(a, b,c):
    n=c
    count=0
    check=0
    remainder=["."]
    if b==0:
        return "can't / by 0"
    if a>b:
        while a - b >= 0:
            a = a - b
            count += 1
        while a!=0 and check!=n:
            r1,a = remaindeOfDiv(a, b)
            check+=1
            remainder.append(str(r1))
        return str(count) + "".join(remainder)
    if a==b:
        return 1
    else:
        while a!=0 and check!=n:
            r1,a = remaindeOfDiv(a, b)
            check+=1
            remainder.append(str(r1))
        return "0" + "".join(remainder)
#example of dividing 2010/4 with 3 num after ","
print divi_sion(2010,4,1)#====>result is : 502.5