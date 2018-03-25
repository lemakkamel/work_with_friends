from __future__ import print_function
def make_draw(letter, i):
    print(" " * 4, end="")
    if (letter=="a" and i ==1):
        print(" " + "*" * 2 + " ", end="")
    if (letter=="a" and i ==2)or(letter=="a" and i ==4)or(letter=="a" and i ==5) :
        print("*" + " " * 2 + "*", end="")
    if (letter=="a" and i ==3):
        print("*" * 4, end="")
    if ((letter=="k" and i ==3)or (letter=="l"and (i==1 or i==2 or i==3 or i==4))):
        print("*" + " " * 2, end="")
    if (letter == "k" and (i == 1 or i == 5)or(letter=="l"and i==5 )):
        print("*" + " " + "*", end="")
    if (letter == "k" and i == 2) or (letter == "k" and i == 4):
        print("*" * 2 + " ", end="")

def draw_letter(string):
    print ("here will draw ",string)
    print()
    x=len(string)

    for i in range(1,6):
        for j in range(0,x):
            #print (j)
            make_draw(string[j],i)
        print ()

string_to_draw=raw_input("Enter you string : ")
draw_letter(string_to_draw)