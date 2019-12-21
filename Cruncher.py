# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import math
import os
import platform
import time
import cmath
from decimal import *
from decimal import Decimal as dec
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def wait():
    if waitsetc == 1:
        clear()
        wait = str(input("Press enter to continue..."))
    if waitsetc == 0:
        wait = str(input("\nPress enter to exit..."))
    clear()
def inttest(x):
    decval = int(x) - x
    if decval == 0:
        return True
    else:
        return False
def factorial(x):
    ans = 1
    for fac in range(x,1,-1):
        ans *= fac
    x = ans
    return x
def settings():
    global pi_interval
    global e_interval
    pi_interval = 250
    e_interval = 100
def BBP_Pi():
    clear()
    global pi_interval
    global x
    global fin
    count = pi_interval
    fin = bool(0)
    x = 0
    pi = 0
    if not(dis_ch_bool):
        print("Calculating...")
        print("\n")
    tstart = time.perf_counter()
    for x in range(0,maxpr): 
        pi += dec((dec(1) / dec(16) ** dec(x)) * (dec(4) / (dec(8) * x + dec(1)) - dec(2) / (dec(8) * x + dec(4)) - dec(1) / (dec(8) * x + dec(5)) - dec(1) / (dec(8) * x + dec(6))))
        if dis_ch_bool:
            print(pi)
        elif x == count:
            percom = x / maxpr * 100
            print("\033[A\b\b\b\b\b\b",'%.3f'%(percom),r"%")
            count += 1
    finalpi = dec(int(pi * dec(10 ** maxpr)) / dec(10 ** maxpr))
    tend = time.perf_counter()
    fin = bool(1)
    clear()
    print("Done!\n")
    print(finalpi)
    if maxpr == 0:
        lensub = 0
    else:
        lensub = 1
    stlength = len(str(finalpi)) - lensub
    print("\nLength",stlength)
    print("\nAccurate Precision",maxpr)
    print("Time:",'%.4f'%(tend - tstart),"Seconds")
    if textfc == "Y" or textfc == "y":
        outFile = open("PI.txt", "w+")
        outFile.write(str(finalpi))
        outFile.close()
def Euler():
    clear()
    global e_interval
    global x
    global fin
    count = e_interval
    fin = bool(0)
    x = 0
    euler = 0
    if not(dis_ch_bool):
        print("Calculating...")
        print("\n")
    tstart = time.perf_counter()
    for x in range(0,maxpr):
        euler += dec(dec(1) / dec(factorial(int(x))))
        if dis_ch_bool:
            print(euler)
        elif x == count:
            percom = x / maxpr * 100
            print("\033[A\b\b\b\b\b\b",'%.3f'%(percom),r"%")
            count += 1 
    finaleuler = dec(int(euler * dec(10 ** maxpr)) / dec(10 ** maxpr))
    tend = time.perf_counter()
    clear()
    print("Done!\n")
    print(finaleuler)
    if maxpr == 0:
        lensub = 0
    else:
        lensub = 1
    stlength = len(str(finaleuler)) - lensub
    print("\nLength",stlength)
    print("\nAccurate Precision",maxpr)
    print("Time:",'%.4f'%(tend - tstart),"Seconds")
    if textfc == "Y" or textfc == "y":
        outFile = open("Euler.txt", "w+")
        outFile.write(str(finaleuler))
        outFile.close() 
def rootcrunch():
    root = dec(input("Root:"))
    x = dec(input("Root of:"))
    clear()
    print("Calculating...")
    tstart = time.perf_counter()
    sq = dec(x ** dec(dec(1) / dec(root)))
    clear()
    print("Converting")
    finalsq = dec(int(sq * dec(10 ** maxpr)) / dec(10 ** maxpr))
    tend = time.perf_counter()
    clear()
    print("Done!\n")
    finalsq = dec(int(sq * dec(10 ** maxpr)) / dec(10 ** maxpr))
    print(finalsq)
    if finalsq - int(finalsq) != 0:
        sqvar = 1
    else:
        sqvar = 0
    stlength = len(str(finalsq)) - sqvar
    print("\nLength",stlength)
    print("\nAccurate Precision",maxpr)
    print("Time:",'%.4f'%(tend - tstart),"Seconds")
def Gratio():
    clear()
    print("Calculating...")
    tstart = time.perf_counter()
    Golden = dec(dec(dec(1) + dec(dec(5) ** dec(0.5))) / dec(2))
    clear()
    print("Converting")
    finalgolden = dec(int(Golden * dec(10 ** maxpr)) / dec(10 ** maxpr))
    tend = time.perf_counter()
    clear()
    print("Done!\n")
    print(finalgolden)
    if maxpr == 0:
        lensub = 0
    else:
        lensub = 1
    stlength = len(str(finalgolden)) - lensub
    print("\nLength",stlength)
    print("\nAccurate Precision",maxpr)
    print("Time:",'%.4f'%(tend - tstart),"Seconds")
textfc = "n"
dis_ch_var = "n"
dis_ch_bool = 0
waitsetc = 1
maxpr = 0
lensub = 2
fin = bool(0)
clear()
settings()
print(r"Select Constant to compute")
print("1:PI\n2:Euler\n3:Root\n4:Golden Ratio")
option = int(input("Option:"))
clear()
if option < 5 and option > 0:
    maxpr = int(input("Precicion:"))
if option == 1 or option == 2:
    print(r"Output Text file Y/N")
    textfc = str(input())
    print(r"Display Interval Y/N")
    dis_ch_var = str(input())
    if dis_ch_var == "Y" or dis_ch_var == "y":
        dis_ch_bool = bool(1)
    wait()
if option == 1:
    getcontext().prec = maxpr + 32
    BBP_Pi()
elif option == 2:
    getcontext().prec = maxpr + 32
    Euler()
elif option == 3:
    getcontext().prec = maxpr + 16
    rootcrunch()
elif option == 4:
    getcontext().prec = maxpr + 8
    Gratio()
else:
    clear()
    print("Invalid Option")
if maxpr < 0:
    clear()
    print("Invalid Option")
waitsetc = 0
wait()
# End of Program
