#! /usr/bin/python3.5
#-*- coding: utf-8 -*-
import Color as C
import os

test = True
stop = str("stop")

def Start():
    os.system("clear")
    print(C.G+"\nUser Stated the test\n"+C.W)
    test = True
    return test

def Stop():
    print(C.R+"\nUser Stoped the test\n"+C.W)
    test = False
    return test

def Int_Test(annee):
    try:
        annee = int(annee)
    except:
        annee = str(annee)
    return annee

def Test(Annee):
    if isinstance(Annee, int):
        annee = int(Annee)
        Verify(Annee)
        test = True

    elif isinstance(Annee, str):
        try:
            if Annee.lower() == str("stop"):
                test = Stop()
            elif Annee.lower() != str("stop"):
                print (C.O+ " ---> "+C.P+ " ** ", str(Annee), " ** " +C.R+ " is not a year, pleas try again" +C.W)
                test = True
            else:
                print ("error")
                test = True
        except:
            print("error try")
            test = True
    else:
        print("Unknown error")
        test = True
    return test

def Verify(Annee):
    if (Annee % 4) != 0:
        print(C.O+ " ---> "+C.B+ " ** ", str(Annee), " ** " +C.R+ " is not a leap year     \# (%4 Test)" +C.W)
    else:
        if (Annee % 100) == 0:
            if (Annee % 400) == 0:
                print(C.O+ " ---> "+C.B+ " ** ", str(Annee), " ** " +C.G+ " is a leap year     \# (%400 Test)" +C.W)
            else:
                print(C.O+ " ---> "+C.B+ " ** ", str(Annee), " ** " +C.R+ " is not a leap year     \# (%400 Test)" +C.W)
        else:
            print(C.O+ " ---> "+C.B+ " ** ", str(Annee), " ** " +C.G+ " is a leap year     \# (%100 Test)" +C.W)

test = Start()
while test == True:
    annee = input(C.C+ "\nenter a Year to verify: " +C.W)
    Annee = Int_Test(annee)
    #print(type(Annee))
    test = Test(Annee)
