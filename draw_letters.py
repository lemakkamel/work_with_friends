from __future__ import print_function
def first_letter(i):
    if i ==1 or i==5:
        print ("*"+" "+"*",end="")
    if i ==2 or i==4:
        print ("*"*2+" ",end="")
    if i ==3:
        print ("*"+" "*2,end="")

def second_letter(i):
    if i ==1 :
        print (" "+"*"*2+" ",end="")
    if i ==2 or i==4 or i==5:
        print ("*"+" "*2+"*",end="")
    if i ==3:
        print ("*"*4,end="")

def draw_letter(string):
    print ("here will draw ",string)
    for i in range(1,6):
        first_letter(i)
        print(" "*4,end="")
        second_letter(i)
        print ()


draw_letter("KA")