import os
import colorama
import sys
from os import system
from colorama import Fore, Back, Style
import re

SMAT = [[0,0]] * 178
CHRS = {
    "Si": [1, 11],
    "John": [2, 77],
    "Gary": [3, 149]
}
REVCH = {
    11: "Si",
    77: "John",
    149: "Gary"
}
EOP = False
DONE = False

def ask_usr(raw_s1, raw_s2, n1, n2, ppage = 0):
    sys.stdout.write("...CHOOSE LOCAL MINDFUCK...\n") #rephrase and rewrite the last two lines in diffrent color
    raw_s1 = raw_s1.replace("turn to page", "")
    raw_s1 = raw_s1.replace(str(n1)+".", "")
    raw_s1.rstrip()
    sys.stdout.write("TO  " + str(raw_s1) + " PRESS 1\n")
    raw_s2 = raw_s2.replace("turn to page", "")
    raw_s2 = raw_s2.replace(str(n2)+".", "")
    raw_s2.rstrip()
    sys.stdout.write("TO  " + str(raw_s2) + " PRESS 2\n")
    while True:
        inp = input("  WHAT WILL IT BE?  ")
        if inp == "1":
            return n1
            break
        elif inp == "2":
            return n2
            break
        else:
            continue


def has_dgt(str1):
    for i in str1:
        if i.isdigit():
            return True
    return False

def clear():
    _= system('clear')

def chooseChar():
    with open("PAGES/page - 0009.txt","rt", encoding = "utf-8", errors = "replace") as fc: #, encoding = "ascii", errors = "replace"
        sys.stdout.write(Fore.RED + fc.read())
    c = CHRS.get(input("\nEnter Your First Name...\n"), None)
    if c == None:
        sys.stdout.write(Fore.RED + "NOT A CORRECT NAME\n")
        return chooseChar()
    else:
        return c

def pageOpn(num = None):
    ax = []
    fnm = " "
    if num != None:
        if num < 100 and num > 9:
            fnm = "page - 00" + str(num) + ".txt"
        elif num < 10:
            fnm = "page - 000" + str(num) + ".txt"
        else:
            fnm = "page - 0" + str(num) + ".txt"
        with open("PAGES/" + fnm, "rt", encoding = "utf-8", errors = "replace") as fn:
            datan = fn.readlines()
            for line in datan:
                 ax.append(line)
        return ax

def pageMkr(datax = None, pgn = None, n = 5):
    sys.stdout.write(Back.BLACK)
    if datax == None:
        return -1
    else: #turn into elif wrt n=0 ie the whole page at once
        for i in range(0, len(datax), n):
            for j in range(0, n, 1):
                if i+j < len(datax):
                    sys.stdout.write(Fore.YELLOW + str(datax[i+j]))
                else:
                    if has_dgt(str(datax[len(datax)-1])):
                        return True, False
                    else:
                        return True, True
            input("...PRESS ENTER TO CONTINUE...\n")
            clear()
