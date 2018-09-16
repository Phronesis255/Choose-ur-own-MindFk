import numpy as np
import colorama
import sys
from os import system
from colorama import Fore, Back, Style
import re
from utls import *
'''
TODO construct a pageNumx2 state x action matrix with each value determining the possible choices and their outcome
as a new page-state. in purely narrative pages, both values will point to the next page and we can know this
is the case whenever the two columns are the same.


 >>> a=[5,6,2,1,55,3331]
>>> operator.indexOf(a,6)
1
>>> operator.indexOf(a,55)
4
>>> operator.indexOf(a,1)
3

'''
pageMtrx = [[0]* 2 for i in range(188)]

def initGo(pn):
    pn += 1
    g = pageOpn(pn)
    ld1 = re.findall(r"\d+", g[-2])
    ld2 = re.findall(r"\d+", g[-1])
    d1 = int(ld1[0])
    d2 = int(ld2[0])
    new_pg = ask_usr(g[-2], g[-1], d1, d2, pn)
    return new_pg 

def Begin(xchar):
    EOP = NXT = False
    x = xchar
    sys.stdout.write(Back.WHITE + Fore.BLUE + "\nHi, you made it, " + REVCH.get(xchar) + "\n")
    while not DONE:
        EOP, NXT = pageMkr(pageOpn(x))  #must somewhere incl the code to strip numvers and "turn to page" stuf
        if NXT:
            pageMtrx[x] = [x+1,x+1]
            x += 1
        else:
            sys.stdout.write("DIGITS!")
            x = initGo(xchar)
            sys.stdout.write("AND BACK")
            
    
def main():
    clear()
    key=" "
    EOP = False
    NXT = False
    colorama.init()
    a = []
    sys.stdout.write(Fore.RED + "-------SUPER GIANT MONSTER TIME-------\n")
    EOP, NXT = pageMkr(pageOpn(1))
    if EOP:
        print("\n")
        print("\n")
        key = input("... END OF PROLOG. PRESS N TO START YOUR MINDFUCK...\n")
    if key == "n":
        char = chooseChar()
        Begin(char[1])
    else:
        input("\nHIT ANY KEY TO EXIT\n")
    colorama.deinit()


if __name__ == '__main__':
    main()